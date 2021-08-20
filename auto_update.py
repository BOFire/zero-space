'''
Author: your name
Date: 2021-08-20 10:57:48
LastEditTime: 2021-08-20 11:45:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /zero-space/auto_update.py
'''
import os
import datetime

now=datetime.datetime.now()

cmd=[
    # "hexo s",
    "hexo g",
    "git add .",
    "git commit -m 'update {time}'".format(time=str(now)),
    "git push"
]

for c in cmd :
    status = os.system(c)
    if status==0:
        print("sucess===>{m}".format(m=c))
    else:
        print("Run Error===>{m}".format(m=c))
        break
