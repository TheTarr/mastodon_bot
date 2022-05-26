# 收到人名，返回参数
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

content = sys.argv[1]
# 下边这条是从node接到的content例子，把上面comment掉测试用（部署之前记得改回去）
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>p<br />张继科</p>'

# 拆出最后一行的文本，返回


def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[108:]
    my_string = my_string[:-4]
    # print(my_string)
    i = len(my_string)
    flag4 = 0
    while i != 0:
        i -= 1
        if my_string[i] == '>':
            flag4 = i
            break
    if flag4 != 0:
        poem_line = my_string[flag4+1:]
        return(poem_line)
    else:
        return("佚名(请换行后输入姓名！)")


rate_list = ['SSR', 'SR', 'R']

skills_list = ['右脚打响指 -> 对全体敌方单位造成5点伤害并有百分之二十的概率混乱敌人', '随地睡着 -> 两回合内无法攻击',
               '狮吼功 -> 对全体敌方单位造成20点伤害并有百分之十的概率使敌人两回合内无法行动', '举铁 -> 下回合攻击提升百分之五十',
               '诱惑の术 -> 使选中敌方单位下回合无法攻击', '葵花点穴手 -> 使选中的敌方单位两回合内无法攻击',
               '念诗之王 -> 使全体敌方混乱两回合', '劈瓜 -> 对选中敌方单位造成20点伤害',
               '三点几啦 -> 回复自身20点HP', '宠物博主 -> 回复全体友方单位10点HP',
               '召唤 -> 召唤两只掉毛厉害的猫对3个随机敌方造成10点伤害', '奥数飞弹 -> 对随机三个敌方单位造成10点伤害',
               '卷 -> 对全体友方单位造成10点伤害', '投喂 -> 回复选中友方单位20点HP',
               '龙吼 -> 对选中敌方单位造成30点伤害', '起飞 -> 下回合无法攻击且不能被攻击',
               '美黑 -> 被动技能，无法被作为目标选中', '没有社交账号 -> 被动技能，受到所有伤害减免10点',
               '飒 -> 被动技能，友方单位攻击时有百分之十概率协战，攻击随机一个敌方单位造成10点伤害', 'holahola -> 使全体友方单位进度条提升百分之三十',
               '写论文 -> 对自身造成10点伤害', '闪光波克尔 -> 对选中敌方单位造成20点伤害，若敌方单位 HP<=20，则为敌方单位剩下1点HP',
               'Kono Dio Da -> 对选中敌方单位造成10点 emotional damage', '掉线 -> 两回合内无法攻击',
               '英雄不朽 -> 复活选中己方阵亡单位', '呀哈哈，再见！-> 回复选中友方单位10点HP',
               '23时已到 -> 宿舍断网，立刻退出本场战斗且不能被复活', '疯狂钻石 -> 回复选中单位30点HP',
               '龙卷风摧毁停车场 -> 对全体敌方单位造成10点伤害', '代餐 -> 回复自身5点HP，持续三回合',
               'cpbe -> 对选中敌方单位造成5点伤害，持续3回合', '力巴尔的勇猛 -> 被动技能，每到自身回合使全体友方单位进度条提升百分之十',
               '力量快劈 -> 被动技能，所有攻击造成的伤害+10','蜂巢之血 -> 被动技能，每回合结束回复自身5点HP',
               '六眼 -> 无法行动直到战斗结束', '多余的情感 -> 使自己混乱两回合',
               '居合气刃拔刀斩 -> 若到下次行动前受到伤害，则免疫第一次伤害并自动反击，造成20点伤害',
               '多重宇宙 -> 对自己造成5点伤害，下回合获得一个随机技能',
               '圆舞棍 -> 旋转战矛，持矛突进直刺敌人，并将其抓取摔翻，造成10点伤害，可破除霸体状态，强制倒地，受身无效。',
               '老烟枪 -> 对在场全体单位造成5点伤害','三段斩 -> 进行三次攻击，每次造成5点伤害',
               '恰似那台机器脉冲的颤跳 -> 下回合免疫所有伤害','Good hunting -> 下回合攻击提升百分之五十',
               '不要牧师 -> 下回合在场所有单位不可使用治疗技能', 'CSDN -> 回复自身5点HP']

# 抽卡牌等级 - card_rate
flag = random.randint(1, 100)
if 0 < flag < 11:
    card_rate = rate_list[0]
elif 20 < flag < 61:
    card_rate = rate_list[1]
else:
    card_rate = rate_list[2]

# 生成技能 - skill_string
if card_rate == 'SSR':
    skill1 = random.randint(0, len(skills_list)-1)
    while True:
        skill2 = random.randint(0, len(skills_list)-1)
        if skill2 != skill1:
            break
    while True:
        skill3 = random.randint(0, len(skills_list)-1)
        if skill3 != skill2 and skill3 != skill1:
            break
    skill_string = "技能1：" + skills_list[skill1] + '\n' + \
        "技能2：" + skills_list[skill2] + '\n' + \
        "技能3：" + skills_list[skill3]
    hp = random.randint(7, 10)
elif card_rate == 'SR':
    skill1 = random.randint(0, len(skills_list)-1)
    while True:
        skill2 = random.randint(0, len(skills_list)-1)
        if skill2 != skill1:
            break
    skill_string = "技能1：" + skills_list[skill1] + '\n' + \
        "技能2：" + skills_list[skill2]
    hp = random.randint(4, 6)
else:
    skill1 = random.randint(0, len(skills_list)-1)
    skill_string = "技能1：" + skills_list[skill1]
    hp = random.randint(1, 3)


person1 = split_content(content)

return_string = "姓名：" + person1 + '\n' + \
                "稀有度：" + card_rate + '\n' + \
    "HP：" + str(hp*10) + '\n' + \
    skill_string

print(return_string)
