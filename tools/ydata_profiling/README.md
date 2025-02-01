# YData Profiling Tool

このツールは、ydata-profilingライブラリを使用してデータの探索的分析を自動化します。

## 機能

- CSVファイルとExcelファイル(.xlsx, .xls)の自動プロファイリング
- 日本語を含むUnicodeデータの適切な処理
- データの統計情報の生成
- データの可視化とレポート作成
- インタラクティブなデータ分析

## インストール

1. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

## 使用方法

### コマンドライン

```bash
# CSVファイルの場合
python ydata_profiling.py your_data.csv

# Excelファイルの場合
python ydata_profiling.py your_data.xlsx
```

### Pythonコード内で使用

```python
import pandas as pd
from ydata_profiling import ProfileReport

# CSVファイルの読み込み（日本語対応）
df = pd.read_csv("your_data.csv", encoding='utf-8')  # または 'cp932', 'shift_jis'

# Excelファイルの読み込み
# df = pd.read_excel("your_data.xlsx")

# プロファイルレポートの生成
profile = ProfileReport(df)

# HTMLレポートとして保存
profile.to_file("output/your_report.html")

# Jupyter Notebookでの表示
profile.to_widgets()
```

## 対応ファイル形式

- CSV (.csv)
  - UTF-8
  - CP932 (Shift-JIS)
  - その他のエンコーディングも自動検出

- Excel
  - .xlsx
  - .xls

## 出力

- HTMLレポートが`output`ディレクトリに生成されます
- ファイル名形式: `{元のファイル名}_profile_{タイムスタンプ}.html`

## レポートの内容

生成されるレポートには以下の情報が含まれます：

- データの概要
- 変数の分析
- 相関分析
- 欠損値の分析
- サンプルデータ

## エラー処理

一般的なエラーと対処方法：

- ファイルが見つからない場合：ファイルパスを確認
- メモリ不足：大きなデータセットの場合はサンプリングを検討
- エンコーディングエラー：
  - CSVファイルの場合、適切なエンコーディングを指定（utf-8, cp932, shift_jis）
  - Excelファイルの場合、ファイルが破損していないか確認

## 貢献

改善案やバグ報告は、issueまたはプルリクエストでお願いします。