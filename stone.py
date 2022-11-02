import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'stone.txt'
total_n = 272

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(1,total_n)
content=linecache.getline(path, i)
flag1 = 0
flag2 = 0
for i in range(0, len(content)-1):
    if content[i] == '	':
        if flag1 == 0:
            flag1 = i
        else:
            flag2=i
        

f.close() #关闭文件

print("的矿物是：" + content[flag1+1:flag2])