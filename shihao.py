# 第一个字随机，第二个字从id中抽一个字符
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]
# content = 'hi'

f = open("shihao.txt","r",encoding="UTF-8")
mstr0 = f.readlines()
mstr=[]
f.close()
for i in mstr0:
    if '\n' in i:
        j = i[0:-1]
        mstr.append(j)
    else:
        mstr.append(i)

beta = '文武明睿康景庄宣懿'

ns = ''
returnstr = ''

round=random.randint(1,10)

temp = []

for x in range(0,round):
    flag = random.randint(0,len(mstr)-1)
    if flag not in temp:
        temp.append(flag)
        returnstr += mstr[flag]
    else:
        continue


for i in content:
    if '\u4e00' <= i <= '\u9fa5':
        ns+=i

if ns == '':
    flag = random.randint(0,len(beta)-1)
    returnstr += beta[flag]
else:
    flag = random.randint(0,len(ns)-1)
    returnstr += ns[flag]

print(returnstr)

