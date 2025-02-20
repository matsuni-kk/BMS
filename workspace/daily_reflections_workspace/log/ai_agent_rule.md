# タスクログ管理

このディレクトリ（workspace/daily_reflections_workspace/log）は、すべてのタスクの実行ログを一元管理するための場所です。
タスクの種類に関わらず、すべてのログはこのディレクトリに集約して管理されます。

## ディレクトリ構造
```
workspace/daily_reflections_workspace/log/
├── ai_agent_rule.md
└── YYYYMMDD/
    ├── task_description.md  # タスクの詳細説明
    └── progress.md         # 進捗状況の記録
```

## 使用方法

1. 新しいタスクログを記録する際は、以下の形式でディレクトリを作成：
   - パス: `workspace/daily_reflections_workspace/log/YYYYMMDD`（例：workspace/daily_reflections_workspace/log/20250116）
   - すべてのタスクログはこのディレクトリに集約

2. 各タスクフォルダには以下のファイルを含める：
   - `task_description.md`: タスクの詳細な説明
   - `progress.md`: 進捗状況の記録

## タスク管理のルール

1. タスクの記録（task_description.md）
   - 目的と目標を明確に記述
   - 期待される成果物を具体的に記載
   - 必要なリソースや参照すべき文書を列挙
   - ログを記録する際は、必ず日時を記載する

2. 進捗管理（progress.md）
   - 日々の進捗を記録
   - 発生した問題点とその解決策
   - 次のアクションアイテム
   - タスクの進行状況をリアルタイムに反映
   - 進捗を記録する際は、必ず日時を記載し、上書きではなく追記する

3. 完了基準
   - タスクの完了条件を明確に定義
   - テスト項目とその結果
   - レビュー要件と実施状況

## メンテナンス

- 定期的に進捗状況を更新
- 完了したタスクは適切にアーカイブ
- 問題点や学習した内容は適切に文書化
- タスクの状態（進行中/完了/保留等）を明確に記録
- 定期的なレビューと改善点の反映