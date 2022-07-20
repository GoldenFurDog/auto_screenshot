# auto screenshot
# v1.0.0
# by goldenfurdog

from PIL import ImageGrab
from time import sleep
from datetime import datetime
from email.mime.text import MIMEText

####################

def sendemail(From,SMTP,Pswd,To,msg):
    import smtplib
    server = smtplib.SMTP_SSL(SMTP,465)
    server.set_debuglevel(1)
    server.login(From,Pswd)
    try:
        server.sendmail(From,[To],msg.as_string())
        print("发送成功！")
    except:
        print("发送失败。")
    server.quit

####################

def checktime():
    checkedtime = int(datetime.now().strftime("%M%S"))
    return checkedtime

####################

def tIme():
    import datetime
    nowtime = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S")
    return nowtime

####################

def auto_screenshot():
    From = input("输入发送邮箱：\n")
    SMTP = input("请输入SMTP服务器地址(如smtp.qq.com) ：\n")
    Pswd = input("请输入发件人密码：\n")
    To = input("请输入接收邮箱：\n")
    print("确认邮箱为" + From + "(" + Pswd + "-" + SMTP + ")" + "--->" + To)
    while True:
        checkedtime = checktime()
        while checkedtime != 0000 and checkedtime != 1500 and checkedtime != 3000 and checkedtime != 4500:
            checkedtime = checktime()
        nowtime = tIme()
        im_name = "screenshot_%s"%(nowtime)
        im = ImageGrab.grab()
        try:
            im.save("%s.jpg"%(im_name))
            msg = MIMEText("截图服务正常运转中..",'plain','utf-8')
            sendemail(From,SMTP,Pswd,To,msg)
        except:
            msg = MIMEText("截图服务意外终止！将在15分钟后重试。",'plain','utf-8')
        sleep(1)

####################

if __name__ == "__main__":
    auto_screenshot()
