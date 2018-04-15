#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from datetime import datetime

import sys
import time
import os

import TabView

from DB_manager import tableModelQtsqlTry
from DBessai import *


# To incorporate UI_view_SARAA inherit QDialog, and UI_view
class MainDialog(QDialog, TabView.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        # appel de la classe du module dbessai
        self.LaBase = LaBase()
        self.model = QSqlTableModel()
        query = QSqlQuery()
        query.prepare("SELECT datetime1, datetime2 FROM Contact1")
        query.exec_()

        self.model = QStandardItemModel(0,3)
        # self.model.setHeaderData((0, Qt.Horizontal("pilot_1")))
        # self.model.setHeaderData((1,Qt.Horizontal,("datetime1")))
        # self.model.setHeaderData((2,Qt.Horizontal,("datetime2")))

        while query.next():
            NewRow = []
            age = query.value(0)
            newcolumn = QStandardItem("age")
            NewRow.append(newcolumn)
            height = query.value(1)
            newcolumn = QStandardItem("height")
            NewRow.append(newcolumn)
            newcolumn = QStandardItem("My Ratio")

            self.model.appendRow(NewRow)
            self.tableView.setModel(self.model)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)

        # create and display splash screen

        splash_pix = QPixmap('Logo_armee.png')

        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)
        # add progress bar
        progressBar = QProgressBar(splash)
        progressBar.setMaximum(10)
        progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)

        splash.show()
        splash.showMessage("<h1><font color='black'>----Bienvenue dans Moise!----</font></h1>",
                           Qt.AlignTop | Qt.AlignCenter, Qt.black)

        for i in range(1, 11):
            progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                app.processEvents()
        # simulating
        time.sleep(1)
        form = MainDialog()
        form.show()
        splash.finish(form)
        app.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window....")
    except Exception:
        print(sys.exc_info()[1])



