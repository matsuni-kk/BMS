import sys
from pathlib import Path
import pandas as pd
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def ensure_output_dir():
    """出力ディレクトリの存在を確認し、なければ作成"""
    output_dir = Path(__file__).parent / 'output'
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    return output_dir

def read_csv(file_path):
    """CSVファイルを読み込む"""
    try:
        return pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        # UTF-8で失敗した場合はShift-JISで試行
        return pd.read_csv(file_path, encoding='shift-jis')

def tokenize_text(text):
    """テキストを形態素解析して名詞のみを抽出"""
    t = Tokenizer()
    tokens = t.tokenize(str(text))
    return ' '.join([token.surface for token in tokens 
                    if token.part_of_speech.split(',')[0] in ['名詞'] 
                    and token.part_of_speech.split(',')[1] not in ['数']])

def create_wordcloud(text, output_path, width=800, height=600):
    """ワードクラウドを生成して保存"""
    wordcloud = WordCloud(
        font_path='C:/Windows/Fonts/msgothic.ttc',
        width=width,
        height=height,
        background_color='white',
        regexp=r"[\w']+",
        prefer_horizontal=1.0,  # 完全に横書きに設定
        min_font_size=20,      # 最小フォントサイズを設定
        max_font_size=100      # 最大フォントサイズを設定
    ).generate(text)

    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()

def main():
    if len(sys.argv) < 2:
        print('使用方法: python generate_wordcloud.py [CSVファイルパス]')
        sys.exit(1)

    input_file = sys.argv[1]
    print(f'ファイルを読み込んでいます: {input_file}')

    # 出力ディレクトリの確認
    output_dir = ensure_output_dir()

    # CSVファイルを読み込む
    df = read_csv(input_file)
    
    # 全ての列のテキストを結合
    text = ' '.join(df.astype(str).values.flatten())
    
    # テキストの前処理
    processed_text = tokenize_text(text)
    
    # 出力ファイル名を設定（必ずoutputディレクトリ内）
    output_file = output_dir / f'{Path(input_file).stem}_wordcloud.png'
    
    # ワードクラウド生成
    create_wordcloud(processed_text, str(output_file))
    print(f'ワードクラウドを生成しました: {output_file}')

if __name__ == '__main__':
    main() 