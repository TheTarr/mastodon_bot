import sys
import random
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

flag = random.randint(0,3)
path = 'pokemon.txt'
total_n = 909

f = open(path,"r",encoding='UTF-8')   #设置文件对象
i = random.randint(1,total_n)
content=linecache.getline(path, i)
f.close() #关闭文件

if flag == 0:
    print('抓捕失败！' + content[:-1] + ' 逃掉了')
elif flag == 1:
    print("抓捕失败！反而被 " + content[:-1] + ' 给抓到了')
else:
    print("抓捕成功！抓到了 " + content[:-1])

# 以下为爬取名字
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# response = urlopen("https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89")
# html = response.read()
# data = html.decode('utf-8')
# soup = BeautifulSoup(data)
# # print soup.findAll('span')

# # 去掉属性名
# ml = ['草','毒','火','飞行','水','虫','一般','恶','电','超能力','地面','冰','钢','妖精','格斗','岩石','幽灵','龙','惡','属性','图像','鋼','蟲','格鬥','電','龍','飛行','幽靈']

# f = open('pokemon.txt','w',encoding='utf-8')
# for item in soup.find_all("a"):
#     if item.string == None:
#         continue
#     else:
#         print(item.string)
#         if item.string not in ml:
#             f.write(item.string+'\n')
# f.close()


# 以下为查重
# readDir = "pokemon.txt"
# writeDir = "pokemon_new.txt"
# outfile=open(writeDir,"w",encoding='utf-8')
# f = open(readDir,"r",encoding='utf-8')
 
# lines_seen = set()  # Build an unordered collection of unique elements.
 
# for line in f:
#     line = line.strip('\n')
#     if line not in lines_seen:
#         outfile.write(line+ '\n')
#         lines_seen.add(line)