import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>p<br />a</p>'

# 拆出最后两行的文本，返回
def split_content(text):
    my_string = text[108:]
    my_string = my_string[:-4]
    # print(my_string)
    i = len(my_string)
    flag2 = 0
    flag3 = 0
    flag4 = 0
    while i != 0:
        i-=1
        if my_string[i] == '>':
            if flag4==0:
                flag4 = i
            else:
                flag2 = i
                break
        if my_string[i] == '<':
            flag3 =i

    if flag2 != 0 and flag3 != 0 and flag4 != 0:
        person1 = my_string[flag2+1:flag3]
        person2 = my_string[flag4+1:]
        return(person1, person2)
    else:
        return("A", "B")

career_list = ['人鱼', '吸血鬼', '丧尸', '龙', '社畜', \
        '模特', '魔法师', '高中生', '花店店员', '厨师', '骑士', \
        '电竞选手', '干净又卫生主播', '美妆博主', \
        '海盗', '仿生人', '机器人', '外星人', \
        '歌手', '研究生兼职辅导员', '演员', '片警', '大学生', \
        '程序员', '作家', '画师', '物理学家', '生物学家', \
        '神奇动物', '超级英雄', '狐狸精', '班长', \
        '俄罗斯人', '体育生', '神父', '棕熊', '老师', \
        '月老', '牙医', '医生', '摄影师', '兽医', \
        '魔术师', '摸金校尉', '鱼贩', '道士', \
        '设计师', '高达驾驶员', '精灵', \
        '暴走族', '牧马人', '乌龟饲养员', '护林员', '飞行员',\
        '婚礼主持人', '商人', '老板', '实习生', '天师']

adj_list = ['温柔的', '显著帅过正常人的', '暴躁的', '凶残的', '勇敢的', \
        '忧心忡忡的', '成熟的', '热爱运动的', '责任心强的', '曾经两次掉进井里的', \
        '事业有成的', '非常有钱的', '腿毛很性感的', '爱热闹的', \
        '野心勃勃的', '不吃香菜的', '乳糖不耐受的', '不太聪明的', '聪明的', \
        '经常面带微笑的', '胸很大的', '忘记吃早饭的', '拥有天籁般嗓音的', \
        '酒量很差的', '富有同情心的', '不太会拒绝别人的', '成绩很好的', \
        '一杯茶一包烟一篇论文写一天的', '正在犯困的', '随性的', '失忆的', \
        '很会做饭的', '不爱看书的', '长出猫耳的', '性欲旺盛的', \
        '地球上最后的', '宇宙里唯一的', '人气极高的', '古穿今的', '饥肠辘辘的']

# '在', '在', '在', '在', \
position_list = ['在学校', '在家里', '在厕所', '在天坛东路', '躺在床上', \
        '在电梯里', '在飞机上', '在森林里', '在街边的超市', '在演唱会', \
        '在老板的办公室', '在发小的生日聚会上', '在十字路口', \
        '在宇宙飞船里', '在外星', '在花鸟鱼虫市场', \
        '在唐人街', '在施工现场', '在地铁里', '在火车站', '在秋叶原', \
        '在自习室', '在加油站', '在河边', '在饭馆', '在肯德基', \
        '在旅馆', '在水族馆', '在动物园', '在办公室', '在医院', \
        '在副本里', '在香菜组成的森林里', '在印度街头', '在厨房里', '蹲在树上']

# '时', '时', '时', '时', \
event_list = ['写论文时', '吃饭时', '看黄片时', '屠龙时', '猎魔时', \
        '撞邪时', '和别人做爱时', '玩手机时', '幻想中了六合彩时', \
        '发呆时', '生闷气时', '吃薯片时', '遛狗时', \
        '祈祷时', '想烦心事时', '写代码时', '被通知自己竟然怀孕！！！时', '发现钱包丢了时', \
        '喝水时', '迷路时', '因为踩到口香糖而火大时', \
        '打游戏时', '练武功时', '看书时', '讲笑话时', '学英语时', '思考晚饭吃什么时']

action_list = ['不小心撞倒了', '碰巧遇到了', '竟然重逢了', '顺手调戏了', '一见钟情了', '连哄带骗带走了', \
        '分手了', '意外失忆, 竟然忘记了', '决定告白']

# 以下代码保证两人的性格和角色不同
adj1 = random.randint(0,len(adj_list)-1)
while True:
    adj2 = random.randint(0,len(adj_list)-1)
    if adj2 != adj1:
        break
career1 = random.randint(0,len(career_list)-1)
while True:
    career2 = random.randint(0,len(career_list)-1)
    if career2 != career1:
        break
position = random.randint(0,len(position_list)-1)
event = random.randint(0,len(event_list)-1)
action = random.randint(0,len(action_list)-1)

person1, person2 = split_content(content)

return_string = "作为一个" + adj_list[adj1] + career_list[career1] + \
    ", " + person1 + position_list[position] + event_list[event] + \
    ", " + action_list[action] + adj_list[adj2] + career_list[career2] + person2 + "。"

print(return_string)