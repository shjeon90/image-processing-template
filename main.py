import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from IpToolbar import IpToolbar
from IpMenubar import IpMenubar
from IpImagePanel import *

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.img = None
        self.path_img = None

        self.init_ui()

    def init_ui(self):
        self.imagePanel = IpImagePanel(self)

        self.menubar = IpMenubar(self, self.imagePanel)
        self.setMenuBar(self.menubar)

        self.toolbar = IpToolbar(self, self.imagePanel)
        self.addToolBar(self.toolbar)

        self.setCentralWidget(self.imagePanel)

        self.setWindowTitle('Image processing')
        self.showMaximized()


def main():
    app = QApplication(sys.argv)
    my_app = MyApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()