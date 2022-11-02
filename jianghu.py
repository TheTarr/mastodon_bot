# 第一个字随机，第二个字从id中抽一个字符
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

f = open("jianghu.txt","r",encoding="UTF-8")
mstr0 = f.readline()
f.close()

menpai = mstr0.split('，')

zhiye = ['上九流 - 佛祖','上九流 - 仙','上九流 - 皇帝','上九流 - 官','上九流 - 王爷','上九流 - 将','上九流 - 商','上九流 - 农','上九流 - 文人',
'中九流 - 举子','中九流 - 医生','中九流 - 风水先生','中九流 - 丹青','中九流 - 书生','中九流 - 琴棋','中九流 - 僧','中九流 - 道','中九流 - 尼',
'下九流 - 衙役','下九流 - 打更人','下九流 - 时妖','下九流 - 剃头','下九流 - 脚夫','下九流 - 高台','下九流 - 吹','下九流 - 马戏','下九流 - 娼',
'外八行 - 金点','外八行 - 乞丐','外八行 - 响马','外八行 - 贼盗','外八行 - 倒斗','外八行 - 走山','外八行 - 领火','外八行 - 采水']

returnstr = '拜入'

flag = random.randint(0,len(menpai)-1)
returnstr += menpai[flag]

returnstr += '，从事：'

flag = random.randint(0,len(zhiye)-1)
returnstr += zhiye[flag]


print(returnstr)

