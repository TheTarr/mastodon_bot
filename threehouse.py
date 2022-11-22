import sys
import io
import random
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

content = sys.argv[1]
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>第一句话<br />走你'

path = 'threehouse.txt'
total_n = 25

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(1,total_n)
color=linecache.getline(path, i)
f.close() #关闭文件

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
return_string = '经检测，最适合 ' + name + ' 的金婚对象是：' + color

print(return_string)