#!/usr/bin/python3.5

import sys
import os.path as osp
from array import array
from PIL import Image


def coder(in_img_path, alpha=255):
    out_img_path = osp.abspath(in_img_path) + '.bin'
    
    arr = array('I')

    im = Image.open(in_img_path)
    w, h = im.size
    print(w, h)

    #for i in im.size:
    #iarr.append(10000000)
    #arr.append(10000000)
    arr.append(w)
    arr.append(h)

    for clr in im.convert("RGB").getdata():
        b = clr[0]
        b |= clr[1] << 8
        b |= clr[2] << 16
        #b |= alpha << 24
        arr.append(b)

    im.close()
    fout = open(out_img_path, 'wb')
    arr.tofile(fout)
    fout.close()


def decoder(in_img_path):
    out_img_path = osp.abspath(in_img_path) + '.png'

    fin = open(in_img_path, 'rb')

    arr = array('I')
    arr.fromfile(fin, 2)
    w, h = arr

    arr = array('I')
    arr.fromfile(fin, w * h)

    fin.close()

    im = Image.frombuffer('RGBA', (w, h), arr, 'raw', 'RGBA', 0, 1)
    im.save(out_img_path, 'PNG')


def main():
    if len(sys.argv) < 2:
        print('Select bin file or image (for example "{0} example.png")'.format(osp.basename(sys.argv[0])))
        sys.exit(1)
    if sys.argv[1].endswith('.bin'):
        decoder(sys.argv[1])
    else:
        coder(sys.argv[1])

if __name__ == '__main__':
    main()
