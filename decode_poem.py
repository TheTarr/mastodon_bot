# 解码接龙诗文本。目前需要新建一个poem.txt，把服务器存好的诗贴下来手动发送
from my_encode import *
# decode_poem('poem.txt')

import os
path = 'letter'
for root, dirs, files in os.walk(path):
    for file in files:
        decode_poem('letter/'+str(file))