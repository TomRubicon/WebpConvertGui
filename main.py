import sys
import os
import subprocess
from os import listdir, path
from os.path import isfile, join
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.assign_widgets()

        self.input_dir = ''
        self.output_dir = ''

        self.thumbnail_suffix = ''

        self.gifs = []

        self.gif2webp_args = []

        self.gif2webp = 'gif2webp.exe'
        self.webpmux = 'webpmux.exe'

        if path.isfile('gif2webp.exe') and path.isfile('webpmux.exe'):
            self.ui.lbl_webpinstallwarning.setText('')


    def assign_widgets(self):
        self.ui.btn_selectdir.clicked.connect(self.set_input_dir)
        self.ui.btn_selectoutputdir.clicked.connect(self.set_output_dir)
        self.ui.btn_convert.clicked.connect(self.convert_gifs)
    
    def set_input_dir(self):
        os.chdir(str(QFileDialog.getExistingDirectory(self, 'Select Directory')))

        self.ui.txt_workingdir.setText(os.getcwd())
        
        self.ui.txt_outputdir.setText(os.getcwd())
        self.output_dir = os.getcwd()

        path = os.getcwd()
        
        for f in listdir(path):
            if f.endswith('.gif'):
                self.gifs.append(f)
        
        self.ui.txt_dircontents.setEnabled(True)
        self.ui.txt_dircontents.setText('')

        self.ui.lbl_gifcount.setText(str(len(self.gifs)))

        self.enable_widgets()

        for f in self.gifs:
            self.ui.txt_dircontents.append(f)
        
        print('self.gifs output:', self.gifs)

    def enable_widgets(self):
        self.ui.txt_outputdir.setEnabled(True)
        self.ui.btn_selectoutputdir.setEnabled(True)

        self.ui.btn_convert.setEnabled(True)
        #Labels
        self.ui.lbl_compressionmode.setEnabled(True)
        self.ui.lbl_lossyfiltering.setEnabled(True)
        self.ui.lbl_quality.setEnabled(True)
        #Check Boxes
        self.ui.chb_minsize.setEnabled(True)
        self.ui.chb_makethumbs.setEnabled(True)
        self.ui.chb_deletegifs.setEnabled(True)
        #Combo box
        self.ui.cmb_compressionmode.setEnabled(True)
        #Text boxes
        self.ui.txt_lossyfiltering.setEnabled(True)
        self.ui.txt_quality.setEnabled(True)

    def set_output_dir(self):
        self.output_dir = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        self.output_dir = os.path.normpath(self.output_dir)
        self.ui.txt_outputdir.setText(self.output_dir)
        print('Output dir set to', self.output_dir)
    
    def convert_gifs(self):
        self.ui.txt_convertlog.setEnabled(True)
        self.ui.progressBar.setEnabled(True)
        print(self.ui.chb_makethumbs.isChecked())
        print('Processing!')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())