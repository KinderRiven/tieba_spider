#encoding=utf-8
import urllib2

#Item class
#init  传入
#url 网页地址
#headers 请求报头
#encoding 返回编码
#parse 根据网站url获得网站源代码
class Item:
    def __init__(self, url, headers, encoding = 'utf-8'):
        self.url = url
        self.headers = headers
        self.encoding = encoding

    def parse(self):
        request = urllib2.Request(self.url, headers=self.headers)
        response = urllib2.urlopen(request)
        self.html = response.read()
        return self.html

    def download(self, path):
        request = urllib2.Request(self.url, headers=self.headers)
        data = urllib2.urlopen(request).read()
        f = file(path, "wb")
        f.write(data)
        f.close()
        return True

'''
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}

Item("http://imgsrc.baidu.com/forum/pic/item/9e12e350352ac65c6dd77c2ffcf2b21192138a35.jpg"
     ,headers=headers).download("H:/1.jpg")
'''