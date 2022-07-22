#!/usr/bin/python
# -*- coding: utf-8 -*-

def checktime():
    from datetime import datetime
    checkedtime = int(datetime.now().strftime("%M%S"))
    return checkedtime

if __name__ == '__main__':
    checktime()
