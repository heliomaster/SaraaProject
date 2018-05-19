#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtSql import *
#from ui_main import MainDialog
from qtSqlTry import Ui_Form


class LaBase():
    def __init__(self):
        #super(LaBase,self).__init__()
        #Création de la basse de données
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('pilote1')  ## Nous nommons ici notre base de données.

        self.db.open() ## Commande permettant d'accéder à la base de données

        query = QSqlQuery()
        query.exec_('''PRAGMA foreign_key = ON''')
        query.exec_('''create table Contact (id INTEGER PRIMARY KEY,pilot_1 TEXT, datetime1 TEXT, datetime2 TEXT,total TEXT)''')
        query.exec_('''create table Contact1 (id INTEGER PRIMARY KEY,pilot_1 TEXT, datetime1 TEXT, datetime2 TEXT, aircraft INTEGER )''')
        query.exec_('''create TABLE Aircraft(id INTEGER PRIMARY KEY , immatriculation TEXT , type_ac TEXT, puissance TEXT)''')
        query.exec_('''create TABLE Pilot (id INTEGER PRIMARY KEY,rank TEXT, first_name TEXT, last_name TEXT)''')
        query.exec_('''CREATE TABLE Mission(id INTEGER PRIMARY KEY,cdb TEXT, copi TEXT,aircraft TEXT, pax1 TEXT, pax2 TEXT,
                        datetime1 TEXT,datetime2 TEXT,mission TEXT,observations TEXT,total TEXT )''')
        query.exec_('''CREATE TABLE Limites(id INTEGER PRIMARY KEY ,pilot TEXT, cempn TEXT, vsa TEXT, license TEXT)''')

        # while query.next():
        #     ladiff = ('''SELECT strftime('%s',datetime2)-strftime('%s',datetime1)  FROM Contact''')
        #

        ## Création de la table Contact dans notre base de données ouverte.
        self.db.commit() ## Enregistrement de la base de données
        self.db.close() ## Fermeture de celle-ci


        # def lire(self):
        #     self.db.open()
        #     query = self.db.exec_("""select * from Contact""")
        #     while query.next():
        #         value = []
        #         record = query.record()
        #         for index in range(record.count()):
        #             value.append(str(record.value(index)))
        #         print(';'.join(value))













if __name__ == '__main__':
    LaBase()
