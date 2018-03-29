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
        self.model.setTable("Contact")
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)
        self.model.select()
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "pilot_1")
        self.model.setHeaderData(2, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(3, Qt.Horizontal, "datetime2")
        self.model.setHeaderData(4, Qt.Horizontal, "Calcul")
        self.tableView.setModel(self.model)

    def setdata(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO Contact (pilot_1,datetime1,datetime2,total)" "VALUES (?,?,?,?)")
        query.bindValue(0, self.lineEdit_pilote.text())
        query.bindValue(1, self.dateTimeEdit.text())
        query.bindValue(2, self.dateTimeEdit_2.text())
        query.bindValue(3, str(self.get_date_diff()))
        query.exec_()
        self.model.select()

    def remove_row(self):
        index = self.tableView.currentIndex()
        deleteconf = QMessageBox.critical(self.parent(), "DELETE ROW", "REALLY DELETE", QMessageBox.Yes,
                                          QMessageBox.No)
        if deleteconf == QMessageBox.Yes:
            self.model.removeRow(index.row())
            self.model.submitAll()
            self.model.select()
            return
        else:
            return

    def get_date_diff(self):
        quer = QSqlTableModel(self.model)
        quer.setTable("Contact")
        quer.select()

        i = 0
        while i < quer.rowCount():
            time1 = quer.record(i).value("datetime1")
            time2 = quer.record(i).value("datetime2")
            i += 1
            print(type(time1))
            diff = datetime.strptime(time2, "%Y-%m-%d %H:%M") - datetime.strptime(time1, "%Y-%m-%d %H:%M")
            print(diff)





                #print(diff)

    @pyqtSlot()
    def on_calculer_clicked(self):
        str(self.get_date_diff)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.setdata()

    @pyqtSlot()
    def on_Effacer_clicked(self):
        self.remove_row()


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
