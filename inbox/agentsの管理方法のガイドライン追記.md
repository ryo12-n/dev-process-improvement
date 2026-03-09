.claude/skills/claude-directory-guide/SKILL.mdをdev-process-improvementにも用意したい。
同期セッションにおいて、同期対象のskillとして扱いたい。
また以下のagentsに関するベストプラクティス的な設計手法の記載を加えたい。今後の.claude/配下の設計で適切に考慮されるようにしたい。

以下が追加したい設計手法
`.claude/agents` と `.claude/skills/<特定スキル>/agents` は、どちらも「エージェントの振る舞いを定義する Markdown+YAML ファイル群」ですが、スコープと読み込まれ方が大きく異なります。[1][2][3]

## 位置づけの違い（グローバル vs スキル内）

- `.claude/agents`  
  - プロジェクト全体で使う「トップレベルのエージェント（サブエージェント）」を定義する場所。[4][1]
  - ここに置いたエージェントは、そのプロジェクト内で広く呼び出される前提の、汎用的・横断的な役割を持たせるのが基本。

- `.claude/skills/<skill-name>/agents`  
  - 特定スキルの内部だけで使う「スキル専用の下位エージェント」を定義する場所。[2][3][5]
  - スキルがトリガーされたときにだけ、そのスキル内エージェントが有効範囲に入るイメージで、あくまでスキルの実装ディテールとして扱われます。

## プロンプト構成・YAML メタデータの違い

どちらも「YAML フロントマター + 本文プロンプト」の構成ですが、想定する役割が異なります。[3][1][2]

### `.claude/agents` のエージェント

- フロントマター例（概略）  
  - `name`: エージェント名（CLI や UI から識別）  
  - `description`: どんなタスク・ドメインを担当するかの一言説明  
  - `allowed_tools`: そのエージェントが使えるツール／スキル  
  - `triggers`（あれば）: どんなリクエスト内容で呼ばれるかのパターン
- 本文プロンプト  
  - プロジェクト全体に対して一貫させたい役割・人格・出力フォーマットなどを記述。[1][4]
  - 例: 「このプロジェクトのテストコードだけを見るレビュー担当」「インフラ IaC 専門レビュー担当」など。

→ 設計的には「プロジェクト共通の役割・ポリシー」を記述する場所なので、あまりドメインに深く依存しない抽象度にしておくと再利用しやすいです。

### `.claude/skills/<skill>/agents` のエージェント

- フロントマター例（概略）  
  - `name`: スキル内での役割名（外から直接呼ばれない前提でもよい）  
  - `description`: そのスキルの処理フローの中での担当（例: 「PDF 分割プランナー」「PDF ページ抽出実行担当」）  
  - `allowed_tools`: そのスキルがバンドルしているスクリプトや外部リソースへのアクセス権  
- 本文プロンプト  
  - SKILL.md の設計方針に強く依存した、かなりタスク特化の指示を書く。[5][2][3]
  - 例:  
    - 「まず SKILL.md に定義された手順 A→B→C のうち B のみを担当し、その結果を JSON で返す」  
    - 「scripts/validate.sh を呼び、バリデーションエラーをユーザ向けメッセージに翻訳する」など。

→ こちらは「スキルの内部実装を分割するためのエージェント」であり、他スキルや他プロジェクトには見せない前提でかなり細かい前提条件・内部 API 契約まで書けるのが特徴です。

## スコープと読み込みタイミングの違い

- `.claude/agents`  
  - プロジェクト開始時（エージェント一覧の構築時）にメタデータが読み込まれ、会話のルーティングに使われます。[4][1]
  - 対話のコンテキスト内には、その時点で選ばれたエージェントの本体プロンプトだけが注入される形が多いです。

- `.claude/skills/<skill>/agents`  
  - まずスキルのメタデータ（SKILL.md の YAML）が常時軽量に保持される。[2][5]
  - ユーザリクエストがスキルにマッチしたタイミングで SKILL.md が読み込まれ、必要に応じてスキル内エージェントのプロンプトが段階的に参照される（progressive disclosure）。[3][5][2]

→ その結果として:

- `.claude/agents`: 「どのエージェントに振るか」を決めるためのトップレベルの経路選択用。  
- スキル内 agents: 「このスキルの中で、どの役割にどこまで任せるか」を決める内部オーケストレーション用。

## 設計パターンとしての使い分け

1. **プロジェクト全体のサブエージェント（共通モジュール）**  
   - レビュー用、リファクタリング用、ドキュメント整形用など「どのスキルからでも使いたい役」  
   - → `.claude/agents` に置き、説明は抽象的に、ただしインターフェース（入力/出力フォーマット）は明確に。

2. **スキル固有のワークフロー分割**  
   - 例: 「PDF 処理スキル」「バックテストスキル」などで、内部でさらに役割分担したい場合  
   - → `.claude/skills/<skill>/agents` の中に、  
     - プランニング担当  
     - 実行担当（スクリプト呼び出し）  
     - 整形・要約担当  
     のような細かいエージェントを作り、SKILL.md からそれらの役割の流れを定義。

3. **プロンプト内容の粒度**  
   - `.claude/agents`:  
     - 「このエージェントはどのプロジェクトでも使える」くらいの汎用性を目標に、ルール・スタイル・安全策などを中心に。  
   - スキル内 agents:  
     - そのスキル内の状態や内部ファイル構成（scripts/, resources/ など）を前提にしてよい。  
     - 具体的なファイル名やコマンド、ドメイン固有の業務ルールなどを遠慮なく書く。

***

もしよければ、今イメージしている「スキル + エージェント構成」（例: コーディング支援、業務フロー自動化など）の具体例を一つ教えてもらえれば、そのケースに最適なディレクトリ構成と YAML/本文プロンプトの雛形を一緒に設計します。

情報源
[1] rahulvrane/awesome-claude-agents: collection of ... - GitHub https://github.com/rahulvrane/awesome-claude-agents
[2] Agent Skills - Claude API Docs https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
[3] Pass arguments to skills https://code.claude.com/docs/en/skills
[4] Create custom subagents - Claude Code Docs https://code.claude.com/docs/en/sub-agents
[5] Claude Agent Skills: A First Principles Deep Dive - Han Lee https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/
[6] Claude Code Sub Agents Directory - AI-Powered Development Tools https://subagents.app/agents
[7] Claude Code overview - Claude Code Docs https://code.claude.com/docs/en/overview
[8] .agent folder is making claude code 10x better... - YouTube https://www.youtube.com/watch?v=MW3t6jP9AOs
[9] Special Files and Usage Guide for the .claude/ Directory - Zenn https://zenn.dev/katsuhisa_/articles/claude-directory-guide?locale=en
[10] [BUG] Claude Project MCP config should be accessible in the .claude folder · Issue #3497 · anthropics/claude-code https://github.com/anthropics/claude-code/issues/3497
[11] How to create your first Claude Skill (step-by-step, with examples) https://skywork.ai/blog/ai-agent/how-to-create-claude-skill-step-by-step-guide/
[12] anthropics/claude-code - Docs about user config directory https://github.com/anthropics/claude-code/issues/2277
[13] Get started with Agent Skills in the API - Claude Console https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart
[14] Agent design lessons from Claude Code | Jannes' Blog https://jannesklaas.github.io/ai/2025/07/20/claude-code-agent-design.html
[15] [BUG] CLAUDE_CONFIG_DIR environment variable behavior ... https://github.com/anthropics/claude-code/issues/3833


はい、その理解でほぼそのまま大丈夫です。どちらも「Claude Code の標準機能として公式に考慮されているディレクトリ構造」です。[1][2][3][4]

### 標準機能としての位置づけ

- `.claude/agents`  
  - 公式ドキュメントで「プロジェクトサブエージェント」を定義する標準パスとして説明されています。[5][1]
  - 同じ構造がグローバル設定 `~/.claude/agents/` にもあり、「ユーザレベル・プロジェクトレベルの標準的な設定ディレクトリ」という扱いです。[6][1]

- `.claude/skills`（および `~/.claude/skills`）  
  - SKILL.md を置く場所として公式に規定されていて、「ここにあるフォルダ＝スキル」として自動検出される前提になっています。[2][3][4]
  - プロジェクトローカルの `.claude/skills/`、ユーザ共通の `~/.claude/skills/`、プラグインの `skills/` など、優先度付きでマージされることも明記されています。[3][4]

### 「スキル配下の agents」について

- ドキュメント上は主に「SKILL.md を中心としたスキルフォルダ構造」が標準として定義されていて、`examples/` や `templates/`、`scripts/` 配下などは自由拡張可能な「サポートファイル」として解説されています。[4][2][3]
- その一環として、スキルフォルダの中に `agents/` を切ってエージェントを分割管理するのは、標準仕様に沿った「慣習的な構成パターン（ベストプラクティス寄り）」と考えるのが自然です（＝独自ハックではなく、公式のディレクトリ解決ロジックの範囲で動く想定のレイアウト）。[7][3]

つまり：

- `.claude/agents` … 完全に公式でサポートされている標準ディレクトリ。  
- `.claude/skills/<skill>/` … SKILL.md を起点とした「標準スキル構造」。その中で `agents/` を切るのは、この標準構造の上に乗った整理テクニック、というイメージで OK です。[2][3]

この前提でいうと、今後も「この構造を前提にした機能追加」がされていく可能性が高いので、積極的に乗っかって設計してしまって良いラインだと思います。  

スキル配下に `agents/` を切るとき、今のところは「どの程度まで細かく分割するか」が設計ポイントになるので、一般的な分割指針（プランナー／実行／整形など）の具体例も見たいですか？

情報源
[1] Create custom subagents - Claude Code Docs https://code.claude.com/docs/en/sub-agents
[2] Extend Claude with skills - Claude Code Docs https://code.claude.com/docs/en/skills
[3] Skills - .claude Directory https://dotclaude.com/skills
[4] How to Use Skills in Claude Code (2026) | CAIO https://www.thecaio.ai/blog/claude-code-skills
[5] Claude Code作者が全公開！9種のカスタマイズ手段と設定の全貌 https://qiita.com/dai_chi/items/252fb5ef031127784757
[6] Understand configuration directories in Claude Code - M.academy https://m.academy/lessons/understand-configuration-directories-claude-code/
[7] 【Claude Code】CLAUDE.mdとフォルダ構成で ... - DevelopersIO https://dev.classmethod.jp/articles/claude-code-directory-autonomy/
[8] Claude Codeが作成する~/.claudeディレクトリの詳細解析 https://tech-lab.sios.jp/archives/48303
[9] Claude Code overview - Claude Code Docs https://code.claude.com/docs/en/overview
[10] How I structure Claude Code projects (CLAUDE.md, Skills, MCP) https://www.reddit.com/r/ClaudeAI/comments/1r66oo0/how_i_structure_claude_code_projects_claudemd/
[11] How Claude remembers your project - Claude Code Docs https://code.claude.com/docs/en/memory
[12] カスタムサブエージェントの作成 - Claude Code Docs https://code.claude.com/docs/ja/sub-agents
[13] Intelligent automation and multi-agent orchestration for Claude Code https://github.com/wshobson/agents
[14] The .claude/ directory is the key to supercharged dev workflows! 🦾 https://www.reddit.com/r/ClaudeAI/comments/1mnikpr/the_claude_directory_is_the_key_to_supercharged/
[15] Claude Code Agents - 60+ Prompts, 230+ Plugins & Skills https://claudecodeagents.com
