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
        MainWindow.resize(1410, 588)
        self.actionEscoger_cliente = QAction(MainWindow)
        self.actionEscoger_cliente.setObjectName(u"actionEscoger_cliente")
        self.action_editar_Categor_as = QAction(MainWindow)
        self.action_editar_Categor_as.setObjectName(u"action_editar_Categor_as")
        self.action_editar_Categor_as.setEnabled(False)
        self.actionActualizar_Exceles = QAction(MainWindow)
        self.actionActualizar_Exceles.setObjectName(u"actionActualizar_Exceles")
        self.actionActualizar_Exceles.setEnabled(False)
        self.actionCancelar_Impresi_n = QAction(MainWindow)
        self.actionCancelar_Impresi_n.setObjectName(u"actionCancelar_Impresi_n")
        self.actionCancelar_Impresi_n.setEnabled(False)
        self.actionImprimir = QAction(MainWindow)
        self.actionImprimir.setObjectName(u"actionImprimir")
        self.actionImprimir.setEnabled(False)
        self.actionsdnsodk = QAction(MainWindow)
        self.actionsdnsodk.setObjectName(u"actionsdnsodk")
        self.actionSelccionar_Impresora = QAction(MainWindow)
        self.actionSelccionar_Impresora.setObjectName(u"actionSelccionar_Impresora")
        self.actionGenerar_Carpetas_Aspel_Coi = QAction(MainWindow)
        self.actionGenerar_Carpetas_Aspel_Coi.setObjectName(u"actionGenerar_Carpetas_Aspel_Coi")
        self.actionActualizar_cat_logos_CFDI = QAction(MainWindow)
        self.actionActualizar_cat_logos_CFDI.setObjectName(u"actionActualizar_cat_logos_CFDI")
        self.actionClaves = QAction(MainWindow)
        self.actionClaves.setObjectName(u"actionClaves")
        self.actionClaves.setEnabled(False)
        self.actionEditar_categor_as_default = QAction(MainWindow)
        self.actionEditar_categor_as_default.setObjectName(u"actionEditar_categor_as_default")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelLogo_sicad = QLabel(self.centralWidget)
        self.labelLogo_sicad.setObjectName(u"labelLogo_sicad")
        self.labelLogo_sicad.setMinimumSize(QSize(250, 79))
        self.labelLogo_sicad.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout.addWidget(self.labelLogo_sicad)

        self.header_cliente = QLabel(self.centralWidget)
        self.header_cliente.setObjectName(u"header_cliente")
        self.header_cliente.setMinimumSize(QSize(600, 100))
        self.header_cliente.setMaximumSize(QSize(600, 16777215))
        font = QFont()
        font.setPointSize(16)
        self.header_cliente.setFont(font)

        self.horizontalLayout.addWidget(self.header_cliente)

        self.labelLogo = QLabel(self.centralWidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setMinimumSize(QSize(164, 79))
        self.labelLogo.setMaximumSize(QSize(164, 16777215))

        self.horizontalLayout.addWidget(self.labelLogo)


        self.verticalLayout.addLayout(self.horizontalLayout)

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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.carpetaChooser = QPushButton(self.centralWidget)
        self.carpetaChooser.setObjectName(u"carpetaChooser")
        self.carpetaChooser.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.carpetaChooser)

        self.excel_anual_button = QPushButton(self.centralWidget)
        self.excel_anual_button.setObjectName(u"excel_anual_button")
        self.excel_anual_button.setEnabled(False)
        self.excel_anual_button.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.excel_anual_button)

        self.excel_mensual_button = QPushButton(self.centralWidget)
        self.excel_mensual_button.setObjectName(u"excel_mensual_button")
        self.excel_mensual_button.setEnabled(False)
        self.excel_mensual_button.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.excel_mensual_button)

        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(200, 0))
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1410, 21))
        self.menuCliente = QMenu(self.menuBar)
        self.menuCliente.setObjectName(u"menuCliente")
        self.menuImprimir = QMenu(self.menuBar)
        self.menuImprimir.setObjectName(u"menuImprimir")
        self.menuProcesar = QMenu(self.menuBar)
        self.menuProcesar.setObjectName(u"menuProcesar")
        self.menuConfiguraci_n = QMenu(self.menuBar)
        self.menuConfiguraci_n.setObjectName(u"menuConfiguraci_n")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMinimumSize(QSize(250, 35))
        self.dockWidget.setFeatures(QDockWidget.DockWidgetClosable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)

        self.menuBar.addAction(self.menuCliente.menuAction())
        self.menuBar.addAction(self.menuImprimir.menuAction())
        self.menuBar.addAction(self.menuProcesar.menuAction())
        self.menuBar.addAction(self.menuConfiguraci_n.menuAction())
        self.menuCliente.addAction(self.actionEscoger_cliente)
        self.menuCliente.addSeparator()
        self.menuCliente.addAction(self.action_editar_Categor_as)
        self.menuCliente.addAction(self.actionActualizar_Exceles)
        self.menuCliente.addAction(self.actionGenerar_Carpetas_Aspel_Coi)
        self.menuCliente.addAction(self.actionClaves)
        self.menuImprimir.addAction(self.actionImprimir)
        self.menuImprimir.addAction(self.actionCancelar_Impresi_n)
        self.menuImprimir.addSeparator()
        self.menuImprimir.addAction(self.actionSelccionar_Impresora)
        self.menuConfiguraci_n.addAction(self.actionActualizar_cat_logos_CFDI)
        self.menuConfiguraci_n.addAction(self.actionEditar_categor_as_default)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Huiini 2.0.4", None))
        self.actionEscoger_cliente.setText(QCoreApplication.translate("MainWindow", u"Escoger cliente", None))
        self.action_editar_Categor_as.setText(QCoreApplication.translate("MainWindow", u"Editar Categor\u00edas", None))
        self.actionActualizar_Exceles.setText(QCoreApplication.translate("MainWindow", u"Actualizar Exceles", None))
        self.actionCancelar_Impresi_n.setText(QCoreApplication.translate("MainWindow", u"Cancelar Impresi\u00f3n", None))
        self.actionImprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.actionsdnsodk.setText(QCoreApplication.translate("MainWindow", u"sdnsodk", None))
        self.actionSelccionar_Impresora.setText(QCoreApplication.translate("MainWindow", u"Selccionar Impresora", None))
        self.actionGenerar_Carpetas_Aspel_Coi.setText(QCoreApplication.translate("MainWindow", u"Generar Carpetas Aspel-Coi", None))
        self.actionActualizar_cat_logos_CFDI.setText(QCoreApplication.translate("MainWindow", u"Actualizar cat\u00e1logos CFDI", None))
        self.actionClaves.setText(QCoreApplication.translate("MainWindow", u"Claves", None))
        self.actionEditar_categor_as_default.setText(QCoreApplication.translate("MainWindow", u"Editar categor\u00edas default", None))
        self.labelLogo_sicad.setText("")
        self.header_cliente.setText("")
        self.labelLogo.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.carpetaChooser.setText(QCoreApplication.translate("MainWindow", u"Selecciona Carpeta", None))
        self.excel_anual_button.setText(QCoreApplication.translate("MainWindow", u"Excel Anual", None))
        self.excel_mensual_button.setText(QCoreApplication.translate("MainWindow", u"Excel mensual", None))
        self.menuCliente.setTitle(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.menuImprimir.setTitle(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.menuProcesar.setTitle(QCoreApplication.translate("MainWindow", u"Procesar", None))
        self.menuConfiguraci_n.setTitle(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

