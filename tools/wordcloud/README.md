# ワードクラウド生成ツール

ExcelファイルやCSVファイルから日本語テキストを読み込み、ワードクラウドを生成するツールです。

## 機能

- Excel (.xlsx, .xls) およびCSVファイルの読み込み
- 日本語テキストの形態素解析（名詞の抽出）
- カスタマイズ可能なワードクラウドの生成

## セットアップ

1. 必要なパッケージをダウンロードします：

```bash
python download_packages.py
```

このコマンドは必要なパッケージを`tools/packages`ディレクトリにダウンロードします。
インターネット接続が必要ですが、一度ダウンロードすれば再度実行する必要はありません。

## 使用方法

基本的な使用方法：

```bash
python wordcloud.py input.xlsx --column テキスト --output wordcloud.png
```

### オプション

- `input_file`: 入力ファイルのパス（必須、.xlsx/.xls/.csv）
- `--column`: テキストデータが含まれる列名（デフォルト: 'text'）
- `--output`: 出力画像のパス（デフォルト: 'wordcloud.png'）
- `--width`: 画像の幅（デフォルト: 800）
- `--height`: 画像の高さ（デフォルト: 600）
- `--font`: カスタムフォントファイルのパス（デフォルト: msgothic.ttc）

### 使用例

1. Excelファイルから特定の列を使用：
```bash
python wordcloud.py data.xlsx --column コメント --output result.png
```

2. CSVファイルを使用：
```bash
python wordcloud.py data.csv --column text --width 1000 --height 800
```

3. カスタムフォントを使用：
```bash
python wordcloud.py data.xlsx --font "C:/Windows/Fonts/yugothic.ttf"
```

## 注意事項

- 入力ファイルには必ず指定した列名が存在する必要があります
- テキストデータは日本語に対応しています
- デフォルトでは名詞のみを抽出してワードクラウドを生成します
- 初回実行時は`download_packages.py`を実行してパッケージをダウンロードする必要があります 