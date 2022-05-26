import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'THUOCL_food.txt'
total_n = 8974

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(0,total_n-1)
content=linecache.getline(path, i)
flag = 0
for i in range(0, len(content)-1):
    if content[i] == '	':
        flag = i
        break

f.close() #关闭文件

print(content[:flag])