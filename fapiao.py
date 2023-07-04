import sys
import random
import io
from datetime import date
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# 操操增值税电子普通发票
# 发票代码6
daima = random.randint(100000,999999)
# 发票号码6
f = open('fapiao.txt','r',encoding='utf-8')
haoma_str = f.readline()
haoma = int(haoma_str)
f.close()
f = open('fapiao.txt','w',encoding='utf-8')
f.write(f'{haoma+1:06d}')
f.close()
# 开票日期
today = date.today()
# 校验码20位
jiaoyan = random.randint(10000,99999)

# 货物或应税劳务、服务名称：
product_list = ['操大师捏肩','操大师踩背','操大师理发','操大师正骨','操大师请仙','操大师做法','操大师炒',
'操大师陪睡（真的只是睡觉）','西瓜','抓海鸥','操大师陪聊','操大师陪酒（喝的是果汁）',
'金矿','电脑及配件','手机及配件','家电','服装鞋帽','机械手','建筑材料','营养保健品','旅游服务','物流服务',
'餐饮服务','住宿服务','运动健身服务','内存条','显示器','键盘','鼠标','硬盘','U盘','显卡','手机壳','手机膜',
'电视机','冰箱','空调','洗衣机','吸尘器','电风扇','医用手套','数控机床','挖掘机','铣床','推土机','电锤',
'砖头','瓦片','玻璃','沙子','石头','水泥','维生素','钙片','蛋白粉','膳食纤维','益生菌','法律咨询',
'IT咨询','移动应用开发','名片印刷','海报印刷','仓储服务','装卸服务','运输保险','车险','外卖服务','酒水服务','餐饮配送','旅店住宿',
'民宿住宿','炉石陪搓','游泳池会员','瑜伽课程','健身房会员','羽毛球场地租赁','操大师美甲','发动机','变速箱','音响','液化石油气','陶瓷艺术品',
'手表','珠宝','文具','工艺品','宠物美容','宠物寄养','茶叶','农机具','肥料','海洋之心','狼人领养',
'宝剑锻造','游戏内购买','购买游戏']
flag = random.randint(0, len(product_list)-1)
product = product_list[flag]
# 数量：
flag = random.randint(1,10)
if flag == 10:
    n = random.randint(100,1000)
elif flag > 7:
    n = random.randint(2,100)
else:
    n = 1
# 单价：
flag = random.randint(1,10)
if flag == 10:
    danjia = random.randint(2000,10000)
elif flag > 8:
    danjia = random.randint(1000,2000)
elif flag > 7:
    danjia = random.randint(100,1000)
else:
    danjia = random.randint(1,100)
# 金额：
jine = n*danjia
# 税率：
flag= random.randint(1,10)
if flag == 10:
    shuilv = rand_num = round(random.uniform(-1, 0), 2)
elif flag == 9:
    shuilv = rand_num = round(random.uniform(0.1, 10), 2)
else:
    shuilv = rand_num = round(random.uniform(0, 0.1), 2)
# 税额：
shuie = round(jine * shuilv,2)

print("bzzzzzz——(打印机正在工作)")
print("┌-----------------------------------------┐")
print("|  操操增值税电子普通发票  |")
print("| 发票代码："+ str(daima) +"            |")
print("| 发票号码："+ haoma_str +"            |")
print("| 开票日期：" + today.strftime("%Y年%m月%d日") +  " |")
print("| 校验码："+ str(jiaoyan) +"                  |")
print("├-----------------------------------------┤")
print("| 货物或应税劳务、服务名称：")
print("|   " + product)
print("| 数量："+ str(n))
print("| 单价："+ str(danjia))
print("| 金额："+ str(jine))
print("| 税率："+ str(shuilv))
print("| 税额："+ str(shuie))
print("└-----------------------------------------┘")