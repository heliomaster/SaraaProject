#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from datetime import datetime

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
        self.model = QSqlTableModel()
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)
        self.model.setTable("Contact1")
        self.model.select()
        self.model.setHeaderData(1, Qt.Horizontal, u"pilot_1")
        self.model.setHeaderData(2, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(3, Qt.Horizontal, "datetime2")
        # tableview created in qt designer assigned to tablemodel
        self.tableView1.setModel(self.model)

    def insertion(self):
        # self.LaBase.db.open()
        liste = [self.lineEditPilote.text(), self.dateTimeEdit_1.dateTime(), self.dateTimeEdit_2.dateTime()]
        self.model.setTable("Contact1")
        # self.model.select()
        # On insère une ligne supplémentaire qui sera remplie par la suite.
        # Si cette ligne de code est oubliée, c'est une modification qui sera effectuée
        self.model.insertRows(0, 1)
        # Nous créons une boucle permettant de rentrer les valeurs des QLineEdit dans notre base de données
        a = 0
        while a <= 2:
            ## setData() requiert en premier argument l'index de la ligne à créer, en deuxième la valeur.
            ## Ici dans le premier argument a+1 correspond à la deuxième colonne de notre table si a = 0.
            # On laisse la première colonne se remplir seule (clé automatique).
            ## Le premier argument de self.model.index peut prendre n'importe quelle valeur. Ceci ne change rien.
            self.model.setData(self.model.index(0, a + 1), liste[a])
            a += 1
        self.model.submitAll()
        #self.LaBase.db.close()

    def lecture(self):
        liste = []
        self.LaBase.db.open()
        self.model.setTable("Contact1")
        self.model.select()
        nb_row = self.model.rowCount()
        a = 0
        while a < nb_row:
            record = self.model.record(a)
            contact = [record.value("pilot_1"), record.value("datetime1"), record.value("datetime2")]
            liste.append(contact)
            a += 1
        self.LaBase.db.close()
        return liste

    def affiche(self):
        #self.lecture()
        print(self.lecture())

    def calcultemps(self):
        self.lire()

    def lire(self):
        query = self.LaBase.db.exec_("SELECT datetime1,datetime2 FROM Contact1")
        while query.next():
            datetime1 = query.value(0)
            datetime2 = query.value(1)
            print(datetime1, datetime2)
            # TODO: VERIF DATETIME1 ET Z A LA FIN
            diff = datetime.strptime(datetime2, "%Y-%m-%dT%H:%M:%S.%f") - datetime.strptime(datetime1,
                                                                                            "%Y-%m-%dT%H:%M:%S.%fZ")
            return diff
            print(diff)

    def inserer_calule_bdd(self):
        pass
        





            # self.LaBase.db.open()
            # query = self.LaBase.db.exec_("""select * from Contact1""")
            # while query.next():
            #     value = []
            #     record = query.record()
            #     for index in range(record.count()):
            #         value.append(record.value(index))
            #         #return (';'.join(answer))
            #     print(value)

            # return (';'.join(value))
            # print(';'.join(value))
            # self.LaBase.db.close()

    def effacer(self):
        index = self.tableView1.currentIndex()
        deleteconf = QMessageBox.critical(self.parent(), "DELETE ROW", "REALLY DELETE?", QMessageBox.Yes,
                                          QMessageBox.No)
        if deleteconf == QMessageBox.Yes:
            self.model.removeRow(index.row())
            self.model.submitAll()

            return
        else:
            return
            # self.LaBase.db.open()
            # #self.model.setTable("Contact1")
            # #model = self.model
            # indices = self.tableView1.selectionModel().selectedRow()
            # for index in sorted(indices):
            #     self.model.removeRow(index.row())
            # self.LaBase.db.close()

    @pyqtSlot()
    def on_calcul_temps_clicked(self):
        print(self.calcultemps())

    @pyqtSlot()
    def on_Calcul_clicked(self):
        return self.lire()
        #print(self.lire())
        #print(labasevar(self))
    #
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.insertion()
        # self.pushButton.clicked.connect(self.insertion)
        self.pushButton.clicked.connect(self.affiche)

    @pyqtSlot()
    def on_pushButton_effacer_clicked(self):
        self.effacer()

        # self.db.close()

        # @pyqtSlot()
        # def on_pushButton_clicked(self):
        #     self.insertion


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
