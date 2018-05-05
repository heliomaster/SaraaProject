from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from datetime import datetime,timedelta

import sys
import time
import os

import TabView
import TabView2
import Dialogu_3



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
        #appel de class pour qdialogu2
        self.enter_new_AC.clicked.connect(self.afficher_classe2)
        self.dialog = Dialogu2(self)

        #appel de classe pour dialogu3
        self.enter_new_pilot.clicked.connect(self.afficher_classe3)
        self.dialogu3 = Dialogu_3(self)



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
        query1 = QSqlQuery("SELECT datetime1,datetime2 FROM Contact1")
        liste=[]
        while query1.next():
            date1 = query1.value(0)
            date2 = query1.value(1)
            essai = datetime.strptime(date2, "%d-%m-%Y %H:%M") - datetime.strptime(date1, "%d-%m-%Y %H:%M")
            liste.append(essai)
        total = sum(liste, timedelta())
        return total

    def hours_minutes(self):
        td = self.get_date_diff()
        resultat = td.days * 24 + td.seconds // 3600
        return resultat

    def afficher_classe2(self):
        self.dialog.show()

    def afficher_classe3(self):
        self.dialogu3.show()


    @pyqtSlot()
    def on_calculer_clicked(self):
        str(self.get_date_diff)

    @pyqtSlot()
    def on_insert_data_clicked(self):
        self.setdata()
        self.lineEdit_heures_total.setText(str(self.hours_minutes()))


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
            ''''# 2nd column is our virtual column.
            # if we are there, we need to calculate and return the value
            # we take the first two columns, get the data, turn it to integer and sum them
            # [0] at the end is necessary because pyqt returns value and a bool
            # http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qvariant.html#toInt'''
            date2 = self.data(self.index(index.row(),3))
            date1 = self.data(self.index(index.row(),2))

            #premiere facon sans variable
            date2B = datetime.strptime(self.data(self.index(index.row(),3)), "%Y-%m-%d %H:%M")
            #deuzieme facon avec variable(plus lisible)
            date1B = datetime.strptime(date1, "%Y-%m-%d %H:%M")
            return str(date2B - date1B)

            #return datetime.strptime(date2, "%Y-%m-%d %H:%M")
            #return self.data(self.index(index.row(),3)) + self.data(self.index(index.row(),2))
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

#Fenetre modal


class Dialogu2(QDialog,TabView2.Ui_insertDialogu):
    """Opens Dialogu box to insert New Aircraft in database"""
    def __init__(self,parent = None):
        super(Dialogu2,self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.setdata_aircraft)
        self.model = Model()

    def setdata_aircraft(self):
        query =QSqlQuery()
        query.prepare("INSERT INTO Aircraft(immatriculation,type_ac,puissance)" "VALUES(?,?,?)")
        query.bindValue(0,self.lineEdit.text())
        query.bindValue(1,self.lineEdit_2.text())
        query.bindValue(2,self.lineEdit_3.text())
        query.exec_()
        self.model.select()


class Dialogu_3(QDialog,Dialogu_3.Ui_Dialog):
    """Opens Dialogu box to insert new pilot in database"""
    def __init__(self,parent= None):
        super(Dialogu_3,self).__init__(parent)
        self.setupUi(self)
        self.buttonBox_Ok_pilot.clicked.connect(self.setdata_pilot)
        self.model = Model()

    def setdata_pilot(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO Pilot(rank,first_name, last_name)" "VALUES (?,?,?)")
        query.bindValue(0,self.comboBox_grade.currentText())
        query.bindValue(1,self.lineEdit_2.text())
        query.bindValue(2,self.lineEdit_3.text())
        query.exec_()
        self.model.select()








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
