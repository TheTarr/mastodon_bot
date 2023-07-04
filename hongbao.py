import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

return_string = ''
path = 'hongbao.txt'

# f = open(path, 'r',encoding='utf-8')
# max = int(f.readline())
# f.close()

flag = random.randint(0,1000)

# 0 - 50 为偷钱
if 0 <= flag <= 50:
    current = random.randint(1, 10)
    return_string = "抱歉！操操调皮了，竟然从您的裤兜里偷走 " + str(current) + " 块钱。"

# 51-750 为 1-200 之间
elif 51 <= flag <= 750:
    current = random.randint(1, 200)
    return_string = "恭喜！您打开操操带来的红包，里面有 " + str(current) + " 块钱。"
    # if current > max:
    #     f = open(path, 'w',encoding='utf-8')
    #     f.write(str(current))
    #     f.close()

# 751 - 965 为 201 - 500
elif 751 <= flag <= 965:
    current = random.randint(201, 500)
    return_string = "恭喜！！您打开操操带来的红包，里面有 " + str(current) + " 块钱。"
    # if current > max:
    #     f = open(path, 'w',encoding='utf-8')
    #     f.write(str(current))
    #     f.close()

# 966 - 996 为 501 - 2000
elif 966 <= flag <= 996:
    current = random.randint(501, 2000)
    return_string = "恭喜！！！您打开操操带来的很厚红包，里面有 " + str(current) + " 块钱。"
    # if current > max:
    #     f = open(path, 'w',encoding='utf-8')
    #     f.write(str(current))
    #     f.close()

# 997 - 1000 为 2001 - 10000000
else:
    current = random.randint(2001, 10000000)
    return_string = "恭喜！！！！！您打开操操带来的巨厚红包，里面有 " + str(current) + " 块钱。"
    # if current > max:
    #     f = open(path, 'w',encoding='utf-8')
    #     f.write(str(current))
    #     f.close()

# return_string+="在您之前的最高记录为 " + str(max) + " 块钱。"



print(return_string)