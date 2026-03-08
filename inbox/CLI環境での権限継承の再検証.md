# CLI 環境での権限継承の再検証

## 気づき

`subagent-permission-model` 施策の実機検証は Claude Agent SDK 環境で実施されたため、Claude Code CLI の対話型環境での Task ツール起動時の権限継承挙動は未検証。

## 背景

本施策の発端は CLI 環境で「allow リストに含まれるコマンドに対して許可プロンプトが出る」という現象だったが、検証は SDK 環境で行われ、CLI 環境の問題は未解決のまま。

## 提案

CLI の対話型環境で Task ツールを使ってサブエージェントを起動し、以下を検証:
- allow リストのコマンドが許可プロンプトなしで実行されるか
- deny リストのコマンドが拒否されるか
- tools フィールドの制限が適用されるか

## 発見元

- 施策: `sessions/initiatives/subagent-permission-model/`
- 作業レポート: `04_work_report.md` 申し送り事項
- 評価レポート: `06_eval_report.md` 参考情報 #1
