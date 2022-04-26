import requests
from bs4 import BeautifulSoup
import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

num = random.randint(1,4999)
host = 'ao3-cn.top'

try: 
    url = "https://" + host + "/works/search?commit=Search&page=" + str(num) +  "&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=zh&work_search%5Bquery%5D=&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D="
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")
    num_of_article = soup.find_all('h3')[1]

    all_li = soup.find_all('h4', class_ = "heading")
    # print(all_li[2:len(all_li)-5])

    num = random.randint(2,len(all_li)-5)
    my_a = all_li[num].a

    print("泥嚎！这是操操在 ao3 共计 "+ num_of_article.get_text()[:-9] + " 篇中文作品中专门为你找到的：" + my_a.get_text() + " https://" + host + my_a['href'])
except:
    print("目前与 " + host + " 之间通信出现问题！抱歉！")