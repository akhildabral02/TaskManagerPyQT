import sys
from PyQt5.QtWidgets import QApplication,QDialog,QBoxLayout,QPushButton,QCheckBox,QGridLayout,QGroupBox,QVBoxLayout, QWidget,QLabel
from PyQt5.QtGui import QIcon

class GridWidget(QWidget):
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
        self.setWindowIcon(QIcon("C:\\Users\\adabral\\Downloads\\task_manager_image.png"))

        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 2)
        layout.setColumnStretch(2, 2)

        task_status = QLabel()
        task_status.setText("Task Status")
        task_description = QLabel()
        task_description.setText("Task Description")

        layout.addWidget(task_status,0,0)
        layout.addWidget(task_description,0,2)
        layout.addWidget(QPushButton('4'), 1, 0)
        layout.addWidget(QPushButton('5'), 1, 1)
        layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)
        layout.addWidget(QPushButton('8'), 2, 1)
        layout.addWidget(QPushButton('9'), 2, 2)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GridWidget()
    sys.exit(app.exec_())
