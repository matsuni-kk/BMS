# 小説管理システム（Novel Management System）

このファイルはnovel_workspaceディレクトリのai_agent_rule.mdとして機能し、小説創作プロセスを体系的に管理するためのフレームワークを定義します。

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
  - 設定の整合性
  - キャラクターの一貫性
  - プロットの論理性
  - 伏線の回収状況
  - 魔法システムの整合性
- テスト用に別途ファイルを作成（tests/setting_tests.md）
- テスト粒度は細かく設定し、クリアするまで自動で反復

## ワークフロー

重要：必ず各ディレクトリのai_agent_ruleを参照し、ワークフローを把握すること:
  workflow: |
    作業を開始する前に、以下の手順で必要な情報を必ず確認してください。
    1. タスクの対象となるworkspaceのai_agent_ruleを熟読し、全体の構造を理解する
    
    created_story:
        timing: |
          作成された小説データを管理するディレクトリです。
          各小説はIDで管理され、以下の構造を持ちます：
          /settings/
          - world_setting.md: 世界観設定
          - character_main.md: メインキャラクター設定
          - sub_characters.md: サブキャラクター設定
          - plot.md: プロット概要
          - magic_regulations.md: 魔法システム規定
          /tests/
          - setting_tests.md: 設定テスト項目
          - setting_test_results.md: テスト結果
        directory: created_story/ai_agent_rule.md
    
    creation_process:
        timing: |
          小説創作プロセスのテンプレートを管理するディレクトリです。
          以下のテンプレートを提供します：
          
          - chapter_structure_template.md
            - 章立て構成の基本フォーマット
            - 各章のタイトル、要約、目的を定義
            - シーン分割のガイドライン
          
          - character_template.md
            - キャラクターの詳細プロフィール
            - 性格、外見、背景設定
            - 人間関係と役割の定義
          
          - novel_creation_process.md
            - 創作プロセス全体の管理
            - タイムライン設定
            - マイルストーン管理
          
          - plot_template.md
            - 物語の展開構造
            - 伏線配置計画
            - クライマックスの設計
          
          - review_template.md
            - レビュー記録フォーマット
            - 改善点のトラッキング
            - フィードバック管理
          
          - scene_template.md
            - シーン単位の構成要素
            - 場面設定の詳細
            - 登場人物の動き
          
          - world_setting_template.md
            - 世界観の基本設定
            - 魔法システムの規則
            - 社会構造の定義
        directory: creation_process/ai_agent_rule.md
    
    log:
        timing: |
          作業ログを記録するディレクトリです。
          以下の情報を記録します：
          - タスクの実行内容と結果
          - エラーや問題点の記録
          - 設定変更の履歴
          - レビュー結果
        directory: log/ai_agent_rule.md
    
    prompts:
        timing: |
          AIプロンプトを管理するディレクトリです。
          以下のプロンプトを含みます：
          - キャラクター生成用プロンプト
          - シーン展開用プロンプト
          - 対話生成用プロンプト
          - 描写改善用プロンプト
        directory: prompts/ai_agent_rule.md

## 開発環境

- Node.js v20.12.2
- npm 10.5.0
- pnpm 9.15.4

## メンテナンス

### バージョン管理
- 各原稿にバージョン番号を付与
- 変更履歴を記録
- 定期的なバックアップ
- 修正履歴の管理

### 更新プロセス
- 各セクションのドキュメントは定期的に更新
- 最新のプロセスとベストプラクティスを反映
- 更新や改善の提案はissueまたはプルリクエストを通じて実施

### 品質管理
- 文章の一貫性維持
- キャラクターの整合性確認
- プロットの論理性検証
- 伏線の回収状況確認
- 描写の質向上
- 文法チェック実施
- 読みやすさの確保

最終更新日: 2025/2/5