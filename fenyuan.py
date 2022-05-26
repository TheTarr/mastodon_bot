import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

mylist = ['格兰芬多','赫奇帕奇','拉文克劳','斯莱特林']

# 保证两个AU不重合
flag1 = random.randint(0, len(mylist)-1)
print(mylist[flag1])
