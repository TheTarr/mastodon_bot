import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

path = 'ow.txt'

f = open(path,"r",encoding='UTF-8')   #设置文件对象
poem_line = f.readlines()
f.close()

try:
    i = len(poem_line)
    flag1 = random.randint(1, i-1)
    while True:
        flag2 = random.randint(1, i-1)
        if flag2 != flag1:
            break
    print("操操认为 " +
            poem_line[flag1][:-1] + " 和 " + poem_line[flag2][:-1] + " 之间必有一段不为人知的绯红往事！")
except:
    print("通信有误！请用换行方式输入两个以上角色！")
