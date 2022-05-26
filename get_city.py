#引入开发包
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import os

# def mkdir(path):
 
# 	folder = os.path.exists(path)
 
# 	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
# 		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
# 		print("ok")
 
# 	else:
# 		print("noy ok")
		

# #请求URL并把结果用UTF-8编码
# resp=urlopen("https://zh.wikipedia.org/wiki/%E5%90%84%E5%9C%8B%E5%9F%8E%E5%B8%82%E5%88%97%E8%A1%A8").read().decode("utf-8")
# #使用BeautifulSoup去解析
# soup=BeautifulSoup(resp,"html.parser")
# #print(soup)
# #获取所有以/wiki/开头的a标签的href属性
# listUrl=soup.findAll("a",href=re.compile("^/wiki/"))

# path = '/address'
# files =  os.listdir(path)
# print(files)

# #输出所有词条对应的名称和URL
# for link in listUrl:
#     if not re.search("\.(jpg|JPG)$",link["href"]):
#     #   file = "/address/" + link.get_text()
#     #   mkdir(file)
#       if link.get_text() in files:
#         print(link.get_text(),"<----->","https://zh.wikipedia.org"+link["href"])
#         #请求URL并把结果用UTF-8编码
#         try:
#             resp1=urlopen("https://zh.wikipedia.org"+link["href"] + "%E5%9F%8E%E5%B8%82%E5%88%97%E8%A1%A8").read().decode("utf-8")
#             #使用BeautifulSoup去解析
#             soup1=BeautifulSoup(resp1,"html.parser")
#             #print(soup)
#             #获取所有以/wiki/开头的a标签的href属性
#             listUrl1=soup1.findAll("a",href=re.compile("^/wiki/"))

#             f = open("/address/" + link.get_text() + '.txt','w', encoding='UTF-8')
#             for link in listUrl1:
#                 if not re.search("\.(jpg|JPG)$",link["href"]):  
#                     word_1 = link.get_text()
#                     res = True
#                     for w in word_1:
#                         if not '\u4e00' <= w <= '\u9fff':
#                             res = False
#                     if res == True:
#                         f.write(link.get_text())
#                         f.write('\n')
#             f.close()
#         except:
#             print(link.get_text() + "没有这个此条！")





import os


# def del_zhou(txt_name):

#     ml=["区","州",'县','省','语','族','教','區']
#     f = open("/address/未处理/" + txt_name,'r', encoding='UTF-8')
#     for i in f.readlines():
#         if i == '\n':
#             continue
#         flag = 0
#         for j in i:
#             if j in ml:
#                 flag = 1
#         if flag ==0:
#             if i[-1:] == '\n':
#                 print(i[:-1])
#             else:
#                 print(i)

# def chachong(txt_name):
#     f = open("/address/未处理/" + txt_name,'r', encoding='UTF-8')
#     ms = set()
#     flag = 0
#     for i in f.readlines():
#         if i in ms:
#             flag +=1
#         else:
#             if i[-1:] == '\n':
#                 print(i[:-1])
#             else:
#                 print(i)
#             ms.add(i)


# def process(txt_name):

#     ml=["区","州",'县','省','语','族','教','區','語','政','府']
#     ms = set()
#     a=0

#     f = open("/address/未处理/" + txt_name,'r', encoding='UTF-8')
#     for i in f.readlines():
#         if i == '\n':
#             continue
#         if i == '查\n':
#             break
#         flag = 0
#         for j in i:
#             if j in ml:
#                 flag = 1
#         if flag ==0:
#             if i in ms:
#                 a +=1
#             else:
#                 if i[-1:] == '\n':
#                     print(i[:-1])
#                 else:
#                     print(i)
#                 ms.add(i)

# # del_zhou("比利時.txt", "區")
# # chachong("比利時.txt")
# # process("冰島.txt")

# path = '/address/未处理'
# files =  os.listdir(path)
# files.sort()
# files.reverse()
# print(files)

# for i in files:
#     print("【【【【" + i + '】】】】\n')
#     process(i)
#     r = input()

path = 'address'
files =  os.listdir(path)
print(files)
total = 0
for i in files:
    count = len(open(path + '/' + i,'r', encoding = 'utf-8').readlines())
    total += count
print(total)