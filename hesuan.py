import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

path = 'color.txt'
total_n = 628

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(1,total_n)
color=linecache.getline(path, i)
f.close() #关闭文件

flag = 0
for i in range(0,len(color)):
    if color[i] == '#':
        flag = i
        break
    if color[i] == ' ':
        flag = i
        break
# print(flag)
color = color[:flag]
# print(color)
if color[len(color)-1]!='色':
    color += '色'

print('核酸结果已出，您是 ' + color + ' 码')