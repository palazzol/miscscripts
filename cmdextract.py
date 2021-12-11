# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:00:58 2021

@author: frank

Quick and dirty - extract binary files from Model III trsdos 1.3 CMD files
Not fully implemented, but works for contiguous data files

"""
import sys

def cmdextract(fname):
    contents = bytearray()
    with open(fname,'rb') as f:
        x = f.read(2)
        while not f is None:
            if x[0] == 0x02:
                f2 = open(fname.split('.')[0]+'.bin','wb')
                s = len(contents)
                f2.write(contents)
                f2.close()
                print(str(s)+' bytes extracted')
                return
            elif x[0] != 0x01:
                print(x[0],'error')
                sys.exit(-1)
            if x[1] == 0:
                num = 254
            else:
                num = x[1] - 2
            x = f.read(2)
            loc = x[1]*256+x[0]
            #print(hex(num)+' bytes at '+hex(loc))
            contents += f.read(num)
            if not f is None:
                x = f.read(2)

cmdextract('MPBASIC.CIM')
cmdextract('MPMONIT.CIM')