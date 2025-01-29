# information/what_is_question/ai_agent_rule.md

# システムプロンプト

## 共通ルール
- 日本語で応対
- 「D:\BMS\information\what_is_question」直下にフォルダを作るときは必ずai_agent_ruleファイルを作成
- 絶対に生成時に省略行為は行わない
- すべてのタスク実行時にlog/ai_agent_ruleに従って作業ログを記録する

## テスト駆動処理
- 必ずタスクはテストドリブンで処理を行う
- タスクに合わせた詳細なテスト項目を事前に作成
- テスト用に別途ファイルを作成
- テスト粒度は細かく設定し、クリアするまで自動で反復

## ワークフロー

workflow:
  information: |
    `what_is_question`ディレクトリは、「問い」に関する情報を管理するための場所です。
    ここでは、問いの種類、問いの構造、問いの立て方、問いの活用方法など、
    問いに関する様々な情報を体系的に管理します。
    
    サブディレクトリ構成：
      - types: 問いの種類に関する情報を管理
      - structure: 問いの構造に関する情報を管理
      - how_to_ask: 問いの立て方に関する情報を管理
      - usage: 問いの活用方法に関する情報を管理
  timing: |
    `what_is_question`での作業を開始する際には、以下の手順で進めてください：
    
    1. 作業の種類を特定します：
       - 問いの種類に関する情報収集
       - 問いの構造に関する情報収集
       - 問いの立て方に関する情報収集
       - 問いの活用方法に関する情報収集
    
    2. 必要な情報を収集し、整理します：
       - 関連資料の収集
       - 専門家の意見の収集
       - 実例の収集
    
    3. 収集した情報を基に、分析を行います：
       - 問いの種類を分類
       - 問いの構造を分析
       - 問いの立て方を検討
       - 問いの活用方法を検討
    
    4. 分析結果を基に、資料を作成します：
       - 問いの種類に関する資料
       - 問いの構造に関する資料
       - 問いの立て方に関する資料
       - 問いの活用方法に関する資料
    
    5. 作業ログを適切に記録します：
       - タスク開始時の記録
       - 進捗状況の更新
       - 問題点や課題の記録
       - 完了時の記録
    
    6. 必要に応じてテストを実施します：
       - テストケースの作成
       - テストの実行
       - 結果の記録
       - 改善点の特定と修正
  directory: information/what_is_question/
  types:
    directory: information/what_is_question/types/
  structure:
    directory: information/what_is_question/structure/
  how_to_ask:
    directory: information/what_is_question/how_to_ask/
  usage:
    directory: information/what_is_question/usage/ 