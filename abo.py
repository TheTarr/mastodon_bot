# 收到用户两个人名，生成一个故事返回
import sys
import random
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>p<br />a</p>'
# content = '<span class="h-card"><a class="u-url mention" href="https://bgme.me/@miantiao07" rel="nofollow noopener noreferrer" target="_blank">@<span>miantiao07</span></a></span>  奇遇<br>大坏狼<br>狐市长'
# 拆出最后两行的文本，返回


def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[108:]
    my_string = my_string[:-4]

    if my_string[-7:] == '</span>':
        my_string = my_string[:-7]
    
    # print(my_string)
    i = len(my_string)
    flag2 = 0
    flag3 = 0
    flag4 = 0
    while i != 0:
        i -= 1
        if my_string[i] == '>':
            if flag4 == 0:
                flag4 = i
            else:
                flag2 = i
                break
        if my_string[i] == '<':
            flag3 = i

    if flag2 != 0 and flag3 != 0 and flag4 != 0:
        person1 = my_string[flag2+1:flag3]
        person2 = my_string[flag4+1:]
        return(person1, person2)
    else:
        return("A", "B")


# '','','','','','','','',
smell_list = [
    # 木质
    '檀木','崖柏','松木','橡木','乌木','竹','广藿','桉树',
    # 果香
    '柠檬','苹果','菠萝','荔枝','橙子','佛手柑','葡萄柚','百香果',
    # 花香
    '薰衣草','天竺葵','玫瑰','茉莉','牡丹','豆蔻','樱花','桂花','橙花','菊花',
    # 香水常见
    '麝香','香草','海腥','还没抽的烟草','洋酒',
    # 其他
    '刚割完的草坪','老干妈','铁观音','绿X薄荷糖','海飞X洗发水',
    '肯德X皮蛋瘦肉粥','BBQ','苯酚','新印刷的书','阿姨的卡布奇诺',
    '电路板','旧报纸','大麦']

type_list = ['A','B','O','E']

# 以下代码保证两人的气味不同
smell1 = random.randint(0, len(smell_list)-1)
while True:
    smell2 = random.randint(0, len(smell_list)-1)
    if smell2 != smell1:
        break

flag = random.randint(0, 10)
if flag < 1:
    type1 = 'E'
elif flag < 4:
    type1 = 'A'
elif flag < 7:
    type1 = 'O'
else:
    type1 = 'B'

flag = random.randint(0, 13)
if flag < 1:
    type2 = 'E'
elif flag < 4:
    type2 = 'A'
elif flag < 7:
    type2 = 'O'
else:
    type2 = 'B'

person1, person2 = split_content(content)

return_string = person1 + '：' + smell_list[smell1] + '味的 ' + type1 + '\n' + person2 + '：' + smell_list[smell2] + '味的 ' + type2

print(return_string)
