import time
from datetime import datetime
import pytz


t = 'poem/'+ datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y_%m_%d_%H_%M_%S')+'.txt'
print(t)    # ==> 2017-12-05 18:39:45 CST+0800

wri = datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y/%m/%d - %H')+' 时'
print(wri)
