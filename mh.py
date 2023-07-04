# f = open('mh.txt','r',encoding = 'utf-8')
# l = f.readline()
# temp = ''
# a = 0
# b = 0
# for i in l:
    
#     if i == '第':
#         temp += l[a:b] + '\n'
#         a = b
#     b+=1
# print(temp)

import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'mh.txt'
total_n = 151

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(1,total_n)
content=linecache.getline(path, i).strip('\n')
f.close() #关闭文件

for i in range(0,len(content)-1):
    if content[i] == ' ':
        flag = i

dragon = content[flag+1:]

x = random.randint(0,2)
if x == 0:
    retu = '恭喜这位猎人！成功操上了 ' + dragon + '！'
elif x == 1:
    retu = '哎呀，这位猎人操作失误！' + dragon + ' 跑掉了。'
else:
    retu = '啊呀！这位猎人一个不幸，反而被 ' + dragon + ' 给操了！'
print(retu)