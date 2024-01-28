# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cryptoDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(829, 631)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.cancelButton = QPushButton(self.splitter)
        self.cancelButton.setObjectName(u"cancelButton")
        self.splitter.addWidget(self.cancelButton)
        self.saveButton = QPushButton(self.splitter)
        self.saveButton.setObjectName(u"saveButton")
        self.splitter.addWidget(self.saveButton)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
    # retranslateUi

