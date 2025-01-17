# BMS (Business Management System)

このリポジトリは、ビジネスマネジメントシステムの包括的なドキュメントとリソースを管理するためのものです。

# システムプロンプト

## 重要：各ディレクトリのREADME.md参照について
作業を開始する前に、以下の手順で必要な情報を必ず確認してください：

1. 最上位階層（このファイル）のREADME.mdを熟読し、全体の構造を理解する
2. **作業対象となる全てのディレクトリのREADME.mdを必ず読む**
   - app_specifications/README.md
   - consult_techniques/README.md
   - daily_reflections/README.md
   - emotional story/README.md
   - ideas/README.md
   - log/README.md
   - Note/README.md
   - novel_management/README.md
   - prompts/README.md
   - sales/README.md
   - sales_techniques/README.md
   - tasks/README.md
   - その他のサブディレクトリのREADME.md
3. 作業内容に関連する可能性のある全てのディレクトリのREADME.mdを参照する
4. README.mdの内容は随時更新される可能性があるため、作業ごとに最新の内容を確認する

## 共通ルール
- 日本語で応対
- 「D:\BMS」直下にフォルダを作るときは必ずreadmeファイルを作成
- 依頼するほとんどのタスクはコーディングとは関係ないことを考慮
- powershellでは「&&」を使用しない
- 絶対に生成時に省略行為は行わない
- すべてのタスク実行時にlog/README.mdに従って作業ログを記録する

## テスト駆動処理
- 必ずタスクはテストドリブンで処理を行う
- タスクに合わせた詳細なテスト項目を事前に作成
- テスト用に別途ファイルを作成
- テスト粒度は細かく設定し、クリアするまで自動で反復

# プロジェクト構造

### log/
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

### Note/
note執筆のためのディレクトリ。執筆中の文章と過去の文章を体系的に管理します。

#### ディレクトリ構造
```
Note/
├── past_articles/        # 完成した過去の文章
│   └── YYYYMMDD/        # 作成日付ごとのフォルダ
│       └── 作品名.md
├── writing_in_progress/ # 執筆中の文章
│   └── note_name/      # 記事ごとのフォルダ
│       ├── 要件.md     # 記事の要件定義
│       └── 文章.md     # 実際の記事
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

### daily_reflections/
日々の所感と課題管理のためのディレクトリ。ビジネスとプライベートの振り返りを体系的に管理します。

#### ディレクトリ構造
```
daily_reflections/
├── business/           # ビジネス関連の日記
│   └── YYYYMMDD/
│       └── reflection.md
└── private/           # プライベート関連の日記
    └── YYYYMMDD/
        └── reflection.md
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

### app_specifications/
アプリケーションの技術仕様を格納するディレクトリ
- `api_specifications/` - APIインターフェースの詳細仕様

### ideas/
創造的なアイデア管理とプロセスに関するドキュメント
- `created_idea/` - 生成されたアイデアの管理
- `idea_process/` - アイデア創出プロセスとテンプレート
  - テストケース
  - スコアリングガイド
  - プロセステンプレート

### novel_management/
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

### prompts/
ビジネス関連のプロンプトテンプレート
- `prompt_bissines/`
  - 議事録プロンプト
  - プロジェクト概要プロンプト

### sales_techniques/
営業技法とカスタマーリレーションのリソース
- analysis/ - 顧客分析手法
- follow_up/ - フォローアップ戦略
- negotiation/ - 交渉スキル
- presentation/ - プレゼンテーション技法
- processes/ - 営業プロセス
- storytelling/ - ストーリーテリングプロセス

### tasks/
タスク管理システム
- `business_tasks/` - ビジネス関連タスク
  - 日付ごとのフォルダ（YYYYMMDD形式）
    - タスクごとの管理フォルダ
      - input/ - タスクの入力データ
      - output/ - タスクの成果物
      - task_detail.md - タスク詳細
- `private_tasks/` - プライベート関連タスク
  - 日付ごとのフォルダ（YYYYMMDD形式）
    - タスクごとの管理フォルダ
      - input/ - タスクの入力データ
      - output/ - タスクの成果物
      - task_detail.md - タスク詳細

## 使用方法

### タスク管理のルール
1. ビジネスタスクの場合：
   - ビジネス関連のタスクは `tasks/business_tasks/YYYYMMDD/task_name` ディレクトリに起票
   - `YYYYMMDD` はタスクが依頼された日付（例: 20250117）
   - `task_name` はタスクの内容を簡潔に表した名称
   - 合わせて`task_name` ディレクトリに `input` 、`output`フォルダを作成してください。
   - 目的に応じて適切なプロンプトを選択
   - task_detail.mdテンプレートに従って記録

2. プライベートタスクの場合：
   - プライベート関連のタスクは `tasks/private_tasks/YYYYMMDD/task_name` ディレクトリに起票
   - `YYYYMMDD` はタスクが依頼された日付（例: 20250117）
   - `task_name` はタスクの内容を簡潔に表した名称
   - 合わせて`task_name` ディレクトリに `input` 、`output`フォルダを作成してください。
   - 目的に応じて適切なプロンプトを選択
   - task_detail.mdテンプレートに従って記録

### 一般的な使用方法
各ディレクトリには独自のREADMEファイルが含まれており、それぞれの領域の詳細な使用方法とガイドラインが記載されています。特定の領域の作業を開始する際は、該当するディレクトリのドキュメントを参照してください。

## 開発環境

- Node.js v20.12.2
- npm 10.5.0
- pnpm 9.15.4

## メンテナンス

各セクションのドキュメントは定期的に更新され、最新のプロセスとベストプラクティスを反映しています。更新や改善の提案は、issueまたはプルリクエストを通じて行ってください。