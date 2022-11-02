# 第一个字随机，第二个字从id中抽一个字符
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]
mask = 0
# content = 'hi'

f = open("hougong.txt","r",encoding="UTF-8")
mstr0 = f.readlines()
mstr=[]
f.close()
for i in mstr0:
    if '\n' in i:
        j = i[0:-1]
        mstr.append(j)
    else:
        mstr.append(i)

beta = '福慧智子觉了本圆可悟周洪普广宗道庆同玄祖清净真如海湛寂淳贞素德行永延恒妙本常坚固心朗照幽深性明鉴崇祚衷正善禧禅谨悫原济度雪庭为导师引汝归铉路'

ns = ''
temp=''
returnstr = ''


flag = random.randint(0,len(mstr)-1)
temp += mstr[flag]


for i in content:
    if '\u4e00' <= i <= '\u9fa5':
        if ord(i)+mask > 40869:
            ns+=chr(ord(i)+mask-40869+19968)
        else:
            ns+=chr(ord(i)+mask)
n=0
for j in temp:
    if j == '：':
        break
    n+=1

returnstr += temp[0:n]
returnstr += ' - '

if ns == '':
    flag = random.randint(0,len(beta)-1)
    returnstr += beta[flag]
else:
    flag = random.randint(0,len(ns)-1)
    returnstr += ns[flag]

returnstr += temp[n+1:]

print(returnstr)

