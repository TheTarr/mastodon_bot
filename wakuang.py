import sys
import random
import io
import json
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'wakuang.json'

with open(path, 'r',encoding='utf-8') as fcc_file:
    data = json.load(fcc_file)
    fcc_file.close()
all_data = []

for v, w in data.items(): 
  temp = [] 
  for i in range(w[1]): 
   temp.append(v) 
  all_data.extend(temp)

n = random.randint(0,len(all_data)-1) 
item = all_data[n]

data[item][2]+=1

data['总价'][2]+=data[item][0]

with open(path,"w",encoding='utf-8') as f:
    json.dump(data,f)

return_string+='恭喜您抓到了价值为 '
return_string+=str(data[item][0])
return_string+=' 的 '
return_string+=item
return_string+=' ！在联邦宇宙，大家一共矿了价值 '
return_string+=str(data['总价'][2])
return_string+=' 的工！'



print(return_string)