# Note管理システム

## フォルダ構造
```
Note/
├── past_articles/         # 完成した記事をジャンル別に保管
│   ├── analysis/         # 考察・分析文書
│   ├── book_reviews/     # 書籍レビュー
│   ├── blog_posts/       # ブログ記事
│   ├── case_studies/     # ケーススタディ
│   ├── essays/           # エッセイ
│   ├── idea_development/ # アイデア展開
│   ├── knowledge_base/   # 知識ベース
│   ├── learning_records/ # 学習記録
│   ├── movie_reviews/    # 映画レビュー
│   ├── project_management/ # プロジェクト管理
│   ├── research_notes/   # 研究ノート
│   └── technical_docs/   # テクニカルドキュメント
├── writing_in_progress/   # 執筆中の記事を格納
│   └── note_name/        # 記事ごとのフォルダ
│       ├── 要件.md       # 記事の要件定義
│       └── 文章.md       # 実際の記事
└── ai_agent_rule.md             # 本ドキュメント
```

## 使用方法

### 新規記事作成時
1. writing_in_progress/に記事名のフォルダを作成
2. フォルダ内に以下を作成：
   - 要件.md：記事の要件を定義
   - 文章.md：実際の記事を執筆

### 記事完成時
1. past_articles/の適切なジャンルディレクトリを選択
2. writing_in_progressから完成した記事を移動
3. 各ジャンルのai_agent_ruleに定義された形式に従ってファイルを整理

## 記事のジャンル分類
- analysis: 考察や分析文書
- blog_posts: ブログ用の記事
- book_reviews: 書籍レビューや読書記録
- case_studies: 事例研究や実例分析
- essays: エッセイや個人的な考察
- idea_development: アイデアの発展と展開
- knowledge_base: 知識の体系化や参考資料
- learning_records: 学習過程の記録
- movie_reviews: 映画レビューや感想
- project_management: プロジェクト管理関連
- research_notes: 研究や調査のノート
- technical_docs: 技術文書やドキュメント

## 文書作成のガイドライン
- 各ジャンルのai_agent_ruleに定義された構成に従う
- 適切なメタデータを含める
- 一貫した文体を維持する
- 要件.mdに定義された要件を満たす

## 注意事項
- フォルダ名は英語で作成
- ファイル名は日本語で作成可能
- 執筆前に必ず要件の定義を行う
- 各ジャンルのガイドラインに従って文書を作成