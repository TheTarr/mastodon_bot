# 收到用户两个人名，生成一个故事返回
import sys
import io
import random
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]
# content = '<p>< a href="https://bgme.me/@ciao" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@ciao@bgme.me</ a><span> 你好<br>李响</span></p>'

def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[108:]
    my_string = my_string[:-4]

    if my_string[-7:] == '</span>':
        my_string = my_string[:-7]

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
        return("佚名")


person = split_content(content)

ml = ['（做法）','（跳大神）','（围炉转圈）','（上香）','𓀀𓀁𓀃𓀅𓀇𓀋𓀌𓀎','（念咒）','（旋转）',
'（摇铃）','（低声吟唱）','（甩旗）','𓀉𓀊𓀋𓀌𓀍']

returnstr = person + '！魂兮归来！'
num_of_round = random.randint(4,12)
i = 0
while i < num_of_round:
    j = random.randint(0,len(ml)-1)
    returnstr += ml[j]
    i+=1

flag = random.randint(1,12)
if flag == 1:
    returnstr += person + "……" + person + "复活成功了！！"
elif flag < 4:
    returnstr += "……招魂幡动了动，但是仅此而已。"
else:
    returnstr += "……操操筋疲力竭……" + person + "没有回应。"
print(returnstr)
