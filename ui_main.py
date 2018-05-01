#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from datetime import datetime,timedelta
from functools import reduce

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

        # # travail sur relation model
        # aircraftType = self.model.fieldIndex('aircraft')
        # self.model.setRelation(aircraftType,QSqlRelation("Aircraft","id","immatriculation"))
        # #self.tableView1.setItemDelegate(QSqlRelationalDelegate(self.tableView1))
        # relModel = self.model.relationModel(aircraftType)
        # self.comboBox.setModel(relModel)
        # self.comboBox.setModelColumn(relModel.fieldIndex('immatriculation'))
        # mapper = QDataWidgetMapper()
        # mapper.setModel(self.model)
        # mapper.setItemDelegate(QSqlRelationalDelegate())
        # mapper.addMapping(self.comboBox,aircraftType)

        self.model.select()
        self.model.setHeaderData(1, Qt.Horizontal, u"pilot_1")
        self.model.setHeaderData(2, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(3, Qt.Horizontal, "datetime2")
        self.model.setHeaderData(4, Qt.Horizontal, "aircraft")

        # tableview created in qt designer assigned to tablemodel
        self.tableView1.setModel(self.model)
        self.tableView1.resizeColumnsToContents()
        self.tableView1.setColumnHidden(0,True)
        self.total_le.setText(str(self.hours_minutes()))

        #travail sur combobox


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
        self.model.setTable("Contact1")
        combodate = self.dateEdit.text()
        combodate_2 = self.dateEdit_2.text()
        print(type(combodate))
        print(combodate)
        print(type(combodate_2))
        print(combodate_2)
        #self.model.setFilter("datetime1 between'1997/12/31' and '1999/12/31' ")
        #self.model.setFilter("datetime1 = '1997/12/31 17:00'")
        #filter = "datetime1 between '{}' AND '{}'".format(combodate,combodate_2)
        #filter = "datetime1 >= '{}' AND datetime1 <= '{}'".format(combodate, combodate_2)
        filter = "cast(datetime1 as datetime)between cast('{}' as datetime) and cast('{}' as datetime)".format(combodate,combodate_2)
        #filter = "datetime1 = '{}' ".format(combodate)
        print(filter)
        self.model.setFilter(filter)
        #self.model.setFilter("datetime1 BETWEEN '{}' AND '{}'".format(combodate,combodate_2))
        #self.model.setFilter("id BETWEEN '1' AND '4'")

        #self.model.setFilter("datetime1 LIKE '{} {}'".format(combodate, '%'))
        #self.model.setFilter("datetime1 LIKE '01-01-2000%'")
        #filter = "datetime1 LIKE '{}'".format(combodate)
        #print(filter)
        #self.model.setFilter("pilot_1 LIKE  ('marc') ")

        self.model.select()













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
    def on_calcul_temps_clicked(self):
        self.total_le.setText(str(self.hours_minutes()))

    @pyqtSlot()
    def on_Calcul_clicked(self):
        return self.query_date_time()

    #
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.setdata()
        self.total_le.setText(str(self.hours_minutes()))
        # self.insertion()
        # # self.pushButton.clicked.connect(self.insertion)
        # self.pushButton.clicked.connect(self.affiche)

    @pyqtSlot()
    def on_pushButton_effacer_clicked(self):
        self.effacer()


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
