# BMS (Business Management System)

このリポジトリは、ビジネスマネジメントシステムの包括的なドキュメントとリソースを管理するためのものです。

- document: 論文や公式のドキュメント
- information: 手法やプロセス、テクニックなど
- workspace: 各種作業

# システムプロンプト

## 重要：各ディレクトリのai_agent_rule参照について
作業を開始する前に、以下の手順で必要な情報を必ず確認してください：

1. 最上位階層（このファイル）のai_agent_ruleを熟読し、全体の構造を理解する
2. **作業対象となる全てのディレクトリのai_agent_ruleを必ず読む**
   - document/app_specifications/ai_agent_rule
   - information/consult_techniques/ai_agent_rule
   - workspace/daily_reflections_workspace/ai_agent_rule
   - information/emotional_story/ai_agent_rule
   - workspace/ideas_workspace/ai_agent_rule
   - log/ai_agent_rule
   - workspace/note_workspace/ai_agent_rule
   - workspace/novel_workspace/ai_agent_rule
   - prompts/ai_agent_rule
   - workspace/sales_workspace/ai_agent_rule
   - information/sales_techniques/ai_agent_rule
   - workspace/business_tasks/ai_agent_rule
   - workspace/private_tasks/ai_agent_rule
   - tools/ai_agent_rule
   - その他のサブディレクトリのtools/ai_agent_rule
3. 作業内容に関連する可能性のある全てのディレクトリのai_agent_ruleを参照する
4. ai_agent_ruleの内容は随時更新される可能性があるため、作業ごとに最新の内容を確認する

## 共通ルール
- 日本語で応対
- 「D:\BMS」直下にフォルダを作るときは必ずtools/ai_agent_ruleファイルを作成
- 依頼するほとんどのタスクはコーディングとは関係ないことを考慮
- powershellでは「&&」を使用しない
- 絶対に生成時に省略行為は行わない
- すべてのタスク実行時にlog/tools/ai_agent_ruleに従って作業ログを記録する

## テスト駆動処理
- 必ずタスクはテストドリブンで処理を行う
- タスクに合わせた詳細なテスト項目を事前に作成
- テスト用に別途ファイルを作成
- テスト粒度は細かく設定し、クリアするまで自動で反復

# プロジェクト構造

## tools/ - AIツール
AIが活用する各種ツールを格納するディレクトリ。各ツールは独自のフォルダで管理され、以下の構造に従います：
```
tools/
├── ai_agent_rule.md
└── [tool_name]/
    ├── README.md
    ├── requirements.txt
    └── src/
```
- 各ツールは独立して動作する形で実装
- テスト駆動での開発を徹底
- セキュリティとメンテナンス性を重視

## document/ - 論文や公式のドキュメント
### document/app_specifications/
アプリケーションの技術仕様を格納するディレクトリ
- `api_specifications/` - APIインターフェースの詳細仕様


### document/tech_docs/ - 技術ドキュメント管理
プログラミング言語、フレームワーク、パッケージ、開発ツールのドキュメントを体系的に管理するディレクトリ。

#### ディレクトリ構造
```
tech_docs/
├── ai_agent_rule.md
├── languages/          - プログラミング言語のドキュメント
├── frameworks/         - フレームワークのドキュメント
├── packages/          - パッケージのドキュメント
└── tools/             - 開発ツールのドキュメント
```

#### ドキュメント管理ルール
1. ファイル命名規則
   - 形式：`[カテゴリ名]_[技術名]_[バージョン].md`
   - 例：`python_basic_3.11.md`

2. メタデータ管理
   - バージョン情報の明記
   - 更新日の記録
   - 関連リンクの管理
   - 互換性情報の記載

3. コンテンツ要件
   - 公式ドキュメントへのリンク
   - 動作確認済みのコードサンプル
   - 環境要件の明記
   - 日本語/英語両方のリソース

### document/papers/ - 研究論文管理
主にLLM（Large Language Model）関連の研究論文を体系的に管理するディレクトリ。

#### ディレクトリ構造
```
papers/
├── ai_agent_rule.md
└── llm/
    ├── applications/    - LLMの応用研究論文
    ├── architectures/   - モデル構造研究論文
    ├── evaluations/     - 評価手法研究論文
    ├── fine_tuning/     - 適応学習研究論文
    └── prompting/       - プロンプト工学研究論文
```

#### 論文管理ルール
1. ファイル命名規則
   - 形式：`YYYY_AuthorName_Title.pdf`
   - 年号は論文の発表年を使用
   - 著者名は筆頭著者のみ使用
   - タイトルは主要な単語をCamelCaseで連結

2. メタデータ管理
   - 各フォルダの`index.md`に論文の要約、キーワード、主要な発見を記録
   - 実装コードへのリンクがある場合は保存

3. 分類基準
   - applications/ - 実用的な応用や実装に関する論文
   - architectures/ - モデルアーキテクチャや構造に関する論文
   - evaluations/ - 評価手法や性能測定に関する論文
   - fine_tuning/ - ファインチューニングや適応学習に関する論文
   - prompting/ - プロンプトエンジニアリングに関する論文

## information/ - 手法やプロセス、テクニック
### information/sales_techniques/
営業技法とノウハウのナレッジベース。効果的な営業活動のための理論的フレームワーク、業界標準のベストプラクティス、および方法論を提供します。
- analysis/ - 顧客分析手法とフレームワーク
- follow_up/ - フォローアップ戦略と理論
- negotiation/ - 交渉スキルと理論体系
- presentation/ - プレゼンテーション技法の体系
- processes/ - 営業プロセスの方法論
- storytelling/ - ストーリーテリング手法の体系

## workspace/ - 各種作業
### workspace/daily_reflections_workspace/
日々の所感と課題管理のためのディレクトリ。ビジネスとプライベートの振り返りを体系的に管理します。

#### ディレクトリ構造
```
workspace/daily_reflections_workspace/
├── business/           # ビジネス関連の日記
│   └── YYYYMMDD/
│       └── reflection.md
├── private/           # プライベート関連の日記
│   └── YYYYMMDD/
│       └── reflection.md
└── prompts/          # 日々の振り返り用プロンプト
```

#### 記載内容
- ビジネス関連（business/）
  - プロンプトに従った業務記録
  - 業務上の気づきと改善案
  - プロジェクトの進捗状況
  - 技術的な学びと共有事項
  - 組織での課題分析
  - キャリアに関する考察

- プライベート関連（private/）
  - プロンプトに従った個人記録
  - 個人的な所感と気づき
  - 趣味や活動の記録
  - 生活改善のヒント
  - 自己啓発の進捗
  - その他の重要事項

#### 使用方法
1. 新規記録作成時は日付フォルダを作成（YYYYMMDD形式）
2. `/prompts`から適切なプロンプトを選択
3. reflection.mdに記録を作成
4. 記載内容は具体的かつ詳細に
5. ビジネス/プライベートを適切に分類

#### メンテナンス
- 定期的な振り返りと分析の実施
- 重要な気づきのプロジェクト反映
- プロンプトの有効性評価と改善

### workspace/ideas_workspace/
創造的なアイデア管理とプロセスに関するドキュメント
- `created_idea/` - 生成されたアイデアの管理
- `idea_process/` - アイデア創出プロセスとテンプレート
  - テストケース
  - スコアリングガイド
  - プロセステンプレート
- `prompts/` - アイデア生成用プロンプト

### workspace/note_workspace/
note執筆のためのディレクトリ。執筆中の文章と過去の文章を体系的に管理します。

#### ディレクトリ構造
```
workspace/note_workspace/
├── past_articles/        # 完成した過去の文章
│   └── YYYYMMDD/        # 作成日付ごとのフォルダ
│       └── 作品名.md
├── writing_in_progress/ # 執筆中の文章
│   └── note_name/      # 記事ごとのフォルダ
│       ├── 要件.md     # 記事の要件定義
│       └── 文章.md     # 実際の記事
├── prompts/            # 記事作成用プロンプト
└── README.md
```

#### 使用方法
1. 新規記事作成時：
   - writing_in_progress/に記事名のフォルダを作成
   - 要件.mdで記事の要件を定義
   - 文章.mdで実際の記事を執筆
2. 記事完成時：
   - past_articles/に日付フォルダを作成（YYYYMMDD形式）
   - 完成した記事を移動
3. 文体の統一：
   - 過去の記事を参考に文体を統一
   - 要件定義に従って執筆

### workspace/novel_workspace/
小説制作と管理のためのリソース
- `created_story/` - 作成された物語の設定と管理
  - キャラクター設定
  - 魔法規制
  - 世界観設定
  - テストケース
- `creation_process/` - 小説制作プロセスのテンプレートと手順書
  - チャプター構造
  - キャラクター
  - プロット
  - シーン
  - レビュー
- `prompts/` - 小説制作用プロンプト

### workspace/sales_workspace/
実際の営業活動の実務管理用ディレクトリ。
- customers/ - 顧客ごとの情報管理（日報・月報など）
- projects/ - プロジェクトごとの進捗管理
- reports/ - 営業報告書
- tools/ - 営業支援ツール
- prompts/ - 営業活動用プロンプト
### workspace/business_tasks/
ビジネスタスク管理システム。tasklist.tsvでタスク一覧を管理し、日付ごとのフォルダでタスクを整理します。

```
business_tasks/
├── tasklist.tsv           # タスク一覧・進捗管理
├── input/                 # 初期インプットデータ置き場
├── daily/                 # 日次タスク
│   └── YYYYMMDD/         # 日付ごとのフォルダ
│       └── task_name/    # タスク別フォルダ
│           ├── input/    # 移動済みインプットデータ
│           ├── output/   # タスク成果物
│           └── task_detail.md
├── monthly/              # 月次タスク（daily同様の構造）
├── projects/             # プロジェクト単位のタスク
│   └── project_name/    # プロジェクト別フォルダ
│       ├── project_detail.md  # プロジェクト詳細
│       ├── input/      # プロジェクトの入力データ
│       └── output/     # プロジェクトの成果物
├── playground/          # 人間とAIの協業作業スペース
└── archive/             # 完了タスクのアーカイブ
```

### workspace/private_tasks/
プライベートタスク管理システム。tasklist.tsvでタスク一覧を管理し、日付ごとのフォルダでタスクを整理します。

```
private_tasks/
├── tasklist.tsv           # タスク一覧・進捗管理
├── input/                 # 初期インプットデータ置き場
├── daily/                 # 日次タスク
│   └── YYYYMMDD/         # 日付ごとのフォルダ
│       └── task_name/    # タスク別フォルダ
│           ├── input/    # 移動済みインプットデータ
│           ├── output/   # タスク成果物
│           └── task_detail.md
├── monthly/              # 月次タスク（daily同様の構造）
├── projects/             # プロジェクト単位のタスク
│   └── project_name/    # プロジェクト別フォルダ
│       ├── project_detail.md  # プロジェクト詳細
│       ├── input/      # プロジェクトの入力データ
│       └── output/     # プロジェクトの成果物
├── playground/          # 人間とAIの協業作業スペース
└── archive/             # 完了タスクのアーカイブ
```
- `prompts/` - タスク管理用プロンプト

## log/ - タスクログ管理
タスクの進捗管理と記録のためのディレクトリ

#### ディレクトリ構造
```
log/
├── README.md
└── YYYYMMDD/
    ├── task_description.md
    └── progress.md
```

#### 使用方法
1. 新規タスク開始時：YYYYMMDDフォーマットでフォルダを作成
2. 各タスクフォルダには以下を含める：
   - task_description.md：タスクの詳細説明
   - progress.md：進捗状況の記録

## 使用方法

### タスク管理のルール
1. ビジネスタスクの場合：
   - ビジネス関連のタスクは `workspace/business_tasks/daily/YYYYMMDD/task_name` ディレクトリに起票
   - `YYYYMMDD` はタスクが依頼された日付（例: 20250117）
   - `task_name` はタスクの内容を簡潔に表した名称
   - 合わせて`task_name` ディレクトリに `input` 、`output`フォルダを作成してください。
   - 目的に応じて適切なプロンプトを選択
   - task_detail.mdテンプレートに従って記録

2. プライベートタスクの場合：
   - プライベート関連のタスクは `workspace/private_tasks/daily/YYYYMMDD/task_name` ディレクトリに起票
   - `YYYYMMDD` はタスクが依頼された日付（例: 20250117）
   - `task_name` はタスクの内容を簡潔に表した名称
   - 合わせて`task_name` ディレクトリに `input` 、`output`フォルダを作成してください。
   - 目的に応じて適切なプロンプトを選択
   - task_detail.mdテンプレートに従って記録

3. playground環境の使用：
   - 人間とAIが協業して一時的にファイルを編集する作業スペース
   - business_tasksまたはprivate_tasksのplaygroundディレクトリを使用
   - 作業完了後は適切なフォルダ（daily/monthly/projects）に移動
   - 一時的な実験や検証にも使用可能

### 一般的な使用方法
各ディレクトリには独自のai_agent_ruleファイルが含まれており、それぞれの領域の詳細な使用方法とガイドラインが記載されています。特定の領域の作業を開始する際は、該当するディレクトリのドキュメントを参照してください。

## 開発環境

- Node.js v20.12.2
- npm 10.5.0
- pnpm 9.15.4

## メンテナンス

各セクションのドキュメントは定期的に更新され、最新のプロセスとベストプラクティスを反映しています。更新や改善の提案は、issueまたはプルリクエストを通じて行ってください。