# 换行输入词语个数，默认为2
import sys
import io
import random
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

content = sys.argv[1]
content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>第一句话<br />0'

# 拆出最后1行的文本，返回
def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[108:]
    my_string = my_string[:-4]

    if my_string[-7:] == '</span>':
        my_string = my_string[:-7]

    # print(my_string)
    i = len(my_string)
    flag4 = 0
    while i != 0:
        i-=1
        if my_string[i] == '>':
            flag4 = i
            break
    if flag4 != 0:
        poem_line = my_string[flag4+1:]
        return(poem_line)
    else:
        return('2')

# path = 'ci.txt'
# total_n = 263309

path = 'ci3.txt'
total_n = 56064

try:
    n = int(split_content(content))
except:
    n = 2

# 最多抽10个词
if n <= 0:
    n = 2
elif n > 10:
    n = 10
ml = []
while n > 0:
    i = random.randint(1,total_n)
    if i not in ml:
        ml.append(i)
    n -= 1

# print(ml)

return_string = ''

cl = []
for x in ml:
    # print(x)
    a = linecache.getline(path, x)
    cl.append(a.strip())
# print(cl)
print('操操为您取的网名是：'+''.join(cl))





# # 准备工作，json转txt方便服务器直接linechache

# import json 
   
# # Opening JSON file 
# f = open('ci.json','r',encoding='utf-8')

# # returns JSON object as  
# # a dictionary 
# data = json.load(f)
   
# # Iterating through the json 
# # list 
# print(len(data))
# wf = open('ci.txt','a',encoding='utf-8')
# for i in range(0,len(data)):
#     if '(' not in data[i]['ci']:
#         wf.write(data[i]['ci']+'\n')
# wf.close()
# # Closing file 
# f.close()