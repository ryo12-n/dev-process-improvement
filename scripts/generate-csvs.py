#!/usr/bin/env python3
"""
CSV 自動生成スクリプト

個別 .md ファイル（正の情報源）から CSV を生成する。
- issues/entries/ISS-*.md → プロセス改善_課題管理.csv
- backlog/entries/*.md → backlog/backlog.csv

Usage:
    python3 scripts/generate-csvs.py          # CSV を生成（上書き）
    python3 scripts/generate-csvs.py --check  # 差分検出のみ（変更があれば exit 1）
    python3 scripts/generate-csvs.py --next-issue-id    # 次の ISS-XXX ID を出力
    python3 scripts/generate-csvs.py --next-backlog-id  # 次の BL-XXX ID を出力
"""

import argparse
import csv
import io
import os
import re
import sys
from pathlib import Path

# プロジェクトルートを基準にする
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

# --- Issues CSV ---

ISSUES_CSV_COLUMNS = [
    "ID", "起票日", "カテゴリ", "種別", "タイトル", "課題詳細",
    "対応方針_案", "ステータス", "優先度", "関連施策", "タスク化先",
    "対応方針_確定", "確定日", "備考", "詳細ファイル"
]

ISSUES_ENTRIES_DIR = PROJECT_ROOT / "issues" / "entries"
ISSUES_CSV_PATH = PROJECT_ROOT / "プロセス改善_課題管理.csv"


def parse_issue_md(filepath: Path) -> dict | None:
    """ISS-XXX.md をパースして CSV 行の dict を返す。"""
    text = filepath.read_text(encoding="utf-8")

    # ID from filename
    match = re.match(r"(ISS-\d+)\.md$", filepath.name)
    if not match:
        print(f"Warning: Skipping {filepath.name} (filename does not match ISS-XXX.md)", file=sys.stderr)
        return None
    issue_id = match.group(1)

    row = {col: "" for col in ISSUES_CSV_COLUMNS}
    row["ID"] = issue_id
    row["詳細ファイル"] = f"issues/entries/{filepath.name}"

    # Parse 基本情報 table
    basic_info = _parse_md_table(text, "基本情報")
    if basic_info:
        field_map = {
            "ID": "ID",
            "起票日": "起票日",
            "カテゴリ": "カテゴリ",
            "種別": "種別",
            "ステータス": "ステータス",
            "優先度": "優先度",
            "関連施策": "関連施策",
        }
        for md_key, csv_key in field_map.items():
            if md_key in basic_info:
                row[csv_key] = basic_info[md_key]

    # Title from H1
    h1_match = re.search(r"^# (?:ISS-\d+:\s*)?(.+)$", text, re.MULTILINE)
    if h1_match:
        row["タイトル"] = h1_match.group(1).strip()

    # 課題詳細 section
    row["課題詳細"] = _extract_section_text(text, "課題詳細")

    # 対応方針（案）section
    row["対応方針_案"] = _extract_section_text(text, "対応方針（案）")

    # 補足・参照 - not in CSV, skip

    # 対応・クローズ情報 table
    close_info = _parse_md_table(text, "対応・クローズ情報")
    if close_info:
        close_map = {
            "対応方針（確定）": "対応方針_確定",
            "確定日": "確定日",
            "タスク化先": "タスク化先",
            "備考": "備考",
        }
        for md_key, csv_key in close_map.items():
            if md_key in close_info:
                val = close_info[md_key]
                # Remove HTML comments
                val = re.sub(r"<!--.*?-->", "", val).strip()
                if val:
                    row[csv_key] = val

    return row


def _parse_md_table(text: str, section_name: str) -> dict | None:
    """Markdown の2列テーブル（| key | value |）をセクション名から探してパースする。"""
    # Find the section
    pattern = rf"^##\s+{re.escape(section_name)}\s*$"
    section_match = re.search(pattern, text, re.MULTILINE)
    if not section_match:
        return None

    # Get text after section header until next ## or end
    rest = text[section_match.end():]
    next_section = re.search(r"^##\s", rest, re.MULTILINE)
    if next_section:
        rest = rest[:next_section.start()]

    result = {}
    for line in rest.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        # parts[0] and parts[-1] are empty (before first | and after last |)
        parts = [p for p in parts if p]
        if len(parts) >= 2:
            key = parts[0].strip("* ")
            val = parts[1].strip()
            # Remove HTML comments from values
            val = re.sub(r"<!--.*?-->", "", val).strip()
            # Skip separator rows
            if re.match(r"^[-:]+$", key) or re.match(r"^[-:]+$", val):
                continue
            # Skip header-like rows
            if key in ("項目", "項目 "):
                continue
            result[key] = val

    return result if result else None


def _extract_section_text(text: str, section_name: str) -> str:
    """セクション名の配下のテキストを抽出する（コメント・空行を除く）。"""
    pattern = rf"^##\s+{re.escape(section_name)}\s*$"
    section_match = re.search(pattern, text, re.MULTILINE)
    if not section_match:
        return ""

    rest = text[section_match.end():]
    next_section = re.search(r"^##\s", rest, re.MULTILINE)
    if next_section:
        rest = rest[:next_section.start()]

    # Remove HTML comments
    rest = re.sub(r"<!--.*?-->", "", rest, flags=re.DOTALL)
    # Strip and join
    lines = [l.strip() for l in rest.strip().split("\n")]
    lines = [l for l in lines if l]
    return " ".join(lines) if lines else ""


def generate_issues_csv() -> str:
    """issues/entries/ から CSV テキストを生成して返す。"""
    entries_dir = ISSUES_ENTRIES_DIR
    if not entries_dir.exists():
        return ""

    rows = []
    for f in sorted(entries_dir.glob("ISS-*.md")):
        row = parse_issue_md(f)
        if row:
            rows.append(row)

    # Sort by ID numerically
    rows.sort(key=lambda r: int(re.search(r"\d+", r["ID"]).group()))

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=ISSUES_CSV_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


# --- Backlog CSV ---

BACKLOG_CSV_COLUMNS = [
    "ID", "施策名", "優先度", "ステータス", "対象リポジトリ",
    "起票日", "簡易説明", "ファイル名", "施策ディレクトリ名"
]

BACKLOG_ENTRIES_DIR = PROJECT_ROOT / "backlog" / "entries"
BACKLOG_CSV_PATH = PROJECT_ROOT / "backlog" / "backlog.csv"

# Priority emoji to text mapping
PRIORITY_EMOJI_TO_TEXT = {
    "🔴 高": "高",
    "🟡 中": "中",
    "🔵 低": "低",
    "🟢 低": "低",
    "🔴": "高",
    "🟡": "中",
    "🔵": "低",
    "🟢": "低",
    "高": "高",
    "中": "中",
    "低": "低",
}

# Status mapping (normalize)
STATUS_MAP = {
    "候補": "候補",
    "起票済み": "起票済み",
    "initiative 開始済": "進行中",
    "進行中": "進行中",
    "完了": "完了",
}


def parse_backlog_md(filepath: Path) -> dict | None:
    """backlog entry .md をパースして CSV 行の dict を返す。"""
    text = filepath.read_text(encoding="utf-8")

    row = {col: "" for col in BACKLOG_CSV_COLUMNS}
    row["ファイル名"] = filepath.name

    # Try new format (meta table) first
    meta = _parse_md_table(text, "メタ情報")
    if meta:
        row["ID"] = meta.get("バックログ ID", "")
        raw_priority = meta.get("優先度", "")
        row["優先度"] = PRIORITY_EMOJI_TO_TEXT.get(raw_priority, raw_priority)
        raw_status = meta.get("ステータス", "")
        row["ステータス"] = STATUS_MAP.get(raw_status, raw_status)
        row["対象リポジトリ"] = meta.get("対象リポジトリ", "")
        row["起票日"] = meta.get("起票日", "")
        row["施策ディレクトリ名"] = meta.get("施策ディレクトリ名", "")

    # Also check blockquote format (some files have both, or only blockquote)
    id_match = re.search(r">\s*\*\*バックログ ID\*\*:\s*(\S+)", text)
    if not row["ID"] and id_match:
        row["ID"] = id_match.group(1)

    repo_match = re.search(r">\s*\*\*対象リポジトリ\*\*:\s*(.+)", text)
    if not row["対象リポジトリ"] and repo_match:
        row["対象リポジトリ"] = repo_match.group(1).strip()

    # Title from H1
    h1_match = re.search(r"^# (.+)$", text, re.MULTILINE)
    if h1_match:
        row["施策名"] = h1_match.group(1).strip()

    # 簡易説明: Try "概要" or "課題・背景" section first line
    desc = _extract_section_text(text, "概要")
    if not desc:
        desc = _extract_section_text(text, "課題・背景")
    if not desc:
        desc = _extract_section_text(text, "期待効果")
    if desc:
        # Truncate to reasonable length
        row["簡易説明"] = desc[:200] if len(desc) > 200 else desc

    if not row["ID"]:
        print(f"Warning: No ID found in {filepath.name}, skipping", file=sys.stderr)
        return None

    return row


def generate_backlog_csv() -> str:
    """backlog/entries/ から CSV テキストを生成して返す。"""
    entries_dir = BACKLOG_ENTRIES_DIR
    if not entries_dir.exists():
        return ""

    rows = []
    for f in sorted(entries_dir.glob("*.md")):
        if f.name.startswith("_"):
            continue  # Skip _template.md
        row = parse_backlog_md(f)
        if row:
            rows.append(row)

    # Sort by ID numerically
    rows.sort(key=lambda r: int(re.search(r"\d+", r["ID"]).group()) if re.search(r"\d+", r["ID"]) else 0)

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=BACKLOG_CSV_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


# --- Next ID ---

def get_next_issue_id() -> str:
    entries_dir = ISSUES_ENTRIES_DIR
    max_id = 0
    if entries_dir.exists():
        for f in entries_dir.glob("ISS-*.md"):
            m = re.search(r"ISS-(\d+)", f.name)
            if m:
                max_id = max(max_id, int(m.group(1)))
    return f"ISS-{max_id + 1:03d}"


def get_next_backlog_id() -> str:
    entries_dir = BACKLOG_ENTRIES_DIR
    max_id = 0
    if entries_dir.exists():
        for f in entries_dir.glob("*.md"):
            if f.name.startswith("_"):
                continue
            text = f.read_text(encoding="utf-8")
            m = re.search(r"BL-(\d+)", text)
            if m:
                max_id = max(max_id, int(m.group(1)))
    return f"BL-{max_id + 1:03d}"


# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="Generate CSV files from .md entries")
    parser.add_argument("--check", action="store_true", help="Check mode: exit 1 if CSV would change")
    parser.add_argument("--next-issue-id", action="store_true", help="Print next available ISS-XXX ID")
    parser.add_argument("--next-backlog-id", action="store_true", help="Print next available BL-XXX ID")
    args = parser.parse_args()

    if args.next_issue_id:
        print(get_next_issue_id())
        return

    if args.next_backlog_id:
        print(get_next_backlog_id())
        return

    issues_csv = generate_issues_csv()
    backlog_csv = generate_backlog_csv()

    if args.check:
        changed = False
        if ISSUES_CSV_PATH.exists():
            existing = ISSUES_CSV_PATH.read_text(encoding="utf-8")
            if existing != issues_csv:
                print(f"CHANGED: {ISSUES_CSV_PATH.relative_to(PROJECT_ROOT)}")
                changed = True
        else:
            if issues_csv:
                print(f"NEW: {ISSUES_CSV_PATH.relative_to(PROJECT_ROOT)}")
                changed = True

        if BACKLOG_CSV_PATH.exists():
            existing = BACKLOG_CSV_PATH.read_text(encoding="utf-8")
            if existing != backlog_csv:
                print(f"CHANGED: {BACKLOG_CSV_PATH.relative_to(PROJECT_ROOT)}")
                changed = True
        else:
            if backlog_csv:
                print(f"NEW: {BACKLOG_CSV_PATH.relative_to(PROJECT_ROOT)}")
                changed = True

        if changed:
            sys.exit(1)
        else:
            print("No changes detected.")
            sys.exit(0)
    else:
        # Write CSVs
        ISSUES_CSV_PATH.write_text(issues_csv, encoding="utf-8")
        print(f"Generated: {ISSUES_CSV_PATH.relative_to(PROJECT_ROOT)}")

        BACKLOG_CSV_PATH.write_text(backlog_csv, encoding="utf-8")
        print(f"Generated: {BACKLOG_CSV_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
