# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(642, 681)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_selectdir = QPushButton(self.centralwidget)
        self.btn_selectdir.setObjectName(u"btn_selectdir")
        self.btn_selectdir.setGeometry(QRect(560, 20, 75, 26))
        self.txt_workingdir = QTextBrowser(self.centralwidget)
        self.txt_workingdir.setObjectName(u"txt_workingdir")
        self.txt_workingdir.setGeometry(QRect(10, 20, 541, 26))
        self.txt_workingdir.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_workingdir.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_workingdir.setLineWrapMode(QTextEdit.NoWrap)
        self.txt_dircontents = QTextBrowser(self.centralwidget)
        self.txt_dircontents.setObjectName(u"txt_dircontents")
        self.txt_dircontents.setEnabled(False)
        self.txt_dircontents.setGeometry(QRect(10, 120, 351, 231))
        self.lbl_dircontents = QLabel(self.centralwidget)
        self.lbl_dircontents.setObjectName(u"lbl_dircontents")
        self.lbl_dircontents.setGeometry(QRect(10, 100, 61, 16))
        self.txt_thumbsuffix = QTextEdit(self.centralwidget)
        self.txt_thumbsuffix.setObjectName(u"txt_thumbsuffix")
        self.txt_thumbsuffix.setEnabled(False)
        self.txt_thumbsuffix.setGeometry(QRect(500, 290, 130, 26))
        self.chb_makethumbs = QCheckBox(self.centralwidget)
        self.chb_makethumbs.setObjectName(u"chb_makethumbs")
        self.chb_makethumbs.setEnabled(False)
        self.chb_makethumbs.setGeometry(QRect(380, 260, 121, 26))
        self.lbl_thumbsuffix = QLabel(self.centralwidget)
        self.lbl_thumbsuffix.setObjectName(u"lbl_thumbsuffix")
        self.lbl_thumbsuffix.setEnabled(False)
        self.lbl_thumbsuffix.setGeometry(QRect(400, 290, 101, 26))
        self.lbl_inputdir = QLabel(self.centralwidget)
        self.lbl_inputdir.setObjectName(u"lbl_inputdir")
        self.lbl_inputdir.setGeometry(QRect(10, 0, 121, 16))
        self.btn_selectoutputdir = QPushButton(self.centralwidget)
        self.btn_selectoutputdir.setObjectName(u"btn_selectoutputdir")
        self.btn_selectoutputdir.setEnabled(False)
        self.btn_selectoutputdir.setGeometry(QRect(560, 70, 75, 26))
        self.lbl_outputdir = QLabel(self.centralwidget)
        self.lbl_outputdir.setObjectName(u"lbl_outputdir")
        self.lbl_outputdir.setGeometry(QRect(10, 50, 121, 16))
        self.txt_outputdir = QTextBrowser(self.centralwidget)
        self.txt_outputdir.setObjectName(u"txt_outputdir")
        self.txt_outputdir.setEnabled(False)
        self.txt_outputdir.setGeometry(QRect(10, 70, 541, 26))
        self.txt_outputdir.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_outputdir.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_outputdir.setLineWrapMode(QTextEdit.NoWrap)
        self.lbl_webpinstallwarning = QLabel(self.centralwidget)
        self.lbl_webpinstallwarning.setObjectName(u"lbl_webpinstallwarning")
        self.lbl_webpinstallwarning.setGeometry(QRect(100, 610, 481, 20))
        font = QFont()
        font.setBold(True)
        self.lbl_webpinstallwarning.setFont(font)
        self.lbl_webpinstallwarning.setAlignment(Qt.AlignCenter)
        self.lbl_gifcount = QLabel(self.centralwidget)
        self.lbl_gifcount.setObjectName(u"lbl_gifcount")
        self.lbl_gifcount.setGeometry(QRect(70, 100, 81, 16))
        self.chb_deletegifs = QCheckBox(self.centralwidget)
        self.chb_deletegifs.setObjectName(u"chb_deletegifs")
        self.chb_deletegifs.setEnabled(False)
        self.chb_deletegifs.setGeometry(QRect(380, 320, 121, 26))
        self.lbl_quality = QLabel(self.centralwidget)
        self.lbl_quality.setObjectName(u"lbl_quality")
        self.lbl_quality.setEnabled(False)
        self.lbl_quality.setGeometry(QRect(380, 200, 101, 26))
        self.txt_quality = QTextEdit(self.centralwidget)
        self.txt_quality.setObjectName(u"txt_quality")
        self.txt_quality.setEnabled(False)
        self.txt_quality.setGeometry(QRect(500, 200, 131, 26))
        self.cmb_compressionmode = QComboBox(self.centralwidget)
        self.cmb_compressionmode.addItem("")
        self.cmb_compressionmode.addItem("")
        self.cmb_compressionmode.addItem("")
        self.cmb_compressionmode.setObjectName(u"cmb_compressionmode")
        self.cmb_compressionmode.setEnabled(False)
        self.cmb_compressionmode.setGeometry(QRect(500, 120, 131, 26))
        self.lbl_compressionmode = QLabel(self.centralwidget)
        self.lbl_compressionmode.setObjectName(u"lbl_compressionmode")
        self.lbl_compressionmode.setEnabled(False)
        self.lbl_compressionmode.setGeometry(QRect(380, 120, 111, 26))
        self.chb_minsize = QCheckBox(self.centralwidget)
        self.chb_minsize.setObjectName(u"chb_minsize")
        self.chb_minsize.setEnabled(False)
        self.chb_minsize.setGeometry(QRect(380, 230, 121, 26))
        self.txt_lossyfiltering = QTextEdit(self.centralwidget)
        self.txt_lossyfiltering.setObjectName(u"txt_lossyfiltering")
        self.txt_lossyfiltering.setEnabled(False)
        self.txt_lossyfiltering.setGeometry(QRect(500, 160, 131, 26))
        self.lbl_lossyfiltering = QLabel(self.centralwidget)
        self.lbl_lossyfiltering.setObjectName(u"lbl_lossyfiltering")
        self.lbl_lossyfiltering.setEnabled(False)
        self.lbl_lossyfiltering.setGeometry(QRect(400, 160, 101, 26))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QRect(10, 410, 631, 23))
        self.progressBar.setValue(0)
        self.btn_convert = QPushButton(self.centralwidget)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setEnabled(False)
        self.btn_convert.setGeometry(QRect(260, 370, 130, 26))
        self.txt_convertlog = QTextBrowser(self.centralwidget)
        self.txt_convertlog.setObjectName(u"txt_convertlog")
        self.txt_convertlog.setEnabled(False)
        self.txt_convertlog.setGeometry(QRect(10, 450, 621, 151))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 642, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WebP Batch Converter", None))
        self.btn_selectdir.setText(QCoreApplication.translate("MainWindow", u"Open Dir", None))
        self.txt_workingdir.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a directory to open ----&gt;</p></body></html>", None))
        self.txt_dircontents.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No directory selected</p></body></html>", None))
        self.lbl_dircontents.setText(QCoreApplication.translate("MainWindow", u"Gifs In Dir:", None))
        self.txt_thumbsuffix.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">_thumb</p></body></html>", None))
        self.chb_makethumbs.setText(QCoreApplication.translate("MainWindow", u"Make Thumbnails", None))
        self.lbl_thumbsuffix.setText(QCoreApplication.translate("MainWindow", u"Thumbnail Suffix:", None))
        self.lbl_inputdir.setText(QCoreApplication.translate("MainWindow", u"Input Directory:", None))
        self.btn_selectoutputdir.setText(QCoreApplication.translate("MainWindow", u"Open Dir", None))
        self.lbl_outputdir.setText(QCoreApplication.translate("MainWindow", u"Output Directory:", None))
        self.txt_outputdir.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lbl_webpinstallwarning.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">WARNING: WEBP executibles are not found in installation dir!</span></p></body></html>", None))
        self.lbl_gifcount.setText("")
        self.chb_deletegifs.setText(QCoreApplication.translate("MainWindow", u"Delete input gifs", None))
        self.lbl_quality.setText(QCoreApplication.translate("MainWindow", u"Quality  (1-100):", None))
        self.txt_quality.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>", None))
        self.cmb_compressionmode.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.cmb_compressionmode.setItemText(1, QCoreApplication.translate("MainWindow", u"Lossy", None))
        self.cmb_compressionmode.setItemText(2, QCoreApplication.translate("MainWindow", u"Mixed", None))

        self.lbl_compressionmode.setText(QCoreApplication.translate("MainWindow", u"Compression Mode:", None))
        self.chb_minsize.setText(QCoreApplication.translate("MainWindow", u"Min Size", None))
        self.txt_lossyfiltering.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>", None))
        self.lbl_lossyfiltering.setText(QCoreApplication.translate("MainWindow", u"Lossy Filtering:", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"Convert Directory!", None))
        self.txt_convertlog.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

