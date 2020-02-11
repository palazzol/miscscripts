# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:03:01 2019

@author: palazzol
"""

from PIL import Image

def doit(prefix):
	img = Image.new('RGB', (8, 2048), color = 'black')
	pixels = img.load()
	fin = open(prefix+'.bin','rb')
	orig = fin.read(2048)
	fin.close()
	i = 0
	for c in orig:
		for bit in range(0,8):
			if (c>>bit)&0x01 == 1:
				pixels[7-bit,i] = (0, 255, 0)
		i+=1
	img.save(prefix+'.png')

doit('2513u')
doit('2513l')