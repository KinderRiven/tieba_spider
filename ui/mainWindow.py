#encoding=utf-8
import sys
from PyQt4 import  QtCore, QtGui
from ui_mainWindow import  Ui_MainWindow
from tieba.Http.Item import Item
from tieba.Tieba.Tieba_Manager import  Tieba_Manager
import time
import thread

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    #准备
    def start_ready(self):
        try:
            self.post_id = int(self.txt_post_id.text())
            self.post_start = int(self.txt_post_start.text())
            self.post_end = int(self.txt_post_end.text())
            return True
        except:
            return False

    #获得图片链接
    def get_img_list(self):
        manager = Tieba_Manager(id=self.post_id, start=self.post_start,
                                      end=self.post_end, headers=headers)
        self.img_list = manager.get_page_img()

    def save_img(self):
        i = 1
        prefix = str(time.time())
        for each in self.img_list:
            Item(url=each, headers=headers).download(self.save_path + "/" + prefix + str(i) + ".jpg")
            i = i + 1

    def img_start(self):
        self.get_img_list()
        self.save_img()

    #开始
    def start(self):
        #self.btn_start.setDisabled(True)
        self.start_ready()
        self.img_start()
        #self.btn_start.setDisabled(False)

    #选择保存的文件夹
    def update_save_path(self):
        print 'update'
        dialog = QtGui.QFileDialog().getExistingDirectory()
        self.save_path = dialog
        self.txt_save_path.setText(self.save_path)

    #初始化
    def __init__( self):
        QtGui.QMainWindow.__init__( self )
        self.setupUi(self)
        self.save_path = ""

app = QtGui.QApplication( sys.argv )
w = MainWindow()
w.show()
app.exec_()