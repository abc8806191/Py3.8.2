# coding: utf-8 -*-
import os ,time
#####################
vpstime = time.time()
#####################
print("歡迎使用一鍵快速更新Py3.8.2系統")
time.sleep(1)
os.system("apt update")
print("系統已更新完畢")
time.sleep(2)
os.system("apt install tar")
print("正在安裝解壓套件")
time.sleep(2)
os.system("apt install build-essential zlib1g-dev libncursee5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libsqlite3-dev wget libbz2-dev")
print("正在安裝相關的更新套件")
time.sleep(1)
os.system("wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz)
print("正在下載Py3.8.2")
time.sleep(2)
os.system("tar -xf Python-3.8.2.tgz")
print("正在解壓縮....")
time.sleep(1)
os.system("cd Python-3.8.2")
os.system("./configure --enable-optimizations")
print("我也不知道這是三小 就這樣了")
time.sleep(2)
os.system("make")
os.system("make install")
print("好像是Make安裝吧")
time.sleep(1)
os.system("make -j 8")
print("自己看啦")
time.sleep(2)
os.system("sudo make altinstall")
print("我已經更新好了啦 ProMa")
print("VPS環境安裝完成 花費時間:{time}".format(time=(time.time() - vpstime)))
print("提醒您 安裝完環境請重啟VPS以正常運作")