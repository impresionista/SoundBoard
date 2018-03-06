import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

 
class MainWindow(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'SoundBoard'
        self.left = 20
        self.top = 20
        self.width = 800
        self.height = 600
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())