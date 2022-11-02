import sys
import random
import io
import json
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'diaoyu.json'
n=61

with open('diaoyu.json', 'r',encoding='utf-8') as fcc_file:
    data = json.load(fcc_file)
    fcc_file.close()

all_data = [] 
for v, w in data.items(): 
  temp = [] 
  for i in range(w[0]): 
   temp.append(v) 
  all_data.extend(temp) 
    
n = random.randint(0,len(all_data)-1) 
fish = all_data[n]

#海草 绿藻 白藻 龙虾 小龙虾 螃蟹 鸟蛤 蚌 虾 蜗牛 玉黍螺 牡蛎

data[fish][1]+=1

with open("diaoyu.json","w",encoding='utf-8') as f:
    json.dump(data,f)

return_string+='恭喜您钓到了 '
return_string+=fish
return_string+=' ！在联邦宇宙，大家一共钓起了 '
return_string+=str(data[fish][1])
return_string+=' 条'
return_string+=fish
return_string+='！'



print(return_string)




# for v, w in data.items(): 
#   if w[0]==4:
#     print(v+'--多见')
#   elif w[0]==3:
#     print(v+'--一般')
#   elif w[0]==2:
#     print(v+'--罕见')
#   else:
#     print(v+'--非常罕见')


with open('diaoyu.json', 'r',encoding='utf-8') as fcc_file:
    data = json.load(fcc_file)
    fcc_file.close()

i = 0
for v, w in data.items(): 
  i+=w[1]

print(i)