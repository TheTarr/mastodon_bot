# from bs4 import BeautifulSoup
# import requests

# url = 'http://baodian123.com/gou/'

# def get_content(url):
#     content_data=requests.get(url)
#     #下面这句话去掉则乱码，加上则正常显示，编码格式gb2312是根据网页源代码中设置的编码格式来指定的  
#     content_data.encoding='utf-8'
#     soup=BeautifulSoup(content_data.text,"html.parser")
#     content=soup.find_all('li')
#     for i in content:
#         print(i.get_text())
#     return content[0].get_text()

# get_content(url)



# f = open('pet_kind.txt','r',encoding='utf-8')
# alll = f.readlines()
# for i in alll:
#     if i != '\n':
#         flag = 0
#         temp = 0
#         for j in i:
#             if j =='）':
#                 flag = temp
#                 break
#             temp +=1
#         print(i[flag+1:-1])

# 返回菜谱
import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

animal_txt_path = 'pet_kind.txt'
animal_txt_len = 313
color_txt_path = 'color.txt'
color_txt_len = 628

color=linecache.getline(color_txt_path, random.randint(0,color_txt_len-1))
flag = 0
for i in range(0,len(color)):
    if color[i] == '#':
        flag = i
        break
    if color[i] == ' ':
        flag = i
        break
# print(flag)
color = color[:flag]
# print(color)
if color[len(color)-1]!='色':
    color += '色'

animal=linecache.getline(animal_txt_path, random.randint(0,animal_txt_len-1))
x = random.randint(0,2)
if x == 0:
    gen = '他'
elif x == 1:
    gen = '她'
else:
    gen = '祂'

print('在旅行的途中，你遇到了眼睛是'+color+'的'+animal[:-1]+'！你们一起度过了愉快的时光。分别时，'+gen+'问你要不要签订契约，成为'+gen+'的赛博宠物！')