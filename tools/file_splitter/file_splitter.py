import os
import math
import argparse

def get_absolute_path(file_path: str) -> str:
    """
    相対パスを絶対パスに変換する
    
    Args:
        file_path: 対象ファイルパス
        
    Returns:
        絶対パス
    """
    if os.path.isabs(file_path):
        return file_path
    return os.path.abspath(file_path)

def split_file(file_path: str, num_splits: int) -> list[str]:
    """
    指定されたファイルを文字数単位で指定数に分割する
    
    Args:
        file_path: 分割対象のファイルパス（相対パスまたは絶対パス）
        num_splits: 分割数
        
    Returns:
        生成された分割ファイルのパスのリスト
    
    Raises:
        FileNotFoundError: ファイルが存在しない場合
        ValueError: 分割数が1未満の場合
    """
    # パスの正規化
    abs_path = get_absolute_path(file_path)
    
    # 入力チェック
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"ファイルが見つかりません: {abs_path}")
    
    if not isinstance(num_splits, int) or num_splits < 1:
        raise ValueError("分割数は1以上の整数を指定してください")
        
    # ファイル読み込み
    with open(abs_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分割サイズ計算
    total_chars = len(content)
    chars_per_split = math.ceil(total_chars / num_splits)
    
    # 分割処理
    splits = []
    dir_path = os.path.dirname(abs_path)
    base_name, ext = os.path.splitext(os.path.basename(abs_path))
    
    for i in range(num_splits):
        start = i * chars_per_split
        end = min((i + 1) * chars_per_split, total_chars)
        split_content = content[start:end]
        
        # 空の分割は作成しない
        if not split_content:
            break
            
        # 分割ファイル名生成（元ファイルと同じディレクトリに作成）
        split_path = os.path.join(dir_path, f"{base_name}_split_{i+1}{ext}")
        
        # 分割ファイル作成
        with open(split_path, 'w', encoding='utf-8') as f:
            f.write(split_content)
            
        splits.append(split_path)
    
    return splits

def main():
    parser = argparse.ArgumentParser(description="ファイルを指定数に分割します")
    parser.add_argument("file_path", help="分割対象のファイルパス（相対パスまたは絶対パス）")
    parser.add_argument("num_splits", type=int, help="分割数")
    
    args = parser.parse_args()
    
    try:
        abs_path = get_absolute_path(args.file_path)
        split_files = split_file(abs_path, args.num_splits)
        print(f"ファイルを{len(split_files)}個に分割しました:")
        print(f"元ファイル: {abs_path}")
        print("\n分割ファイル:")
        for file in split_files:
            print(f"- {file}")
    except (FileNotFoundError, ValueError) as e:
        print(f"エラー: {e}")
        exit(1)

if __name__ == "__main__":
    main()