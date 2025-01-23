import os
import sys
import re
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, quote_plus
from datetime import datetime
from pathlib import Path

# パッケージのパスを追加
package_path = Path(__file__).parent.parent / 'packages/url_md'
sys.path.append(str(package_path))

try:
    import langchain_community
except ImportError:
    print("必要なパッケージがインストールされていません。")
    print("以下のコマンドを実行してください：")
    print(f"pip install -r {package_path}/requirements.txt")
    sys.exit(1)

def extract_title(soup):
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.string.strip()
    return None

def extract_description(soup):
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        return meta_desc.get('content', '').strip()
    return None

def get_domain(url):
    parsed_uri = urlparse(url)
    return parsed_uri.netloc

def encode_url(url):
    """URLを正しくエンコードする"""
    parsed = urlparse(url)
    path_parts = parsed.path.split('/')
    encoded_parts = [quote_plus(part, safe='') for part in path_parts if part]
    encoded_path = '/' + '/'.join(encoded_parts)
    return f"{parsed.scheme}://{parsed.netloc}{encoded_path}"

def fetch_url_info(url):
    try:
        # URLをエンコード
        encoded_url = encode_url(url)
        response = requests.get(encoded_url)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = extract_title(soup)
        description = extract_description(soup)
        domain = get_domain(url)
        
        # Markdown形式で情報を整形
        markdown = []
        markdown.append(f"# {title if title else 'ページタイトルなし'}\n\n")
        markdown.append(f"URL: {url}\n")
        markdown.append(f"ドメイン: {domain}\n")
        markdown.append(f"取得日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        if description:
            markdown.append(f"## 説明\n\n{description}\n\n")
            
        # 本文の抽出（主要なコンテンツ領域を探す）
        main_content = soup.find('main') or soup.find(id='content') or soup.find(class_='content')
        if main_content:
            markdown.append("## 本文\n\n")
            for p in main_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                text = p.get_text().strip()
                if text:
                    if p.name.startswith('h'):
                        level = int(p.name[1])
                        markdown.append(f"{'#' * level} {text}\n\n")
                    else:
                        markdown.append(f"{text}\n\n")
        
        return ''.join(markdown)
        
    except requests.RequestException as e:
        return f"# エラー\n\nURLの取得中にエラーが発生しました: {str(e)}\n"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("使用方法: python url_md.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1]
    markdown_content = fetch_url_info(url)
    
    # 出力ディレクトリを固定
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)
    
    # 出力ファイル名を生成
    domain = get_domain(url)
    output_file = output_dir / f"{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    
    # 結果を保存
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"変換が完了しました: {output_file}")