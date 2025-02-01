#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BMSのデータ分析自動化ツール
ydata-profilingを使用してデータの探索的分析を行います。
CSVファイルとExcelファイルに対応し、日本語のデータも適切に処理します。
"""

import os
import sys
import pandas as pd
from ydata_profiling import ProfileReport
from datetime import datetime

def detect_file_type(file_path):
    """
    ファイルの拡張子からファイルタイプを判定します。

    Parameters:
        file_path (str): ファイルパス
    
    Returns:
        str: ファイルタイプ ('csv', 'excel', または 'unknown')
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.csv':
        return 'csv'
    elif ext in ['.xlsx', '.xls']:
        return 'excel'
    return 'unknown'

def read_data_file(file_path):
    """
    CSVまたはExcelファイルを読み込みます。
    日本語の文字化けを防ぐため、適切なエンコーディングを使用します。

    Parameters:
        file_path (str): ファイルパス
    
    Returns:
        pd.DataFrame: 読み込んだデータフレーム
    """
    file_type = detect_file_type(file_path)
    
    try:
        if file_type == 'csv':
            # 日本語文字化け対策として複数のエンコーディングを試行
            encodings = ['utf-8', 'cp932', 'shift_jis']
            for encoding in encodings:
                try:
                    return pd.read_csv(file_path, encoding=encoding)
                except UnicodeDecodeError:
                    continue
            raise ValueError(f"ファイルのエンコーディングを特定できません: {file_path}")
        
        elif file_type == 'excel':
            return pd.read_excel(file_path)
        
        else:
            raise ValueError(f"未対応のファイル形式です: {file_path}")
            
    except Exception as e:
        print(f"ファイルの読み込み中にエラーが発生しました: {str(e)}", file=sys.stderr)
        raise

def create_profile_report(file_path, output_dir='output'):
    """
    CSVまたはExcelファイルからプロファイルレポートを生成します。

    Parameters:
        file_path (str): 分析対象のファイルパス（CSVまたはExcel）
        output_dir (str): 出力ディレクトリ（デフォルト: 'output'）
    
    Returns:
        str: 生成されたレポートのパス
    """
    try:
        # 出力ディレクトリの作成
        os.makedirs(output_dir, exist_ok=True)
        
        # ファイルの読み込み
        print(f"ファイルを読み込んでいます: {file_path}")
        df = read_data_file(file_path)
        
        # ファイル名から拡張子を除去
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # タイムスタンプ
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # レポートの生成（日本語フォントに対応）
        print("プロファイルレポートを生成しています...")
        profile = ProfileReport(
            df,
            title=f"Profiling Report - {base_name}",
            html={
                'style': {'full_width': True},
                'minify': True
            },
            progress_bar=True,
            explorative=True
        )
        
        # レポートの保存
        output_path = os.path.join(output_dir, f"{base_name}_profile_{timestamp}.html")
        profile.to_file(output_path)
        
        print(f"レポートが生成されました: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}", file=sys.stderr)
        raise

def main():
    """
    コマンドライン引数からファイルを読み込み、レポートを生成します。
    CSVファイルとExcelファイルに対応しています。
    """
    if len(sys.argv) < 2:
        print("使用方法: python profile_generator.py <ファイル名>", file=sys.stderr)
        print("対応形式: .csv, .xlsx, .xls", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"ファイルが見つかりません: {file_path}", file=sys.stderr)
        sys.exit(1)
    
    try:
        output_path = create_profile_report(file_path)
        print("\n分析が完了しました。")
        print(f"レポートは以下のパスに保存されました:\n{output_path}")
    except Exception as e:
        print(f"プログラムの実行中にエラーが発生しました: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()