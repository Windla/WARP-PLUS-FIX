# coding = uft-8
import json
import datetime
import random
import string
import time
import os
import sys

import requests


# ID [偏好设置-常规-设备ID]
referrer = ""

# 是否在Actions中运行 | 0：否(不间断运行) 1：是(运行6h自动停止)
actions = 0

# 快速启动 0：否 1：是 | 开启后刚开始速度会不准
fast_start = 1

# 超时时间设定
timeout = 10


# Author: ALIILAPRO
def gen_string(string_length):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(string_length))
    except Exception as error:
        print(error)


# Author: ALIILAPRO
def digit_string(string_length):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for _ in range(string_length)))
    except Exception as error:
        print(error)


# Author: ALIILAPRO
def run_requests():
    try:
        url = f'https://api.cloudflareclient.com/v0a{digit_string(3)}/reg'
        install_id = gen_string(22)
        body = {"key": "{}=".format(gen_string(43)),
                "install_id": install_id,
                "fcm_token": "{}=".format(gen_string(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'Host': 'api.cloudflareclient.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.1'}
        response = requests.post(url=url, headers=headers, data=data, timeout=timeout)
        status_code = response.status_code
        return status_code
    except requests.exceptions.RequestException:
        print("[warn]连接超时")

    except Exception as error:
        print(error)


def main():
    t0 = time.time()  # 入点
    g = 0  # 成功
    b = 0  # 失败
    t1 = 0  # 计时

    os.system("title WARP-PLUS-FIX By ALIILAPRO + Windla(fix)")
    print("WARP-PLUS-FIX By ALIILAPRO + Windla(fix)")
    if referrer == "":
        print("你还未设置你的设备ID!\n请检查你的py文件内设置\n将在20s后自动退出!")
        time.sleep(20)
        exit()
    elif actions == 0 and fast_start == 0:
        print("将在20s后继续运行")
        time.sleep(20)

    while True:
        # 针对Workflows 6h的限制 保留100s冗余
        if actions == 1 and t1 >= 21500:
            sys.exit()

        result = run_requests()

        if result == 200:
            g = g + 1
            os.system('cls' if os.name == 'nt' else 'clear')

            t = time.time() - t0  # 已用时间
            t2 = t - t1  # 距离上一次触发的时间
            t1 = t  # 更新已用时间
            print("--------------------------------------------------------")
            print(f"[info]已用时间:  {int(t1)} s")
            print(f"[info]当前速度:  {int(t2)} s/GB")
            print(f"[info]平均速度:  {int(g / t1 * 21600)} GB/6h")
            print(f"[info]运行结果:  {g} Good {b} Bad")
            print("--------------------------------------------------------")
            time.sleep(10)
            print("[info]Ready")
            time.sleep(10)
            print("[info]Running")
        else:
            b = b + 1
            os.system('cls' if os.name == 'nt' else 'clear')

            t = time.time() - t0  # 已用时间
            t1 = t  # 更新已用时间
            print("--------------------------------------------------------")
            print(f"[info]已用时间:  {int(t1)} s")
            print(f"[info]当前速度:  0 s/GB")
            print(f"[info]平均速度:  {int(g / t1 * 21600)} GB/6h")
            print(f"[info]运行结果:  {g} Good {b} Bad")
            print("--------------------------------------------------------")
            print("[info]Ready")
            time.sleep(1)
            print("[info]Running")


if __name__ == "__main__":
    main()
