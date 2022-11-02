import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]

path = 'zhongdi.txt'

f = open(path,"r",encoding='UTF-8')   #设置文件对象
lines = f.readlines()
f.close()

f = open(path,"a",encoding='UTF-8')   #设置文件对象
try:
    flag = 0
    for i in lines:
        if i == content+'\n':
            flag+=1
    if flag <= 3:
        f.write(content+'\n')
        return_string = '种好了一颗大西瓜！'
    else:
        return_string = '您已经种满了三颗西瓜！'
except:
    return_string = '种下了……可是没有发芽！'
f.close()

print(return_string)