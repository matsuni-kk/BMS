# Markitdown

URLからMarkdownファイルを作成するツール

## 概要

このツールは、指定されたURLのウェブページをMarkdown形式に変換します。LangChainのToMarkdownLoaderを使用しています。

## インストール

1. 必要なライブラリをインストールします。

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. `markitdown.py` を実行します。

   ```bash
   python markitdown.py
   ```

2. プロンプトが表示されたら、Markdownに変換したいウェブページのURLを入力します。

   ```
   Enter the URL:
   ```

3. 変換されたMarkdownが標準出力に出力されます。

## テスト

1. テストを実行するには、以下のコマンドを実行します。

   ```bash
   pytest
   ```

## 仕様

-   LangChainのToMarkdownLoaderを使用
-   非同期処理
-   URLはユーザーが入力