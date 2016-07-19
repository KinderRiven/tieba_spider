#encoding=utf-8
from bs4 import BeautifulSoup
from tieba.Http.Item import Item
import threading

######################################
#帖子页面处理核心函数(多线程)
#1.根据传入的url获得网页源码
#2.根据网页源代码提取图片地址
#####################################
class Tieba(threading.Thread):

    #初始化
    def __init__(self, url, headers):
        threading.Thread.__init__(self)
        self.url = url
        self.headers = headers
        self.prefix = "http://imgsrc.baidu.com/forum/pic/item/"
        self.img_prefix = "http://imgsrc.baidu.com/forum/"
        self.o_img = []

    #获得网页源码
    def get_html(self):
        self.html = Item(self.url, self.headers).parse()

    #获取图片
    def get_image(self):
        #解析器很重要,使用html.parse
        html = BeautifulSoup(self.html, "html.parser")
        list = html.select("img.BDE_Image")
        ret = []
        for each in list:
            ret.append(each.get("src"))
        return ret

    #增加前缀获得原图
    def deal_image_url(self, url):
        size = len(url)
        new_url = ""
        for i in range(size - 1, -1, -1):
            if url[i] == '/':
                break
            new_url = url[i] + new_url
        return new_url

    def get_original_image(self):
        self.get_html()
        list = self.get_image()
        for each in list:
            if self.img_prefix in each:
                self.o_img.append(self.prefix + self.deal_image_url(each))
        return self.o_img

    #Start线程
    def run(self):
        self.get_original_image()

'''
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}

solver = Tieba(url="http://tieba.baidu.com/p/4363942384?pn=5", headers=headers)
list = solver.get_original_image()
for each in list:
    print each
'''
#print solver.html