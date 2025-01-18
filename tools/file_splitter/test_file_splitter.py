import os
import pytest
from file_splitter import split_file, get_absolute_path

def create_test_file(path: str, content: str):
    """テストファイル作成用ヘルパー関数"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def read_file(path: str) -> str:
    """ファイル読み込み用ヘルパー関数"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

@pytest.fixture
def test_file(tmp_path):
    """テストファイル作成用フィクスチャ"""
    file_path = tmp_path / "test.txt"
    content = "あいうえお" * 20  # 100文字
    create_test_file(file_path, content)
    yield file_path
    # クリーンアップ
    for f in tmp_path.glob("test_split_*.txt"):
        f.unlink()

def test_get_absolute_path():
    """パス変換機能のテスト"""
    # 相対パスのテスト
    rel_path = "test.txt"
    abs_path = get_absolute_path(rel_path)
    assert os.path.isabs(abs_path)
    assert abs_path.endswith("test.txt")
    
    # 絶対パスのテスト
    if os.name == 'nt':  # Windows
        abs_input = "C:\\temp\\test.txt"
    else:  # Unix系
        abs_input = "/tmp/test.txt"
    assert get_absolute_path(abs_input) == abs_input

def test_split_file_basic(test_file):
    """基本的な分割機能のテスト"""
    # 5分割で実行（絶対パスを使用）
    abs_path = get_absolute_path(str(test_file))
    split_files = split_file(abs_path, 5)
    
    # 5つのファイルが生成されていることを確認
    assert len(split_files) == 5
    
    # 各分割ファイルの内容を確認
    total_content = ""
    for file in split_files:
        assert os.path.isabs(file)  # 絶対パスであることを確認
        content = read_file(file)
        assert len(content) == 20  # 100文字÷5=20文字
        total_content += content
    
    # 全体の内容が元ファイルと一致することを確認
    original_content = read_file(abs_path)
    assert total_content == original_content

def test_split_file_relative_path(test_file):
    """相対パスでの分割テスト"""
    # カレントディレクトリを変更してテスト
    original_dir = os.getcwd()
    os.chdir(str(test_file.parent))
    
    try:
        rel_path = test_file.name
        split_files = split_file(rel_path, 3)
        
        # 分割ファイルが生成されていることを確認
        assert len(split_files) == 3
        # すべての分割ファイルが絶対パスで返されることを確認
        assert all(os.path.isabs(f) for f in split_files)
    finally:
        os.chdir(original_dir)

def test_split_file_invalid_path():
    """存在しないファイルパスの場合のテスト"""
    with pytest.raises(FileNotFoundError):
        split_file("not_exists.txt", 5)

def test_split_file_invalid_splits():
    """不正な分割数の場合のテスト"""
    with pytest.raises(ValueError):
        split_file("dummy.txt", 0)
    with pytest.raises(ValueError):
        split_file("dummy.txt", -1)

def test_split_file_uneven_split(tmp_path):
    """不均等な分割のテスト"""
    file_path = tmp_path / "uneven.txt"
    content = "あいうえお" * 7  # 35文字
    create_test_file(str(file_path), content)
    
    # 3分割で実行
    split_files = split_file(str(file_path), 3)
    
    # 分割ファイルの内容を確認
    contents = [read_file(f) for f in split_files]
    assert len(contents[0]) == 12  # 最初の分割
    assert len(contents[1]) == 12  # 2番目の分割
    assert len(contents[2]) == 11  # 最後の分割（余り）
    
    # 全体の内容が元ファイルと一致することを確認
    combined = "".join(contents)
    assert combined == content