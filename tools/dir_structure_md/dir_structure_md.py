from typing import Union
import os
from pathlib import Path
from datetime import datetime
import logging
import sys

# ログファイルの設定：ログファイルはBMS\tools\markitdown_anyfolder\logに保存する
log_dir = Path(__file__).parent / 'log'
log_dir.mkdir(parents=True, exist_ok=True)
LOG_FILE = log_dir / 'dir_structure_md.log'
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(str(LOG_FILE), encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DirStructureToMarkdown:
    def __init__(self, debug: bool = False):
        self.debug = debug

    def _log(self, message: str):
        """デバッグログを出力"""
        if self.debug:
            logger.debug(message)

    def generate_markdown(self, dir_path: Union[str, Path]) -> str:
        """
        ディレクトリ構造をMarkdown形式で生成します。

        Args:
            dir_path: ディレクトリのパス

        Returns:
            str: Markdown形式のディレクトリ構造
        """
        dir_path = Path(dir_path).resolve()
        self._log(f"入力ディレクトリ: {dir_path}")

        if not dir_path.exists():
            error_msg = f"ディレクトリが見つかりません: {dir_path}"
            logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        if not dir_path.is_dir():
            error_msg = f"指定されたパスはディレクトリではありません: {dir_path}"
            logger.error(error_msg)
            raise NotADirectoryError(error_msg)

        markdown_lines = []
        markdown_lines.append(f"# ディレクトリ構造: {dir_path.name}\n\n")
        markdown_lines.append(f"生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for root, dirs, files in os.walk(dir_path):
            level = root.replace(str(dir_path), '').count(os.sep)
            indent = '    ' * level
            root_name = Path(root).name
            markdown_lines.append(f"{indent}{root_name}/")
            sub_indent = '    ' * (level + 1)
            for f in files:
                file_path = Path(root) / f
                file_size = file_path.stat().st_size
                file_size_str = self._format_file_size(file_size)
                markdown_lines.append(f"{sub_indent}├── {f} ({file_size_str})")
            if not files and not dirs and root != str(dir_path): # rootがdir_path自身でない場合のみ
                markdown_lines.pop() # 親ディレクトリのエントリを削除
                markdown_lines.append(f"{indent}{root_name}/  # 空")


        return '\n'.join(markdown_lines)

    def save_markdown(self, markdown_content: str, output_path: Path):
        """
        Markdownコンテンツをファイルに保存します。
        """
        self._log(f"保存先: {output_path}")
        try:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            self._log("保存完了")
        except Exception as e:
            logger.error(f"保存エラー: {str(e)}")
            raise

    def run(self, dir_path: Union[str, Path]):
        """
        メインの実行関数
        """
        try:
            markdown_content = self.generate_markdown(dir_path)

            # 出力ディレクトリを作成
            output_dir = Path(__file__).parent / 'output'
            output_dir.mkdir(parents=True, exist_ok=True)

            # 出力ファイル名を生成
            output_filename = "dir_structure_" + datetime.now().strftime('%Y%m%d_%H%M%S') + '.md'
            output_path = output_dir / output_filename

            # Markdownファイルを保存
            self.save_markdown(markdown_content, output_path)
            print(f"ディレクトリ構造をMarkdown形式で保存しました: {output_path}")

        except Exception as e:
            logger.error(f"エラーが発生しました: {str(e)}")
            logger.exception("詳細なエラー情報:")
            print(f"エラーが発生しました: {str(e)}")
            sys.exit(1)

    def _format_file_size(self, size_in_bytes: int) -> str:
        """
        ファイルサイズを適切な単位でフォーマットします。
        """
        if size_in_bytes < 1024:
            return f"{size_in_bytes} B"
        elif size_in_bytes < 1024 * 1024:
            size_in_kb = size_in_bytes / 1024
            return f"{size_in_kb:.2f} KB"
        elif size_in_bytes < 1024 * 1024 * 1024:
            size_in_mb = size_in_bytes / (1024 * 1024)
            return f"{size_in_mb:.2f} MB"
        else:
            size_in_gb = size_in_bytes / (1024 * 1024 * 1024)
            return f"{size_in_gb:.2f} GB"


def main():
    if len(sys.argv) < 2:
        print("使用方法: python dir_structure_md.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1]
    converter = DirStructureToMarkdown(debug=True)
    converter.run(dir_path)

if __name__ == "__main__":
    main() 