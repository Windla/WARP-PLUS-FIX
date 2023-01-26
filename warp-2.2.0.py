# coding = uft-8
import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import eventlet

os.system("title WARP-PLUS-CLOUDFLARE By ALIILAPRO + Windla(fix)") # 原作者 ALIILAPRO


#
# -----------设置部分开始-----------
#
# WRIP+ ID [偏好设置-常规-设备ID]
referrer = ""
#
# 是否在Actions中运行 | 0：否(不间断运行) 1：是(运行6h自动停止)
actions = 0
# 兼容性设置 猴子补丁 | False: 否(超时跳过功能失效) True: 是(与Termux有兼容性问题) | 已知bug
monkey_socket = True
#
# 超时时间，默认为10s | 对应monkey_socket = True
overtime = 10
#
# 快速启动 0：否 1：是 | 开启后刚开始速度会不准
faststart = 0
#
# -----------设置部分结束-----------
#

eventlet.monkey_patch(socket=monkey_socket,
					 os=False,
                     select=False,
                     thread=False,
                     time=False)

t0 = time.time()      # 入点
g = 0                 # 成功
b = 0                 # 失败
t1 = 0                # 计时

print("WARP-PLUS-CLOUDFLARE By ALIILAPRO + Wind_la(fix)")
print("注意: 需要使用eventlet, 请在终端内输入(如已安装则可忽略)")
print("pip install eventlet")
if referrer == str(""):
	print("你还未设置你的设备ID!\n请检查你的py文件内设置\n将在20s后自动退出!")
	time.sleep(20)
	exit()
elif actions == 0 and faststart == 0:
	print("将在20s后继续运行")
	time.sleep(20)

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
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
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)

while True:
	# 针对Workflows 6h的限制 保留100s冗余
	if actions == 1 and t1 >= 21500:
		sys.exit()
	result = 0 # 清空状态码
	with eventlet.Timeout(overtime,False):
		result = run()
	
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		
		t = time.time() - t0  # 已用时间
		t2 = t - t1           # 距离上一次触发的时间
		t1 = t                # 更新已用时间
		print("--------------------------------------------------------")
		print(f"[+]已用时间:  {int(t1)} s")
		print(f"[+]当前速度:  {int(t2)} s/GB")
		print(f"[+]平均速度:  {int(g/t1*21600)} GB/6h")
		print(f"[+]运行结果:  {g} Good {b} Bad")
		print("--------------------------------------------------------")
		time.sleep(10)
		print("Ready")
		time.sleep(10)
		print("Running")
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		
		t = time.time() - t0  # 已用时间
		t2 = t - t1           # 距离上一次触发的时间
		t1 = t                # 更新已用时间
		print("--------------------------------------------------------")
		print(f"[+]已用时间:  {int(t1)} s")
		print(f"[-]当前速度:  null s/GB")
		print(f"[+]平均速度:  {int(g/t1*21600)} GB/6h")
		print(f"[-]运行结果:  {g} Good {b} Bad")
		print("--------------------------------------------------------")
		print("Ready")
		time.sleep(1)
		print("Running")
