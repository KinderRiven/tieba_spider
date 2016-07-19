#encoding=utf-8
from tieba.Http.Item import Item
from tieba.Tieba.Tieba import Tieba
from tieba.Tieba.Tieba_Manager import Tieba_Manager

import time


################################# GLOBAL VALUE ################################################

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}

url = "http://tieba.baidu.com/p/4270494993"
prefix = "http://imgsrc.baidu.com/forum/pic/item/"

################################################################################################

date = time.localtime(time.time())
print str(time.time())