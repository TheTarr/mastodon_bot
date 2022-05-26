import sys
import random
import os
import io
import linecache
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'address'
total_n = 169
files =  os.listdir(path)

country = random.randint(0,total_n-1)

count = len(open(path + '/' + files[country],'r', encoding = 'utf-8').readlines())
# print(count)
if count == 1:
    content=linecache.getline(path + '/' + files[country], 1)
    print(files[country][:-4] + ' -> ' + content)
else:
    i = random.randint(1,count-1)
    # print(i)
    content=linecache.getline(path + '/' + files[country], i)
    print(files[country][:-4] + ' -> ' + content)