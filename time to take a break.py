# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:58:22 2018

@author:Xia
"""
import time
import webbrowser
count_break=0
num_breaks=3
print('now it\'s time to take a break' +time.ctime())
while (count_break<num_breaks):
    time.sleep(60*30)
    webbrowser.open('https://www.youtube.com/watch?v=CaPRFm3EZWY&index=4&list=WL&t=167s')
    count_break+=1
