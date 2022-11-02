# 以下是读取列表形态
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from unicodedata import normalize

# table_MN = pd.read_html('https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%AF%B4%E7%94%9F%E7%89%A9%E5%88%97%E8%A1%A8')

# print(f'Total tables: {len(table_MN)}')


# for i in range(1,21):
#     df = table_MN[i]
#     for j in df['中文']:
#         print(j)

# f=open('yaoguai.txt','r',encoding='utf-8')
# r = f.readlines()
# f.close()
# for j in r:
#     if j != "nan":
#         print(j)

#引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#请求URL并把结果用UTF-8编码
resp=urlopen("https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%AF%B4%E7%94%9F%E7%89%A9%E5%88%97%E8%A1%A8").read().decode("utf-8")
#使用BeautifulSoup去解析
soup=BeautifulSoup(resp,"html.parser")
#print(soup)
#获取所有以/wiki/开头的a标签的href属性
listUrl=soup.findAll("a",href=re.compile("^/wiki/"))
for i in listUrl:
    print(i.string)