import sys
import io
import random
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

content = sys.argv[1]
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>第一句话<br />走你'

# 拆出最后1行的文本，返回
def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[108:]
    my_string = my_string[:-4]

    if my_string[-7:] == '</span>':
        my_string = my_string[:-7]

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
        return("佚名（请换行后输入名字）")

name = split_content(content)
return_string = '经检测，' + name + ' 的狂攻程度是：'

i = random.randint(-1,100)
if i <= 0:
    print(return_string + str(i) + '……百年一遇的狂受！')
elif i <= 20:
    print(return_string + str(i) + '。看来只是稍微有点攻呢？')
elif i <= 40:
    print(return_string + str(i) + '。是一般的攻度呢。')
elif i <= 60:
    print(return_string + str(i) + '。勉强及格的狂攻。')
elif i <= 80:
    print(return_string + str(i) + '。合格的狂攻！')
elif i <= 99:
    print(return_string + str(i) + '。双开门冰箱的般的狂攻！!')
else:
    print(return_string + str(i) + '！！！空前绝后的狂攻！！！！！！')