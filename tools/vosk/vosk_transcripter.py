import sounddevice as sd
import queue
import sys
import json
from datetime import datetime, timedelta
from vosk import Model, KaldiRecognizer
import os
import numpy as np

def get_script_dir():
    """
    スクリプトファイルのディレクトリを動的に取得する関数
    ※PyInstaller等で実行している場合は sys.executable を利用
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

# スクリプトが配置されているディレクトリを取得
SCRIPT_DIR = get_script_dir()

# モデルディレクトリの指定
# 必要なモデル群はこのスクリプトと同じディレクトリ（例：D:\vosk）に配置してください
MODEL_PATH = SCRIPT_DIR

# 出力ルートディレクトリの指定 (スクリプトの配置ディレクトリを基準)
VOSK_DIR = SCRIPT_DIR
current_date = datetime.now().strftime("%Y%m%d")
OUTPUT_DIR = os.path.join(VOSK_DIR, "output", current_date)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# モデルのロード
try:
    model = Model(MODEL_PATH)
except Exception as e:
    print(f"モデルが見つかりません: {e}")
    print("小型モデルを https://alphacephei.com/vosk/models からダウンロードし、解凍してこのフォルダに配置してください。")
    sys.exit(1)

# 音声データをキューで管理
q = queue.Queue()

def find_loopback_device():
    """WASAPIループバックデバイスを探す"""
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0 and ('Stereo Mix' in device['name'] or 'What U Hear' in device['name']):
            return i
    return None

def find_microphone_device():
    """デフォルトのマイクデバイスを探す"""
    devices = sd.query_devices()
    default_input = sd.default.device[0]
    if default_input is not None:
        return default_input
    
    # デフォルトデバイスが設定されていない場合は最初のマイクを使用
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0 and 'マイク' in device['name']:
            return i
    return None

def audio_callback(indata, frames, time, status):
    """音声データをキューに追加"""
    if status:
        print(f"ステータス: {status}", file=sys.stderr)
    # ステレオの場合はモノラルにダウンミックス
    if len(indata.shape) > 1 and indata.shape[1] > 1:
        mono_data = np.mean(indata, axis=1)
    else:
        mono_data = indata.flatten()
    
    # 16ビット整数に変換
    mono_data = (mono_data * 32767).astype(np.int16)
    q.put(bytes(mono_data))

def get_next_file_number():
    """次のファイル番号を取得"""
    files = os.listdir(OUTPUT_DIR)
    numbers = [int(f.split('_')[0]) for f in files if f.endswith('.txt')]
    return max(numbers) + 1 if numbers else 1

def list_all_devices():
    """全てのオーディオデバイスを表示"""
    print("\n利用可能なオーディオデバイス:")
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:  # 入力デバイスのみ表示
            print(f"{i}: {device['name']} (入力チャンネル: {device['max_input_channels']})")
    return devices

def main():
    # デバイス情報を表示
    devices = list_all_devices()
    
    # マイクとループバックデバイスを探す
    mic_device = find_microphone_device()
    loopback_device = find_loopback_device()
    
    print("\n使用するデバイス:")
    if mic_device is not None:
        mic_info = sd.query_devices(mic_device)
        print(f"マイク: {mic_info['name']}")
    if loopback_device is not None:
        loopback_info = sd.query_devices(loopback_device)
        print(f"システム音声: {loopback_info['name']}")
    else:
        print("※システム音声の録音には'ステレオミキサー'を有効にしてください")
        print("※設定 > システム > サウンド > 入力 で'ステレオミキサー'を有効にしてください")

    # 起動時刻を記録
    start_time = datetime.now()
    next_file_time = start_time + timedelta(hours=1)
    
    # 現在のファイル番号を取得
    current_file_number = get_next_file_number()
    
    # 出力ファイル名を生成
    output_file = os.path.join(OUTPUT_DIR, f"{current_file_number}_transcription.txt")
    
    recognizer = KaldiRecognizer(model, 16000)  # 16kHzで認識
    print(f"\nマイクとPC音声の認識を開始します。Ctrl+Cで終了します。")
    print(f"文字起こし結果は {output_file} に保存されます。")
    print(f"1時間ごとに新しいファイルが作成されます。")

    current_file = open(output_file, "w", encoding="utf-8")
    
    try:
        # マイク用のストリーム
        mic_stream = sd.InputStream(device=mic_device, samplerate=16000,
                                    channels=1, callback=audio_callback)
        mic_stream.start()

        # システム音声用のストリーム（利用可能な場合）
        if loopback_device is not None:
            sys_stream = sd.InputStream(device=loopback_device, samplerate=16000,
                                        channels=1, callback=audio_callback)
            sys_stream.start()

        print("\n録音開始...")
        
        while True:
            # 1時間経過したかチェック
            if datetime.now() >= next_file_time:
                current_file.close()
                current_file_number += 1
                output_file = os.path.join(OUTPUT_DIR, f"{current_file_number}_transcription.txt")
                current_file = open(output_file, "w", encoding="utf-8")
                next_file_time = datetime.now() + timedelta(hours=1)
                print(f"\n新しいファイルを作成しました: {output_file}")

            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print(f"認識結果: {result}")
                # 認識結果をJSONとしてパースし、テキストのみを取り出して保存
                json_result = json.loads(result)
                if json_result["text"]:  # テキストが空でない場合のみ保存
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    current_file.write(f"[{timestamp}] {json_result['text']}\n")
                    current_file.flush()  # バッファをフラッシュして即座に書き込み
            else:
                partial_result = recognizer.PartialResult()
                print(f"途中結果: {partial_result}")
    finally:
        if 'mic_stream' in locals():
            mic_stream.stop()
        if 'sys_stream' in locals() and loopback_device is not None:
            sys_stream.stop()
        current_file.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nプログラムを終了します。")
        sys.exit(0)
    except Exception as e:
        print(f"エラー: {e}")