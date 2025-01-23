import sys
import subprocess
from pathlib import Path

def setup_packages():
    """必要なパッケージをダウンロードしてtools/packagesに保存"""
    packages_dir = Path(__file__).parent.parent / 'packages'
    if not packages_dir.exists():
        packages_dir.mkdir(parents=True)
        
    requirements_file = Path(__file__).parent.parent / 'packages/wordcloud/requirements.txt'
    
    print('パッケージをダウンロードしています...')
    try:
        subprocess.run([
            sys.executable,
            '-m',
            'pip',
            'download',
            '-r',
            str(requirements_file),
            '--dest',
            str(packages_dir),
            '--no-deps'
        ], check=True)
        print('パッケージのダウンロードが完了しました')
    except subprocess.CalledProcessError as e:
        print(f'パッケージのダウンロード中にエラーが発生しました: {e}')
        sys.exit(1)

def install_packages():
    """パッケージをインストール"""
    requirements_file = Path(__file__).parent.parent / 'packages/wordcloud/requirements.txt'
    
    print('パッケージをインストールしています...')
    try:
        subprocess.run([
            sys.executable,
            '-m',
            'pip',
            'install',
            '-r',
            str(requirements_file)
        ], check=True)
        print('パッケージのインストールが完了しました')
    except subprocess.CalledProcessError as e:
        print(f'パッケージのインストール中にエラーが発生しました: {e}')
        sys.exit(1)

def generate_wordcloud(input_file):
    """ワードクラウドを生成"""
    try:
        subprocess.run([
            sys.executable,
            Path(__file__).parent / 'generate_wordcloud.py',
            input_file
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f'ワードクラウドの生成中にエラーが発生しました: {e}')
        sys.exit(1)

def show_usage():
    """使用方法を表示"""
    print('使用方法:')
    print('  1. 初回セットアップ:')
    print('     python run.py --setup')
    print()
    print('  2. ワードクラウド生成:')
    print('     python run.py [CSVファイルパス]')
    print()
    print('  サンプルデータを使用する場合:')
    print('     python run.py samples/customer_survey.csv')
    print()
    print('  出力ファイルは output/ ディレクトリに保存されます')

def main():
    if len(sys.argv) < 2:
        show_usage()
        sys.exit(1)

    if sys.argv[1] == '--setup':
        setup_packages()
        install_packages()
        print('\nセットアップが完了しました')
        print('ワードクラウドを生成するには:')
        print('python run.py [CSVファイルパス]')
    else:
        input_file = sys.argv[1]
        if not Path(input_file).exists():
            print(f'エラー: ファイル {input_file} が見つかりません')
            sys.exit(1)
        generate_wordcloud(input_file)

if __name__ == '__main__':
    main() 