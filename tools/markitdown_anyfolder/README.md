# Markitdown Anyfolder

## 概要
指定したフォルダ内のあらゆるファイル（DOCX、XLSX、PPTX、PDF、画像、HTML等）をMarkdown形式に変換し、1つのMarkdownファイルにまとめるツールです。

## 機能
- フォルダ内の全ファイルをMarkdown形式に一括変換
- サブフォルダ内のファイルも再帰的に処理
- 以下のファイル形式に対応：
  - Word文書（.docx）
  - Excelファイル（.xlsx）
  - PowerPointファイル（.pptx）
  - PDFファイル
  - 画像ファイル（.jpg, .jpeg, .png, .gif）
  - HTMLファイル
  - CSVファイル
  - JSONファイル
  - XMLファイル
  - Markdownファイル
  - テキストファイル
- 変換結果を1つのMarkdownファイルに統合
- 各ファイルのメタデータ保持

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
### 基本的な使用方法
```bash
python markitdown_anyfolder.py <directory_path>
```

### テストモードの実行
```bash
python markitdown_anyfolder.py test
```

### 単一ファイルの変換
```bash
python markitdown_anyfolder.py <file_path>
```

## 出力
- 変換結果は`output`フォルダに保存されます
- ファイル名は`combined_YYYYMMDD_HHMMSS.md`形式
- 各ファイルの変換結果は見出し（##）で区切られます
- ファイルパスと変換日時が記録されます

## メタデータ
各ファイル形式に応じて以下のメタデータが保持されます：
- Word文書：タイトル
- Excelファイル：シート名一覧
- PowerPoint：スライド数
- PDF：ページ数
- 画像：フォーマット、サイズ、モード、EXIFデータ
- HTML：タイトル、エンコーディング
- JSON：タイプ情報
- XML：ルートタグ

## ログ
- ログファイルは`log/markitdown.log`に保存されます
- デバッグ情報や変換エラーの詳細が記録されます

## 注意事項
- 大量のファイルを処理する場合はメモリ使用量に注意してください
- 画像のOCRには`pytesseract`が必要です
- PDFの変換はテキストレイヤーがある場合のみ正常に機能します
- 一部のファイル形式では文字化けが発生する可能性があります
