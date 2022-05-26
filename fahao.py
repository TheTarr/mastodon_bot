# 第一个字随机，第二个字从id中抽一个字符
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]
# content = 'hi'

mstr = '福慧智子觉了本圆可悟周洪普广宗道庆同玄祖清净真如海湛寂淳贞素德行永延恒妙本常坚固心朗照幽深性明鉴崇祚衷正善禧禅谨悫原济度雪庭为导师引汝归铉路'
beta = '海山操善行清文水回灵'

ns = ''
returnstr = ''
flag = random.randint(0,len(mstr)-1)
returnstr += mstr[flag]

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

