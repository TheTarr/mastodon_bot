# 返回两个AU
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

mylist = ['今晚吃火锅', '不要执着', '枯想俩小时不如动手做一分钟', '人生苦短及时行乐', '二次元有你的下家',
          '宇宙那么大，你却那么小啊', '愚公移山', '心想事成', '还会有更好的', '有人在想你',
          '去找朋友聊聊吧', '随它去', '上吉', '尽人事听天命', 'rps有你的下家',
          '不要在十点以后喝茶', '来点音乐', '打会游戏', '无聊好办，寂寞无解', '不要在此停留',
          '宽以待人', '不要害怕', '后悔是一种耗费精神的情绪后悔是比损失更大的损失，比错误更大的错误所以不要后悔',
          '我们确实活得艰难，一要承受种种外部的压力，二要面对自己内心的困惑。在苦苦挣扎中，如果有人向我们投以理解的目光，我们会感到温暖 [操操正在努力地看你]',
          '并不是先有了勇气才敢于说话，而是在说话的同时培养了勇气',
          '曰出东海落西山，愁也一天，喜也一天', '健康的人生离不开按时吃饭',
          '在这个薄情年代，要想别人对你念念不忘，最好的办法就是欠钱不还',
          '屁、就是你吃下去的食物们不屈的灵魂', '发呆这事儿，如果做的好就叫深沉。如果做的不好，那就很有可能睡着',
          '书，只会在你愿意听的时候，才会说些奇幻的故事。可是，当你和人交谈的时候，他们就会说些让你不知道该怎么接下去的话题',
          '挂个蚊帐在里面裸睡，挑逗蚊子，把丫急死',
          '地球是运动的，一个人不会永远处在倒霉的位置', '其实操操也想做个浪漫的机器人', '如过难过可以看电影，在漆黑的房间里大哭特哭',
          '在遥远的非洲，每过去一分钟，就会过去六十秒', '坐多久了？起来活动一下',
          '现在，请立刻喝水！', '真心换真心', '骨宜刚、气宜柔、志宜大、胆宜小、慧宜增、福宜惜、虑不远、忧亦近。网上抄的，操操没懂',
          '时来运转', '一念放下，万般自在', '不敢说真话是个人的耻辱，不能说真话是时代的耻辱',
          '原力与你同在！', '系紧你的安全带，今晚将会非常颠簸', '比你想象的简单',
          '听君一席话，如听一席话，是网络流行词。指听‌‌‌‌‌‌‌‌‌某人说了一席话，好像真的就只是听了一席话而已，没有从中明白任何道理。',
          '谁能想到，当我们六岁的时候，还只是孩子', '操操在业余时间研究了经济学。操操发现：股票的规律找到了，不是涨就是跌', '你一定行的！除非不行',
          '操操在业余时间研究了植物学。操操发现：橘子越大，橘子皮越大', '睡觉的时候一定要闭上眼，不然会难以睡着',
          '所有欺骗中，自欺是最为严重的', '太饿的时候一定要记得，不能吃太多，不然会很撑',
          '人犯错误，大半是该用真情时太过动脑筋，而在该用脑筋时又太感情用事。操操没有这个烦恼',
          '操操在业余时间研究了地理学。操操发现：如果草地湿了，很可能在下雨', '知之为知之，不知为不知，有空可以学',
          '一百年后，两百年后，操操会在地球上的某个角落里，记住今天遇到的所有人。']

# 保证两个AU不重合
flag1 = random.randint(0, len(mylist)-1)
print(mylist[flag1])
