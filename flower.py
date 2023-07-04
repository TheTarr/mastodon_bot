import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'flower.txt'
total_n = 123

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(1,total_n)
content=linecache.getline(path, i)
flag1 = 0
for i in range(0, len(content)-1):
    if content[i] == '：':
        flag1 = i
        

f.close() #关闭文件

print("操操为您叼来了一朵 " + content[0:flag1] + "！花语为" + content[flag1:-1] + "…… ChatGPT 这么说的，应该没骗我吧？")