import shutil
import time
shutil.copy('poem.txt','poem/'+time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())+'.txt')