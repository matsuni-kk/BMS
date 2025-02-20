# YouTube to MP3 Converter

## 概要
YouTubeの動画からMP3形式で音声を抽出するツールです。高品質な音声抽出（192kbps）に対応しています。

## 機能
- YouTubeの動画URLから音声を抽出
- MP3形式（192kbps）での保存
- 動画タイトルを自動的にファイル名として使用
- 出力フォルダへの自動保存

## 必要要件
- Python 3.x
- yt-dlp
- ffmpeg（音声変換に必要）

## インストール方法
```bash
# yt-dlpのインストール
pip install yt-dlp

# ffmpegのインストール（Windowsの場合）
# 1. https://www.ffmpeg.org/download.html からffmpegをダウンロード
# 2. 解凍したファイルをC:\ffmpegに配置
# 3. システム環境変数のPATHにC:\ffmpeg\binを追加
```

## 使用方法
### 基本的な使用方法
```bash
cd tools/youtube4mp3
python youtube_audio_extractor.py <YouTube URL>
```

### カスタムファイル名の指定
```bash
cd tools/youtube4mp3
python youtube_audio_extractor.py <YouTube URL> --filename "カスタム名.%(ext)s"
```

## 出力
- 抽出された音声ファイルは、ツールと同じディレクトリの`output`フォルダに保存されます
- デフォルトのファイル名は動画のタイトルに基づきます
- ファイル形式は.mp3、ビットレートは192kbpsです

## 注意事項
- このツールは個人使用目的のみを想定しています
- 著作権を遵守し、適切な権利を持つコンテンツのみを処理してください
- YouTubeの利用規約に従って使用してください
- ネットワーク環境によってはダウンロード速度が異なる場合があります
