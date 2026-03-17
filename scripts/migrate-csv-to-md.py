#!/usr/bin/env python3
"""
CSV → .md 移行スクリプト

1. プロセス改善_課題管理.csv の全行を読み取り:
   - ISS-XXX.md が存在しない行 → テンプレートに従い新規生成
   - 既存 .md がある行 → 「対応・クローズ情報」セクションを追記（未存在の場合）
2. 旧フォーマット backlog エントリ（ブロッククォート形式）→ テーブル形式に変換

Usage:
    python3 scripts/migrate-csv-to-md.py          # 実行
    python3 scripts/migrate-csv-to-md.py --dry-run # プレビューのみ
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

ISSUES_CSV_PATH = PROJECT_ROOT / "プロセス改善_課題管理.csv"
ISSUES_ENTRIES_DIR = PROJECT_ROOT / "issues" / "entries"
BACKLOG_ENTRIES_DIR = PROJECT_ROOT / "backlog" / "entries"
BACKLOG_CSV_PATH = PROJECT_ROOT / "backlog" / "backlog.csv"

# --- Issue migration ---

ISSUE_TEMPLATE = """# {id}: {title}

## 基本情報

| 項目 | 値 |
|------|-----|
| ID | {id} |
| 起票日 | {date} |
| カテゴリ | {category} |
| 種別 | {kind} |
| ステータス | {status} |
| 優先度 | {priority} |
| 関連施策 | {related} |

## 課題詳細

{detail}

## 対応方針（案）

{proposal}

## 補足・参照

{supplement}

## 対応・クローズ情報

| 項目 | 内容 |
|------|------|
| 対応方針（確定） | {confirmed_policy} |
| 確定日 | {confirmed_date} |
| タスク化先 | {task_target} |
| 備考 | {note} |

---
**起票者**: L2（CSV移行による自動生成）
**CSV転記済み**: はい
"""

CLOSE_INFO_SECTION = """
## 対応・クローズ情報

| 項目 | 内容 |
|------|------|
| 対応方針（確定） | {confirmed_policy} |
| 確定日 | {confirmed_date} |
| タスク化先 | {task_target} |
| 備考 | {note} |
"""


def migrate_issues(dry_run: bool = False):
    """CSV の全行を .md に移行する。"""
    if not ISSUES_CSV_PATH.exists():
        print(f"CSV not found: {ISSUES_CSV_PATH}", file=sys.stderr)
        return

    with open(ISSUES_CSV_PATH, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    created = 0
    updated = 0
    skipped = 0

    for row in rows:
        issue_id = row.get("ID", "").strip()
        if not issue_id:
            continue

        md_path = ISSUES_ENTRIES_DIR / f"{issue_id}.md"

        if md_path.exists():
            # Check if 対応・クローズ情報 section exists
            text = md_path.read_text(encoding="utf-8")
            if "## 対応・クローズ情報" not in text:
                # Add the section
                close_section = CLOSE_INFO_SECTION.format(
                    confirmed_policy=row.get("対応方針_確定", ""),
                    confirmed_date=row.get("確定日", ""),
                    task_target=row.get("タスク化先", ""),
                    note=row.get("備考", ""),
                )

                # Insert before the footer (---) at the end, or append
                # Find the last "---" line
                lines = text.rstrip().split("\n")
                insert_idx = len(lines)
                for i in range(len(lines) - 1, -1, -1):
                    if lines[i].strip() == "---":
                        insert_idx = i
                        break

                new_lines = lines[:insert_idx] + close_section.strip().split("\n") + [""] + lines[insert_idx:]
                new_text = "\n".join(new_lines) + "\n"

                if dry_run:
                    print(f"UPDATE: {md_path.relative_to(PROJECT_ROOT)} (add 対応・クローズ情報)")
                else:
                    md_path.write_text(new_text, encoding="utf-8")
                    print(f"Updated: {md_path.relative_to(PROJECT_ROOT)}")
                updated += 1
            else:
                # Already has the section, update values if CSV has data
                has_csv_data = any([
                    row.get("対応方針_確定", "").strip(),
                    row.get("確定日", "").strip(),
                    row.get("タスク化先", "").strip(),
                    row.get("備考", "").strip(),
                ])
                if has_csv_data:
                    text = _update_close_info_in_existing(text, row)
                    if dry_run:
                        print(f"UPDATE: {md_path.relative_to(PROJECT_ROOT)} (update 対応・クローズ情報 values)")
                    else:
                        md_path.write_text(text, encoding="utf-8")
                        print(f"Updated: {md_path.relative_to(PROJECT_ROOT)} (close info values)")
                    updated += 1
                else:
                    skipped += 1
        else:
            # Create new .md
            content = ISSUE_TEMPLATE.format(
                id=issue_id,
                title=row.get("タイトル", ""),
                date=row.get("起票日", ""),
                category=row.get("カテゴリ", ""),
                kind=row.get("種別", ""),
                status=row.get("ステータス", ""),
                priority=row.get("優先度", ""),
                related=row.get("関連施策", ""),
                detail=row.get("課題詳細", ""),
                proposal=row.get("対応方針_案", ""),
                supplement="",
                confirmed_policy=row.get("対応方針_確定", ""),
                confirmed_date=row.get("確定日", ""),
                task_target=row.get("タスク化先", ""),
                note=row.get("備考", ""),
            )

            if dry_run:
                print(f"CREATE: {md_path.relative_to(PROJECT_ROOT)}")
            else:
                md_path.write_text(content, encoding="utf-8")
                print(f"Created: {md_path.relative_to(PROJECT_ROOT)}")
            created += 1

    print(f"\nIssues migration: {created} created, {updated} updated, {skipped} skipped")


def _update_close_info_in_existing(text: str, row: dict) -> str:
    """既存 .md の対応・クローズ情報テーブルの値を CSV データで更新する。"""
    # Find the close info section
    section_match = re.search(r"^## 対応・クローズ情報\s*$", text, re.MULTILINE)
    if not section_match:
        return text

    rest = text[section_match.end():]
    next_section = re.search(r"^##\s", rest, re.MULTILINE)
    if next_section:
        section_end = section_match.end() + next_section.start()
    else:
        # Find footer ---
        footer = re.search(r"^---\s*$", rest, re.MULTILINE)
        if footer:
            section_end = section_match.end() + footer.start()
        else:
            section_end = len(text)

    new_section = """## 対応・クローズ情報

| 項目 | 内容 |
|------|------|
| 対応方針（確定） | {confirmed_policy} |
| 確定日 | {confirmed_date} |
| タスク化先 | {task_target} |
| 備考 | {note} |

""".format(
        confirmed_policy=row.get("対応方針_確定", ""),
        confirmed_date=row.get("確定日", ""),
        task_target=row.get("タスク化先", ""),
        note=row.get("備考", ""),
    )

    return text[:section_match.start()] + new_section + text[section_end:]


# --- Backlog migration ---

BACKLOG_TABLE_TEMPLATE = """# {title}

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | {bl_id} |
| **優先度** | {priority} |
| **ステータス** | {status} |
| **対象リポジトリ** | {repo} |
| **施策ディレクトリ名** | {initiative_dir} |
| **起票日** | {date} |
| **依存する環境前提** | {env_dep} |

## 課題・背景

{background}

## 期待効果

{effect}

## 補足・参考情報

{supplement}

## 関連エントリ

{related}
"""

# Priority text to emoji mapping for backlog
PRIORITY_TEXT_TO_EMOJI = {
    "高": "🔴 高",
    "中": "🟡 中",
    "低": "🔵 低",
}

# Status mapping for backlog (CSV → md)
STATUS_CSV_TO_MD = {
    "候補": "候補",
    "進行中": "initiative 開始済",
    "完了": "完了",
}


def migrate_backlog(dry_run: bool = False):
    """旧フォーマット backlog エントリをテーブル形式に変換する。"""
    if not BACKLOG_CSV_PATH.exists():
        print(f"Backlog CSV not found: {BACKLOG_CSV_PATH}", file=sys.stderr)
        return

    # Read CSV for supplementary data
    csv_data = {}
    with open(BACKLOG_CSV_PATH, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            bl_id = row.get("ID", "").strip()
            if bl_id:
                csv_data[bl_id] = row

    converted = 0

    for md_path in sorted(BACKLOG_ENTRIES_DIR.glob("*.md")):
        if md_path.name.startswith("_"):
            continue

        text = md_path.read_text(encoding="utf-8")

        # Check if old format (blockquote ID)
        id_match = re.search(r">\s*\*\*バックログ ID\*\*:\s*(\S+)", text)
        if not id_match:
            continue  # Already new format or no ID

        # Check if already has meta table
        if re.search(r"^##\s+メタ情報\s*$", text, re.MULTILINE):
            # Has meta table but also blockquote - partial migration, check if table has BL ID
            meta_text = text[re.search(r"^##\s+メタ情報\s*$", text, re.MULTILINE).end():]
            next_sec = re.search(r"^##\s", meta_text, re.MULTILINE)
            if next_sec:
                meta_text = meta_text[:next_sec.start()]
            if "バックログ ID" in meta_text:
                continue  # Already migrated

        bl_id = id_match.group(1)
        csv_row = csv_data.get(bl_id, {})

        # Extract title from H1
        h1_match = re.search(r"^# (.+)$", text, re.MULTILINE)
        title = h1_match.group(1).strip() if h1_match else md_path.stem

        # Get priority from CSV
        raw_priority = csv_row.get("優先度", "")
        priority = PRIORITY_TEXT_TO_EMOJI.get(raw_priority, raw_priority)

        # Get status from CSV
        raw_status = csv_row.get("ステータス", "候補")
        status = STATUS_CSV_TO_MD.get(raw_status, raw_status)

        # Get repo - check blockquote first, then CSV
        repo_match = re.search(r">\s*\*\*対象リポジトリ\*\*:\s*(.+)", text)
        repo = repo_match.group(1).strip() if repo_match else csv_row.get("対象リポジトリ", "")

        date = csv_row.get("起票日", "")
        initiative_dir = csv_row.get("施策ディレクトリ名", "")

        # Extract existing content sections
        # Remove blockquote lines and H1
        content_lines = []
        skip_blockquote = True
        for line in text.split("\n"):
            if skip_blockquote and (line.startswith(">") or line.startswith("# ")):
                continue
            if line.strip() and skip_blockquote:
                skip_blockquote = False
            if not skip_blockquote:
                content_lines.append(line)

        remaining_text = "\n".join(content_lines).strip()

        # Try to extract specific sections from remaining text
        background = _extract_old_section(remaining_text, ["内容", "概要", "背景", "課題・背景", "課題"])
        effect = _extract_old_section(remaining_text, ["期待効果", "提案内容", "提案"])
        supplement = _extract_old_section(remaining_text, ["補足・参考情報", "補足", "検討事項", "対象リポジトリ", "判断待ち", "発見元"])
        related = _extract_old_section(remaining_text, ["関連エントリ"])

        # If no structured sections found, use all remaining text as background
        if not background and not effect:
            # Remove any existing メタ情報 section first
            cleaned = re.sub(r"##\s+メタ情報.*?(?=^##|\Z)", "", remaining_text, flags=re.MULTILINE | re.DOTALL).strip()
            if cleaned:
                background = cleaned

        # Build new content
        new_content = BACKLOG_TABLE_TEMPLATE.format(
            title=title,
            bl_id=bl_id,
            priority=priority if priority else "🔵 低",
            status=status if status else "候補",
            repo=repo if repo else "dev-process-improvement",
            initiative_dir=initiative_dir,
            date=date,
            env_dep="",
            background=background if background else "",
            effect=effect if effect else "",
            supplement=supplement if supplement else "",
            related=related if related else "",
        ).rstrip() + "\n"

        if dry_run:
            print(f"CONVERT: {md_path.relative_to(PROJECT_ROOT)} ({bl_id})")
        else:
            md_path.write_text(new_content, encoding="utf-8")
            print(f"Converted: {md_path.relative_to(PROJECT_ROOT)} ({bl_id})")
        converted += 1

    print(f"\nBacklog migration: {converted} entries converted to table format")


def _extract_old_section(text: str, section_names: list) -> str:
    """複数のセクション名候補から内容を抽出する。"""
    for name in section_names:
        pattern = rf"^##\s+{re.escape(name)}\s*$"
        match = re.search(pattern, text, re.MULTILINE)
        if match:
            rest = text[match.end():]
            next_section = re.search(r"^##\s", rest, re.MULTILINE)
            if next_section:
                rest = rest[:next_section.start()]
            content = rest.strip()
            # Remove HTML comments
            content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL).strip()
            if content:
                return content
    return ""


def main():
    parser = argparse.ArgumentParser(description="Migrate CSV data to .md files")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, don't write files")
    args = parser.parse_args()

    print("=== Issues Migration ===")
    migrate_issues(dry_run=args.dry_run)
    print()
    print("=== Backlog Migration ===")
    migrate_backlog(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
