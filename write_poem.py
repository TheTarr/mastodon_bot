import sys
import io
import time
import shutil
from datetime import datetime
import pytz
from post_poem import *
from my_encode import *
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>第一句话<br />走你'
# content = '<p>< a href="https://bgme.me/@ciao" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@ciao@bgme.me</ a><span> 你好<br>建设数字北京，享受现代生活。北京市政交通一卡通有限公司</span></p>'

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
        return("操！")

poem_line = split_content(content)
return_string = "通信良好。您的诗句已被记录！"

# 如果没有出现在本诗中就记录，不然不记录
# ml = [] // encode 版本
# f = open('poem.txt', "r", encoding='UTF-8')   #设置文件对象
# for i in f.readlines():
#     h = decrypt_oralce(i[2:])
#     ml.append(h.decode())
# f.close() #关闭文件

ml = []
f = open('poem.txt', "r", encoding='UTF-8')   #设置文件对象
for i in f.readlines():
    ml.append(i)
f.close() #关闭文件

flag = 0
for i in ml:
    if i == poem_line+'\n':
        flag = 1

if flag ==0:
    f = open("poem.txt","a",encoding='UTF-8')   #设置文件对象
    # f.write(str(encrypt_oracle(poem_line+'\n'))+'\n')
    f.write(poem_line+'\n')
    f.close() #关闭文件

flag = 0

f = open("poem.txt","r",encoding='UTF-8')   #设置文件对象
res = len(f.readlines()) 
f.close() #关闭文件

if res >= 15:
    flag = 1
    post_poem('poem.txt')

if flag == 1:
    # shutil.copy('poem.txt','poem/'+time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())+'.txt')
    # f = open("poem.txt", 'w')
    # f.write(str(encrypt_oracle(time.strftime('%Y/%m/%d - %H', time.localtime())+' 时\n'))+'\n')
    # f.close()
    shutil.copy('poem.txt','poem/'+ datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y_%m_%d_%H_%M_%S')+'.txt')
    f = open("poem.txt", 'w', encoding='UTF-8')
    # f.write(str(encrypt_oracle(time.strftime('%Y/%m/%d - %H', time.localtime())+' 时\n'))+'\n')
    f.write(datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y/%m/%d - %H')+' 时\n')
    f.close()

print(return_string)