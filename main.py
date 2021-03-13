import sys
from glob import glob
import os
from os import listdir
from os.path import isfile, join
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.assign_widgets()

    def assign_widgets(self):
        self.ui.btn_selectdir.clicked.connect(self.set_dir)
        self.ui.btn_selectoutputdir.clicked.connect(self.set_output_dir)
    
    def set_dir(self):
        os.chdir(str(QFileDialog.getExistingDirectory(self, 'Select Directory')))
        self.ui.txt_workingdir.setText(os.getcwd())
        self.ui.txt_outputdir.setEnabled(True)
        self.ui.btn_selectoutputdir.setEnabled(True)
        self.ui.txt_outputdir.setText(os.getcwd())

        path = os.getcwd()
        files = []
        
        for f in os.listdir(path):
            if f.endswith('.gif'):
                files.append(f)
        
        self.ui.txt_dircontents.setEnabled(True)
        self.ui.txt_dircontents.setText('')

        self.ui.lbl_gifcount.setText(str(len(files)))

        for f in files:
            self.ui.txt_dircontents.append(f)
    
    def set_output_dir(self):
        set_dir = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        set_dir = os.path.normpath(set_dir)
        self.ui.txt_outputdir.setText(set_dir)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())