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
        self.model = Model()
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

class Model(QSqlTableModel):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.setEditStrategy(QSqlTableModel.OnFieldChange)

        self.setTable("Contact")
        self.select()

    def columnCount(self, parent=QModelIndex()):
        # this is probably obvious
        # since we are adding a virtual column, we need one more column
        return super(Model, self).columnCount() + 1

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and index.column() == 4:
            # 2nd column is our virtual column.
            # if we are there, we need to calculate and return the value
            # we take the first two columns, get the data, turn it to integer and sum them
            # [0] at the end is necessary because pyqt returns value and a bool
            # http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qvariant.html#toInt
            return self.data(self.index(index.row(),0)) - self.data(self.index(index.row(),0))
            #return  sum(self.data(self.index(index.row(), i)).toInt()[0] for i in range(2))
        if index.column() > 4:
            # if we are past 2nd column, we need to shift it to left by one
            # to get the real value
            index = self.index(index.row(), index.column() - 1)
        # get the value from base implementation
        return super(Model, self).data(index, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # this is similar to `data`
        if section == 4 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return 'Sum'
        if section > 4 and orientation == Qt.Horizontal:
            section -= 1
        return super(Model, self).headerData(section, orientation, role)

    def flags(self, index):
        # since 2nd column is virtual, it doesn't make sense for it to be Editable
        # other columns can be Editable (default for QSqlTableModel)
        if index.column() == 4:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def setData(self, index, data, role):
        # similar to data.
        # we need to be careful when setting data (after edit)
        # if column is after 2, it is actually the column before that
        if index.column() > 4:
            index = self.index(index.row(), index.column() - 1)
        return super(Model, self).setData(index, data, role)
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
