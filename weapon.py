import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'weapon.txt'
total_n = 147

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(1,total_n)
content=linecache.getline(path, i)
f.close()

f = open('suit.txt',"r",encoding='UTF-8')
tao = f.readlines()
f.close()

tou = ['古代兵装头盔','雷鸣头盔','克洛格的面具','魔吉拉的面具',
'罗维奥的头巾','波克布林面罩','莫力布林面罩','蜥蜴战士面罩','莱尼尔面罩',
'琥珀耳坠','红宝石头饰','蓝宝石头饰','黄玉耳坠','蛋白石耳坠','钻石头饰']
shen = ['老旧的衬衫','防寒服','英杰服','蓝色大虾衬衫','它的衬衫']
jiao = ['老旧的裤子','沙地靴','雪地靴']

for i in tao:
    tou.append(i[:-1] + ' [头部]')
    shen.append(i[:-1] + ' [躯干]')
    jiao.append(i[:-1] + ' [腿部]')

e1 = tou[random.randint(0,len(tou)-1)]
e2 = shen[random.randint(0,len(shen)-1)]
e3 = jiao[random.randint(0,len(jiao)-1)]

print("操操认为最时尚的搭配是：" + e1 + " + " + e2 + " + "  + e3 + " + "  + content[:-1] + "！！！")