'''
Author: your name
Date: 2021-08-20 10:57:48
LastEditTime: 2021-08-20 11:41:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /zero-space/auto_update.py
'''
import os
import datetime

now=datetime.datetime.now()

cmd=[
    "hexo g",
    "git add .",
    "git commit -m 'update {time}'".format(time=str(now)),
    "git push"
]

for c in cmd :
    status = os.system(c)
    if status==0:
        print("sucess!")
    else:
        print("Run Error!")
        break
