import requests
from bs4 import BeautifulSoup
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

# 以下两个参数用来爬诗词网站，若出问题请更换
randpage = random.randint(1,83)
url = "http://www.chinapoesy.com/XianDaiList_" + str(randpage) + ".html"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

all_a = soup.find_all('a', class_ = "Green")
# 第40-100是页面的随机，非推荐
poem_flag = random.randint(40, len(all_a))
poem_url = all_a[poem_flag]["href"]


# print(poem_url)
res2 = requests.get("http://www.chinapoesy.com/"+ poem_url)
soup2 = BeautifulSoup(res2.text, "html.parser")

poem_body = soup2.find_all(class_ = "HeightBorderCenter")

return_string = ''
for i in poem_body:
    return_string += i.get_text()

print(return_string)