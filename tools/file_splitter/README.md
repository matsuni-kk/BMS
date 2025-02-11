# File Splitter

## 概要
テキストファイルを指定した数に分割するツールです。文字数単位での分割を行い、分割されたファイルは自動的にoutputディレクトリに保存されます。

## 機能
- テキストファイルを指定した数に分割
- 文字数単位での均等分割
- UTF-8エンコーディング対応
- 相対パス・絶対パスの両方に対応
- 自動的なoutputディレクトリ作成
- 元のファイル拡張子の維持

## 必要要件
- Python 3.x

## 使用方法
### コマンドライン引数
```bash
python file_splitter.py <file_path> <num_splits>

# 例：test.txtを3分割する場合
python file_splitter.py test.txt 3
```

### プログラムでの利用
```python
from file_splitter import split_file

# ファイルを分割して、分割ファイルのパスのリストを取得
split_files = split_file("path/to/file.txt", 3)
```

## パラメータ
- `file_path`: 分割対象のファイルパス（相対パスまたは絶対パス）
- `num_splits`: 分割数（1以上の整数）

## 出力
- 分割されたファイルは`output`ディレクトリに保存
- ファイル名形式：`{元のファイル名}_split_{番号}{元の拡張子}`
- 例：`document_split_1.txt`, `document_split_2.txt`, ...

## 戻り値
分割されたファイルのパスのリストを返します：
```python
[
    "output/document_split_1.txt",
    "output/document_split_2.txt",
    "output/document_split_3.txt"
]
```

## 例外処理
- `FileNotFoundError`: ファイルが存在しない場合
- `ValueError`: 分割数が1未満の場合
- 空の分割は作成されません

## 注意事項
- 入力ファイルはUTF-8でエンコードされている必要があります
- 分割サイズは文字数単位で計算されます
- メモリ使用量は入力ファイルのサイズに依存します
- 非常に大きなファイルを処理する場合はメモリ使用量に注意してください
