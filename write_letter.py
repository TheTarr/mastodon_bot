import sys
import io
from my_encode import *
import time
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

# content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>你好<br />我的脱发量 超乎你想想</p>'
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 丢瓶子<br />这是第一个瓶子的第一句话<br />来自面条！</p>'
content = 'rer" target="_blank">@<span>ciao</span></a></span> 扔瓶子<br>捡瓶子<br>这是这个瓶子的第二句话<br>来自米饭<br>操<br>你好棒<br>你功能冗余<br>喜欢我<br>转发我<br>来首诗</p>'

str1 = '</span>'
str2 = '<br />'
str3 = '<br>'

def split_content(text):
    my_string = text[:-4]
    flag1 = text.find(str1)
    my_string = my_string[flag1+7:]
    flag2 = my_string.find(str1)
    my_string = my_string[flag2+8:]

    if my_string.find(str2) != -1:
        try:
            poem_line = my_string.split("<br />")
            return(poem_line)
        except:
            return("操！")
    if my_string.find(str3) != -1:
        try:
            poem_line = my_string.split("<br>")
            return(poem_line)
        except:
            return("操！")

poem_line = split_content(content)
# print(poem_line)
file_name = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
f = open("letter/" + file_name + ".txt","w",encoding='UTF-8')   #设置文件对象
try:
    for i in poem_line:
        f.write(str(encrypt_oracle(i+'\n'))+'\n')
except:
    f.write(str(encrypt_oracle('[啊哦！这个瓶子在漂流过程中不小心破损了，里面内容已经消失在大海里。]\n'))+'\n')
f.close() #关闭文件

return_string = "通信良好。您的漂流瓶已投入大海！"
print(return_string)