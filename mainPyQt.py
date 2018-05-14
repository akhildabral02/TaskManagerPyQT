import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,600,600)
        self.setWindowTitle("Task Manager")
        self.setWindowIcon(QIcon("C:\\Users\\adabral\\Downloads\\task_manager_image.png"))
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Application()
    sys.exit(app.exec_())
