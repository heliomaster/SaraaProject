# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TabView.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(842, 560)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Qtable = QtWidgets.QTabWidget(Dialog)
        self.Qtable.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Qtable.setMovable(True)
        self.Qtable.setObjectName("Qtable")
        self.Insertion = QtWidgets.QWidget()
        self.Insertion.setObjectName("Insertion")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Insertion)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.Insertion)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_heures_total = QtWidgets.QLineEdit(self.Insertion)
        self.lineEdit_heures_total.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_heures_total.setObjectName("lineEdit_heures_total")
        self.horizontalLayout_2.addWidget(self.lineEdit_heures_total)
        self.label = QtWidgets.QLabel(self.Insertion)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Insertion)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.Insertion)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_observations = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_observations.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_observations.setObjectName("lineEdit_observations")
        self.gridLayout_2.addWidget(self.lineEdit_observations, 9, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 3, 0, 1, 1)
        self.comboBox_avion = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_avion.setObjectName("comboBox_avion")
        self.gridLayout_2.addWidget(self.comboBox_avion, 2, 0, 1, 1)
        self.comboBox_pilot2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_pilot2.setObjectName("comboBox_pilot2")
        self.gridLayout_2.addWidget(self.comboBox_pilot2, 1, 0, 1, 1)
        self.comboBox_pilot1 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_pilot1.setObjectName("comboBox_pilot1")
        self.gridLayout_2.addWidget(self.comboBox_pilot1, 0, 0, 1, 1)
        self.lineEdit_pax2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_pax2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pax2.setObjectName("lineEdit_pax2")
        self.gridLayout_2.addWidget(self.lineEdit_pax2, 6, 0, 1, 1)
        self.lineEdit_pax1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_pax1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pax1.setObjectName("lineEdit_pax1")
        self.gridLayout_2.addWidget(self.lineEdit_pax1, 5, 0, 1, 1)
        self.lineEdit_mission = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_mission.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mission.setObjectName("lineEdit_mission")
        self.gridLayout_2.addWidget(self.lineEdit_mission, 8, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit_2.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_2.addWidget(self.dateTimeEdit_2, 4, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.Insertion)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_pilote = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_pilote.setObjectName("comboBox_pilote")
        self.gridLayout.addWidget(self.comboBox_pilote, 1, 2, 1, 1)
        self.tableView_3 = QtWidgets.QTableView(self.groupBox_4)
        self.tableView_3.setObjectName("tableView_3")
        self.gridLayout.addWidget(self.tableView_3, 0, 0, 1, 4)
        self.comboBox_pilote2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_pilote2.setObjectName("comboBox_pilote2")
        self.gridLayout.addWidget(self.comboBox_pilote2, 1, 3, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_4)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dateEdit.setDate(QtCore.QDate(2017, 12, 26))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7999, 12, 30), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.UTC)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox_4)
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setTimeSpec(QtCore.Qt.UTC)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 3, 1, 1)
        self.tableView = QtWidgets.QTableView(self.Insertion)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 2, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.insert_data = QtWidgets.QPushButton(self.Insertion)
        self.insert_data.setObjectName("insert_data")
        self.horizontalLayout.addWidget(self.insert_data)
        self.Effacer = QtWidgets.QPushButton(self.Insertion)
        self.Effacer.setObjectName("Effacer")
        self.horizontalLayout.addWidget(self.Effacer)
        self.calculer = QtWidgets.QPushButton(self.Insertion)
        self.calculer.setObjectName("calculer")
        self.horizontalLayout.addWidget(self.calculer)
        self.enter_new_AC = QtWidgets.QPushButton(self.Insertion)
        self.enter_new_AC.setObjectName("enter_new_AC")
        self.horizontalLayout.addWidget(self.enter_new_AC)
        self.enter_new_pilot = QtWidgets.QPushButton(self.Insertion)
        self.enter_new_pilot.setObjectName("enter_new_pilot")
        self.horizontalLayout.addWidget(self.enter_new_pilot)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 4)
        self.Qtable.addTab(self.Insertion, "")
        self.Limites = QtWidgets.QWidget()
        self.Limites.setObjectName("Limites")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Limites)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.Limites)
        self.groupBox.setObjectName("groupBox")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setGeometry(QtCore.QRect(20, 90, 231, 26))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.comboBox_avions = QtWidgets.QComboBox(self.splitter_3)
        self.comboBox_avions.setObjectName("comboBox_avions")
        self.lineEdit_avion_2 = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_avion_2.setObjectName("lineEdit_avion_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 371, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateEdit_pilote = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_pilote.setObjectName("dateEdit_pilote")
        self.horizontalLayout_4.addWidget(self.dateEdit_pilote)
        self.comboBox_pilote_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_pilote_2.setObjectName("comboBox_pilote_2")
        self.horizontalLayout_4.addWidget(self.comboBox_pilote_2)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.lineEdit_pilote_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_pilote_2.setObjectName("lineEdit_pilote_2")
        self.horizontalLayout_4.addWidget(self.splitter_2)
        self.buttonBox_print = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox_print.setGeometry(QtCore.QRect(460, 50, 170, 32))
        self.buttonBox_print.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_print.setObjectName("buttonBox_print")
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.Limites)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableView_limites = QtWidgets.QTableView(self.groupBox_2)
        self.tableView_limites.setGeometry(QtCore.QRect(0, 21, 641, 201))
        self.tableView_limites.setObjectName("tableView_limites")
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.Qtable.addTab(self.Limites, "")
        self.table = QtWidgets.QWidget()
        self.table.setObjectName("table")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.table)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.table)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableView_2 = QtWidgets.QTableView(self.splitter)
        self.tableView_2.setObjectName("tableView_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        self.gridLayout_4.addWidget(self.splitter, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.table)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.Qtable.addTab(self.table, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_5.addWidget(self.textEdit, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_imprimer = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_imprimer.setObjectName("pushButton_imprimer")
        self.horizontalLayout_7.addWidget(self.pushButton_imprimer)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.tab_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.Qtable.addTab(self.tab_6, "")
        self.verticalLayout.addWidget(self.Qtable)
        self.label_2.setBuddy(self.lineEdit_heures_total)
        self.label.setBuddy(self.lineEdit_3)

        self.retranslateUi(Dialog)
        self.Qtable.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_pax1, self.lineEdit_pax2)
        Dialog.setTabOrder(self.lineEdit_pax2, self.insert_data)
        Dialog.setTabOrder(self.insert_data, self.Effacer)
        Dialog.setTabOrder(self.Effacer, self.calculer)
        Dialog.setTabOrder(self.calculer, self.enter_new_AC)
        Dialog.setTabOrder(self.enter_new_AC, self.enter_new_pilot)
        Dialog.setTabOrder(self.enter_new_pilot, self.tableView_3)
        Dialog.setTabOrder(self.tableView_3, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.dateEdit_2)
        Dialog.setTabOrder(self.dateEdit_2, self.comboBox_pilote)
        Dialog.setTabOrder(self.comboBox_pilote, self.comboBox_pilote2)
        Dialog.setTabOrder(self.comboBox_pilote2, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_4)
        Dialog.setTabOrder(self.lineEdit_4, self.tableView)
        Dialog.setTabOrder(self.tableView, self.lineEdit_heures_total)
        Dialog.setTabOrder(self.lineEdit_heures_total, self.tableView_limites)
        Dialog.setTabOrder(self.tableView_limites, self.effacer_btn)
        Dialog.setTabOrder(self.effacer_btn, self.tableView_2)
        Dialog.setTabOrder(self.tableView_2, self.autre_btn)
        Dialog.setTabOrder(self.autre_btn, self.dateEdit_pilote)
        Dialog.setTabOrder(self.dateEdit_pilote, self.lineEdit_pilote_2)
        Dialog.setTabOrder(self.lineEdit_pilote_2, self.inserer_btn)
        Dialog.setTabOrder(self.inserer_btn, self.calculer_btn)
        Dialog.setTabOrder(self.calculer_btn, self.comboBox_pilote_2)
        Dialog.setTabOrder(self.comboBox_pilote_2, self.comboBox_avions)
        Dialog.setTabOrder(self.comboBox_avions, self.lineEdit_avion_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Master Window"))
        Dialog.setWhatsThis(_translate("Dialog", "Inserer Appareil"))
        self.label_2.setText(_translate("Dialog", "HEURES TOTALES"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_3.setTitle(_translate("Dialog", "INSERTION"))
        self.lineEdit_observations.setPlaceholderText(_translate("Dialog", "Observations"))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm"))
        self.lineEdit_pax2.setPlaceholderText(_translate("Dialog", "pax 2"))
        self.lineEdit_pax1.setPlaceholderText(_translate("Dialog", "pax 1"))
        self.lineEdit_mission.setPlaceholderText(_translate("Dialog", "Mission"))
        self.groupBox_4.setTitle(_translate("Dialog", "SELECTION"))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd"))
        self.dateEdit_2.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd"))
        self.insert_data.setText(_translate("Dialog", "Inserer"))
        self.Effacer.setText(_translate("Dialog", "Effacer"))
        self.Effacer.setShortcut(_translate("Dialog", "Backspace"))
        self.calculer.setText(_translate("Dialog", "Calculer"))
        self.enter_new_AC.setText(_translate("Dialog", "Appareil"))
        self.enter_new_pilot.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Permet de creer un nouveau Pilote et de l\'inserer dans la base de donnée</span></p></body></html>"))
        self.enter_new_pilot.setText(_translate("Dialog", "Pilote"))
        self.Qtable.setTabText(self.Qtable.indexOf(self.Insertion), _translate("Dialog", "Insertion"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.groupBox_2.setTitle(_translate("Dialog", "GroupBox"))
        self.Qtable.setTabText(self.Qtable.indexOf(self.Limites), _translate("Dialog", "Limites"))
        self.autre_btn.setText(_translate("Dialog", "autre"))
        self.calculer_btn.setText(_translate("Dialog", "calculer"))
        self.inserer_btn.setText(_translate("Dialog", "inserer"))
        self.effacer_btn.setText(_translate("Dialog", "effacer"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.Qtable.setTabText(self.Qtable.indexOf(self.table), _translate("Dialog", "table"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_imprimer.setText(_translate("Dialog", "IMPRIMER"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.Qtable.setTabText(self.Qtable.indexOf(self.tab_6), _translate("Dialog", "Page"))

