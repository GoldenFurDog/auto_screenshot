#!/usr/bin/python
# -*- coding: utf-8 -*-
# auto screenshot
# v1.2.0
# by goldenfurdog

from PIL import ImageGrab
from time import sleep
from email.mime.text import MIMEText
import os

####################

from sendemail import sendemail
from checktime import checktime
from tIme import tIme
from getinfo import getinfo

####################

def auto_screenshot():
    userkey = input("输入用户代号：\n")
    info = getinfo(userkey)
    From = info[0]
    SMTP = info[1]
    Pswd = info[2]
    To = info[3]
    print("确认邮箱为" + From + "(" + Pswd + "-" + SMTP + ")" + "--->" + To)
    path = "./screenshot"
    if not os.path.exists(path):
        os.mkdir(path)
    while True:
        checkedtime = checktime()
        while checkedtime != 0000 and checkedtime != 1500 and checkedtime != 3000 and checkedtime != 4500:
            checkedtime = checktime()
        nowtime = tIme()
        im_name = "./screenshot/screenshot_%s"%(nowtime)
        im = ImageGrab.grab()
        try:
            im.save("%s.jpg"%(im_name))
            msg = MIMEText("截图服务正常运转中..",'plain','utf-8')
            sendemail(From,SMTP,Pswd,To,msg)
        except:
            msg = MIMEText("截图服务意外终止！将在15分钟后重试。",'plain','utf-8')
            sendemail(From,SMTP,Pswd,To,msg)
        sleep(1)

####################

if __name__ == "__main__":
    auto_screenshot()
