# 文章作成・記事管理プロンプト管理システム

## 概要
このディレクトリでは、効果的な文章作成と記事管理に必要なプロンプトテンプレートを管理します。
様々なタイプの文章作成をサポートし、品質の高いコンテンツ制作を促進します。

## ディレクトリ構造
```
prompts/
├── article_types/        # 記事タイプ別プロンプト
│   ├── technical/       # 技術記事
│   ├── blog/           # ブログ記事
│   ├── review/         # レビュー記事
│   └── academic/       # 学術的記事
├── writing_process/     # 執筆プロセス用プロンプト
│   ├── planning/       # 企画立案
│   ├── drafting/       # 下書き作成
│   ├── editing/        # 編集作業
│   └── reviewing/      # レビュー
└── management/         # 記事管理用プロンプト
    ├── organization/   # 整理・分類
    ├── versioning/     # バージョン管理
    └── publishing/     # 公開準備
```

## プロンプトカテゴリ

### 1. 記事タイプ別プロンプト
- 技術文書作成プロンプト
- ブログ記事作成プロンプト
- 製品レビュープロンプト
- 研究記事作成プロンプト
- ケーススタディプロンプト

### 2. 執筆プロセス
- アウトライン作成プロンプト
- 本文執筆プロンプト
- 校正・編集プロンプト
- 引用・参考文献管理プロンプト
- SEO最適化プロンプト

### 3. 記事管理
- カテゴリ分類プロンプト
- タグ付けプロンプト
- バージョン管理プロンプト
- 公開準備チェックリスト

## プロンプト作成ガイドライン

### 1. 基本構造
- 記事の目的明確化
- 対象読者の定義
- 構成要素の指定
- 品質基準の設定

### 2. フォーマット要件
- マークダウン形式の活用
- 見出しの階層化
- リストの効果的使用
- コードブロックの適切な配置

### 3. 品質基準
- 正確性の確保
- 読みやすさの向上
- 一貫性の維持
- オリジナリティの確保

## 執筆プロセス

### 1. 企画フェーズ
1. トピックの選定
2. アウトラインの作成
3. リサーチ計画の立案

### 2. 執筆フェーズ
1. 下書きの作成
2. 構成の最適化
3. 表現の洗練化

### 3. 編集フェーズ
1. 内容の確認
2. 文章の推敲
3. フォーマットの調整

## メンテナンス

### 1. 定期レビュー
- テンプレートの有効性評価
- 使用状況の分析
- 改善点の特定

### 2. 更新プロセス
- 新規テンプレートの追加
- 既存テンプレートの改訂
- ベストプラクティスの更新

## 注意事項
- 著作権への配慮
- 引用ルールの遵守
- プライバシーの保護
- 事実確認の徹底

最終更新日: 2025/1/18

## ログ記載ルール

### 1. タスクの記録
- 目的と目標を明確に記述
- 期待される成果物を具体的に記載
- 必要なリソースや参照すべき文書を列挙

### 2. 進捗管理
- 日々の進捗を記録
- 発生した問題点とその解決策
- 次のアクションアイテム

### 3. 完了基準
- タスクの完了条件を明確に定義
- テスト項目とその結果
- レビュー要件

### 4. ログの保管
- BMS\log配下の日付フォルダ（YYYYMMDD）内にtask_description.mdを作成
- タスクの詳細な説明と実行ログを記録
- 定期的に進捗状況を更新
- すべてのタスクログはBMS\logディレクトリに集約して管理