# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowV4.ui',
# licensing of 'mainwindowV4.ui' applies.
#
# Created: Sat Oct  2 18:41:30 2021
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1111, 738)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.carpetaChooser = QtWidgets.QPushButton(self.frame)
        self.carpetaChooser.setObjectName("carpetaChooser")
        self.gridLayout.addWidget(self.carpetaChooser, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 1, 1, 1)
        self.labelLogo = QtWidgets.QLabel(self.frame)
        self.labelLogo.setText("")
        self.labelLogo.setObjectName("labelLogo")
        self.gridLayout.addWidget(self.labelLogo, 3, 0, 3, 1)
        self.agrega_cats = QtWidgets.QPushButton(self.frame)
        self.agrega_cats.setEnabled(False)
        self.agrega_cats.setObjectName("agrega_cats")
        self.gridLayout.addWidget(self.agrega_cats, 2, 0, 1, 1)
        self.tableWidget_resumen = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_resumen.setAutoScroll(True)
        self.tableWidget_resumen.setObjectName("tableWidget_resumen")
        self.tableWidget_resumen.setColumnCount(0)
        self.tableWidget_resumen.setRowCount(0)
        self.tableWidget_resumen.horizontalHeader().setVisible(True)
        self.tableWidget_resumen.horizontalHeader().setHighlightSections(False)
        self.tableWidget_resumen.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_resumen.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget_resumen, 0, 1, 3, 5)
        self.imprimir = QtWidgets.QPushButton(self.frame)
        self.imprimir.setEnabled(False)
        self.imprimir.setObjectName("imprimir")
        self.gridLayout.addWidget(self.imprimir, 3, 3, 1, 2)
        self.folderPDF = QtWidgets.QLabel(self.frame)
        self.folderPDF.setText("")
        self.folderPDF.setObjectName("folderPDF")
        self.gridLayout.addWidget(self.folderPDF, 5, 2, 1, 1)
        self.folder = QtWidgets.QLabel(self.frame)
        self.folder.setText("")
        self.folder.setObjectName("folder")
        self.gridLayout.addWidget(self.folder, 3, 2, 2, 1)
        self.listaDeImpresoras = QtWidgets.QListWidget(self.frame)
        self.listaDeImpresoras.setEnabled(False)
        self.listaDeImpresoras.setObjectName("listaDeImpresoras")
        self.gridLayout.addWidget(self.listaDeImpresoras, 3, 5, 3, 1)
        self.botonCancela = QtWidgets.QPushButton(self.frame)
        self.botonCancela.setObjectName("botonCancela")
        self.gridLayout.addWidget(self.botonCancela, 4, 3, 2, 1)
        self.impresora = QtWidgets.QPushButton(self.frame)
        self.impresora.setObjectName("impresora")
        self.gridLayout.addWidget(self.impresora, 4, 4, 2, 1)
        self.excel_anual_button = QtWidgets.QPushButton(self.frame)
        self.excel_anual_button.setEnabled(False)
        self.excel_anual_button.setObjectName("excel_anual_button")
        self.gridLayout.addWidget(self.excel_anual_button, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1111, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Huiini 1.7", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Tab 1", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Tab 2", None, -1))
        self.carpetaChooser.setText(QtWidgets.QApplication.translate("MainWindow", "Selecciona Carpeta", None, -1))
        self.agrega_cats.setText(QtWidgets.QApplication.translate("MainWindow", "Editar categorías", None, -1))
        self.imprimir.setText(QtWidgets.QApplication.translate("MainWindow", "Imprimir", None, -1))
        self.botonCancela.setText(QtWidgets.QApplication.translate("MainWindow", "Cancelar impresión", None, -1))
        self.impresora.setText(QtWidgets.QApplication.translate("MainWindow", "Selecciona Impresora", None, -1))
        self.excel_anual_button.setText(QtWidgets.QApplication.translate("MainWindow", "Excel Anual", None, -1))

