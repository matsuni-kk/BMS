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
    def __init__(self, debug: bool = False, start_date: datetime = None, end_date: datetime = None):
        self.debug = debug
        self.start_date = start_date
        self.end_date = end_date

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

        # ヘッダー情報の生成（生成日時は日付のみ表示）
        markdown_lines = []
        markdown_lines.append(f"# ディレクトリ構造: {dir_path.name}\n")
        markdown_lines.append(f"生成日時: {datetime.now().strftime('%Y-%m-%d')}\n")

        # 再帰的にディレクトリ構造を生成
        tree_lines = self._generate_markdown_tree(dir_path)
        markdown_lines.extend(tree_lines)

        return "\n".join(markdown_lines)

    def _generate_markdown_tree(self, current_path: Path, prefix: str = "") -> list:
        """
        ディレクトリとファイルを再帰的に探索し、Markdown形式のツリー構造を生成します。

        ディレクトリは ├── または └── を先頭に、子要素のインデントは "│   " または "    " を利用して表現します。
        もしディレクトリ内にファイルやサブディレクトリがなければ「# 空」と表示します。
        """
        try:
            entries = list(current_path.iterdir())
        except Exception as e:
            logger.error(f"ディレクトリエントリの取得に失敗しました: {current_path} - {e}")
            return []
        # ソート：ディレクトリを先に、次にファイル（アルファベット順）
        entries = sorted(entries, key=lambda p: self._safe_key(p))
        lines = []
        for index, entry in enumerate(entries):
            connector = "└── " if index == len(entries) - 1 else "├── "
            if entry.is_dir():
                line = f"{prefix}{connector}{entry.name}/"
                sub_prefix = prefix + ("    " if index == len(entries) - 1 else "│   ")
                children = self._generate_markdown_tree(entry, sub_prefix)
                if not children:
                    line += "  # 空"
                    lines.append(line)
                else:
                    lines.append(line)
                    lines.extend(children)
            else:
                try:
                    stat_info = entry.stat()
                    file_size = stat_info.st_size
                    # 最終更新日時を日付のみ取得（YYYY-MM-DD）
                    mod_time = datetime.fromtimestamp(stat_info.st_mtime).date()
                    mod_time_str = mod_time.strftime('%Y-%m-%d')
                    file_size_str = self._format_file_size(file_size)
                except Exception as e:
                    logger.error(f"ファイル情報の取得に失敗しました: {entry} - {e}")
                    file_size_str = "取得失敗"
                    mod_time = None
                    mod_time_str = "取得失敗"
                # 期間指定が有効なら、更新日時フィルターを適用（比較は日付同士）
                if self.start_date is not None and self.end_date is not None:
                    if mod_time is None or not (self.start_date <= mod_time <= self.end_date):
                        continue
                lines.append(f"{prefix}{connector}{entry.name} ({file_size_str}, 更新: {mod_time_str})")
        return lines

    def _safe_key(self, p: Path) -> tuple:
        """
        ソート用のキーを安全に取得します。
        p.is_dir() や p.name の取得で例外が発生した場合はエラーログを出力し、
        ディレクトリでない（＝ファイル扱い）として扱います。
        """
        try:
            is_dir = p.is_dir()
        except Exception as e:
            logger.error(f"ディレクトリ判断に失敗しました: {p} - {e}")
            is_dir = False
        try:
            name = p.name.lower()
        except Exception as e:
            logger.error(f"名称取得に失敗しました: {p} - {e}")
            name = ""
        return (not is_dir, name)

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

    elif len(sys.argv) == 4:
        try:
            # 期間指定を日付のみ（YYYY-MM-DD）で受け付ける
            start_date = datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
            end_date = datetime.strptime(sys.argv[3], "%Y-%m-%d").date()
        except Exception as e:
            print("日付のフォーマットは YYYY-MM-DD の形式で入力してください。")
            sys.exit(1)
        converter = DirStructureToMarkdown(debug=True, start_date=start_date, end_date=end_date)
    else:
        converter = DirStructureToMarkdown(debug=True)

    dir_path = sys.argv[1]
    converter.run(dir_path)

if __name__ == "__main__":
    main() 