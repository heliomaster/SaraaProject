#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery




import os

Fichier_DB = "qsSqlTry.db"

class tableModelQtsqlTry(QAbstractTableModel,QWidget):

    def __init__(self):
        super(tableModelQtsqlTry,self).__init__()
        bd_existe = os.path.exists(Fichier_DB)
        bd = QSqlDatabase.addDatabase('QSQLITE')
        bd.setDatabaseName(Fichier_DB)
        bd.open()
        if not bd_existe:
            QMessageBox.critical(None,
                    "Ouverture de la base de données",
                        "Erreur d'ouverture: {}".format(bd.lastError().text()))

        #self.litBD()

    def creerBD(self):
        QSqlQuery('''CREATE TABLE  pilot_try_qt(
                      pilot_id INTEGER PRIMARY KEY,
                      pilot_name1 TEXT,
                      datetime1 TEXT,
                      datetime2 TEXT,
                      resultat TEXT )''')






if __name__ == '__main__':
    tableModelQtsqlTry()



