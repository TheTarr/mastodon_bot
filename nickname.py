import sys
import io
import random
from post_poem import *
from my_encode import *
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>第一句话<br />郑云龙'

# 拆出最后1行的文本，返回
def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[108:]
    my_string = my_string[:-4]
    # print(my_string)
    i = len(my_string)
    flag4 = 0
    while i != 0:
        i-=1
        if my_string[i] == '>':
            flag4 = i
            break
    if flag4 != 0:
        poem_line = my_string[flag4+1:]
        return(poem_line)
    else:
        return("[啊哦！数据传输出现问题]")

full_name = split_content(content)
type = random.randint(1,19)

# 1：选个字叠字
if type < 5:
    flag = random.randint(0,len(full_name)-1)
    return_name = full_name[flag] + full_name[flag]
# 2：小x
elif type < 13:
    flag = random.randint(0,len(full_name)-1)
    return_name = '小' + full_name[flag]
# 2：俩字
elif type < 19 and len(full_name) >= 2:
    flag = random.randint(0,len(full_name)-2)
    return_name = full_name[flag:flag+2]
else:
# 4：完全无关
    name_list = ['旺财','咪咪','乐乐',
    '章鱼哥','底部里舅舅邓布利多','马大叔',
    '隔壁老王','李华','小红']
    flag = random.randint(0,len(name_list)-1)
    return_name = name_list[flag]
print(return_name)