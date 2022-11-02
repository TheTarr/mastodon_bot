import sys
import io
import random
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>王杰希</p><p>肖时钦<br>叶修<br>张新杰</p>'
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 丢瓶子<br />这是第一个瓶子的第一句话<br />来自面条！</p>'
# content = 'rer" target="_blank">@<span>ciao</span></a></span> 拉郎 bug测试</p>'

str1 = '</span>'
str2 = '<br />'
str3 = '<br>'


def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[:-4]
    if my_string[-7:] == '</span>':
        my_string = my_string[:-7]

    flag1 = text.find(str1)
    my_string = my_string[flag1+7:]
    flag2 = my_string.find(str1)
    my_string = my_string[flag2+8:]

    if my_string.find(str2) != -1:
        my_string = my_string.replace("</p><p>",'<br />')
        poem_line = my_string.split("<br />")
        return(poem_line)
    elif my_string.find(str3) != -1:
        my_string = my_string.replace("</p><p>",'<br>')
        poem_line = my_string.split("<br>")
        return(poem_line)
    else:
        return(my_string)


poem_line = split_content(content)
# print(poem_line)

try:
    if len(poem_line)<=2 or type(poem_line) == type("string"):
        print("请用换行方式输入两个以上角色！")
    else:
        i = len(poem_line)
        flag1 = random.randint(1, i-1)
        while True:
            flag2 = random.randint(1, i-1)
            if flag2 != flag1:
                break
        print("操操认为天造地设的一对新人是：" +
              poem_line[flag1] + " × " + poem_line[flag2] + "！")
except:
    print("通信有误！请用换行方式输入两个以上角色！")
