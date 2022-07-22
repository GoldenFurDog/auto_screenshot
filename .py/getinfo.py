#!/usr/bin/python
# -*- coding: utf-8 -*-

def getinfo(userkey):
    import json
    import sys
    try:
        file = open("./auth.json")
        infos = json.load(file)
    except:
        print("auth.json文件访问异常")
        sys.exit
    try:
        info = infos.get(userkey)
        From = info.get('From')
        SMTP = info.get('SMTP')
        Pswd = info.get('Pswd')
        To = info.get('To')
    except:
        print("缺失元素或其他，请严格按照example添加数据")
        sys.exit
    return(From,SMTP,Pswd,To)

if __name__ == '__main__':
    getinfo('example')
