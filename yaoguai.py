import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'yaoguai.txt'
total_n = 1950

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(1,total_n)
content=linecache.getline(path, i)
        
f.close() #关闭文件

print("的原形是：" + content)