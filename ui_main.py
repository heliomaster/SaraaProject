#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from datetime import datetime,timedelta
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

from PyQt5 import QtWebEngineWidgets



import sys
import os

import qtSqlTry
from DB_manager import tableModelQtsqlTry
from DBessai import *


# To incorporate UI_view_SARAA inherit QDialog, and UI_view
class MainDialog(QDialog, qtSqlTry.Ui_Form):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        # appel de la classe du module dbessai
        self.LaBase = LaBase()
        # tablemodel = editable data model
        self.model = QSqlRelationalTableModel()
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)
        #todo: gerer la sauvegarde base de donnée
        #QFileDialog.setFileMode(QFileDialog().AnyFile)
        self.model.setTable("Contact1")

        # travail sur relation model
        aircraftType = self.model.fieldIndex('aircraft')
        self.model.setRelation(aircraftType,QSqlRelation("Aircraft","id","immatriculation"))
        #self.tableView1.setItemDelegate(QSqlRelationalDelegate(self.tableView1))
        relModel = self.model.relationModel(aircraftType)
        self.comboBox.setModel(relModel)
        self.comboBox.setModelColumn(relModel.fieldIndex('immatriculation'))
        mapper = QDataWidgetMapper()
        mapper.setModel(self.model)
        mapper.setItemDelegate(QSqlRelationalDelegate())
        mapper.addMapping(self.comboBox,aircraftType)

        self.model.select()
        self.model.setHeaderData(1, Qt.Horizontal, u"pilot_1")
        self.model.setHeaderData(2, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(3, Qt.Horizontal, "datetime2")
        self.model.setHeaderData(4, Qt.Horizontal, "aircraft")

        # tableview created in qt designer assigned to tablemodel1
        self.tableView1.setModel(self.model)
        self.tableView1.resizeColumnsToContents()
        self.tableView1.setColumnHidden(0,True)
        self.label_total.setText(str(self.hours_minutes()))

        # self.fourqueux = Fourqeux()
        self.proxymodel()

    ###########Proxymodel#################################
    def proxymodel(self):

        self.proxymodel = QSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.model)
        self.proxymodel.setDynamicSortFilter(True)
        self.proxymodel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxymodel.setFilterKeyColumn(-1)
        #self.proxymodel.setFilterFixedString("azerty")

        self.tableView2.setModel(self.proxymodel)
        self.tableView2.setAlternatingRowColors(True)

        self.lineEdit.textChanged.connect(self.proxymodel.setFilterFixedString)


    # @pyqtSlot()
    # def on_lineEdit_textChanged(self):
    #     print("marche")





    def filter_table(self):
        combodate = self.dateEdit.text()
        combodate_2 = self.dateEdit_2.text()
        filter = "cast(datetime1 as datetime)between cast('{}' as datetime) and cast('{}' as datetime)".format(
            combodate, combodate_2)

    def filterAcceptsRow(self, sourceRow, sourceParent):
        index0 = self.sourceModel().index(sourceRow, 0, sourceParent)
        index1 = self.sourceModel().index(sourceRow, 1, sourceParent)
        index2 = self.sourceModel().index(sourceRow, 2, sourceParent)

    def dateInRange(self, date):
        return (self.minDate.isValid() or date > self.minDate) and (self.maxDate.isValid() or date <self.maxDate)

    def setFilterMinimumDate(self, date):
        self.minDate = date
        self.invalidateFilter()

    def setFilterMaximumDate(self, date):
        self.maxDate = date
        self.invalidateFilter()

    @pyqtSlot()
    def on_pushButton_filter_clicked(self):
        self.filter_table()



        # tableview created in qt designer assigned to tablemodel2
        # self.tableView2.setModel(self.model)
        # self.tableView2.resizeColumnsToContents()
        # self.tableView2.setColumnHidden(0,True)
        # self.label_total.setText(str(self.hours_minutes()))

        # #travail sur PDF
    # def print(self):
    #     dialogu = QtPrintSupport.QPrintDialog()
    #     if dialogu.exec_() == QDialog.Accepted:
    #         self.handlepaintrequest(dialogu.printer())
    # def handlepaintrequest(self,printer):
    #     html = """<!DOCTYPE html>
    #     <html>
    #     <head> ESSAI <head>
    #     <body>smdlqsdmlsdkmlsdk<body>
    #     <html>"""
    #     web_view = QtWebEngineWidgets.QWebEngineView()
    #     web_view.setHtml(html)
    #     web_view.print_(printer)
    def print(self):
        name = (self.dateEdit.text())
        date = QDate.currentDate().toString()
        pilot = self.lineEditPilote.text()
        html = ("""
                < html >
                < body >
                Hello
        world!
        <p>name is {}</p>
        <p> and the date is {}
        <p> pilot is {}
        </body>
            < / html >
                """).format(name, date,pilot)


        # create a QPrinter object for the printer the user later selects
        myPrinter = QPrinter()

        # let user select and configure a printer, saved in the object created above
        myDialog = QPrintDialog(myPrinter, self)

        # execute the print if the user clicked "Print"
        if myDialog.exec_():
        # create a QTextDocument in memory to hold our HTML
            myDocument = QTextDocument()

        # load the html into the document
        myDocument.setHtml(html)

        # send the html to the physical printer
        myDocument.print_(myPrinter)


    def setdata(self):
        query = QSqlQuery()
        query.prepare("INSERT INTO Contact1 (pilot_1,datetime1,datetime2,aircraft)" "VALUES (?,?,?,?)")
        query.bindValue(0, self.lineEditPilote.text())
        query.bindValue(1, self.dateTimeEdit_1.text())
        query.bindValue(2, self.dateTimeEdit_2.text())
        query.bindValue(3, self.lineEdit_aircraft.text())
        query.exec_()
        self.model.select()

    def query_date_time(self):
        liste =[]
        self.model.setTable("Contact1")
        combodate = self.dateEdit.text()
        combodate_2 = self.dateEdit_2.text()
        # print(type(combodate))
        # print(combodate)
        # print(type(combodate_2))
        # print(combodate_2)
        #self.model.setFilter("datetime1 between'1997/12/31' and '1999/12/31' ")
        #self.model.setFilter("datetime1 = '1997/12/31 17:00'")
        filter = "cast(datetime1 as datetime)between cast('{}' as datetime) and cast('{}' as datetime)".format(combodate,combodate_2)
        #print(filter)
        self.model.setFilter(filter)
        #self.model.setFilter("datetime1 LIKE '{} {}'".format(combodate, '%'))
        #self.model.setFilter("datetime1 LIKE '01-01-2000%'")
        #filter = "datetime1 LIKE '{}'".format(combodate)
        #print(filter)
        #self.model.setFilter("pilot_1 LIKE  ('marc') ")
        self.model.select()
        for i in range(self.model.rowCount()):
            date1 = self.model.record(i).value("datetime1")
            date1_time = datetime.strptime(date1,"%Y/%m/%d %H:%M")
            date2 = self.model.record(i).value("datetime2")
            print('values are: {} and {}'.format(date1,date2))
            print(type(date1_time))



    def affiche(self):
        print(self.lecture())

    def calcultemps(self):
        self.lire()

    def inserer_calule_bdd(self):
        query1 = QSqlQuery("SELECT datetime1,datetime2 FROM Contact1")
        liste=[]
        while query1.next():
            date1 = query1.value(0)
            date2 = query1.value(1)
            essai = datetime.strptime(date2, "%Y/%m/%d %H:%M") - datetime.strptime(date1, "%Y/%m/%d %H:%M")
            liste.append(essai)
        total = sum(liste, timedelta())
        return total

    def hours_minutes(self):
        td = self.inserer_calule_bdd()
        resultat = td.days * 24 + td.seconds // 3600
        return resultat

    def effacer(self):
        index = self.tableView1.currentIndex()
        deleteconf = QMessageBox.critical(self.parent(), "DELETE ROW", "REALLY DELETE?", QMessageBox.Yes,
                                          QMessageBox.No)
        if deleteconf == QMessageBox.Yes:
            self.model.removeRow(index.row())
            self.model.submitAll()
            return




    @pyqtSlot()
    def on_pushButton_print_clicked(self):
        self.print()
    @pyqtSlot()
    def on_calcul_temps_clicked(self):
        self.label_total.setText(str(self.hours_minutes()))

    @pyqtSlot()
    def on_Calcul_clicked(self):
        return self.query_date_time()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.setdata()
        self.label_total.setText(str(self.hours_minutes()))
        # self.insertion()
        # # self.pushButton.clicked.connect(self.insertion)
        # self.pushButton.clicked.connect(self.affiche)

    @pyqtSlot()
    def on_pushButton_effacer_clicked(self):
        self.effacer()


# class Fourqeux(QSortFilterProxyModel,qtSqlTry.Ui_Form):
#
#     def __init__(self,parent=None):
#         super(Fourqeux, self).__init__(parent)
#         self.model = QSqlRelationalTableModel()
#         self.model.setTable("Contact1")
       #
       # table.setModel(self.model)



        # proxymodel = QSortFilterProxyModel(self)
        # proxymodel.setSourceModel(self.model)
        # self.table.setModel(proxymodel)


    # def sorting(self):
    #     self.maindialog.lineEditPilote.setText()








if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        form = MainDialog()
        # LaBase()
        form.show()
        app.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window....")
    except Exception:
        print(sys.exc_info()[1])
