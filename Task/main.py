import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
#import GridWidgets
import Table

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Task Manager -PyQt5"
        self.left = 100
        self.top = 200
        self.width = 600
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon("C:\\git\\TaskManagerPyQT\\task_manager_image.png"))

        # Lets start with Basic Menu Bar Creation
        # mainMenu = self.menuBar()
        # fileMenu = mainMenu.addMenu('File')
        # editMenu = mainMenu.addMenu('Edit')
        # viewMenu = mainMenu.addMenu('View')
        # searchMenu = mainMenu.addMenu('Search')
        # toolsMenu = mainMenu.addMenu('Tools')
        # helpMenu = mainMenu.addMenu('Help')

        # Add box layout, add table to box layout and add box layout to widget
        windowlayout = QVBoxLayout()
        windowlayout.addWidget(Table.App())
        self.setLayout(windowlayout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Application()
    sys.exit(app.exec_())
