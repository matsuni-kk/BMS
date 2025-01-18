# Dify チャットAPI仕様書

## 概要
高度なチャットアプリケーションAPIで、セッションの持続性をサポートしています。以前のチャット履歴を応答のコンテキストとして使用できるため、チャットボットやカスタマーサービスAIなどに適用できます。

## ベースURL

```
http://35.164.37.16/v1
```

## 認証

サービスAPIはAPI-Key認証を使用します。APIキーはサーバー側に保存し、クライアント側で共有または保存しないことを強く推奨します。APIキーの漏洩は深刻な結果を招く可能性があります。

すべてのAPIリクエストには、以下のようにAuthorizationHTTPヘッダーにAPIキーを含める必要があります：

```
Authorization: Bearer {API_KEY}
```

## APIエンドポイント一覧

### メッセージ関連

#### POST /chat-messages
チャットメッセージを送信します。

**リクエストボディ**
| パラメータ | 型 | 説明 |
|------------|------|------|
| query | string | ユーザー入力/質問内容 |
| inputs | object | アプリによって定義された変数値の入力（オプション、デフォルト{}） |
| response_mode | string | 応答の返却モード（streaming/blocking） |
| user | string | ユーザー識別子 |
| conversation_id | string | 会話ID |
| files | array[object] | ファイルリスト |
| auto_generate_name | bool | タイトルを自動生成（デフォルトtrue） |

**応答**
- response_modeがblockingの場合：CompletionResponseオブジェクト
- response_modeがstreamingの場合：ChunkCompletionResponseストリーム

#### POST /chat-messages/:task_id/stop
ストリーミングモードでの生成を停止します。

#### POST /messages/:message_id/feedbacks
メッセージのフィードバックを提供します。

#### GET /messages/:message_id/suggested
現在のメッセージに対する次の質問の提案を取得します。

#### GET /messages
会話履歴メッセージを取得します。

### 会話関連

#### GET /conversations
現在のユーザーの会話リストを取得します。

#### DELETE /conversations/:conversation_id
指定した会話を削除します。

#### POST /conversations/:conversation_id/name
会話の名前を変更します。

### ファイル関連

#### POST /files/upload
メッセージ送信時に使用するファイルをアップロードします。

**サポートされているファイル形式**
- ドキュメント: TXT, MD, MARKDOWN, PDF, HTML, XLSX, XLS, DOCX, CSV, EML, MSG, PPTX, PPT, XML, EPUB
- 画像: JPG, JPEG, PNG, GIF, WEBP, SVG
- 音声: MP3, M4A, WAV, WEBM, AMR
- 動画: MP4, MOV, MPEG, MPGA

### 音声関連

#### POST /audio-to-text
音声をテキストに変換します。

**対応フォーマット**: mp3, mp4, mpeg, mpga, m4a, wav, webm
**ファイルサイズ制限**: 15MB

#### POST /text-to-audio
テキストを音声に変換します。

### その他

#### GET /info
アプリケーションの基本情報を取得します。

#### GET /parameters
アプリケーションのパラメータ情報を取得します。

#### GET /meta
アプリケーションのメタ情報を取得します。

## システムパラメータ

### ファイルサイズ制限
- ドキュメント: 15MB
- 画像: 10MB
- 音声: 50MB
- 動画: 100MB

### 応答イベントタイプ
- message: LLMテキストチャンクイベント
- message_file: メッセージファイルイベント
- message_end: メッセージ終了イベント
- tts_message: TTSオーディオストリームイベント
- tts_message_end: TTSオーディオストリーム終了イベント
- message_replace: メッセージ内容置換イベント
- workflow_started: ワークフロー開始イベント
- node_started: ノード開始イベント
- node_finished: ノード終了イベント
- workflow_finished: ワークフロー終了イベント
- error: エラーイベント
- ping: 接続維持用イベント（10秒間隔）
