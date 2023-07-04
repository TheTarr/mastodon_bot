# 收到用户两个人名，生成一个故事返回
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]

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
    print("格式有误！请输入关键词后换行，输入A的名字，换行，再输入B的名字。一共三行！")

else:
    print("操操对"+ person1 + "说：" + person1 + "，你是否愿意这个" + person2 + "成为你的陌生人并与ta离婚？")
    print(person1 + "：我愿意。")
    print("操操又问"+ person2 +"：" + person2 + "，你是否愿意这个" + person1 + "成为你的陌生人与ta离婚？")
    print(person2 + "：我愿意。")
    print("操操：主啊，戒指将不再代表ta们发出的誓言的约束。")
    print("众网友看着" + person1 + "和" + person2 + "脱下戒指：阿门阿门。")
    print("操操：我以圣父圣子圣灵的名义宣布你们离婚。")
    print("操操："+ person1 + "，" + person2 + "，我已证明你们互相发誓不再爱对方，我感到万分悲伤向在坐各位宣布你们为陌生人，此刻" + person1 + "不能够吻" + person2 + "了。")