import requests
from my_encode import *

def get_poem(path):
    ml = []
    f = open(path, "r", encoding='UTF-8')   #设置文件对象
    for i in f.readlines():
        h = decrypt_oralce(i[2:])
        ml.append(h.decode())
    f.close() #关闭文件
    return ml

def post_poem(path):
    ms = '\r\n'.join(get_poem(path))
    ms += '\r\n\r\n操！'
    # print(ms)
    data = { "status": ms,
            "visibility": 'public'}
    url = "%s/api/v1/statuses" % 'http://bgme.me'
    r = requests.post(url, 
            data=data, 
            headers={'Authorization': 'Bearer %s' % '你的访问令牌']})
    # json_data = r.json() # you can inspect the json response to check for problems
    # print(json_data)

