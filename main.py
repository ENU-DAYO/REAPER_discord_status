import time
import psutil
import pypresence

client_id = "1279434241607733339"  # ここにあなたのApplication IDを入力してください
rpc = pypresence.Presence(client_id)
rpc.connect()

# 開始時間を記録
start_time = time.time()

# 画像やテキストの設定
large_image = "reaper_logo"  # ここに大きな画像の名前（キー）を入力
large_text = "おお"  # ここに大きな画像に表示するテキストを入力

while True:
    data = None
    for proc in psutil.process_iter():
        # プロセスの名前を小文字にしてマッチング
        match proc.name().lower():
            case "reaper.exe":
                data = {
                    "state": "EVALUATION LICENSE",
                    #"details": "EVALUATION LICENSE",
                    "start": start_time,  # 経過時間を表示
                    "large_image": large_image,
                    "large_text": large_text,
                    # small_imageとsmall_textを削除または省略
                }
                break

    if data:
        rpc.update(**data)
    else:
        rpc.clear()

    time.sleep(15)  # リッチプレゼンスの更新は15秒に一度に制限されています
