# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TabView.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1023, 695)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Qtable = QtWidgets.QTabWidget(Dialog)
        self.Qtable.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Qtable.setMovable(True)
        self.Qtable.setObjectName("Qtable")
        self.Insertion = QtWidgets.QWidget()
        self.Insertion.setObjectName("Insertion")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Insertion)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_pilote = QtWidgets.QLineEdit(self.Insertion)
        self.lineEdit_pilote.setObjectName("lineEdit_pilote")
        self.verticalLayout.addWidget(self.lineEdit_pilote)
        self.lineEdit_avion = QtWidgets.QLineEdit(self.Insertion)
        self.lineEdit_avion.setObjectName("lineEdit_avion")
        self.verticalLayout.addWidget(self.lineEdit_avion)
        self.comboBox_pilote = QtWidgets.QComboBox(self.Insertion)
        self.comboBox_pilote.setObjectName("comboBox_pilote")
        self.verticalLayout.addWidget(self.comboBox_pilote)
        self.comboBox_pilote2 = QtWidgets.QComboBox(self.Insertion)
        self.comboBox_pilote2.setObjectName("comboBox_pilote2")
        self.verticalLayout.addWidget(self.comboBox_pilote2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.Insertion)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout.addWidget(self.dateTimeEdit)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.Insertion)
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.verticalLayout.addWidget(self.dateTimeEdit_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.tableView = QtWidgets.QTableView(self.Insertion)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.afficher = QtWidgets.QPushButton(self.Insertion)
        self.afficher.setObjectName("afficher")
        self.horizontalLayout.addWidget(self.afficher)
        self.Effacer = QtWidgets.QPushButton(self.Insertion)
        self.Effacer.setObjectName("Effacer")
        self.horizontalLayout.addWidget(self.Effacer)
        self.calculer = QtWidgets.QPushButton(self.Insertion)
        self.calculer.setObjectName("calculer")
        self.horizontalLayout.addWidget(self.calculer)
        self.pushButton_4 = QtWidgets.QPushButton(self.Insertion)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.Qtable.addTab(self.Insertion, "")
        self.Limites = QtWidgets.QWidget()
        self.Limites.setObjectName("Limites")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Limites)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Limites)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.Limites)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.Limites)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 30, 113, 29))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 30, 113, 29))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_4.addWidget(self.groupBox)
        self.Qtable.addTab(self.Limites, "")
        self.table = QtWidgets.QWidget()
        self.table.setObjectName("table")
        self.splitter = QtWidgets.QSplitter(self.table)
        self.splitter.setGeometry(QtCore.QRect(9, 9, 961, 591))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableView_2 = QtWidgets.QTableView(self.splitter)
        self.tableView_2.setObjectName("tableView_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.autre_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.autre_btn.setObjectName("autre_btn")
        self.horizontalLayout_3.addWidget(self.autre_btn)
        self.calculer_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.calculer_btn.setObjectName("calculer_btn")
        self.horizontalLayout_3.addWidget(self.calculer_btn)
        self.inserer_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.inserer_btn.setObjectName("inserer_btn")
        self.horizontalLayout_3.addWidget(self.inserer_btn)
        self.effacer_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.effacer_btn.setObjectName("effacer_btn")
        self.horizontalLayout_3.addWidget(self.effacer_btn)
        self.Qtable.addTab(self.table, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.Qtable.addTab(self.tab_6, "")
        self.horizontalLayout_2.addWidget(self.Qtable)

        self.retranslateUi(Dialog)
        self.Qtable.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm"))
        self.afficher.setText(_translate("Dialog", "Afficher"))
        self.Effacer.setText(_translate("Dialog", "Effacer"))
        self.Effacer.setShortcut(_translate("Dialog", "Backspace"))
        self.calculer.setText(_translate("Dialog", "Calculer"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))
        self.Qtable.setTabText(self.Qtable.indexOf(self.Insertion), _translate("Dialog", "Insertion"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.Qtable.setTabText(self.Qtable.indexOf(self.Limites), _translate("Dialog", "Limites"))
        self.autre_btn.setText(_translate("Dialog", "autre"))
        self.calculer_btn.setText(_translate("Dialog", "calculer"))
        self.inserer_btn.setText(_translate("Dialog", "inserer"))
        self.effacer_btn.setText(_translate("Dialog", "effacer"))
        self.Qtable.setTabText(self.Qtable.indexOf(self.table), _translate("Dialog", "table"))
        self.Qtable.setTabText(self.Qtable.indexOf(self.tab_6), _translate("Dialog", "Page"))

