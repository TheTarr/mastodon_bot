import sys
import io
import random
import os
from my_encode import *
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

# 读取文件夹中所有txt文件名
filePath = 'letter/'
files = os.listdir(filePath)
# 随机抽一个
flag = random.randint(0,len(files)-1)
decode_poem("letter/" + files[flag])