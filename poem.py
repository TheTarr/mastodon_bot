# 收到关键词诗，返回一首诗
# import requests
# from bs4 import BeautifulSoup
import sys
import random
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

# 美国服务器无法连接www.chinapoesy.com，改为使用本地数据集。数据集是：https://github.com/sheepzh/poetry/tree/master/data
# # 以下两个参数用来爬诗词网站，若出问题请更换
# randpage = random.randint(1,82)
# url = "http://www.chinapoesy.com/XianDaiList_" + str(randpage) + ".html"

# res = requests.get(url)
# soup = BeautifulSoup(res.text, "html.parser")

# all_a = soup.find_all('a', class_ = "Green")
# # 第40-100是页面的随机，非推荐
# poem_flag = random.randint(40, len(all_a))
# poem_url = all_a[poem_flag]["href"]


# # print(poem_url)
# res2 = requests.get("http://www.chinapoesy.com/"+ poem_url)
# soup2 = BeautifulSoup(res2.text, "html.parser")

# poem_body = soup2.find_all(class_ = "HeightBorderCenter")

# return_string = ''
# for i in poem_body:
#     return_string += i.get_text()

return_string = ''
path = 'data'
files =  os.listdir(path)

# 随机一个诗人文件夹
poemer = files[random.randint(0,len(files)-1)]
# print(poemer)

# 取出诗人名字:poemer[:flag]
flag = 0
for i in range(0,len(poemer)-1):
    if poemer[i]=='_':
        flag = i
# print(return_string)

# 取出一首诗
files =  os.listdir(path+'/'+poemer)
poem = files[random.randint(0,len(files)-1)]
# print(poem)

f = open(path+'/'+poemer+'/'+poem,"r",encoding='UTF-8')   #设置文件对象
content = f.readlines()
f.close() #关闭文件
# print(content[0][6:])
# print(content[1][5:])

return_string = content[0][6:] + poemer[:flag] + ' ' + content[1][5:] + '\n '
for i in range(2,len(content)):
    return_string += content[i]

print(return_string)