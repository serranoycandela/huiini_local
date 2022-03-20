# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowV4.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1111, 738)
        self.actionEscoger_cliente = QAction(MainWindow)
        self.actionEscoger_cliente.setObjectName(u"actionEscoger_cliente")
        self.action_editar_Categor_as = QAction(MainWindow)
        self.action_editar_Categor_as.setObjectName(u"action_editar_Categor_as")
        self.actionActualizar_Exceles = QAction(MainWindow)
        self.actionActualizar_Exceles.setObjectName(u"actionActualizar_Exceles")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_cliente = QLabel(self.centralWidget)
        self.header_cliente.setObjectName(u"header_cliente")
        self.header_cliente.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(24)
        self.header_cliente.setFont(font)

        self.verticalLayout.addWidget(self.header_cliente)

        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 370))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame = QFrame(self.centralWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 180))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 5, 2, 1, 1)

        self.listaDeImpresoras = QListWidget(self.frame)
        self.listaDeImpresoras.setObjectName(u"listaDeImpresoras")
        self.listaDeImpresoras.setEnabled(False)

        self.gridLayout.addWidget(self.listaDeImpresoras, 3, 6, 3, 1)

        self.agrega_cats = QPushButton(self.frame)
        self.agrega_cats.setObjectName(u"agrega_cats")
        self.agrega_cats.setEnabled(False)

        self.gridLayout.addWidget(self.agrega_cats, 2, 0, 1, 1)

        self.folderPDF = QLabel(self.frame)
        self.folderPDF.setObjectName(u"folderPDF")

        self.gridLayout.addWidget(self.folderPDF, 5, 3, 1, 1)

        self.impresora = QPushButton(self.frame)
        self.impresora.setObjectName(u"impresora")

        self.gridLayout.addWidget(self.impresora, 4, 5, 2, 1)

        self.carpetaChooser = QPushButton(self.frame)
        self.carpetaChooser.setObjectName(u"carpetaChooser")

        self.gridLayout.addWidget(self.carpetaChooser, 0, 0, 1, 1)

        self.botonCancela = QPushButton(self.frame)
        self.botonCancela.setObjectName(u"botonCancela")

        self.gridLayout.addWidget(self.botonCancela, 4, 4, 2, 1)

        self.folder = QLabel(self.frame)
        self.folder.setObjectName(u"folder")

        self.gridLayout.addWidget(self.folder, 3, 3, 2, 1)

        self.labelLogo = QLabel(self.frame)
        self.labelLogo.setObjectName(u"labelLogo")

        self.gridLayout.addWidget(self.labelLogo, 3, 0, 3, 1)

        self.excel_anual_button = QPushButton(self.frame)
        self.excel_anual_button.setObjectName(u"excel_anual_button")
        self.excel_anual_button.setEnabled(False)

        self.gridLayout.addWidget(self.excel_anual_button, 1, 0, 1, 1)

        self.imprimir = QPushButton(self.frame)
        self.imprimir.setObjectName(u"imprimir")
        self.imprimir.setEnabled(False)

        self.gridLayout.addWidget(self.imprimir, 3, 4, 1, 2)

        self.tableWidget_resumen = QTableWidget(self.frame)
        self.tableWidget_resumen.setObjectName(u"tableWidget_resumen")
        self.tableWidget_resumen.setAutoScroll(True)
        self.tableWidget_resumen.horizontalHeader().setVisible(True)
        self.tableWidget_resumen.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_resumen.horizontalHeader().setHighlightSections(False)
        self.tableWidget_resumen.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableWidget_resumen, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1111, 21))
        self.menuCliente = QMenu(self.menuBar)
        self.menuCliente.setObjectName(u"menuCliente")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuCliente.menuAction())
        self.menuCliente.addAction(self.actionEscoger_cliente)
        self.menuCliente.addSeparator()
        self.menuCliente.addAction(self.action_editar_Categor_as)
        self.menuCliente.addAction(self.actionActualizar_Exceles)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Huiini 1.7", None))
        self.actionEscoger_cliente.setText(QCoreApplication.translate("MainWindow", u"Escoger cliente", None))
        self.action_editar_Categor_as.setText(QCoreApplication.translate("MainWindow", u"Editar Categor\u00edas", None))
        self.actionActualizar_Exceles.setText(QCoreApplication.translate("MainWindow", u"Actualizar Exceles", None))
        self.header_cliente.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.agrega_cats.setText(QCoreApplication.translate("MainWindow", u"Editar categor\u00edas", None))
        self.folderPDF.setText("")
        self.impresora.setText(QCoreApplication.translate("MainWindow", u"Selecciona Impresora", None))
        self.carpetaChooser.setText(QCoreApplication.translate("MainWindow", u"Selecciona Carpeta", None))
        self.botonCancela.setText(QCoreApplication.translate("MainWindow", u"Cancelar impresi\u00f3n", None))
        self.folder.setText("")
        self.labelLogo.setText("")
        self.excel_anual_button.setText(QCoreApplication.translate("MainWindow", u"Excel Anual", None))
        self.imprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.menuCliente.setTitle(QCoreApplication.translate("MainWindow", u"Cliente", None))
    # retranslateUi

