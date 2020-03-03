# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:15:20 2020

@author: palazzol
"""

f = open('h1_019_raw.bin','rb')
f2 = open('h1_019.bin','wb')
for i in range(0,0x1000,2):
    f.read(1)
    b=f.read(1)
    f2.write(b)
f.close()
f2.close()

