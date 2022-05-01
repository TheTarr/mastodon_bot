# 收到一句话，返回加儿化音的这句话
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>p<br />你好，亲爱的朋友</p>'

# 拆出最后一行的文本
def split_content(text):
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
        return("[格式有误！]")

# 这个程序员居然想起来用递归了=w=
def add_er(text, round):
    if round == 0:
        return text
    position = random.randint(1,len(text))
    my_string = text[:position] + '儿' + text[position:]
    return add_er(my_string, round-1)
    
    # l = len(text)
    # if l < 10:
    #     flag = 1
    # else:
    #     flag = 2
    # if flag == 1:
    #     position = random.randint(1,l)
    #     return_string = text[:position] + '儿' + text[position:]
    #     return return_string
    # elif flag == 2:
    #     position1 = random.randint(1,l)
    #     while(True):
    #         position2  = random.randint(1,l)
    #         if position2 != position1:
    #             break
    #     if position1 < position2:
    #         return_string = text[:position1] + '儿' + text[position1:position2] + '儿' + text[position2:]
    #     else:
    #         return_string = text[:position2] + '儿' + text[position2:position1] + '儿' + text[position1:]
    #     return return_string

my_string = split_content(content)
if len(my_string) > 30:
    return_string = add_er(my_string, 4)
elif len(my_string) > 20:
    return_string = add_er(my_string, 3)
elif len(my_string) > 10:
    return_string = add_er(my_string, 2)
else:
    return_string = add_er(my_string, 1)

print(return_string)
