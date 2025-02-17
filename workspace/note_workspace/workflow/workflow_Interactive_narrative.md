## 共通タスクフロー

### 1. タスク受付
1. タスクの受け取り時に以下を実施：
   - tasklist.tsvへの記録
     * タスクID（BT-XXXまたはPT-XXX形式）の採番
     * タスク名、起票日時の記録
     * 優先度、期限の設定
     * 初期ステータスを「新規」として記録

### 2. アイデアファイルを確認
1. BMS\workspace\note_workspace\idea\idea_Interactive_narrative.mdを確認
2. チェックボックスを確認し、完了していない項目から実施
3. 対象トピックを元に次タスクを実施。

### 3. タスク実施
1. 対象トピック名を抽出し、BMS\workspace\note_workspace\past_articles\Interactive_narrative直下にXXXX.md形式でファイルを作成。
2. チェックボックスを確認し、完了していない項目から実施
3. 対象トピックを変数として`D:\BMS\workspace\note_workspace\prompts\Interactive_narrative.md`に記載のあるプロンプトを実行。
4. 生成結果をXXXX.mdファイルに記載。

### 4. タスク完了報告
1. タスクの完了時に以下を実施：
   - tasklist.tsvへの完了の旨記録
     * 完了日時の記録
     * ステータスを「完了」に変更
2. ユーザーに完了の旨を報告。
