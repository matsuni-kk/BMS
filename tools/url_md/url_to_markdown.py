from langchain_community.document_loaders import WebBaseLoader
import datetime
import os

OUTPUT_DIR = "url_md/output"

def convert_url_to_markdown(url):
    """
    指定されたURLのウェブページを読み込み、Documentオブジェクトを返す関数。

    Args:
        url (str): 読み込むウェブページのURL。

    Returns:
        Document: ウェブページのコンテンツとメタデータを含むDocumentオブジェクト。
    """
    loader = WebBaseLoader(url)
    document = loader.load()[0]
    return document

# 使用例
if __name__ == "__main__":
    url = "https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%B3%E3%83%87%E3%83%BC%E3%82%B5%E3%82%A4%E3%83%AC%E3%83%B3%E3%82%B9"  # 変換したいURLを指定
    document = convert_url_to_markdown(url)

    # ファイル名を生成
    now = datetime.datetime.now()
    filename = f"{now.strftime('%Y%m%d')}_output.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # ファイルに書き込み
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(document.page_content)

    print(f"Saved to {filepath}")