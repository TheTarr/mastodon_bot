# 收到用户两个人名，生成一个故事返回
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]

#content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>@第一句话<br />@ciao@hge'

def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[108:]
    my_string = my_string[:-4]
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
        return("thisisnot", 'cantbetrue')

person1, person2 = split_content(content)

if person1 == "thisisnot" and person2 == 'cantbetrue':
    print("格式有误！请输入关键词后换行，输入收件人完整地址（如：ciao@bgme.me），换行，再输入快递的物品。一共三行！")

elif person1 == 'ciao@bgme.me':
    print("哎？居然有人类给我寄了一个包裹！内容是……" + person2 + '……？谢谢！操！')
    
else:
    if person1[0] != "@":
        print('@' + person1 + ' 您好！有一份寄给您的匿名包裹，内容为：' + person2 + '。祝您生活愉快！')
    else:
        print(person1 + ' 您好！有一份寄给您的匿名包裹，内容为：' + person2 + '。祝您生活愉快！')