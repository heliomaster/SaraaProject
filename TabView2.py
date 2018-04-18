# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TabView2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_insertDialogu(object):
    def setupUi(self, insertDialogu):
        insertDialogu.setObjectName("insertDialogu")
        insertDialogu.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(insertDialogu)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(insertDialogu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 261, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

        self.retranslateUi(insertDialogu)
        self.buttonBox.accepted.connect(insertDialogu.accept)
        self.buttonBox.rejected.connect(insertDialogu.reject)
        QtCore.QMetaObject.connectSlotsByName(insertDialogu)

    def retranslateUi(self, insertDialogu):
        _translate = QtCore.QCoreApplication.translate
        insertDialogu.setWindowTitle(_translate("insertDialogu", "Dialog"))
        self.label.setText(_translate("insertDialogu", "IMMATRICULATION"))
        self.lineEdit.setPlaceholderText(_translate("insertDialogu", "FGTPH"))
        self.label_2.setText(_translate("insertDialogu", "TYPE D\'APPAREIL"))
        self.lineEdit_2.setPlaceholderText(_translate("insertDialogu", "DR400"))
        self.label_3.setText(_translate("insertDialogu", "PUISSANCE(CV)"))
        self.lineEdit_3.setPlaceholderText(_translate("insertDialogu", "120"))

