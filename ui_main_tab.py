"""MOÏSE : MOYEN OPERATIONNEL D'INFORMATION ET DE SOUTIEN  DES EQUIPAGES"""

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
        self.model.setHeaderData(4, Qt.Horizontal, "pax1")
        self.model.setHeaderData(5, Qt.Horizontal, "pax2")
        self.model.setHeaderData(6, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(7, Qt.Horizontal, "datetime2")
        self.model.setHeaderData(8, Qt.Horizontal, "Mission")
        self.model.setHeaderData(9, Qt.Horizontal, "Observations")
        self.model.setHeaderData(10, Qt.Horizontal, "total")
        self.tableView.setModel(self.model)
        self.tableView.setSortingEnabled(True)
        self.tableView.resizeColumnsToContents()
        self.tableView.setColumnHidden(0, True)

        # setting table in table_2
        self.tableView_2.setModel(self.model)
        self.tableView_2.setSortingEnabled(True)
        self.tableView_2.resizeColumnsToContents()
        self.tableView_2.setColumnHidden(0, True)

        #setting table_view 3

        self.tableView_3.setModel(self.model)
        self.tableView_3.setSortingEnabled(True)
        self.tableView_3.resizeColumnsToContents()
        self.tableView_3.setColumnHidden(0, True)

        # call to moncuq class with edit resize columns
        self.mydata = Moncuq()
        self.tableView_limites.setModel(self.mydata)
        self.tableView_limites.resizeColumnsToContents()
        self.tableView_limites.setColumnHidden(0, True)
        self.tableView.selectAll()

        ###########  RELATION MODEL################
        aircraftType = self.model.fieldIndex('aircraft')
        self.model.setRelation(aircraftType, QSqlRelation("Aircraft", "immatriculation", "immatriculation"))
        pilot_type_cdb = self.model.fieldIndex('CDB')
        self.model.setRelation(pilot_type_cdb,QSqlRelation("Pilot","last_name","last_name"))
        pilot_type_fo = self.model.fieldIndex('Copi')
        self.model.setRelation(pilot_type_fo,QSqlRelation("Pilot","last_name","last_name"))


        # #self.comboBox_avion.setModel(self.model)
        # # self.comboBox_avion.setItemDelegate(QSqlRelationalDelegate(self.comboBox_avion))
        # relModel = self.model.relationModel(aircraftType)
        # #self.comboBox_avion.setModel(relModel)
        # #self.comboBox_avion.setModelColumn(relModel.fieldIndex('immatriculation'))
        #
        # self.comboBox_sel_ac.setModel(relModel)
        # self.comboBox_sel_ac.setModelColumn(relModel.fieldIndex('immatriculation'))
        # print(self.comboBox_sel_ac.setModelColumn(relModel.fieldIndex('immatriculation')))



        #Filling combox _avion

        query_aircraft = QSqlQuery("SELECT immatriculation FROM Aircraft")
        liste_ac = []
        while query_aircraft.next():
            aircraft = query_aircraft.value(0)
            liste_ac.append(aircraft)
        self.comboBox_avion.addItems(liste_ac)
        self.comboBox_sel_ac.addItems(liste_ac)


        # Filling combox pilot
        # todo: set relation sql
        query_pilot = QSqlQuery("SELECT last_name FROM Pilot")
        liste = []
        while query_pilot.next():
            pilot1 = query_pilot.value(0)
            liste.append(pilot1)
        self.comboBox_pilot1.addItems(liste)
        self.comboBox_pilot2.addItems(liste)
        self.comboBox_pilote.addItems(liste)
        self.comboBox_pilote2.addItems(liste)


        # appel de class pour qdialogu2
        self.enter_new_AC.clicked.connect(self.afficher_classe2)
        self.dialog = Dialogu2(self)

        # appel de classe pour dialogu3
        self.enter_new_pilot.clicked.connect(self.afficher_classe3)
        self.dialogu3 = Dialogu_3(self)


    #
    #     self.comboBox_avion.activated.connect(self.mapper1())
    #
    # def mapper1(self):
    #     mapper = QDataWidgetMapper()
    #     self.model.setTable("Aircract")
    #     mapper.setModel(self.model)
    #     mapper.setItemDelegate(QSqlRelationalDelegate())
    #     mapper.addMapping(self.comboBox_avion, 1)
    #     self.model.select()

    # @pyqtSlot()
    # def on_comboBox_avion_currentIndexChanged(self):
    #     self.mapper1()
    #     print("marche")



    def setdata(self):
        query = QSqlQuery()
        query.prepare(
            "INSERT INTO Mission (cdb,copi,aircraft,datetime1,datetime2,pax1,pax2,mission,observations,total)" "VALUES (?,?,?,?,?,?,?,?,?,?)")
        query.bindValue(0, self.comboBox_pilot1.currentText())
        query.bindValue(1, self.comboBox_pilot2.currentText())
        query.bindValue(2, self.comboBox_avion.currentText())
        query.bindValue(3, self.dateTimeEdit.text())
        query.bindValue(4, self.dateTimeEdit_2.text())
        query.bindValue(5, self.lineEdit_pax1.text())
        query.bindValue(6, self.lineEdit_pax2.text())
        query.bindValue(7, self.lineEdit_mission.text())
        query.bindValue(8, self.lineEdit_observations.text())
        query.bindValue(9, str(self.get_date_diff()))
        query.exec_()
        self.model.select()

    @pyqtSlot()
    def on_insert_data_clicked(self):
        self.setdata()
        self.lineEdit_heures_total.setText(str(self.hours_minutes()))

    def setdata_limites_table(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO Limites(pilot,cempn,vsa,license) " "VALUES  (?,?,?,?)")
        query.bindValue(0, self.lineEdit_lim_pilot.text())
        query.bindValue(1, self.dateEdit_lim_cempn.text())
        query.bindValue(2, self.dateEdit_lim_vsa.text())
        query.bindValue(3, self.dateEdit_lim_vsa.text())
        query.exec_()
        self.mydata.select()

    @pyqtSlot()
    def on_pushButton_lim_inserer_clicked(self):
        self.setdata_limites_table()

    #########  SETTING QUERIES ON TABLEVIEW3#################

    def query_date_time(self):
        self.model.setTable("Mission")
        combodate_1 = self.dateEdit.text()
        combodate_2 = self.dateEdit_2.text()
        filter = "cast(datetime1 as datetime)between cast('{}' as datetime) and cast('{}' as datetime)".format(
            combodate_1, combodate_2)
        self.model.setFilter(filter)
        self.model.select()

    # @pyqtSlot()
    # def on_calculer_clicked(self):
    #     print("marche")
    #     #self.query_date_time()





    #######remove row   lim     #########

    def remove_row_lim(self):
        index = self.tableView_limites.currentIndex()
        deleteconf = QMessageBox.critical(self.parent(), "DELETE ROW", "REALLY DELETE", QMessageBox.Yes,
                                          QMessageBox.No)
        if deleteconf == QMessageBox.Yes:
            self.mydata.removeRow(index.row())
            self.mydata.submitAll()
            self.mydata.select()
            return
        else:
            return

    @pyqtSlot()
    def on_pushButton_lim_supprimer_clicked(self):
        self.remove_row_lim()

    ############################

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

    @pyqtSlot()
    def on_Effacer_clicked(self):
        self.remove_row()

    ##############################

    #TODO:  write remove method for row aircraft and pilot


    ############### HOURS DATETIME DIFF#################
    def get_date_diff(self):
        """select dates from database to display on tableView_3"""
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
        """conversion of time delta get_date_diff to hours"""
        td = self.get_date_diff()
        resultat = td.days * 24 + td.seconds // 3600
        return resultat

    @pyqtSlot()
    def on_calculer_clicked(self):
        self.lineEdit_heures_total.setText(str(self.hours_minutes()))
        #self.query_date_time()



    #########################################

    def afficher_classe2(self):
        self.dialog.show()

    def afficher_classe3(self):
        self.dialogu3.show()

    ################### PRINTER ########################
    def my_printer(self):
        """sets printer to PDF report for hours"""
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

    def text_view(self):
        self.my_printer()

    @pyqtSlot()
    def on_pushButton_imprimer_clicked(self):
        self.text_view()


class Moncuq(QSqlRelationalTableModel, TabView.Ui_Dialog):
    """Class to display Limites Table and color and implement method DATA to override
    otherwise Model table would be selected"""

    def __init__(self, parent=None):
        super(Moncuq, self).__init__(parent)
        self.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
        self.setTable("Limites")
        self.select()
        self.now = datetime.now().date()
        # print(self.now)
        # print(type(self.now))

    def data(self, item, role):
        if role == Qt.BackgroundRole:
            if item.column() == 2 or item.column()== 3 or item.column() == 4:
                raw_format = QSqlQueryModel.data(self, item,Qt.DisplayRole)
                formated_date = datetime.strptime(raw_format,"%Y-%m-%d").date()
                return QBrush(Qt.red) if formated_date < self.now else False
        return QSqlQueryModel.data(self, item, role)

    ################# A CONVERVER EXEMPLE DISPLAY ROLE#############################
    # def data(self, item, role):
    #     if role == Qt.BackgroundRole:
    #         if QSqlQueryModel.data(self, self.index(item.row(), 2), Qt.DisplayRole) == "Young":
    #             return QBrush(Qt.yellow)
    #     if role == Qt.DisplayRole:
    #         if item.column() == 3:
    #             return True if QSqlQueryModel.data(self, item, Qt.DisplayRole) == 1 else False
    #     return QSqlQueryModel.data(self, item, role)

    ###################################################################################

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


############### Fenetres modal


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
