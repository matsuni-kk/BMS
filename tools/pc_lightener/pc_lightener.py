#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
【PC 軽量化・不要ファイル削除・キャッシュクリア・ディスククリーンアップツール】
注意:
    このツールは以下の機能を実行し、PC のリソース解放やディスク容量の拡大、パフォーマンス向上を目的としています。
      1. 不要なプロセスの強制終了（メモリ使用量が一定以上のプロセス、ただし重要プロセス（chrome、cursor、vscode など）は除外）
      2. ユーザーTEMPファイルおよびシステムTEMPファイルの削除
      3. Windows更新ファイルの削除
      4. Prefetch ファイルの削除
      5. ごみ箱の内容削除
      6. ハイバネーションの無効化（hiberfil.sys の削除）【※休止状態を使用する場合は実行しないでください】
      7. Windowsエラーレポート (WER) の削除
      8. IE/Edge のキャッシュ（INetCache）の削除
      9. Windowsディスククリーンアップツール（cleanmgr）の実行 ※「cleanmgr /sageset:1」で事前に設定が必要
     10. コンポーネントストアのクリーンアップ ※chrome、cursor、vscode 系以外を対象
     11. ログファイルの削除 ※chrome、cursor、vscode 系以外を対象
     12. 不要なバックアップファイルの整理 ※chrome、cursor、vscode 系以外を対象（.bak、.old、.backup など）
     13. その他の一時ファイルやキャッシュの削除 ※chrome、cursor、vscode 系以外を対象

    ※各処理は管理者権限での実行が必須です。実行前に十分な検証およびバックアップを取得し、自己責任でご利用ください。
"""

import os
import shutil
import subprocess
import psutil

# 重要システムプロセスおよび除外対象プロセスのリスト
CRITICAL_PROCESSES = [
    "System Idle Process",
    "System",
    "wininit.exe",
    "winlogon.exe",
    "csrss.exe",
    "lsass.exe",
    "services.exe",
    "svchost.exe",
    "smss.exe",
    "dwm.exe",
    "explorer.exe",
    "chrome.exe",     # Google Chrome（除外対象）
    "code.exe",       # VSCode（除外対象）
    "cursor",         # Cursor 系（除外対象）
    "cursor.exe",
    "powershell.exe", # PowerShell（除外対象）
]

# プロセス強制終了の基準となるメモリ使用量の閾値（MB）
MEMORY_THRESHOLD_MB = 100.0

def is_critical_process(proc_name: str) -> bool:
    """
    プロセス名が重要なプロセスまたは除外対象に含まれているかをチェックします。
    """
    if proc_name is None:
        return True  # プロセス名が取得できない場合は、安全のため除外対象とする
    for crit in CRITICAL_PROCESSES:
        if proc_name.lower() == crit.lower():
            return True
    return False

def lighten_pc():
    """
    PC の軽量化のため、メモリ使用量が 100MB 以上の不要プロセス（重要プロセスは除外）を強制終了します。
    """
    print("---- PC 軽量化ツール（プロセス強制終了） を実行します ----")
    print("注意: このツールは不要プロセスの強制終了を実施します。\n")
    for proc in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            proc_info = proc.info
            proc_name = proc_info.get("name")
            if is_critical_process(proc_name):
                continue
            mem_info = proc_info.get("memory_info")
            mem_usage_mb = mem_info.rss / (1024 * 1024) if mem_info else 0
            if mem_usage_mb >= MEMORY_THRESHOLD_MB:
                print(f"プロセス終了: PID={proc_info.get('pid')}, 名称={proc_name}, メモリ使用量={mem_usage_mb:.2f} MB")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"プロセス終了に失敗しました: {e}")
    print("---- プロセス強制終了 完了 ----\n")

def clean_temp_files():
    """
    ユーザー TEMP フォルダ内のファイルおよびフォルダを削除します。
    """
    temp_dir = os.environ.get("TEMP")
    if not temp_dir:
        print("ユーザー TEMP ディレクトリが見つかりませんでした。")
        return
    print(f"---- ユーザー TEMP ファイル削除開始: {temp_dir} ----")
    for item in os.listdir(temp_dir):
        path = os.path.join(temp_dir, item)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
                print(f"削除: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"ディレクトリ削除: {path}")
        except Exception as e:
            print(f"削除できませんでした: {path}, エラー: {e}")
    print("---- ユーザー TEMP 削除完了 ----\n")

def clean_system_temp_files():
    """
    システム TEMP フォルダ（%WINDIR%/Temp）内のファイルおよびフォルダを削除します。
    """
    windir = os.environ.get("WINDIR")
    if not windir:
        print("WINDIR が見つかりませんでした。")
        return
    system_temp = os.path.join(windir, "Temp")
    if not os.path.exists(system_temp):
        print(f"システム TEMP ディレクトリが存在しません: {system_temp}")
        return
    print(f"---- システム TEMP ファイル削除開始: {system_temp} ----")
    for item in os.listdir(system_temp):
        path = os.path.join(system_temp, item)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
                print(f"削除: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"ディレクトリ削除: {path}")
        except Exception as e:
            print(f"削除できませんでした: {path}, エラー: {e}")
    print("---- システム TEMP 削除完了 ----\n")

def clean_windows_update_files():
    """
    Windows 更新で使用済みの更新ファイルを削除します。（通常 "C:\Windows\SoftwareDistribution\Download" フォルダ）
    """
    update_dir = os.path.join("C:\\", "Windows", "SoftwareDistribution", "Download")
    if not os.path.exists(update_dir):
        print(f"Windows 更新ファイルディレクトリが存在しません: {update_dir}")
        return
    print(f"---- Windows 更新ファイル削除開始: {update_dir} ----")
    for item in os.listdir(update_dir):
        path = os.path.join(update_dir, item)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
                print(f"削除: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"ディレクトリ削除: {path}")
        except Exception as e:
            print(f"削除できませんでした: {path}, エラー: {e}")
    print("---- Windows 更新ファイル削除完了 ----\n")

def clean_prefetch_files():
    """
    Prefetch フォルダ内のファイルおよびフォルダを削除します。（通常 "C:\Windows\Prefetch"）
    """
    windir = os.environ.get("WINDIR", "C:\\Windows")
    prefetch_dir = os.path.join(windir, "Prefetch")
    if not os.path.exists(prefetch_dir):
        print(f"Prefetch ディレクトリが存在しません: {prefetch_dir}")
        return
    print(f"---- Prefetch ファイル削除開始: {prefetch_dir} ----")
    for item in os.listdir(prefetch_dir):
        path = os.path.join(prefetch_dir, item)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
                print(f"削除: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"ディレクトリ削除: {path}")
        except Exception as e:
            print(f"削除できませんでした: {path}, エラー: {e}")
    print("---- Prefetch 削除完了 ----\n")

def clean_recycle_bin():
    """
    Windows のごみ箱の内容を削除します。
    ※システムドライブの $Recycle.bin フォルダを削除する方式を使用しています。
    """
    print("---- ごみ箱内容削除開始 ----")
    try:
        subprocess.run("rd /s /q C:\\$Recycle.bin", shell=True)
        print("---- ごみ箱内容削除完了 ----\n")
    except Exception as e:
        print(f"ごみ箱削除に失敗しました: {e}")

def disable_hibernation():
    """
    ハイバネーションを無効化して hiberfil.sys を削除します。
    ※休止状態を使用する場合は、この処理を実行しないでください。
    """
    print("---- ハイバネーション無効化開始 ----")
    try:
        subprocess.run(["powercfg", "-h", "off"], check=True)
        print("---- ハイバネーション無効化完了 ----\n")
    except subprocess.CalledProcessError as e:
        print(f"ハイバネーション無効化に失敗しました: {e}")

def clean_error_reports():
    """
    Windows エラーレポート（WER）のフォルダ内容を削除します。
    """
    local_appdata = os.environ.get("LOCALAPPDATA")
    if not local_appdata:
        print("LOCALAPPDATA が見つかりませんでした。")
        return
    wer_dir = os.path.join(local_appdata, "Microsoft", "Windows", "WER")
    if not os.path.exists(wer_dir):
        print(f"WER ディレクトリが存在しません: {wer_dir}")
        return
    print(f"---- Windows エラーレポート削除開始: {wer_dir} ----")
    for item in os.listdir(wer_dir):
        path = os.path.join(wer_dir, item)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
                print(f"削除: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"ディレクトリ削除: {path}")
        except Exception as e:
            print(f"削除できませんでした: {path}, エラー: {e}")
    print("---- Windows エラーレポート削除完了 ----\n")

def clean_inet_cache():
    """
    IE/Edge のキャッシュ（INetCache）の内容を削除します。
    """
    local_appdata = os.environ.get("LOCALAPPDATA")
    if not local_appdata:
        print("LOCALAPPDATA が見つかりませんでした。")
        return
    inetcache_dir = os.path.join(local_appdata, "Microsoft", "Windows", "INetCache")
    if not os.path.exists(inetcache_dir):
        print(f"INetCache ディレクトリが見つかりません: {inetcache_dir}")
        return
    print(f"---- INetCache 削除開始: {inetcache_dir} ----")
    for root, dirs, files in os.walk(inetcache_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"削除: {file_path}")
            except Exception as e:
                print(f"削除できませんでした: {file_path}, エラー: {e}")
        for d in dirs:
            dir_path = os.path.join(root, d)
            try:
                shutil.rmtree(dir_path)
                print(f"ディレクトリ削除: {dir_path}")
            except Exception as e:
                print(f"削除できませんでした: {dir_path}, エラー: {e}")
    print("---- INetCache 削除完了 ----\n")

def run_disk_cleanup():
    """
    Windows 標準のディスククリーンアップツール（cleanmgr）を実行します。
    ※本機能を使用するには、事前に "cleanmgr /sageset:1" による設定が必要です。
    """
    print("---- ディスククリーンアップ開始 ----")
    try:
        subprocess.run(["cleanmgr", "/sagerun:1"], check=True)
        print("---- ディスククリーンアップ完了 ----\n")
    except subprocess.CalledProcessError as e:
        print(f"ディスククリーンアップに失敗しました: {e}")

# --- 追加機能 ---

def clean_component_store():
    """
    コンポーネントストアのクリーンアップを実行します。
    ※ chrome、cursor、vscode 系以外を対象としています。
    """
    print("---- コンポーネントストアのクリーンアップ開始 ----")
    try:
        subprocess.run(["dism", "/Online", "/Cleanup-Image", "/StartComponentCleanup"], check=True)
        print("---- コンポーネントストアのクリーンアップ完了 ----\n")
    except subprocess.CalledProcessError as e:
        print(f"コンポーネントストアのクリーンアップ失敗: {e}")

def clean_log_files():
    """
    ログファイルの削除を実行します。
    ※ chrome、cursor、vscode 系を含むパスは対象外とします。
    対象ディレクトリ: %WINDIR%\Logs, %WINDIR%\System32\LogFiles
    """
    windir = os.environ.get("WINDIR", "C:\\Windows")
    log_dirs = [os.path.join(windir, "Logs"), os.path.join(windir, "System32", "LogFiles")]
    excluded_keywords = ["chrome", "cursor", "vscode"]
    print("---- ログファイルの削除開始 ----")
    for log_dir in log_dirs:
        if not os.path.exists(log_dir):
            continue
        for root, dirs, files in os.walk(log_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if any(keyword in file_path.lower() for keyword in excluded_keywords):
                    continue
                if file.lower().endswith(".log"):
                    try:
                        os.remove(file_path)
                        print(f"削除: {file_path}")
                    except Exception as e:
                        print(f"ログファイル削除失敗: {file_path}, エラー: {e}")
    print("---- ログファイルの削除完了 ----\n")

def clean_backup_files():
    """
    不要なバックアップファイル（.bak, .old, .backup）の整理を実行します。
    ※ chrome、cursor、vscode 系を含むパスは対象外とします。
    """
    user_profile = os.environ.get("USERPROFILE")
    if not user_profile:
        print("USERPROFILE が見つかりません。")
        return
    excluded_keywords = ["chrome", "cursor", "vscode"]
    backup_extensions = [".bak", ".old", ".backup"]
    print("---- 不要なバックアップファイルの整理開始 ----")
    for root, dirs, files in os.walk(user_profile):
        for file in files:
            file_path = os.path.join(root, file)
            if any(keyword in file_path.lower() for keyword in excluded_keywords):
                continue
            if any(file.lower().endswith(ext) for ext in backup_extensions):
                try:
                    os.remove(file_path)
                    print(f"削除: {file_path}")
                except Exception as e:
                    print(f"バックアップファイル削除失敗: {file_path}, エラー: {e}")
    print("---- 不要なバックアップファイルの整理完了 ----\n")

def clean_misc_cache_files():
    """
    その他の一時ファイルやキャッシュの削除を実行します。
    ※ chrome、cursor、vscode 系を含むパスは対象外とします。
    対象は %LOCALAPPDATA% 内の "Cache" を名前に含むディレクトリです。
    """
    local_appdata = os.environ.get("LOCALAPPDATA")
    if not local_appdata:
        print("LOCALAPPDATA が見つかりません。")
        return
    excluded_keywords = ["chrome", "cursor", "vscode"]
    print("---- その他の一時ファイルやキャッシュの削除開始 ----")
    for root, dirs, files in os.walk(local_appdata):
        for d in dirs:
            if "cache" in d.lower():
                dir_path = os.path.join(root, d)
                if any(keyword in dir_path.lower() for keyword in excluded_keywords):
                    continue
                try:
                    shutil.rmtree(dir_path)
                    print(f"キャッシュディレクトリ削除: {dir_path}")
                except Exception as e:
                    print(f"キャッシュディレクトリ削除失敗: {dir_path}, エラー: {e}")
    print("---- その他の一時ファイルやキャッシュの削除完了 ----\n")

if __name__ == "__main__":
    lighten_pc()
    clean_temp_files()
    clean_system_temp_files()
    clean_windows_update_files()
    clean_prefetch_files()
    clean_recycle_bin()
    disable_hibernation()      # ※休止状態を使用する場合はこの呼び出しをコメントアウトしてください
    clean_error_reports()
    clean_inet_cache()
    run_disk_cleanup()
    clean_component_store()
    clean_log_files()
    clean_backup_files()
    clean_misc_cache_files() 