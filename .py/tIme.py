#!/usr/bin/python
# -*- coding: utf-8 -*-

def tIme():
    import datetime
    nowtime = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S")
    return nowtime

if __name__ == '__main__':
    tIme()
