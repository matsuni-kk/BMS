# URL to Markdown Converter

## 概要
指定されたURLからコンテンツを取得し、Markdown形式に変換するツールです。HTMLとPDFの両方に対応しており、日本語サイトの文字化けにも対応しています。

## 機能
- HTMLページの内容をMarkdown形式に変換
- PDFファイルの内容をMarkdown形式に変換
- 同一ドメイン内の関連URLを抽出して変換（BFS方式）
- DeepSearch機能による深い階層のURLの抽出と変換
- 日本語サイト（.jp）の文字化け対策（Shift-JIS自動判定）
- 複数ページの並列処理による高速変換

## 必要要件
- Python 3.x
- requests
- beautifulsoup4
- langchain_community
- UnstructuredHTMLLoader
- UnstructuredPDFLoader

## インストール方法
```bash
pip install -r packages/url_md/requirements.txt
```

## 使用方法
### 基本的な使用方法
```bash
python url_md.py --url <URL> --mode single
```

### 集約モード（関連URLも含めて変換）
```bash
python url_md.py --url <URL> --mode aggregate
```

### DeepSearchモード（より深い階層まで探索）
```bash
python url_md.py --url <URL> --mode deepsearch
```

## モードの説明
- `single`: 指定されたURLのみを変換
- `aggregate`: 同一ドメイン内の関連URLを最大50ページまで変換
- `deepsearch`: レベル1のURLを最大20件、各レベル1URLからレベル2のURLを最大10件まで変換

## 出力
変換されたMarkdownファイルは、ツールと同じディレクトリの`output`フォルダに保存されます。
出力ファイルには以下の情報が含まれます：
- URL
- ドメイン
- 取得日時
- 本文内容

## 注意事項
- アクセス制限のあるページやJavaScriptで動的に生成されるコンテンツは正しく取得できない場合があります
- PDFファイルの変換は、テキストレイヤーが存在する場合のみ正常に機能します
- DeepSearchモードは処理に時間がかかる場合があります
- Webサイトのロボット排除規約を遵守してください
