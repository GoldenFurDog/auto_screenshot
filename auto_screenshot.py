# auto screenshot
# v1.0.0
# by goldenfurdog

from PIL import ImageGrab
from time import sleep
from email.mime.text import MIMEText

####################

def sendemail(From,SMTP,Pswd,To,msg):
    import smtplib
    print("确认邮箱为" + From + "(" + Pswd + SMTP + ")" + "--->" + To)
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
    import datetime
    checkedtime = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S")
    return checkedtime

####################

def auto_screenshot():
    From = input("输入发送邮箱：\n")
    SMTP = input("请输入SMTP服务器地址(如smtp.qq.com) ：\n")
    Pswd = input("请输入发件人密码：\n")
    To = input("请输入接收邮箱：\n")
    while True:
        checkedtime = checktime()
        im_name = "scrshot_%s"%(checkedtime)
        im = ImageGrab.grab()
        try:
            im.save("%s.jpg"%(im_name))
            msg = MIMEText("截图服务正常运转中..",'plain','utf-8')
            sendemail(From,SMTP,Pswd,To,msg)
        except:
            msg = MIMEText("截图服务意外终止！将在15分钟后重试。",'plain','utf-8')
        sleep(900)

####################

if __name__ == "__main__":
    auto_screenshot()
