import pytest
from .url_to_markdown import convert_url_to_markdown

def test_convert_url_to_markdown_valid_url():
    """
    有効なURLを指定した場合に、Markdown形式の文字列が返されることを確認するテスト。
    """
    url = "https://example.com"
    markdown_text = convert_url_to_markdown(url)
    assert isinstance(markdown_text, str)
    assert len(markdown_text) > 0

def test_convert_url_to_markdown_invalid_url():
    """
    無効なURLを指定した場合に、空の文字列が返されることを確認するテスト。
    """
    url = "https://invalid-url"
    markdown_text = convert_url_to_markdown(url)
    assert markdown_text == ""