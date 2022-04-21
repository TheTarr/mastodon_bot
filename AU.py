import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

mylist = ['人鱼', '吸血鬼', '赛博朋克', '丧尸', '龙', '社畜', \
        '一方年操', '校园', '模特', '古风', 'ABO', '公路', 'HP', \
        '电子竞技', '女装攻', '原作', '一方长出了猫耳', '普通地一起吃饭', \
        '花吐', '学长和学弟的关系', '仿生人', '机器人', '大家去外星研究阿凡达', \
        '一日男友', '激烈地做爱', '演员', '片警', '偶尔尝试一下群像也不错？', \
        '我也想不出来', '只有处男才有猫耳的那个动画片是什么来着', \
        '神奇动物在我的楼顶', '超级英雄', '两方长出了猫耳', '队里有一个人是O究竟是谁呢', \
        '酒后乱性', '变成狗了', '接吻就会交换运气']

flag1 = random.randint(0,len(mylist)-1)
flag2 = random.randint(0,len(mylist)-1)
print(mylist[flag1] + " + " +  mylist[flag2])