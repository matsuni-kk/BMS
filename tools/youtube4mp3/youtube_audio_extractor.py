import os
import yt_dlp

def download_audio(youtube_url: str, output_template: str):
    """
    YouTubeのURLから音声を抽出し、MP3形式に変換して保存する関数。

    Args:
        youtube_url (str): 処理対象のYouTubeのURL
        output_template (str): 出力ファイル名のテンプレート。必ずこのpyファイルと同階層の "output" フォルダに保存されます。
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([youtube_url])
        except Exception as e:
            print(f"エラーが発生しました: {e}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="YouTubeから音声を抽出し、MP3に変換するツール"
    )
    parser.add_argument('url', help='変換対象のYouTubeのURL')
    parser.add_argument(
        '--filename',
        default='%(title)s.%(ext)s',
        help='出力ファイル名のテンプレート（ディレクトリは固定: このpyファイルと同階層の「output」フォルダ）'
    )

    args = parser.parse_args()

    # このpyファイルと同階層にある "output" フォルダのパスを設定
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fixed_output_dir = os.path.join(script_dir, "output")
    os.makedirs(fixed_output_dir, exist_ok=True)

    # ユーザ引数の--filenameにディレクトリ構造が含まれていた場合でも、basenameのみ抽出して固定ディレクトリと連結する
    output_template = os.path.join(fixed_output_dir, os.path.basename(args.filename))

    download_audio(args.url, output_template)