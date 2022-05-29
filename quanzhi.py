import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

mylist = ['枪手系 - 枪炮师', '枪手系 - 神枪手', '枪手系 - 弹药专家', '圣职系 - 驱魔师',
          '剑士系 - 剑客', '暗夜系 - 术士', '剑士系 - 鬼剑士', '格斗系 - 气功师',
          '圣职系 - 牧师', '圣职系 - 守护天使', '格斗系 - 拳法家', '法师系 - 战斗法师',
          '暗夜系 - 忍者', '暗夜系 - 刺客', '法师系 - 魔道学者', '剑士系 - 狂剑士',
          '枪手系 - 机械师', '法师系 - 元素法师', '剑士系 - 魔剑士', '暗夜系 - 盗贼',
          '格斗系 - 流氓', '法师系 - 召唤师', '格斗系 - 柔道', '圣职系 - 骑士',
          '未转职 - 散人！！']
mylist2 = ['蓝溪阁','中草堂','霸气雄图','嘉王朝','轮回','百花谷','踏破虚空','兴欣','义斩天下','呼啸山庄','雷霆','烟雨楼']

# 保证两个AU不重合
flag1 = random.randint(0, len(mylist)-1)
flag2 = random.randint(0, len(mylist2)-1)
print("是"+ mylist2[flag2]+"公会的："+ mylist[flag1])
