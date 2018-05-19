from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from datetime import datetime, timedelta
from PyQt5 import QtWebEngineCore, QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5 import QtPrintSupport

import sys
import time
import os

import TabView
import TabView2
import Dialogu_3

from DB_manager import tableModelQtsqlTry
from DBessai import *
############################################################

# To incorporate UI_view_SARAA inherit QDialog, and UI_view
class MainDialog(QDialog, TabView.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        # appel de la classe du module dbessai
        self.LaBase = LaBase()
        # setting MainDialogu to Model class => Override of current class(Class now qsqlrelationalmodel
        self.model = Model()
        self.model.setTable("Mission")
        self.model.setEditStrategy(QSqlRelationalTableModel.OnRowChange)
        self.model.select()

        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "CDB")
        self.model.setHeaderData(2, Qt.Horizontal, "Copi")
        self.model.setHeaderData(3, Qt.Horizontal, "Avion")
        self.model.setHeaderData(4, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(5, Qt.Horizontal, "datetime2")
        self.model.setHeaderData(6, Qt.Horizontal, "pax1")
        self.model.setHeaderData(7, Qt.Horizontal, "pax2")
        self.model.setHeaderData(8, Qt.Horizontal, "Mission")
        self.model.setHeaderData(9, Qt.Horizontal, "Observations")
        self.model.setHeaderData(10, Qt.Horizontal, "total")
        self.tableView.setModel(self.model)
        self.tableView.setSortingEnabled(True)
       # self.create_limit_table()

        self.mydata = Moncuq()
        self.tableView_limites.setModel(self.mydata)



        #
        # '''Relationaltablemodel: The setRelation() function calls establish a relationship between two tables.
        #  The first call specifies that column 1 in table Mission is a foreign key that maps with field id of table Pilot
        # and that the view should present the last_name's name field to the user. The second call does something similar
        # with column 2'''

        # self.model.setRelation(1, QSqlRelation("Pilot", "id", 'last_name'))
        # self.model.setRelation(2, QSqlRelation("Pilot", "id", 'last_name'))
        # self.model.setRelation(3, QSqlRelation("Aircraft", "id", "immatriculation"))
        #
        # # Not necessary just to make reading clearer could use Int
        # aircraft_type = self.model.fieldIndex("aircraft")
        # # display custom combobox
        # relmodel = self.model.relationModel(aircraft_type)
        # self.comboBox_avion.setModel(relmodel)
        # self.comboBox_avion.setModelColumn(relmodel.fieldIndex("immatriculation"))
        # mapper = QDataWidgetMapper()
        # mapper.setModel(self.model)
        # mapper.setItemDelegate(QSqlRelationalDelegate(self.comboBox_avion))
        # mapper.addMapping(self.comboBox_avion, aircraft_type)

        # travail sur relation model
        aircraftType = self.model.fieldIndex('aircraft')
        self.model.setRelation(aircraftType,QSqlRelation("Aircraft","id","immatriculation"))
        #self.tableView1.setItemDelegate(QSqlRelationalDelegate(self.tableView1))
        relModel = self.model.relationModel(aircraftType)
        self.comboBox_avion.setModel(relModel)
        self.comboBox_avion.setModelColumn(relModel.fieldIndex('immatriculation'))
        mapper = QDataWidgetMapper()
        mapper.setModel(self.model)
        mapper.setItemDelegate(QSqlRelationalDelegate())
        mapper.addMapping(self.comboBox_avion,aircraftType)
        self.model.select()



        # appel de class pour qdialogu2
        self.enter_new_AC.clicked.connect(self.afficher_classe2)
        self.dialog = Dialogu2(self)

        # appel de classe pour dialogu3
        self.enter_new_pilot.clicked.connect(self.afficher_classe3)
        self.dialogu3 = Dialogu_3(self)
        # Filling combox pilot

        query_pilot = QSqlQuery("SELECT last_name FROM Pilot")
        liste = []
        while query_pilot.next():
            pilot1 = query_pilot.value(0)
            liste.append(pilot1)
        self.comboBox_pilot1.addItems(liste)
        self.comboBox_pilot2.addItems(liste)

        # filling combobox AVEC TABLE VIEW
        # self.query_pilot.setQuery()
        # self.query_pilot.setHeaderData(0,Qt.Horizontal,"id")
        # self.query_pilot.setHeaderData(0,Qt.Horizontal,"PILOTE COMMANDANT DE BORD")
        # view = QTableView()
        # self.comboBox_pilot1.setModel(self.query_pilot)
        # self.comboBox_pilot1.setView(view)

    def setdata(self):
        query = QSqlQuery()
        query.prepare(
            "INSERT INTO Mission (cdb,copi,aircraft,datetime1,datetime2,pax1,pax2,mission,observations,total)" "VALUES (?,?,?,?,?,?,?,?,?,?)")
        query.bindValue(0, self.comboBox_pilot1.currentText())
        query.bindValue(1, self.comboBox_pilot2.currentText())
        query.bindValue(2, self.comboBox_avion.currentIndex())
        query.bindValue(3, self.dateTimeEdit.text())
        query.bindValue(4, self.dateTimeEdit_2.text())
        query.bindValue(5, self.lineEdit_pax1.text())
        query.bindValue(6, self.lineEdit_pax2.text())
        query.bindValue(7, self.lineEdit_mission.text())
        query.bindValue(8, self.lineEdit_observations.text())
        query.bindValue(9, str(self.get_date_diff()))
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
        query1 = QSqlQuery("SELECT datetime1,datetime2 FROM Mission")
        liste = []
        while query1.next():
            date1 = query1.value(0)
            date2 = query1.value(1)
            essai = datetime.strptime(date2, "%Y-%m-%d %H:%M") - datetime.strptime(date1, "%Y-%m-%d %H:%M")
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

    def text_view(self):
        self.my_printer()

    @pyqtSlot()
    def on_pushButton_imprimer_clicked(self):
        self.text_view()

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

    def my_printer(self):
        with open('document.html', 'r') as file:
            content = file.read()
            print(content)
            print(type(content))
        name = "marc morgand"
        # self.textEdit.setText("<address> le puit morgand <de la motte des bois<br> 18000 BOURGES</address><div>esssaii </div> <br><b>sdsfqslkjqslkdjqd qsdqksjd</b><br> {}".format(self.dateEdit.text()))
        self.doc = QTextDocument()
        self.doc.setDefaultStyleSheet("body{color : red}")
        # self.doc.setHtml("<body><p> TRY 123 {} </p></body>".format(name))
        self.doc.setHtml("{} ".format(content).format(name))

        self.textEdit.setDocument(self.doc)
        self.printer = QtPrintSupport.QPrinter()
        self.printer.setPageSize(QtPrintSupport.QPrinter.A4)
        self.printer.setOutputFormat(QtPrintSupport.QPrinter.NativeFormat)
        # self.printer.setOutputFileName('pdffile')
        dialog = QtPrintSupport.QPrintDialog(self.printer)
        if dialog.exec_():
            self.doc.print_(self.printer)

class Moncuq(QSqlRelationalTableModel,TabView.Ui_Dialog):

    def __init__(self, parent=None):
        super(Moncuq, self).__init__(parent)
        self.setEditStrategy(QSqlRelationalTableModel.OnRowChange)
        self.setTable("Limites")
        self.select()



        # def create_limit_table(self):
        #     """Setting Table for Limits"""

        # model = QSqlRelationalTableModel()
        # self.setTable("Limites")
        # self.select()
        # self.tableView_limites.setModel()





        # tableviewmodel = QSqlQueryModel()
        #
        #
        # tableviewmodel.setQuery("SELECT * FROM Limites")
        # tableviewmodel.setHeaderData(0,Qt.Horizontal,"PILOTES")
        # tableviewmodel.setHeaderData(1, Qt.Horizontal, "CEMPN")
        # tableviewmodel.setHeaderData(2, Qt.Horizontal, "VSA")
        # tableviewmodel.setHeaderData(3, Qt.Horizontal, "LICENSE")
        #
        # self.tableView_limites.setModel(tableviewmodel)
        # self.tableView_limites.setSortingEnabled(True)
        # self.tableView_limites.resizeColumnsToContents()
        # self.tableView_limites.setAlternatingRowColors(True)




# class SubClassTableModel(QSqlRelationalTableModel):
#     def __init__(self,parent=None):
#         super(SubClassTableModel).__init__(parent)
#
#     def data(self, QModelIndex,role=Qt.DisplayRole):
#         if role == Qt.BackgroundColorRole:
#
#             self.data(self.index(Qt.DisplayRole))
#             return QColor(Qt.red)







class Model(QSqlRelationalTableModel):
    """Virtual column overiding base class datetime 1 and 2 substraction"""

    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.setEditStrategy(QSqlRelationalTableModel.OnRowChange)

        self.setTable("Mission")
        self.select()

    def columnCount(self, parent=QModelIndex()):
        # this is probably obvious
        # since we are adding a virtual column, we need one more column
        return super(Model, self).columnCount() + 1

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and index.column() == 8:
            ''''# 2nd column is our virtual column.
            # if we are there, we need to calculate and return the value
            # we take the first two columns, get the data, turn it to integer and sum them
            # [0] at the end is necessary because pyqt returns value and a bool
            # http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qvariant.html#toInt'''
            # date2 = self.data(self.index(index.row(),4))
            date1 = self.data(self.index(index.row(), 6))

            # premiere facon sans variable
            date2B = datetime.strptime(self.data(self.index(index.row(), 7)), "%Y-%m-%d %H:%M")
            # deuzieme facon avec variable(plus lisible)
            date1B = datetime.strptime(date1, "%Y-%m-%d %H:%M")
            return str(date2B - date1B)

            # return datetime.strptime(date2, "%Y-%m-%d %H:%M")
            # return self.data(self.index(index.row(),3)) + self.data(self.index(index.row(),2))
            # return  sum(self.data(self.index(index.row(), i)).toInt()[0] for i in range(2))
        if index.column() > 8:
            # if we are past 2nd column, we need to shift it to left by one
            # to get the real value
            index = self.index(index.row(), index.column() - 1)
        # get the value from base implementation
        return super(Model, self).data(index, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # this is similar to `data`
        if section == 8 and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return 'Sum'
        if section > 8 and orientation == Qt.Horizontal:
            section -= 1
        return super(Model, self).headerData(section, orientation, role)

    def flags(self, index):
        # since 2nd column is virtual, it doesn't make sense for it to be Editable
        # other columns can be Editable (default for QSqlTableModel)
        if index.column() == 8:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def setData(self, index, data, role):
        # similar to data.
        # we need to be careful when setting data (after edit)
        # if column is after 2, it is actually the column before that
        if index.column() > 8:
            index = self.index(index.row(), index.column() - 1)
        return super(Model, self).setData(index, data, role)


# Fenetre modal


class Dialogu2(QDialog, TabView2.Ui_insertDialogu):
    """Opens Dialogu box to insert New Aircraft in database"""

    def __init__(self, parent=None):
        super(Dialogu2, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.setdata_aircraft)
        self.model = Model()

    def setdata_aircraft(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO Aircraft(immatriculation,type_ac,puissance)" "VALUES(?,?,?)")
        query.bindValue(0, self.lineEdit.text())
        query.bindValue(1, self.lineEdit_2.text())
        query.bindValue(2, self.lineEdit_3.text())
        query.exec_()
        self.model.select()


class Dialogu_3(QDialog, Dialogu_3.Ui_Dialog):
    """Opens Dialogu box to insert new pilot in database"""

    def __init__(self, parent=None):
        super(Dialogu_3, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox_Ok_pilot.clicked.connect(self.setdata_pilot)
        self.model = Model()

    def setdata_pilot(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO Pilot(rank,first_name, last_name)" "VALUES (?,?,?)")
        query.bindValue(0, self.comboBox_grade.currentText())
        query.bindValue(1, self.lineEdit_2.text())
        query.bindValue(2, self.lineEdit_3.text())
        query.exec_()
        self.model.select()


# class htmlViewer(QtWebEngineWidgets):
#     def __init__(self, parent=None):
#         super(QtWebEngineWidgets).__init__(parent=None)
#
#         self.webview = QtWebEngineWidgets.QWebEngineView()
#         self.template_text = open("htmlFile.html")
#         self.templatate_txt = self.template_text.read()
#         self.webview.setHtml(self.templatate_txt)

#         self.printer= QPrinter(QPrinterInfo.defaultPrinter(), QPrinter.HighResolution)
#
#     def Essai_print(self):
#         a = htmlViewer("http://www.google.fr")
#         QWebEngineView.__init__(self)
#         self.setZoomFactor(1)
#         self.setUrl(QUrl(a))
#         self.printer.setOutputFormat(QPrinter.PdfFormat)
#         self.printer.setOrientation(QPrinter.Portrait)
#         self.printer.setPaperSize(QPrinter.A4)
#         self.printer.setFullPage(True)
#         self.printer.setOutputFileName("printyou.pdf")
#
#         self.loadFinished.connect(self.execpreview)
#
#     def execpreview(self):
#         self.print_(self.printer)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)

        # create and display splash screen

        splash_pix = QPixmap('Logo_armee.png')

        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        # splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
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
