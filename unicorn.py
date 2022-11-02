import sys
import random
import io
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
content = sys.argv[1]

def post_message():
    ms = "恭喜 @" + content + " 找到了独角兽！！操！"
    # print(ms)
    data = { "status": ms,
            "visibility": 'public'}
    url = "%s/api/v1/statuses" % 'http://bgme.me'
    r = requests.post(url, 
            data=data, 
            headers={'Authorization': 'Bearer %s' % '你的访问令牌'})

flag = random.randint(1,1000)
if flag == 100:
    print("恭喜你找到了独角兽！！")
    post_message()
else:
    print("很遗憾没有找到独角兽。")
