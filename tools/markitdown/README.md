# Markitdown

## 概要
様々な形式のファイル（DOCX、XLSX、PPTX、PDF、画像、HTML等）をMarkdown形式に変換するツールです。変換したMarkdownファイルは、出力フォルダに保存されます。

## 機能
- Word文書（.docx）をMarkdownに変換
- Excelファイル（.xlsx）をMarkdownテーブルに変換
- PowerPointファイル（.pptx）のスライドをMarkdownに変換
- PDFファイルのテキストをMarkdownに変換
- 画像ファイル（.jpg, .jpeg, .png, .gif）からOCRでテキストを抽出しMarkdown化
- HTMLファイルをMarkdownに変換
- CSVファイルをMarkdownテーブルに変換
- JSONファイルを構造化Markdownに変換
- XMLファイルを構造化Markdownに変換
- 既存のMarkdownファイルの変換（そのまま返す）
- テキストファイルを基本的なMarkdownに変換

## 必要要件
- Python 3.x
- python-docx
- openpyxl
- python-pptx
- PyPDF2
- Pillow
- pytesseract
- beautifulsoup4
- langchain-community

## インストール方法
```bash
pip install -r packages/markitdown/requirements.txt
```

## 使用方法
### 単一ファイルの変換
```bash
python markitdown.py <file_path>
```

### ディレクトリ内の全ファイルの変換
```bash
python markitdown.py <directory_path>
```

## 出力
変換されたMarkdownファイルは、ツールと同じディレクトリの`output`フォルダに保存されます。
ファイル名は元のファイル名にタイムスタンプを付加した形式（例：`document_20250211_120000.md`）となります。

## メタデータ
変換結果には以下のようなメタデータが含まれます：
- Word文書：タイトル
- Excelファイル：シート名一覧
- PowerPoint：スライド数
- PDF：ページ数
- 画像：フォーマット、サイズ、モード、EXIFデータ（利用可能な場合）
- HTML：タイトル、エンコーディング
- JSON：ファイルタイプ
- XML：ルートタグ

## 注意事項
- 画像のOCRには`pytesseract`を使用しているため、Tesseract OCRのインストールが必要です
- PDFの変換は、テキストレイヤーがある場合のみ正常に機能します
- メモリ使用量の多いファイルを処理する場合は、十分なメモリを確保してください
