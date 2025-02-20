import argparse
import os
import sys
import requests
import tempfile
import re
from datetime import datetime
from urllib.parse import urlparse, urljoin
from langchain_community.document_loaders import UnstructuredHTMLLoader, UnstructuredPDFLoader
from bs4 import BeautifulSoup
import concurrent.futures

def get_domain(url):
    """
    URLからドメインを取得する関数
    """
    parsed_uri = urlparse(url)
    return parsed_uri.netloc

def fetch_url_to_markdown(url):
    """
    URLの内容を取得してMarkdown形式に変換する関数

    ・URLがPDFの場合:
      UnstructuredPDFLoader（mode="paged", languages=["ja"]）を使用してPDFからドキュメントを読み込みます。
    ・URLがPDF以外の場合:
      UnstructuredHTMLLoaderを使用してHTMLを解析しMarkdown化します。

    ※取得したコンテンツはHTTPヘッダーや内部情報からエンコーディングを自動検出し、適切にデコードします。
      また、対象のURLのドメインが日本のサイト（.jp）の場合は、強制的にshift_jisを使用します。
    """
    try:
        if url.lower().endswith('.pdf'):
            # PDFの場合
            response = requests.get(url)
            response.raise_for_status()
            pdf_content = response.content
            # 一時ファイルにPDFを保存（バイナリモード）
            with tempfile.NamedTemporaryFile(mode='wb', suffix='.pdf', delete=False) as temp_file:
                temp_file.write(pdf_content)
                temp_path = temp_file.name

            try:
                # UnstructuredPDFLoaderを使用してPDFからドキュメントを読み込む（ページ単位・日本語対応）
                loader = UnstructuredPDFLoader(temp_path, mode="paged", languages=["ja"])
                documents = loader.load()

                domain = get_domain(url)
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                markdown_content = [
                    "# ページコンテンツ\n",
                    f"URL: {url}\n",
                    f"ドメイン: {domain}\n",
                    f"取得日時: {current_time}\n\n",
                    "## 本文\n\n"
                ]
                for doc in documents:
                    markdown_content.append(doc.page_content)
                return ''.join(markdown_content)
            finally:
                os.unlink(temp_path)
        else:
            # HTMLの場合
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'ja,en-US;q=0.7,en;q=0.3'
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            current_domain = get_domain(url)
            if current_domain.endswith('.jp'):
                response.encoding = 'shift_jis'
            elif not response.encoding:
                response.encoding = response.apparent_encoding
            html_content = response.text

            # 一時ファイルにHTMLを保存（UnstructuredHTMLLoaderの仕様上）
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.html', delete=False) as temp_file:
                temp_file.write(html_content)
                temp_path = temp_file.name

            try:
                loader = UnstructuredHTMLLoader(temp_path)
                documents = loader.load()

                domain = current_domain
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                markdown_content = [
                    "# ページコンテンツ\n",
                    f"URL: {url}\n",
                    f"ドメイン: {domain}\n",
                    f"取得日時: {current_time}\n\n",
                    "## 本文\n\n"
                ]
                for doc in documents:
                    markdown_content.append(doc.page_content)
                return ''.join(markdown_content)
            finally:
                os.unlink(temp_path)

    except requests.RequestException as e:
        return f"# エラー\n\nURLの取得中にエラーが発生しました: {str(e)}\n"
    except Exception as e:
        return f"# エラー\n\n予期せぬエラーが発生しました: {str(e)}\n"

def extract_related_urls(url, domain):
    """
    指定URLのHTMLから、同一ドメイン内のリンクを抽出する関数

    ※変更点:
      - 従来のaタグによるリンク抽出に加え、
      - scriptタグ内に埋め込まれたJavaScriptのテキストからも正規表現を使用してURLを抽出、
      - scriptタグおよびiframeタグのsrc属性からもURLを抽出します。
      また、対象のURLのドメインが日本のサイト（.jp）であれば、shift_jisを使用します。
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve {url}")
            return []
        current_domain = get_domain(url)
        if current_domain.endswith('.jp'):
            response.encoding = 'shift_jis'
        elif not response.encoding:
            response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()
        # aタグによるリンク抽出
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            abs_url = urljoin(url, href)  # 絶対URLに変換
            if get_domain(abs_url) == domain:
                links.add(abs_url)
        # scriptタグからのリンク抽出（src属性および内部JavaScript）
        for script in soup.find_all("script"):
            if script.has_attr("src"):
                src_url = script.get("src")
                abs_url = urljoin(url, src_url)
                if get_domain(abs_url) == domain:
                    links.add(abs_url)
            if script.string:
                found_urls = re.findall(r"(https?://[^\s'\"<>]+)", script.string)
                for found_url in found_urls:
                    abs_url = urljoin(url, found_url)
                    if get_domain(abs_url) == domain:
                        links.add(abs_url)
        # iframeタグのsrc属性からの抽出
        for iframe in soup.find_all("iframe", src=True):
            src_url = iframe.get("src")
            abs_url = urljoin(url, src_url)
            if get_domain(abs_url) == domain:
                links.add(abs_url)
        return list(links)
    except Exception as e:
        print(f"Error extracting links from {url}: {e}")
        return []

def process_single_url(url, domain):
    """
    指定URLについて、Markdown変換と関連リンク抽出を
    ローカルのスレッドプールを用いて並列処理する関数
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as local_executor:
        future_md = local_executor.submit(fetch_url_to_markdown, url)
        future_links = local_executor.submit(extract_related_urls, url, domain)
        md = future_md.result()
        links = future_links.result()
    return md, links

def crawl_and_collect_markdown_parallel(start_url, max_pages=50):
    """
    入力URLを起点に、同一ドメイン内の関連URLをBFS方式で巡回しながら
    並列処理でMarkdown化する関数
    最大 max_pages 件のページを1つのMarkdown文字列にまとめて返します。
    並列処理は max_workers=20 として実行
    """
    domain = get_domain(start_url)
    visited = set()
    queue = [start_url]
    markdown_results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        while queue and len(visited) < max_pages:
            current_batch = []
            while queue and len(current_batch) < (max_pages - len(visited)):
                next_url = queue.pop(0)
                if next_url in visited:
                    continue
                current_batch.append(next_url)

            future_to_url = {executor.submit(process_single_url, url, domain): url for url in current_batch}

            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    md, related = future.result()
                except Exception as e:
                    md = f"# エラー\n\n{url} の処理中にエラーが発生しました: {e}\n"
                    related = []
                header = f"\n\n# {url}\n\n"
                markdown_results.append(header + md)
                visited.add(url)
                print(f"Finished processing: {url}")
                for rel_url in related:
                    if rel_url not in visited and rel_url not in queue and len(visited) + len(queue) < max_pages:
                        queue.append(rel_url)

    return "\n\n".join(markdown_results)

def crawl_and_collect_markdown_deepsearch(start_url):
    """
    DeepSearch機能:
    - 開始URLから関連URL（レベル1）を最大20件抽出し、
    - 各レベル1のURLからさらに関連URL（レベル2）を最大10件抽出する
    並列処理でMarkdown化し、全体を1つのMarkdown文字列にまとめて返します。
    並列処理は max_workers=20 として実行
    """
    domain = get_domain(start_url)
    visited = set()
    markdown_results = []

    print(f"Processing: {start_url}")
    md_start = fetch_url_to_markdown(start_url)
    markdown_results.append(f"\n\n# {start_url}\n\n" + md_start)
    visited.add(start_url)

    level1_urls = extract_related_urls(start_url, domain)
    level1_urls = list(dict.fromkeys(level1_urls))
    if len(level1_urls) > 20:
        level1_urls = level1_urls[:20]

    results_level1 = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(process_single_url, url, domain): url for url in level1_urls if url not in visited}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                md, related = future.result()
            except Exception as e:
                md = f"# エラー\n\n{url} の処理中にエラーが発生しました: {e}\n"
                related = []
            results_level1.append((url, md, related))
            visited.add(url)
            print(f"Finished processing: {url}")

    for url, md, _ in results_level1:
        markdown_results.append(f"\n\n# {url}\n\n" + md)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {}
        for parent_url, _, related in results_level1:
            unique_related = []
            for rel_url in related:
                if rel_url not in visited:
                    unique_related.append(rel_url)
                    visited.add(rel_url)
            if len(unique_related) > 10:
                unique_related = unique_related[:10]
            for url in unique_related:
                future = executor.submit(fetch_url_to_markdown, url)
                future_to_url[future] = url
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                md = future.result()
            except Exception as e:
                md = f"# エラー\n\n{url} の処理中にエラーが発生しました: {e}\n"
            markdown_results.append(f"\n\n# {url}\n\n" + md)
            print(f"Finished processing: {url}")

    return "\n\n".join(markdown_results)

def save_markdown_file(content, output_dir=None):
    """
    生成したMarkdown文字列を、ツールファイルと同じ階層の output ディレクトリに
    タイムスタンプ付きファイル名で保存する関数
    """
    if output_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(base_dir, "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"output_{timestamp}.md"
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Markdown saved to: {file_path}")
    return file_path

def main():
    parser = argparse.ArgumentParser(description="URLからMarkdown作成ツール")
    parser.add_argument("--url", type=str, required=True, help="変換対象のURL")
    parser.add_argument("--mode", type=str, choices=["single", "aggregate", "deepsearch"], default="single",
                        help="抽出モード: 'single'は単一URLのみ、'aggregate'は関連URLも含めた複数ページを並列処理、'deepsearch'はさらにレベルを深く探査します")
    args = parser.parse_args()

    if args.mode == "single":
        print(f"Processing single URL: {args.url}")
        md_content = fetch_url_to_markdown(args.url)
        if md_content:
            md_content = f"# {args.url}\n\n" + md_content
            print(f"Finished processing single URL: {args.url}")
            save_markdown_file(md_content)
        else:
            print("Markdown生成に失敗しました。")
    elif args.mode == "aggregate":
        print(f"Processing aggregate mode for URL: {args.url}")
        aggregated_md = crawl_and_collect_markdown_parallel(args.url, max_pages=50)
        if aggregated_md:
            save_markdown_file(aggregated_md)
        else:
            print("Markdown生成に失敗しました。")
    elif args.mode == "deepsearch":
        print(f"Processing deepsearch mode for URL: {args.url}")
        deep_md = crawl_and_collect_markdown_deepsearch(args.url)
        if deep_md:
            save_markdown_file(deep_md)
        else:
            print("Markdown生成に失敗しました。")

if __name__ == "__main__":
    main()
