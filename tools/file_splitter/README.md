# File Splitter

テキストファイルを指定した分割数で文字数単位に分割するツール

## 機能

- mdやtxtファイルを指定した分割数で文字数単位に分割
- 分割ファイルは元ファイルと同じディレクトリに生成
- 自動的に文字数を計算して均等に分割
- 日本語文字を含むUTF-8エンコードのファイルに対応
- 相対パス・絶対パス両方に対応
- パスの自動正規化機能

## 使用方法

```bash
python file_splitter.py ファイルパス 分割数
```

### パス指定について

以下のいずれの形式でもファイルを指定可能：

1. 絶対パス
```bash
python file_splitter.py C:/Documents/example.txt 5
```

2. 相対パス（実行時のカレントディレクトリからの相対パス）
```bash
# 同じディレクトリ内のファイル
python file_splitter.py example.txt 5

# サブディレクトリ内のファイル
python file_splitter.py docs/example.txt 5

# 親ディレクトリのファイル
python file_splitter.py ../example.txt 5
```

### 出力ファイル

- 分割ファイルは元のファイルと同じディレクトリに生成されます
- ファイル名形式：`{元ファイル名}_split_{番号}{拡張子}`
- 例）`example.txt`を分割した場合：
  - example_split_1.txt
  - example_split_2.txt
  - example_split_3.txt
  （分割数に応じて続く）

## エラー処理

- 存在しないファイルを指定した場合
- 1未満の分割数を指定した場合
- ファイルパスが無効な場合

## プログラムでの利用

```python
from file_splitter import split_file

# 関数の使用例
split_files = split_file("path/to/file.txt", 5)
print(f"生成されたファイル: {split_files}")
```

## 開発者向け情報

### テスト実行

```bash
pytest test_file_splitter.py -v
```

### テストケース

- 基本的な分割機能のテスト（均等分割）
- 不均等分割のテスト
- エラーケースのテスト
- パス処理のテスト（相対パス・絶対パス）
- 異なるディレクトリからの実行テスト