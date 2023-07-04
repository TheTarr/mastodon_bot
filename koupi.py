import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

ability = [
    'pyon','央','卓','鼓咯','瓦力',
    '库','噫','吉','操','sql','toss','sob',
    'muli','哞','zeb','jazz','hip','huh',
    '亲','呼','啥啊','嗯哼','kira','waye','呜呜',
    'diwu','啾啾','怎么办','是哦','mogu','嗬哟',
    '赋能','对齐','沉淀','解耦','心智',
    'web','protein','落地','汪','喵','噜','惹',
    '噎','牙','寮','姐','bali',
    'nyan','wan','piyo','zun','doko',
    'mofu','guzu','doki','kura','ufufu',
    'hara','piko','ra','rua'
]
flag1 = random.randint(0, len(ability)-1)

print("操操想到的口癖是 " + ability[flag1] + "！怎么样呀" + ability[flag1] + "！")