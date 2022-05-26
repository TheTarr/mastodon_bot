# import shutil
# import time
# shutil.copy('poem.txt','poem/'+time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())+'.txt')

import time
f = open("poem.txt", 'w', encoding='UTF-8')
    # f.write(str(encrypt_oracle(time.strftime('%Y/%m/%d - %H', time.localtime())+' 时\n'))+'\n')
f.write(time.strftime('%Y/%m/%d - %H', time.localtime())+' 时\n')
f.close()