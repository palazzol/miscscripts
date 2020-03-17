# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:56:52 2020

@author: palazzol
"""

from PIL import Image

infname = 'de-0025b_f2_3d-II.bin'
outfname = 'de-0025b_f2_3d-II.png'

f = open(infname,'rb')
img = Image.new("RGB",(16*8,4*8))

for i in range(0,32):
    c = f.read(1)
    data = int.from_bytes(c, byteorder='big')
    r1_bit = (data >> 0) & 0x01
    r2_bit = (data >> 1) & 0x01
    g1_bit = (data >> 2) & 0x01
    g2_bit = (data >> 3) & 0x01
    b1_bit = (data >> 4) & 0x01
    b2_bit = (data >> 5) & 0x01

    # this is probably not quite right, but I don't have the
    # knowledge to figure out the actual weights - ZV
    r = (0xc0 * r1_bit) + (0x3f * r2_bit)
    g = (0xc0 * g1_bit) + (0x3f * g2_bit)
    b = (0xc0 * b1_bit) + (0x3f * b2_bit)

    for x in range(0,8):
        for y in range(0,8):
            img.putpixel((x+i%16 * 8,y+i//16 * 8), (r,g,b))
            img.putpixel((x+i%16 * 8,y+16+i//16 * 8), (0xff,g,b))
img.save(outfname)

f.close()
