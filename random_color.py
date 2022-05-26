import random

ml = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
ms = ''

for i in range(0,6):
    ms+=ml[random.randint(0,15)]
print(ms)