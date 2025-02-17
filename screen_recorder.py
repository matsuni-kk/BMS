#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FocuSeeのようなクリック部分への自動ズームおよび自動キャプション機能を備えた画面録画アプリです。
GUI上に録画開始ボタンと録画停止ボタンを配置し、録画対象領域（ROI）の選択と、録画中のクリックによるズーム・強調機能を実装しています。
各ディレクトリのai_agent_rule.mdのルールに従い、全文記載しております。
"""

import threading
import time
import cv2
import numpy as np
import mss
from pynput import mouse
import tkinter as tk

# グローバル変数
recording = False  # 録画中かどうか
last_click_pos = None  # 録画対象領域内での最後のクリック座標（相対座標）
last_click_time = 0    # クリックされた時刻
click_duration = 0.5   # クリックエフェクトの表示時間（秒）
selected_region = None # ユーザーが選択した録画対象領域（辞書型: left, top, width, height）


def on_click(x, y, button, pressed):
    """
    マウスのクリックイベントハンドラ。
    録画中で、クリック位置が選択された領域内であれば、相対座標と時刻を記録する。
    """
    global last_click_pos, last_click_time, selected_region, recording
    if pressed and recording and selected_region is not None:
        left = selected_region["left"]
        top = selected_region["top"]
        width = selected_region["width"]
        height = selected_region["height"]
        if left <= x <= left + width and top <= y <= top + height:
            # クリック位置を録画対象内の相対座標として記録
            last_click_pos = (x - left, y - top)
            last_click_time = time.time()


def start_mouse_listener():
    """
    マウスリスナーを開始する。
    """
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    return listener


def record_loop():
    """
    録画処理のループ。選択されたROI領域のみをキャプチャし、録画中にクリックがあればズーム・強調表示する。
    """
    global recording, selected_region, last_click_pos, last_click_time
    sct = mss.mss()
    monitor = selected_region  # 録画対象の領域
    output_filename = "output.avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 15.0
    video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (monitor["width"], monitor["height"]))

    while recording:
        frame_start = time.time()
        # 選択領域のスクリーンショットを取得
        screen_shot = sct.grab(monitor)
        frame = np.array(screen_shot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        current_time = time.time()
        if last_click_pos is not None and (current_time - last_click_time) <= click_duration:
            # クリック位置を中心にズームするエリアを計算（録画領域内の相対座標）
            zoom_factor = 2.0    # ズーム倍率（必要に応じて変更）
            zoom_size = 200      # ズームするエリアのサイズ（ピクセル単位）
            mouse_x, mouse_y = last_click_pos

            # クリック位置を中心とする矩形領域の計算（範囲外にならないよう調整）
            x1 = int(max(mouse_x - zoom_size // 2, 0))
            y1 = int(max(mouse_y - zoom_size // 2, 0))
            x2 = int(min(mouse_x + zoom_size // 2, monitor["width"]))
            y2 = int(min(mouse_y + zoom_size // 2, monitor["height"]))

            zoom_area = frame[y1:y2, x1:x2]
            # ズーム処理：矩形領域を録画領域全体のサイズへリサイズ
            zoomed_area = cv2.resize(zoom_area, (monitor["width"], monitor["height"]), interpolation=cv2.INTER_LINEAR)
            alpha = 0.3  # オーバーレイの透明度
            frame = cv2.addWeighted(zoomed_area, alpha, frame, 1 - alpha, 0)

            # キャプションの表示（クリック位置付近に "Click!" を表示）
            caption_text = "Click!"
            text_position = (mouse_x + 10, mouse_y - 10)
            cv2.putText(frame, caption_text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            # クリック位置を強調するために円を描画
            cv2.circle(frame, (mouse_x, mouse_y), 20, (0, 255, 0), 3)

        # フレームを書き込み
        video_writer.write(frame)

        # プレビュー表示
        cv2.imshow("Screen Recorder", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            recording = False
            break

        # FPS維持のための待機
        elapsed_time = time.time() - frame_start
        delay = max(1.0 / fps - elapsed_time, 0)
        time.sleep(delay)

    video_writer.release()
    sct.close()
    cv2.destroyAllWindows()


def start_recording():
    """
    録画開始処理。選択領域が未設定の場合、全画面からROIを選択してもらう。
    録画フラグをTrueにし、録画スレッドを開始する。
    """
    global recording, selected_region
    if recording:
        return  # すでに録画中の場合は何もしない

    # ROI選択（録画対象領域）
    if selected_region is None:
        sct = mss.mss()
        full_img = np.array(sct.grab(sct.monitors[0]))
        full_img = cv2.cvtColor(full_img, cv2.COLOR_BGRA2BGR)
        roi_rect = cv2.selectROI("ROI Selector", full_img, showCrosshair=True, fromCenter=False)
        cv2.destroyWindow("ROI Selector")
        # roi_rect は (x, y, w, h) のタプル
        selected_region = {
            "left": int(roi_rect[0]),
            "top": int(roi_rect[1]),
            "width": int(roi_rect[2]),
            "height": int(roi_rect[3])
        }
    recording = True
    # 録画スレッドを開始
    t = threading.Thread(target=record_loop)
    t.start()


def stop_recording():
    """
    録画停止処理。録画フラグをFalseにする。
    """
    global recording
    recording = False


def create_gui():
    """
    Tkinterを用いた簡易GUIを生成する。
    録画開始ボタンと録画停止ボタンを配置。
    """
    root = tk.Tk()
    root.title("画面録画アプリ")

    start_btn = tk.Button(root, text="録画開始", width=20, command=start_recording)
    start_btn.pack(pady=10)

    stop_btn = tk.Button(root, text="録画停止", width=20, command=stop_recording)
    stop_btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    # マウスリスナーを起動
    listener = start_mouse_listener()
    create_gui()
    listener.stop() 