# 送礼，如果格式正确则送出礼物，抓取上一个礼物回赠
import sys
import io
import time
import os
import random
import shutil
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]


def move_file(src_path, dst_path, file):
    try:
        f_src = os.path.join(src_path, file)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        f_dst = os.path.join(dst_path, file)
        shutil.move(f_src, f_dst)
    except Exception as e:
        print ("移动文件时遇到bug")

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
        gift = my_string[flag2+1:flag3]
        word = my_string[flag4+1:]
        return(gift, word)
    else:
        return("thisisnot", 'cantbetrue')

gift, word = split_content(content)

if gift == "thisisnot" and word == 'cantbetrue':
    print("[格式有误！请输入关键词后换行，在第二行输入【礼物本身】例如大苹果，换行，在第三行输入【祝福语】例如祝你身体健康。一共三行！]")
else:
    # # 先存礼物
    # file_name = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    # f = open("gift/" + file_name + ".txt", "w", encoding='UTF-8')
    # try:
    #     f.write(str(gift)+'\n')
    #     f.write(str(word)+'\n')
    # except:
    #     f.write(str('[啊哦！这个礼物不小心破损了，里面内容已经消失在宇宙中。]'+'\n'))
    # f.close()  # 关闭文件

    # 再收一个最新的礼物
    filePath = 'gift/'
    files = os.listdir(filePath)
    if len(files) == 0:
        filePath = 'gift_done/'
        files = os.listdir(filePath)
        flag = random.randint(0,len(files)-1)
        f = open("gift_done/" + files[flag], "r", encoding='UTF-8')
        lines = f.readlines()
        print("礼物已送出！树下没有礼物了……操操为您找到了一份很久之前其他人留下的礼物：")
        for i in lines:
            print(i)
        f.close() #关闭文件
    # 随机抽一个
    else:
        flag = random.randint(0,len(files)-1)
        f = open("gift/" + files[flag], "r", encoding='UTF-8')
        lines = f.readlines()
        print("礼物已送出！操操也为您找到了一份其他人留下的礼物：")
        for i in lines:
            print(i)
        f.close() #关闭文件
        # 把这个文件移走
        move_file("gift/","gift_done/", files[flag])

# 最后存礼物
    file_name = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    f = open("gift/" + file_name + ".txt", "w", encoding='UTF-8')
    try:
        f.write(str(gift)+'\n')
        f.write(str(word)+'\n')
    except:
        f.write(str('[啊哦！这个礼物不小心破损了，里面内容已经消失在宇宙中。]'+'\n'))
    f.close()  # 关闭文件