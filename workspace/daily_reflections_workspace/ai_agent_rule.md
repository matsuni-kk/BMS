# 日々の振り返り管理システム（Daily Reflections Management System）

このファイルはdaily_reflections_workspaceディレクトリのai_agent_rule.mdとして機能し、日々の振り返りを体系的に管理するためのフレームワークを定義します。

# システムプロンプト

## 共通ルール
- 日本語で応対
- 「D:\BMS」直下にフォルダを作るときは必ずai_agent_ruleファイルを作成
- 依頼するほとんどのタスクはコーディングとは関係ないことを考慮
- powershellでは「&&」を使用しない
- 絶対に生成時に省略行為は行わない
- すべてのタスク実行時にlog/ai_agent_ruleに従って作業ログを記録する

## テスト駆動処理
- 必ずタスクはテストドリブンで処理を行う
- タスクに合わせた詳細なテスト項目を事前に作成
  - 記録内容の完全性確認
    - 必要な項目の網羅
    - 具体的な事実の記載
    - 感情や思考の表現
  - 記録品質の検証
    - プロンプトの適切な使用
    - 客観的/主観的記述の区別
    - 改善点の具体性
  - 活用可能性の評価
    - アクションプランの実行可能性
    - フォローアップの容易さ
    - データ分析の可能性
- テスト用に別途ファイルを作成
- テスト粒度は細かく設定し、クリアするまで自動で反復

## ワークフロー

重要：必ず各ディレクトリのai_agent_ruleを参照し、ワークフローを把握すること:
  workflow: |
    作業を開始する前に、以下の手順で必要な情報を必ず確認してください。
    1. タスクの対象となるworkspaceのai_agent_ruleを熟読し、全体の構造を理解する

    reflections:
        information: |
          日々の振り返りを管理するディレクトリです。
          各日付フォルダ（YYYYMMDD）には以下の内容を含むreflection.mdが作成されます：
        timing: |
          1. ユーザーが振り返りの作成を依頼したときに実施します
        action:
          基本情報:
          - 日付
          - カテゴリ（ビジネス/プライベート/複合）
          
          振り返り内容:
          【ビジネス関連】（該当する場合）
          - 重要な意思決定とその根拠
          - プロジェクトの進捗状況
          - チーム内のコミュニケーション
          - 技術的な学びや気づき
          - 組織での課題と改善案
          - キャリアに関する考察
          
          【プライベート関連】（該当する場合）
          - 体調・コンディション
          - メンタル面での気づき
          - 生活習慣の改善点
          - 趣味や自己啓発の進捗
          - 個人的な目標の進捗
          - 重要な出来事の記録
          
          統合的な考察:
          - 今日の主要な学び
          - 改善が必要な点
          - 次のアクションプラン
          
          レビュー期間:
          - 週次: 重要事項の要約と計画
          - 月次: 傾向分析と目標確認
          - 四半期: 大きな変化の把握
          
          利用タイミング:
          - 日々の振り返り時
          - 重要な出来事後
          - 定期レビュー時

## 開発環境

- Node.js v20.12.2
- npm 10.5.0
- pnpm 9.15.4

## メンテナンス

### バージョン管理
- 振り返り記録の履歴管理
- プロンプトの更新履歴
- 定期的なバックアップ
- アーカイブの整理

### 更新プロセス
- 各セクションのドキュメントは定期的に更新
- 最新の振り返り手法とベストプラクティスを反映
- 更新や改善の提案はissueまたはプルリクエストを通じて実施

### 品質管理
- 記録の完全性確保
  - 必要項目の網羅
  - 具体的な事実の記載
  - 感情や思考の表現
  - アクションプランの設定
- 振り返りの質の維持
  - プロンプトの適切な使用
  - 客観/主観の明確な区別
  - 建設的な視点の保持
  - 改善点の具体化
- データの活用促進
  - パターンの分析
  - 知見の体系化
  - ベストプラクティスの抽出
  - 継続的な改善

最終更新日: 2025/2/21
