import pytest
import asyncio
from tools.markitdown.markitdown import convert_to_markdown

@pytest.mark.asyncio
async def test_convert_to_markdown_valid_url():
    # 有効なURLのテスト
    url = "https://www.example.com"
    result = await convert_to_markdown(url)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "#" in result  # Markdownコンテンツに#が含まれていることを確認

@pytest.mark.asyncio
async def test_convert_to_markdown_invalid_url():
    # 無効なURLのテスト
    url = "https://invalid-url"
    with pytest.raises(Exception):
        await convert_to_markdown(url)