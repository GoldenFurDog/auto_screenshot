#!/usr/bin/python
# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
    sendemail()
