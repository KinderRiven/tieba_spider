#encoding=utf-8
from tieba.Tieba.Tieba import Tieba
import re
from tieba.Http.Item import Item
import threading
import thread

#####################################
#管理一个帖子的类
#1.获得帖子总页数
#2.进行任务指派，下方给各个子线程进行爬取
#####################################
class Tieba_Manager:

    #初始化
    def __init__(self, headers, encoding='utf-8', id=-1, start=-1, end=-1):
        self.id = id
        self.headers = headers
        self.encoding = 'utf-8'
        self.prefix = "http://tieba.baidu.com/p/" #帖子前缀
        self.start = start
        self.end = end

    #利用正则匹配获得页码
    def get_page_number(self):

        url = self.prefix + str(self.id)
        html = Item(url, headers=self.headers, encoding=self.encoding).parse()
        pattern = re.compile('<span class="red">(.*?)</span>')
        match = pattern.findall(html)
        ret = 0
        if match:
            ret = int(match[0])
        return ret

    #抓取从start - to的页面图片
    def check_start_end(self):
        p_num = self.get_page_number()
        if self.start < 1:
            self.start = 1
        if self.end < 1:
            self.end = 1
        if self.start > p_num:
            self.start = p_num
        if self.end > p_num:
            self.end = p_num

    #建立线程类准备
    def build_thread(self):
        url = self.prefix + str(self.id) + "?pn="
        thread_list = []
        for i in range(self.start, self.end + 1, 1):
            cur = url + str(i)
            thread_list.append(Tieba(url=cur, headers=self.headers))
        return thread_list

    def get_page_img(self):

        #检测起始结束页
        ret = []

        self.check_start_end()
        thread_list = self.build_thread()

        for each in thread_list:
            print "[start]" + each.url + "..."
            each.start()

        for each in thread_list:
            each.join()

        for i in thread_list:
            list = i.o_img
            for j in list:
                ret.append(j)
        return ret


'''
################################# GLOBAL VALUE ################################################

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}

prefix = "http://imgsrc.baidu.com/forum/pic/item/"

################################################################################################

#manager = Tieba_Manager(headers=headers, id=4363942384, encoding="utf-8", start=1, end=10)
#ret = manager.get_page_img()

#for each in ret:
#    print each
'''