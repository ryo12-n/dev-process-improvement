# 実装ワークログ: [施策名] - Worker W<N>

> **このファイルの役割**: Worker W<N> の作業ログ。壁打ちフェーズとチェックポイントを記録する。
> 各セクションのプレースホルダーを埋めて使用する。

## Worker 情報

- **Worker ID**: W<N>
- **担当タスク**: IMPL-XXX
- **Wave**: Wave M
- **Worktree パス**: （マネージャーから指定）
- **ブランチ**: impl/<施策名>-W<N>

---

## 壁打ちフェーズ [YYYY-MM-DD HH:MM]

### 理解のサマリー
- タスクの目的:
- 割り当てタスク: IMPL-XXX
- 対象ファイル:
- テストコマンド:

### 前提条件チェック
- [ ] 設計ドキュメント（02_impl_design.md）の確認: （確認済み / 要確認）
- [ ] worktree パスのアクセス確認: （確認済み / 要確認）
- [ ] per-worker ブランチへのチェックアウト: （確認済み / 要確認）
- [ ] テスト環境の動作確認: （確認済み / 要確認）

### 不明点・確認事項
<!-- 不明点がなければ「なし」と記載 -->

---

## チェックポイント

### [YYYY-MM-DD HH:MM] CHECKPOINT: START
- **Task**: IMPL-XXX
- **Assigned files**: <!-- ファイルリストを記入 -->
- **Branch**: impl/<施策名>-W<N>

---

### [YYYY-MM-DD HH:MM] CHECKPOINT: TEST-RUN-1
- **Command**: <!-- テストコマンドを記入 -->
- **Result**: <!-- PASS / FAIL -->
- **Details**: <!-- テスト出力の要約 -->
- **Action**: <!-- FAIL の場合: 修正内容 -->

### [YYYY-MM-DD HH:MM] CHECKPOINT: TEST-RUN-2
<!-- テストリトライ時のみ記入。不要なら削除 -->
- **Command**:
- **Result**: <!-- PASS / FAIL -->
- **Details**:
- **Action**:

### [YYYY-MM-DD HH:MM] CHECKPOINT: TEST-RUN-3
<!-- テストリトライ時のみ記入。不要なら削除 -->
- **Command**:
- **Result**: <!-- PASS / FAIL -->
- **Details**:
- **Action**:

---

<!-- 以下、COMPLETE または ESCALATE のいずれかを記入する -->

### [YYYY-MM-DD HH:MM] CHECKPOINT: COMPLETE
- **Task**: IMPL-XXX
- **Commits**: <!-- コミットハッシュのリスト -->
- **Files changed**: <!-- 変更ファイルリスト -->
- **Test result**: <!-- PASS (attempt N of 3) -->
- **Push status**: <!-- pushed to origin/impl/<施策名>-W<N> -->

### [YYYY-MM-DD HH:MM] CHECKPOINT: ESCALATE
<!-- エスカレーション時のみ記入 -->
- **Task**: IMPL-XXX
- **Reason**: <!-- エスカレーション理由 -->
- **Attempted fixes**: <!-- 試行した修正のリスト -->
- **Recommendation**: <!-- 推奨される解決策 -->

---

### [YYYY-MM-DD HH:MM] COMPLETION CHECKLIST
- [ ] COMPLETE or ESCALATE チェックポイントを記録済み
- [ ] テスト結果を TEST-RUN チェックポイントに記録済み
- [ ] per-worker ブランチにコミット・プッシュ済み
  - ブランチ: impl/<施策名>-W<N>
  - git diff --name-only の出力を記録
- [ ] 課題があれば 07_issues_W<N>.md に起票済み
  （課題なし → 「課題なし」と記載）
- [ ] 変更ファイルが Assigned files の範囲内であることを確認
