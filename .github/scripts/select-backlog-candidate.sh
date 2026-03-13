#!/usr/bin/env bash
# select-backlog-candidate.sh
#
# backlog/backlog.csv を読み込み、以下の条件でフィルタして最古の1件を選択する:
#   - 優先度 = 低
#   - ステータス = 候補
#   - 対象リポジトリ = dev-process-improvement
#
# 結果を $GITHUB_OUTPUT に出力する:
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

# CSV ヘッダ: 施策名,優先度,ステータス,対象リポジトリ,起票日,簡易説明,ファイル名,施策ディレクトリ名
# 列番号:      $1     $2     $3         $4             $5     $6       $7       $8

# awk でフィルタ・ソートし、最古の1件を選択
# 注: CSV のフィールドにカンマが含まれる場合を考慮し、単純なカンマ分割を使用
#     （現在の backlog.csv にはカンマを含むフィールドは存在しない）
candidate=$(awk -F',' '
  NR == 1 { next }  # ヘッダ行スキップ
  /^[[:space:]]*$/ { next }  # 空行スキップ
  {
    # 各フィールドの前後空白を除去
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $2)  # 優先度
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $3)  # ステータス
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $4)  # 対象リポジトリ
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $5)  # 起票日

    if ($2 == "低" && $3 == "候補" && $4 == "dev-process-improvement") {
      # 起票日|施策名|ファイル名|簡易説明 の形式で出力
      print $5 "|" $1 "|" $7 "|" $6
    }
  }
' "$CSV_FILE" | sort -t'|' -k1,1 | head -n 1)

if [[ -z "$candidate" ]]; then
  echo "No candidate found" >&2
  echo "has_candidate=false" >> "$GITHUB_OUTPUT"
  exit 0
fi

# パイプ区切りで分割
IFS='|' read -r _date name file description <<< "$candidate"

echo "has_candidate=true" >> "$GITHUB_OUTPUT"
echo "name=$name" >> "$GITHUB_OUTPUT"
echo "file=$file" >> "$GITHUB_OUTPUT"
echo "description=$description" >> "$GITHUB_OUTPUT"

echo "Selected candidate: $name (file: $file, date: $_date)"
