import sys
import io
from my_encode import *
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>第一句话<br />这是第二句话</p>'

# 拆出最后1行的文本，返回
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
        return("操！")

poem_line = split_content(content)
return_string = "通信良好。您的诗句已被记录！"
f = open("poem.txt","a",encoding='UTF-8')   #设置文件对象
f.write(str(encrypt_oracle(poem_line+'\n'))+'\n')
f.close() #关闭文件

print(return_string)