import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

def print_line():
    # 动森所有音符，Xx 是无声
    # mylist = ['Do','Re','Mi','Fa','So','La','Si','XX','--']
    mylist = ['1','2','3','4','5','6','7','x','--']
    # 所有有低音部的音符，高音部只有 Do
    lowl = ['1','2','3','4','5','6','7']
    # lowl = ['Do','Re','Mi','Fa','So','La','Si']
    # 最终返回的音符句子
    rl = ''
    # 八个一行共两行，low 和 high 表记录可以进行高低音操作的位置
    i = 0
    low = []
    high = []

    while i < 8:
        # 第一个位置必须是音符
        if i == 0:
            current = mylist[random.randint(0, len(mylist) - 3)]
            if current in lowl:
                low.append(i)
            if current == 'Do':
                high.append(i)
            rl += current
            rl += ' '
            i += 1
        else:
            # X 后边不能接 -
            if rl[-1] == 'x':
                current = mylist[random.randint(0, len(mylist) - 2)]
                if current in lowl:
                    low.append(i)
                if current == '1':
                    high.append(i)
                rl += current
                rl += ' '
                i += 1
            else:
                current = mylist[random.randint(0, len(mylist) - 1)]
                if current in lowl:
                    low.append(i)
                if current == '1':
                    high.append(i)
                rl += current
                rl += ' '
                i += 1
    # print(rl)

    # high 的取值和打印
    myhigh=''
    # print(high)
    r = len(high)
    if r >= 1 :
        z = random.randint(0,1)
        if z == 1:
            x = random.randint(0,r-1)
            # print('youle')
            previous = int(high[x])
            myhigh += '   '* previous
            myhigh += ' · '
            if x in low:
                low.remove(x)
    # print(myhigh)

    # low 的取值和打印
    mylow = ''
    temp = []
    # print(low)
    r = len(low)
    if r < 4:
        x = random.randint(0,r-1)
        # print(low[x])
        temp.append(low[x])
    else:
        j = 0
        while j < r % 3:
            x = random.randint(0,r-1)
            # print(low[x])
            temp.append(low[x])
            j += 1
    g = 0
    while g < 8:
        if g in temp:
            mylow += ' · '
        else:
            mylow += '   '
        g += 1
    # print(mylow)

    print(myhigh)
    print(rl)
    print(mylow)

def web_print():
    rl = ''
    # mylist = ["Do↓","Re↓","Mi↓","Fa↓","So↓","La↓","Si↓",'Do','Re','Mi','Fa','So','La','Si',"Do↑",'xx','--']
    mylist = ["G↓","A↓","B↓",'C','D','E','F','G','A','B',"C↑",'D↑','E↑','xx','--']
    i = 0
    while i < 8:
        if i == 0:
            current = mylist[random.randint(0, len(mylist) - 3)]
        else:
            if rl[-1] == 'xx':
                current = mylist[random.randint(0, len(mylist) - 2)]
            else:
                current = mylist[random.randint(0, len(mylist) - 1)]
        rl += current
        rl += ' '
        i += 1
    print(rl)

print('（清嗓子）咳咳！请听：')
web_print()
web_print()

# print_line()
# print_line()