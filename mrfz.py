import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

# 名字
name0 = sys.argv[1]
# 职业
zhiye = ['先锋','近卫','特种','重装','术士','医疗','辅助','狙击']
zhiye0 = zhiye[random.randint(0,len(zhiye)-1)]
# 阵营
zhenying = ['罗德岛','卡西米尔','汐斯塔','巴别塔','莱塔尼亚','维多利亚','莱茵生命','企鹅物流','黑钢国际','喀兰贸易','拉特兰','雷姆必拓','龙门']
# 战斗经验
zhandoujingyan = ['仨小时','俩礼拜','一个月','半年','一年','两年','三年','四年','五年','六年','七年','八年','九年','十年','十五年']
zhandoujingyan0 = zhandoujingyan[random.randint(0,len(zhandoujingyan)-1)]
# 出身地
# 阿戈尔 - 阿戈尔，伊比利亚
# 萨卡兹 - 卡兹戴尔
# 卡普里尼 - 莱塔尼亚
# 丰蹄 - 米诺斯 
# 佩洛 - 玻利瓦尔 
# 萨科塔- 拉特兰
# 鲁珀 - 叙拉古
# 沃尔珀 - 叙拉古
# 菲林 - 谢拉格、维多利亚
# 乌萨斯 - 乌萨斯
# 卡特斯 - 雷姆必拓
# 库兰塔 - 卡西米尔
chushendi = ['汐斯塔','萨米','莱塔尼亚','龙门','炎国','伊比利亚','米诺斯','玻利瓦尔','拉特兰','叙拉古','谢拉格','乌萨斯','雷姆必拓','东国','卡西米尔','萨尔贡','哥伦比亚','维多利亚']

# 种族+出身地
zhongzu = ['菲林','黎博利','沃尔珀','萨卡兹','卡特斯','佩洛','库兰塔','乌萨斯','丰蹄','阿戈尔','瓦伊凡','鲁珀','卡普里尼','萨科塔','札拉克','萨弗拉','鬼','阿纳缇','埃拉菲亚','阿达克利斯','支援机械','瑞柏巴','斐迪亚','杜林','阿斯兰','依特拉','赛拉托','皮洛萨','匹特拉姆','安努拉','德拉克','龙','曼提柯','奇美拉','麒麟']
zhongzu0 = zhongzu[random.randint(0,len(zhongzu)-1)]

if zhongzu0 == '阿戈尔':
    for i in range(0,30):
        zhenying.append('深海猎人')
        chushendi.append('阿戈尔')
    for i in range(0,5):
        chushendi.append('伊比利亚')
elif zhongzu0 == '萨卡兹':
    for i in range(0,30):
        chushendi.append('卡兹戴尔')
elif zhongzu0 == '卡普里尼':
    for i in range(0,20):
        chushendi.append('莱塔尼亚')
elif zhongzu0 == '丰蹄':
    for i in range(0,20):
        chushendi.append('米诺斯')
elif zhongzu0 == '佩洛':
    for i in range(0,20):
        chushendi.append('玻利瓦尔')
elif zhongzu0 == '萨科塔':
    for i in range(0,30):
        zhenying.append('拉特兰')
        chushendi.append('拉特兰')
elif zhongzu0 == '鲁珀':
    for i in range(0,20):
        chushendi.append('叙拉古')
elif zhongzu0 == '沃尔珀':
    for i in range(0,20):
        chushendi.append('叙拉古')
elif zhongzu0 == '乌萨斯':
    for i in range(0,30):
        zhenying.append('乌萨斯')
        chushendi.append('乌萨斯')
elif zhongzu0 == '菲林':
    for i in range(0,10):
        chushendi.append('谢拉格')
    for i in range(0,10):
        chushendi.append('维多利亚')
elif zhongzu0 == '卡特斯':
    for i in range(0,30):
        chushendi.append('雷姆必拓')
elif zhongzu0 == '库兰塔':
    for i in range(0,30):
        chushendi.append('卡西米尔')

chushendi0 = chushendi[random.randint(0,len(chushendi)-1)]
zhenying0 = zhenying[random.randint(0,len(zhenying)-1)]

# 身高
shengao0 = str(random.randint(142,198))
# 矿石病感染情况
kuangshibing = ['参照医学检测报告，确认为非感染者。','体表有源石结晶分布，参照医学检测报告，确认为感染者。','参照医学检测报告，确认为感染者。','体表未发现任何源石结晶，确认为非感染者。']
kuangshibing0 = kuangshibing[random.randint(0,len(kuangshibing)-1)]

# 语音
# f = open('mrfz.txt','r',encoding='utf-8')
total_n = 376
i = random.randint(1,total_n)
content=linecache.getline('mrfz.txt', i)

return_string = ' ' +  '\n' + \
    '----------干员信息----------' +  '\n' + \
    '姓名：' + name0 + '\n' + \
    "职业：" + zhiye0 + '\n' + \
    '阵营：' + zhenying0 + '\n' + \
        ' ' +  '\n' + \
    '----------基础档案----------' +  '\n' + \
    '【战斗经验】' + zhandoujingyan0 + '\n' + \
        '【出身地】' + chushendi0 + '\n' + \
            '【种族】' + zhongzu0 + '\n' + \
                '【身高】' + shengao0 + 'cm\n' + \
                    '【矿石病感染情况】' + kuangshibing0 + '\n' + \
                        ' ' +  '\n' + \
                        '----------召唤语音----------' +  '\n' + \
                            content +  '\n'


print(return_string)