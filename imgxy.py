# -*- coding: utf-8 -*-
import os
import sys

from PIL import Image

root = os.getcwd()
a = '''
[Rename Config]
FoundExist=0
FoundExistAndExchange=0

[Rename Programme]
'''
for rt, dirs, files in os.walk(root):
    op = open('gm.txt', 'wb+')

    for f in files:
        try:
            img = Image.open(f)
            newname = str(img.size[0])+'x'+str(img.size[1])+'-'+f

            cwd = os.path.join(rt, f)+'='+newname
            print(newname, cwd)
            op.write(cwd+'\n')
        except:
            print(root)
    op.close()
