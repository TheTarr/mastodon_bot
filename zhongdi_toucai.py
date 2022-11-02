import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

path = 'zhongdi.txt'

f = open(path,"r",encoding='UTF-8')   #设置文件对象
lines = f.readlines()
f.close()

total_n = len(lines)
# print(total_n)
# print(lines)

try:
    i = random.randint(0,total_n-1)
    content=lines[i]
    del lines[i]

    # print(lines)

    f = open(path,"w",encoding='UTF-8')
    f.writelines(lines)
    f.close() #关闭文件

    return_string = "恭喜您偷到了 @" + content[:-1] + " 种好的大西瓜！"
except:
    return_string = '瓜田里已经没有瓜了！'

print(return_string)