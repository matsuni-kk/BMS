# PC Lightener

## 概要
Windows PCのリソース解放、ディスク容量の拡大、パフォーマンス向上を目的とした最適化ツールです。不要なプロセスの終了、一時ファイルの削除、キャッシュのクリア、ディスククリーンアップなどを行います。

## 機能
1. プロセスの最適化
   - メモリ使用量が100MB以上の不要プロセスを自動終了
   - 重要プロセス（chrome、cursor、vscode等）は保護

2. 一時ファイルの削除
   - ユーザーTEMPファイル削除
   - システムTEMPファイル削除
   - Windows更新ファイル削除
   - Prefetchファイル削除

3. システムクリーンアップ
   - ごみ箱の内容削除
   - ハイバネーション無効化（hiberfil.sys削除）
   - Windowsエラーレポート(WER)削除
   - IE/Edgeのキャッシュ（INetCache）削除

4. Windows最適化
   - Windowsディスククリーンアップ実行
   - コンポーネントストアのクリーンアップ
   - 不要なログファイル削除
   - 不要なバックアップファイル整理
   - その他の一時ファイルやキャッシュの削除

## 必要要件
- Windows 10
- Python 3.x
- psutil
- 管理者権限での実行

## インストール方法
```bash
pip install psutil
```

## 使用方法
```bash
python pc_lightener.py
```

## 保護対象
以下のプロセスは自動終了の対象外となります：
- システム重要プロセス（System、wininit.exe等）
- 開発関連プロセス（chrome.exe、code.exe、cursor.exe等）
- プログラミング関連プロセス（python.exe、node.exe等）

## 注意事項
- 必ず管理者権限で実行してください
- 実行前にデータのバックアップを推奨します
- ハイバネーション機能を使用する場合は、コード内の `disable_hibernation()` の呼び出しをコメントアウトしてください
- chrome、cursor、vscode系およびプログラミング関連パッケージを含むパスは、クリーンアップ対象から除外されます
