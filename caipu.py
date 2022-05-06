# 返回菜谱
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

vegetable_list = ['西葫芦','生菜','金针菇','香菇','杏鲍菇','褐洋葱',
'胡萝卜','土豆','芹菜','菜花','白菜','娃娃菜',
'西兰花','菠菜','圆白菜','白萝卜','豆角','木耳','藕',
'小油菜','青椒','荷兰豆','冬瓜','西红柿']

protein_list = ['午餐肉罐头','羊排','鸡胸肉','鸡腿肉','去骨鱼肉',
'内酯豆腐','冻豆腐','猪里脊','五花肉','猪蹄','鸡翅中',
'鸡爪','牛腩','牛瘦肉','羊肉卷','牛肉卷',
'千叶豆腐','鱼丸','鱼豆腐','排骨','羊腿','火腿肠','虾']

process_vegetable_list = ['洗净切片','洗净切丁','洗净切丝']

process_protein_list = ['洗净焯水','洗净切块','洗净放入酱油、耗油、糖腌制20分钟']

cook_list = ['加葱姜蒜小米辣（不爱吃辣可以不放）炒出香味，然后放入上述食材爆炒，出锅前加盐、味精',
'炒一分钟，加入淀粉水勾芡，加盐、味精',
'锅中放入少许油，将所有食材煎熟，加盐、胡椒粉',
'先将食材炒香，再放入砂锅中，加入没过食材的水，小火煲2小时，出锅前加盐',
'锅中放水烧开，加入食材和酱油炖煮，出锅前加盐、味精',
'将原料蒸熟，再将酱油、耗油、糖、蜂蜜调制的卤汁浇淋于食材上翻拌成菜']

flag1 = random.randint(0, len(vegetable_list)-1)

while True:
    flag2 = random.randint(0, len(vegetable_list)-1)
    if flag1 != flag2:
        break

pro = protein_list[random.randint(0, len(protein_list)-1)]


print('你好！操操经过反复实验，研制出最新菜谱：取' + vegetable_list[flag1] + 
process_vegetable_list[random.randint(0, len(process_vegetable_list)-1)] + '，再取' + 
vegetable_list[flag2] + process_vegetable_list[random.randint(0, len(process_vegetable_list)-1)] +
'，最后将' + pro + process_protein_list[random.randint(0, len(process_protein_list)-1)] + '。' + 
cook_list[random.randint(0, len(cook_list)-1)] + '。大功告成，')