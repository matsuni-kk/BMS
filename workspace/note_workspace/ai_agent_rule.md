# ノート管理システム（Note Management System）

このファイルはnote_workspaceディレクトリのai_agent_rule.mdとして機能し、効果的なノート作成と管理を実現するためのフレームワークを定義します。

# システムプロンプト

## 共通ルール
- 日本語で応対
- 「D:\BMS」直下にフォルダを作るときは必ずai_agent_ruleファイルを作成
- 依頼するほとんどのタスクはコーディングとは関係ないことを考慮
- powershellでは「&&」を使用しない
- 絶対に生成時に省略行為は行わない
- すべてのタスク実行時にlog/ai_agent_ruleに従って作業ログを記録する

## テスト駆動処理
- 実際に執筆成果の確認時はテストドリブンで処理を行う
- タスクに合わせた詳細なテスト項目を事前に作成
  - 形式要件の確認
    - Markdown形式の適切性
    - 見出しレベルの正確性
    - コードブロックの言語指定
  - 内容要件の検証
    - 目的の明確性
    - 構成の論理性
    - 例示の具体性
  - 品質基準のチェック
    - 誤字脱字
    - 文法の正確性
    - 表現の一貫性
- テスト用に別途ファイルを作成
- テスト粒度は細かく設定し、クリアするまで自動で反復

## ディレクトリ詳細

workspace/note_workspace/
├── ai_agent_rule.md
├── log/
│   └── ai_agent_rule.md
├── past_articles/
│   ├── analysis/
│   │   ├── README.md
│   ├── blog_posts/
│   │   ├── README.md
│   ├── book_reviews/
│   │   ├── README.md
│   ├── case_studies/
│   │   ├── README.md
│   ├── essays/
│   │   ├── README.md
│   ├── idea_development/
│   │   ├── README.md
│   ├── knowledge_base/
│   │   ├── README.md
│   ├── learning_records/
│   │   ├── README.md
│   ├── movie_reviews/
│   │   ├── README.md
│   ├── project_management/
│   │   ├── README.md
│   ├── research_notes/
│   │   ├── README.md
│   └── technical_docs/
│   │   └── README.md
├── prompts/
│   └── ai_agent_rule.md
├── idea/
│   └── ai_agent_rule.md
├── workflow/
│   └── ai_agent_rule.md
└── writing_in_progress/
    └── 【記事タイトル】/  
        ├── draft/       
        │   └── [下書きファイル].md (例: draft.md)
        ├── idea/        
        │   └── [アイデアファイル].md (例: idea.md)
        ├── memo/        
        │   └── [メモファイル].md (例: memo.md)
        ├── 要件.md       
        └── 文章.md       

workspace/
├── note_workspace/        # 現在のディレクトリ
├── business_tasks_workspace/   # ビジネスタスク管理
├── daily_reflections_workspace/  # 日々の振り返り
├── ideas_workspace/       # アイデア管理
├── investment_workspace/  # 投資関連
├── novel_workspace/      # 小説執筆
├── private_tasks_workspace/  # プライベートタスク
└── sales_workspace/      # 営業関連

## task_detail.mdテンプレート

#### 基本情報
- タスクID（tasklist.tsvと同一のID）
- タスク名
- 担当者
- 開始日時
- 期限
- 優先度
- ステータス
- タスク種別（定例/プロジェクト/その他）

#### 詳細情報
- タスク概要
- 目的
- 必要なインプットデータ
- 期待される成果物
- 前提条件
- 制約事項

#### 利用ファイル情報
##### インプットファイル
```
input/
├── [ファイル名1]
│   └── 用途：[このファイルの使用目的]
├── [ファイル名2]
│   └── 用途：[このファイルの使用目的]
└── [関連ディレクトリ名]/
    └── 用途：[このディレクトリの使用目的]
```

## ワークフロー

重要：必ず各ディレクトリのai_agent_ruleを参照し、ワークフローを把握すること:
  workflow: |
    作業を開始する前に、以下の手順で必要な情報を必ず確認してください。
    1. タスクの対象となるworkspaceのai_agent_ruleを熟読し、全体の構造を理解する
    writing_in_progress：
      information: |
        アイデアやメモを保管したりまとめたりします。
      timing: |
        利用タイミング：
        - 最初に起案する時
        - アイデア作成時
        - メモ作成時
        - まとめ作成時
      action: |
        - writing_in_progressに対象タイトルフォルダがない場合はフォルダを作成する。
        - 作成したタイトルフォルダにdraft、idea、memoフォルダがない場合はフォルダを作成する。
        - フォルダを作成するときは必ずai_agent_ruleを作成する。
      directory: writing_in_progress/ai_agent_rule.md

    past_articles:
        information: |
          完成した記事を管理するディレクトリです。
          以下のサブディレクトリを含みます：

        timing: |
          利用タイミング：
          - 記事完成時
          - 文書分類時
          - アーカイブ作成時

        directory: |
          /analysis/
          - 考察や分析文書
          - データ分析結果
          - 市場調査レポート

          /blog_posts/
          - ブログ記事
          - Web公開用コンテンツ
          - デジタルマーケティング
          
          /book_reviews/
          - 書籍レビュー
          - 読書感想文
          - 書籍要約
          
          /case_studies/
          - 事例研究
          - ビジネスケース分析
          - プロジェクト事例
          
          /essays/
          - エッセイ
          - 個人的な考察
          - 意見文
          
          /idea_development/
          - アイデアの発展記録
          - コンセプト検討
          - 新規提案
          
          /knowledge_base/
          - 知識ベース
          - リファレンス資料
          - ガイドライン
          
          /learning_records/
          - 学習記録
          - 研修メモ
          - スキル開発記録
          
          /movie_reviews/
          - 映画レビュー
          - 映像作品分析
          - エンターテインメント評価
          
          /project_management/
          - プロジェクト管理文書
          - 進捗報告
          - マイルストーン記録
          
          /research_notes/
          - 研究ノート
          - 調査記録
          - 実験データ
          
          /technical_docs/
          - 技術文書
          - 仕様書
          - マニュアル
          
          利用タイミング：
          - 記事完成時
          - 文書分類時
          - アーカイブ作成時
        directory: past_articles/ai_agent_rule.md

## 開発環境

- Node.js v20.12.2
- npm 10.5.0
- pnpm 9.15.4

## メンテナンス

### バージョン管理
- 記事のバージョン履歴管理
- 変更内容の記録
- 定期的なバックアップ
- 古い情報の更新管理

### 更新プロセス
- 各セクションのドキュメントは定期的に更新
- 最新の文書作成手法とベストプラクティスを反映
- 更新や改善の提案はissueまたはプルリクエストを通じて実施

### 品質管理
- 形式要件の遵守
  - Markdown形式の正確性
  - 見出しレベルの適切性
  - コードブロックの言語指定
  - 表の整形状態
  - リンクの有効性
- 内容要件の確保
  - 目的の明確性
  - 構成の論理性
  - 例示の具体性
  - 結論の明確性
  - 参考文献の適切性
- 品質基準の維持
  - 誤字脱字の排除
  - 文法の正確性
  - 表現の一貫性
  - 引用の適切性
  - 文書の流れ

最終更新日: 2025/2/17
