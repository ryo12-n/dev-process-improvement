#!/usr/bin/env bash
# select-backlog-candidate.sh
#
# backlog/backlog.csv を読み込み、以下の条件でフィルタして最適な1件を選択する:
#   - ステータス = 候補
#   - 対象リポジトリ = dev-process-improvement
#
# ソート順: 優先度ASC（低=1, 中=2, 高=3）→ 起票日ASC
#
# 結果を $GITHUB_OUTPUT に出力する:
#   - id: バックログ ID（BL-XXX 形式）
#   - name: 施策名
#   - file: バックログエントリファイル名
#   - description: 簡易説明
#   - has_candidate: true/false

set -euo pipefail

CSV_FILE="backlog/backlog.csv"

if [[ ! -f "$CSV_FILE" ]]; then
  echo "Error: $CSV_FILE not found" >&2
  echo "has_candidate=false" >> "$GITHUB_OUTPUT"
  exit 0
fi

# CSV ヘッダ: ID,施策名,優先度,ステータス,対象リポジトリ,起票日,簡易説明,ファイル名,施策ディレクトリ名
# 列番号:     $1  $2    $3     $4         $5             $6     $7       $8       $9

# awk でフィルタ・ソートし、最適な1件を選択
# 優先度を数値に変換してソートキーに使用（低=1, 中=2, 高=3）
# 注: CSV のフィールドにカンマが含まれる場合を考慮し、単純なカンマ分割を使用
#     （現在の backlog.csv にはカンマを含むフィールドは存在しない）
candidate=$(awk -F',' '
  NR == 1 { next }  # ヘッダ行スキップ
  /^[[:space:]]*$/ { next }  # 空行スキップ
  {
    # 各フィールドの前後空白を除去
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $1)  # ID
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $3)  # 優先度
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $4)  # ステータス
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $5)  # 対象リポジトリ
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $6)  # 起票日

    if ($4 == "候補" && $5 == "dev-process-improvement") {
      # 優先度を数値に変換
      priority_num = 9  # デフォルト（不明な優先度は最後）
      if ($3 == "低") priority_num = 1
      else if ($3 == "中") priority_num = 2
      else if ($3 == "高") priority_num = 3

      # 優先度数値|起票日|ID|施策名|ファイル名|簡易説明 の形式で出力
      print priority_num "|" $6 "|" $1 "|" $2 "|" $8 "|" $7
    }
  }
' "$CSV_FILE" | sort -t'|' -k1,1n -k2,2 | head -n 1)

if [[ -z "$candidate" ]]; then
  echo "No candidate found" >&2
  echo "has_candidate=false" >> "$GITHUB_OUTPUT"
  exit 0
fi

# パイプ区切りで分割
IFS='|' read -r _priority _date id name file description <<< "$candidate"

echo "has_candidate=true" >> "$GITHUB_OUTPUT"
echo "id=$id" >> "$GITHUB_OUTPUT"
echo "name=$name" >> "$GITHUB_OUTPUT"
echo "file=$file" >> "$GITHUB_OUTPUT"
echo "description=$description" >> "$GITHUB_OUTPUT"

echo "Selected candidate: $name (id: $id, file: $file, priority: $_priority, date: $_date)"
