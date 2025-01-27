# マネジメント領域作業ルール

## 概要
このディレクトリは、ビジネスにおけるマネジメントに関する知識、手法、知見を体系的に整理し、AIエージェントが効果的に活用するための情報を提供します。
各サブディレクトリは、特定のマネジメント領域に焦点を当て、詳細な情報と実践的なガイドラインを提供します。

## ディレクトリ構造
```
management/
├── ProjectManagement/        # プロジェクトマネジメント
├── ProgramManagement/        # プログラムマネジメント
├── PortfolioManagement/      # ポートフォリオマネジメント
├── RiskManagement/           # リスクマネジメント
├── QualityManagement/        # 品質マネジメント
├── ResourceManagement/        # 資源マネジメント
├── CommunicationManagement/    # コミュニケーションマネジメント
├── StakeholderManagement/     # ステークホルダーマネジメント
├── FinancialManagement/       # 財務マネジメント
├── InformationManagement/     # 情報マネジメント
├── KnowledgeManagement/       # 知識マネジメント
├── ChangeManagement/          # 変革マネジメント
├── CrisisManagement/          # 危機管理
├── InnovationManagement/      # イノベーションマネジメント
├── OperationManagement/       # オペレーションマネジメント
├── StrategicManagement/       # 戦略マネジメント
├── TalentManagement/          # 人材マネジメント
├── TechnologyManagement/      # テクノロジーマネジメント
└── ai_agent_rule.md         # マネジメント領域全体ルール (このファイル)
```

## ファイル命名規則
- ファイル名は英語で記述する (例: `theory_project_planning.md`)
- 内容を端的に表す名前とする
- 拡張子は `.md` (Markdown形式) を使用する

## ファイル内容記述ルール
- ファイル内容はすべて日本語で記述する
- 各マネジメント領域に関する知識、手法、知見を詳細かつ体系的に記述する
- 具体的な事例や参考文献を積極的に引用する
- AIエージェントが理解しやすいように、簡潔かつ明確な表現を心がける

## 作業ログ記述ルール
- 各ファイルの変更履歴や作業内容を詳細に記録する
- 作業ログはファイル末尾に追記する形式とする
- 日付、作業内容、担当者を明記する

## テスト駆動ルール
- 各ファイルの内容について、AIエージェントが正しく理解し、活用できることを確認するためのテストケースを作成する
- テストケースは別ファイル (`tests/management/`) に記述する
- テスト駆動開発 (TDD) の原則に従い、テストケースを先に作成し、そのテストをパスするようにファイル内容を記述する