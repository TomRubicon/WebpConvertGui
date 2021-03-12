import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.assign_widgets()

    def assign_widgets(self):
        self.ui.pushButton.clicked.connect(self.go_pushed)
    
    def go_pushed(self):
        self.ui.textEdit.append('It Worked')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())