# tech_docsのai_agent_rule.md

# システムプロンプト

## 共通ルール
- 日本語で応対
- 「D:\BMS\document\tech_docs」直下にフォルダを作るときは必ずai_agent_ruleファイルを作成
- 依頼するほとんどのタスクはコーディングとは関係ないことを考慮
- powershellでは「&&」を使用しない
- 絶対に生成時に省略行為は行わない
- すべてのタスク実行時にlog/ai_agent_ruleに従って作業ログを記録する

## テスト駆動処理
- 必ずタスクはテストドリブンで処理を行う
- タスクに合わせた詳細なテスト項目を事前に作成
- テスト用に別途ファイルを作成
- テスト粒度は細かく設定し、クリアするまで自動で反復

## ワークフロー

重要：必ず各ディレクトリのai_agent_ruleを参照し、ワークフローを把握すること:

workflow:
  tech_docs: |
    tech_docsディレクトリは、技術ドキュメントを管理するための場所です。
    ここでは、プログラミング言語、フレームワーク、パッケージ、開発ツールなど、
    様々な技術ドキュメントを体系的に管理します。
  timing: |
    tech_docsでの作業を開始する際には、以下の手順で進めてください：
    
    1. 作業の種類を特定し、適切なサブディレクトリを選択します：
       - プログラミング言語 → languages
       - フレームワーク → frameworks
       - パッケージ → packages
       - 開発ツール → tools
    
    2. 選択したサブディレクトリのai_agent_ruleを確認します：
       - ディレクトリ固有のルールとガイドラインを理解
       - 必要なテンプレートの場所を確認
       - 作業フローの把握
       - 注意事項の確認
    
    3. 定められたディレクトリ構造に従って作業を開始します：
       - 必要なフォルダの作成
       - テンプレートの配置
       - ファイルの命名規則の遵守
       - フォルダ階層の維持
    
    4. 作業ログを適切に記録します：
       - タスク開始時の記録
       - 進捗状況の更新
       - 問題点や課題の記録
       - 完了時の記録
    
    5. 必要に応じてテストを実施します：
       - テストケースの作成
       - テストの実行
       - 結果の記録
       - 改善点の特定と修正