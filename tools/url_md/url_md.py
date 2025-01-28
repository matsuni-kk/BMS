import os
import sys
import requests
import tempfile
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
from langchain_community.document_loaders import UnstructuredHTMLLoader

def get_domain(url):
    """URLからドメインを取得する"""
    parsed_uri = urlparse(url)
    return parsed_uri.netloc

def fetch_url_to_markdown(url):
    """URLの内容を取得してMarkdown形式に変換する"""
    try:
        # ブラウザのように振る舞うヘッダーを設定
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ja,en-US;q=0.7,en;q=0.3'
        }

        # ウェブページのHTMLコンテンツを取得
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.content.decode('utf-8', 'ignore')

        # 一時ファイルを作成してHTMLを保存
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.html', delete=False) as temp_file:
            temp_file.write(html_content)
            temp_path = temp_file.name

        try:
            # UnstructuredHTMLLoaderを使用してHTMLを読み込み
            loader = UnstructuredHTMLLoader(temp_path)
            documents = loader.load()

            # Markdownコンテンツを生成
            markdown_content = []
            
            # メタ情報を追加
            domain = get_domain(url)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            markdown_content.extend([
                "# ページコンテンツ\n",
                f"URL: {url}\n",
                f"ドメイン: {domain}\n",
                f"取得日時: {current_time}\n\n",
                "## 本文\n\n"
            ])

            # ドキュメントの内容を追加
            for doc in documents:
                markdown_content.append(doc.page_content)

            return ''.join(markdown_content)

        finally:
            # 一時ファイルを削除
            os.unlink(temp_path)

    except requests.RequestException as e:
        return f"# エラー\n\nURLの取得中にエラーが発生しました: {str(e)}\n"
    except Exception as e:
        return f"# エラー\n\n予期せぬエラーが発生しました: {str(e)}\n"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("使用方法: python url_md.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1]
    markdown_content = fetch_url_to_markdown(url)
    
    # 出力ディレクトリを固定
    output_dir = Path("D:/BMS/tools/url_md/output")
    output_dir.mkdir(exist_ok=True)
    
    # 出力ファイル名を生成
    domain = get_domain(url)
    output_file = output_dir / f"{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    # 結果を保存
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"変換が完了しました: {output_file}")