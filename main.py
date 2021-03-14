import sys
import os
from os import listdir, path
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QProcess
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()

        self.p = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.assign_widgets()

        self.base_dir = os.getcwd() + '\\'
        self.input_dir = ''
        self.output_dir = ''

        self.thumbnail_suffix = ''

        self.gifs = []

        self.gif2webp_args = []

        self.gif2webp = os.getcwd() + '\\gif2webp.exe'
        self.webpmux = os.getcwd() + '\\webpmux.exe'

        if path.isfile('gif2webp.exe') and path.isfile('webpmux.exe'):
            self.ui.lbl_webpinstallwarning.setText('')

    def start_process(self, program, args):
        if self.p == None:
            self.p = QProcess(self)
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)
            self.p.start(program, args)

    def output_message(self, m):
        self.ui.txt_convertlog.append(str(m))

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode('utf-8')
        self.output_message(stdout)
    
    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode('utf-8')
        self.output_message(stderr)
    
    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not Running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.output_message(state_name)

    def process_finished(self):
        self.output_message('Process finished')
        self.p = None

    def assign_widgets(self):
        self.ui.btn_selectdir.clicked.connect(self.set_input_dir)
        self.ui.btn_selectoutputdir.clicked.connect(self.set_output_dir)
        self.ui.btn_convert.clicked.connect(self.convert_gifs)
        self.ui.chb_makethumbs.stateChanged.connect(self.enable_thumb_text)

        #self.ui.cmb_compressionmode.
    def set_input_dir(self):
        os.chdir(str(QFileDialog.getExistingDirectory(self, 'Select Directory')))

        self.ui.txt_workingdir.setText(os.getcwd())
        self.input_dir = os.getcwd()
        
        if self.ui.txt_outputdir.toPlainText() == '':
            self.ui.txt_outputdir.setText(os.getcwd())
            self.output_dir = os.getcwd()

        path = os.getcwd()
        
        self.gifs.clear()

        for f in listdir(path):
            if f.endswith('.gif'):
                self.gifs.append(f)
        
        self.ui.txt_dircontents.setEnabled(True)
        self.ui.txt_dircontents.clear()

        self.ui.lbl_gifcount.setText(str(len(self.gifs)))

        self.enable_widgets()

        for f in self.gifs:
            self.ui.txt_dircontents.append(f)
        
        print('self.gifs output:', self.gifs)
        print(self.base_dir)
        

    def enable_widgets(self):
        self.ui.txt_convertlog.setEnabled(True)
        #There must be a way to group widgets and enable/disable easier. But for now...
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

    def enable_thumb_text(self):
        if self.ui.chb_makethumbs.isChecked():
            self.ui.txt_thumbsuffix.setEnabled(True)
        else:
            self.ui.txt_thumbsuffix.setEnabled(False)
    
    def enable_lossy(self, b):
        if b == True:
            self.ui.lbl_lossyfiltering.setEnabled(True)
            self.ui.txt_lossyfiltering.setEnabled(True)
        else:
            self.ui.lbl_lossyfiltering.setEnabled(False)
            self.ui.txt_lossyfiltering.setEnabled(False)

    def set_output_dir(self):
        self.output_dir = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        self.output_dir = os.path.normpath(self.output_dir)
        self.ui.txt_outputdir.setText(self.output_dir)
        print('Output dir set to', self.output_dir)
    
    def convert_gifs(self):
        #Enable the progress bar and the conversion log
        self.ui.txt_convertlog.setEnabled(True)
        self.ui.progressBar.setEnabled(True)

        #self.gif2webp_args.append(self.gif2webp)

        if self.ui.cmb_compressionmode.currentText() == 'Lossy':
            print('Lossy')
            self.gif2webp_args.append('-lossy')
            self.gif2webp_args.append('-f')
            self.gif2webp_args.append(f' {self.ui.txt_lossyfiltering.toPlainText()}')

        elif self.ui.cmb_compressionmode.currentText() == 'Mixed':
            print('Mixed')
            self.gif2webp_args.append('-mixed')

        self.gif2webp_args.append('-q')
        self.gif2webp_args.append(f' {self.ui.txt_quality.toPlainText()}')
        #if self.ui.
        print('Args so far:', self.gif2webp_args)
        print(self.gif2webp)

        if self.ui.chb_makethumbs.isChecked():
            print('Do thumbnail processing!')

        print('Processing!')

        final_args = []
        progress = 0
        total_progress = len(self.gifs)

        for gif in self.gifs:
            final_args.clear()
            final_args.extend(self.gif2webp_args)

            thumb_name = self.output_dir + '\\' + gif[:-4] + self.ui.txt_thumbsuffix.toPlainText() + '.webp'
            webp = self.output_dir + '\\' + gif[:-3] + 'webp'
            gif = self.input_dir + '\\' + gif

            final_args.extend(['-v', gif, '-o', webp])
            print(final_args)
            
            self.start_process(self.gif2webp, final_args)
            self.p.waitForFinished()

            if self.ui.chb_makethumbs.isChecked():
                self.start_process(self.webpmux, ['-get', 'frame', '1', webp, '-o', thumb_name])
                self.p.waitForFinished()

            progress += 1
            self.ui.progressBar.setValue(int(100 * float(progress)/float(total_progress)))
            #subprocess.run(final_args)

        self.gif2webp_args.clear()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())