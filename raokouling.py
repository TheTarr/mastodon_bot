import sys
import random
import os
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'raokouling'
total_n = 249
files =  os.listdir(path)

country = random.randint(0,total_n-1)

count = open(path + '/' + files[country],'r', encoding = 'utf-8').readlines()
# print(count)
ms = '咳咳！\n\n'
for i in count:
    if i == '\n':
        continue
    else:
        ms+=i
print(ms)


# from bs4 import BeautifulSoup
# import requests
# import sys
# import random
# import io
# import os
# import re
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

# path = 'http://rkl.intowz.com'
# # main = '/wap/html2/rkl.html'

# # url = path+main


# # res = requests.get(url)
# # res = res.text.encode('iso-8859-1').decode('gbk')

# # soup = BeautifulSoup(res, "html.parser")

# # all_a = soup.find_all("a",href=re.compile("/wap/"))
# # # test_dict = {}
# # for i in range (0,400):
# #     print(all_a[i].get_text())
# #     print(all_a[i]['href'])
# #     with open("temp.txt","a",encoding='utf-8') as f:
# #         f.write(all_a[i].get_text() + '%' + all_a[i]['href']+'\n')
# #     # test_dict = {}



# # test_dict = {'bigberg': 'url1'}
# # print(test_dict)
# # print(type(test_dict))
# # #dumps 将数据转换成字符串
# # json_str = json.dumps(test_dict)
# # print(json_str)
# # print(type(json_str))
# # new_dict = json.loads(json_str)

# # with open("temp.json","w") as f:
# #     json.dump(new_dict,f)
# #     print("加载入文件完成...")

# f = open("temp.txt","r",encoding='utf-8')
# lines = f.readlines()
# folder = 'raokouling/'
# for i in lines:
#     flag = 0
#     for j in range(0,len(i)):
#         if i[j] == '%':
#             flag = j
#     name = i[:flag]
#     print(i[flag+1:])
#     res = requests.get(path+i[flag+1:-1])
#     # res = requests.get(path+'/wap/html/z5598m8528j373.html')
#     res = res.text.encode('iso-8859-1').decode('gbk')
#     soup = BeautifulSoup(res, "html.parser")
#     r = soup.find('div',class_ = 'zmj_body4')
#     f = open(folder+name,'w',encoding='utf-8')
#     f.write(r.text)
# # folder = 'raokouling/'
# # name = '标兵'
# # res = requests.get(path+'/wap/html/z5598m8528j373.html')
# # res = res.text.encode('iso-8859-1').decode('gbk')
# # soup = BeautifulSoup(res, "html.parser")
# # r = soup.find('div',class_ = 'zmj_body4')
# # # detials=soup.select('div')[0].text
# # print(r.text)

# # f = open(folder+name,'w',encoding='utf-8')
# # f.write(r.text)