#-*- encoding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtCore import Qt, QDir
from PySide2.QtGui import *
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import QTableWidget, QLineEdit, QTableWidgetItem, QFileDialog, QProgressDialog, QMessageBox, QListView, QAbstractItemView, QTreeView, QDialog, QVBoxLayout, QDialogButtonBox, QFileSystemModel, QInputDialog
from PySide2.QtWidgets import QPushButton, QListWidget, QListWidgetItem, QComboBox, QMenu, QAction
import sys
import guiV4
from os import listdir, environ
from os.path import isfile, join, basename
import shutil
import os
try:
    import win32print
    import win32api
except:
    print("soy linux")
import time as time_old
from subprocess import Popen, call
from FacturasLocal import FacturaLocal as Factura
import math
import json
#import xlsxwriter
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

from openpyxl import load_workbook,  Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Border, Side, PatternFill, Font, Alignment, numbers
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter



from datetime import datetime
from copy import copy
try:
    import ghostscript
except:
    print("ghostscript no está instalado")
import locale

import filecmp
# import subprocess
# import psutil
# import signal


##C:\Python36\Scripts\pyside2-uic.exe mainwindowV2.ui -o guiV2.py
##C:\Python36\Scripts\pyside2-uic.exe mainwindowV4.ui -o guiV4.py
##C:\Python36\Scripts\pyinstaller.exe huiini.py
## C:\Users\Mio\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\pyinstaller.exe huiini.py
## C:\Users\Mio\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\pyside2-uic.exe mainwindowV4.ui -o guiV4.py


try:
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
except NameError:  # We are the main py2exe script, not a module
    scriptDirectory = os.path.dirname(os.path.abspath(sys.argv[0]))

class categorias_widget(QDialog):
    def __init__(self, parent=None):
        super(categorias_widget, self).__init__(parent)
        self.setMinimumSize(520, 850)
        layout = QVBoxLayout()
        self.add_button = QPushButton("Nueva")
        layout.addWidget(self.add_button)
        self.edit_button = QPushButton("Editar")
        layout.addWidget(self.edit_button)
        self.remove_button = QPushButton("Eliminar")
        layout.addWidget(self.remove_button)
        self.myListWidget = QListWidget()
        layout.addWidget(self.myListWidget)
        self.setLayout(layout)

class impresoras_widget(QDialog):
    def __init__(self, parent=None):
        super(impresoras_widget, self).__init__(parent)
        self.setMinimumSize(200, 100)
        layout = QVBoxLayout()
        self.lista = QListWidget()
        layout.addWidget(self.lista)
        self.setLayout(layout)
        self.lista.currentItemChanged.connect(self.cambiaSeleccionDeImpresora)

    def cambiaSeleccionDeImpresora(self, curr, prev):
        print(curr.text())
        self.impresoraDefault = curr.text()
        win32print.SetDefaultPrinter(self.impresoraDefault)

class getFilesDlg(QDialog):

    # sendPaths is a signal emitted by getPaths containing a list of file paths from
    # the users selection via this dialog.
    sendPaths = Signal(list)

    def __init__(self, parent=None):
        super(getFilesDlg, self).__init__(parent)

        self.setMinimumSize(520,850)

        self.fileDlgPaths = []

        layout = QVBoxLayout()

        self.btnBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.btnBox.accepted.connect(self.getPaths)
        self.btnBox.rejected.connect(self.close)

        self.fsModel = QFileSystemModel()
        self.fsModel.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)

        self.treeView = QTreeView()
        self.treeView.setSelectionMode(QTreeView.ExtendedSelection)

        self.treeView.setModel(self.fsModel)
        self.treeView.setColumnWidth(0, 361)
        self.treeView.setColumnHidden(1, True)
        self.treeView.setColumnHidden(2, True)
        self.fsModel.setRootPath("")
        self.treeView.setSortingEnabled(True)
        layout.addWidget(self.treeView)
        layout.addWidget(self.btnBox)
        self.setLayout(layout)
        self.treeView.setRootIndex(self.fsModel.index(""))
        appdatapath = os.path.expandvars('%APPDATA%\huiini')
        
        self.huiini_home_folder_path = ""
        if os.path.exists(os.path.join(appdatapath,"huiini_home_folder_path.txt")):
            with open(os.path.join(appdatapath,"huiini_home_folder_path.txt")) as f:
                self.huiini_home_folder_path = f.readline()
        print(self.huiini_home_folder_path)


        path_restante = self.huiini_home_folder_path
        while path_restante != os.path.split(path_restante)[0]:
            index_previo = self.fsModel.index(path_restante)
            self.treeView.expand(index_previo)
            path_restante = os.path.split(path_restante)[0]
        index_previo = self.fsModel.index(path_restante)
        self.treeView.expand(index_previo)

        # self.treeView.setRootIndex(self.fsModel.index("C:\\Dropbox"))
        # self.treeView.expand(self.treeView.rootIndex())
        #self.fsModel.setRootPath(environ['HOMEPATH'])
        # self.treeView.setRootIndex(self.fsModel.index("\\"))
        #self.treeView.expand(self.treeView.rootIndex())


    def getPaths(self):
    	# For some reason duplicates were being returned when they weren't supposed to.
    	# This obtains the selected files from the dialog and only returns individual
    	# paths.
        indexes = self.treeView.selectedIndexes()
        if indexes:
            self.fileDlgPaths = []
            for i in indexes:

    			# Possible permission error occuring here
    			# unable to replicate at this time
                path = self.fsModel.filePath(i)
                if path not in self.fileDlgPaths:
                    self.fileDlgPaths.append(path)
            self.close() # To close the dialog on an accept signal
            self.sendPaths.emit(self.fileDlgPaths)

class ImgWidgetPalomita(QtWidgets.QLabel):

    def __init__(self, parent=None):
        super(ImgWidgetPalomita, self).__init__(parent)
        pic_palomita = QtGui.QPixmap(join(scriptDirectory,"palomita.png"))
        self.setPixmap(pic_palomita)

class ImgWidgetTache(QtWidgets.QLabel):

    def __init__(self, parent=None):
        super(ImgWidgetTache, self).__init__(parent)
        pic_tache = QtGui.QPixmap(join(scriptDirectory,"x.png"))
        self.setPixmap(pic_tache)



class Ui_MainWindow(QtWidgets.QMainWindow, guiV4.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

        print(scriptDirectory)
        logoPix = QtGui.QPixmap(join(scriptDirectory,"logo.png"))
        with open(join(scriptDirectory,"conceptos.json"), "r") as jsonfile:
            self.concepto = json.load(jsonfile)
        self.labelLogo.setPixmap(logoPix)
        appdatapath = os.path.expandvars('%APPDATA%\huiini')
        self.tiene_pdflatex = True
        try:
            with open(os.path.join(appdatapath,"pdflatex_path.txt")) as f:
                self.pdflatex_path = f.readline()
        except:
            if shutil.which('pdflatex'):
                with open(os.path.join(appdatapath,"pdflatex_path.txt"), "w") as f:
                    f.write(shutil.which('pdflatex').replace("\\","\\\\"))
            else:
                reply = QMessageBox.question(self, 'No se detectó Miktex',"¿está Miktex instalado?\n contesta que si para buscar la ruta de pdflatex manualmete\n o no para cancelar", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                if reply == QMessageBox.Yes:
                    path_to_file, _ = QFileDialog.getOpenFileName(self, "ruta de pdflatex", "~")
                    if "pdflatex.exe" in path_to_file.lower():
                        with open(os.path.join(appdatapath,"pdflatex_path.txt"), "w") as f:
                            f.write(path_to_file.replace("\\","\\\\"))
                    else:
                        QMessageBox.information(self, "Advertencia", "ruta incorrecta, la creación de pdfs quedará desactivada")
                        self.tiene_pdflatex = False
                if reply == QMessageBox.No:
                    QMessageBox.information(self, "Advertencia", "la creación de pdfs quedará desactivada")
                    self.tiene_pdflatex = False

        self.tiene_gswin64c = True
        try:
            with open(os.path.join(appdatapath,"gswin64c_path.txt")) as f:
                self.gswin64c_path = f.readline()
        except:
            if shutil.which('gswin64c'):
                with open(os.path.join(appdatapath,"gswin64c_path.txt"), "w") as f:
                    f.write(shutil.which('gswin64c').replace("\\","\\\\"))
                self.gswin64c_path = shutil.which('gswin64c').replace("\\","\\\\")
            else:
                reply = QMessageBox.question(self, 'No se detectó Ghostscript',"¿está Ghostscript instalado?\n contesta que si para buscar la ruta de gswin64c manualmete\n o no para cancelar", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                if reply == QMessageBox.Yes:
                    path_to_file, _ = QFileDialog.getOpenFileName(self, "ruta de gswin64c", "~")
                    if "gswin64c.exe" in path_to_file.lower():
                        with open(os.path.join(appdatapath,"gswin64c_path.txt"), "w") as f:
                            f.write(path_to_file.replace("\\","\\\\"))
                        self.gswin64c_path = path_to_file.replace("\\","\\\\")
                    else:
                        QMessageBox.information(self, "Advertencia", "ruta incorrecta, la impresión quedará desactivada")
                        self.tiene_gswin64c = False
                if reply == QMessageBox.No:
                    QMessageBox.information(self, "Advertencia", "la impresión quedará desactivada")
                    self.tiene_gswin64c = False

        self.actionEscoger_cliente.triggered.connect(self.escoger_cliente)



        self.carpetaChooser.clicked.connect(self.cualCarpeta)
        self.action_editar_Categor_as.triggered.connect(self.edita_categorias)
        self.actionImprimir.triggered.connect(self.imprime)
        self.excel_anual_button.clicked.connect(self.abre_excel_anual)
        #self.descarga_bt.clicked.connect(self.descarga_mesta)
        self.actionImprimir.triggered.connect(self.imprime)

        self.actionSelccionar_Impresora.triggered.connect(self.cambiaImpresora)
        self.actionCancelar_Impresi_n.triggered.connect(self.cancelaImpresion)

        if self.tiene_gswin64c == False:
            print("desabilitando la impresión....")
            self.actionCancelar_Impresi_n.setEnabled(False)
            self.actionSelccionar_Impresora.setEnabled(False)
            self.actionImprimir.setEnabled(False)

        self.tables = {}
        self.facturas = {}
        self.sumaRFC = {}





        #self.tableWidget_resumen.cellDoubleClicked.connect(self.meDoblePicaronResumen)
        self.progressBar.hide()

        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.numeroDeFacturasValidas = {}

    def escoger_cliente(self):
        file_dialog = getFilesDlg()
        file_dialog.sendPaths.connect(self.despliega_cliente)
        file_dialog.exec()
    def despliega_cliente(self,paths):
        self.cliente_path = paths.copy()[0]
        with open(join(self.cliente_path,"Doc_Fiscal","claves.txt")) as fp:
            nombre = ""
            rfc = ""
            Lines = fp.readlines()
            for line in Lines:
                if "Nombre: " in line:
                    nombre = line.split("Nombre: ")[1]
                if "RFC: " in line:
                    rfc = line.split("RFC: ")[1]
        
        self.header_cliente.setText("Nombre: "+nombre+"\nRFC: "+rfc)

    def tabChanged(self, index):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA estoy cambiando a ",str(index))
        name = self.tabWidget.tabText(index)
        folder_mes = {"ENERO":"01 ENERO",
                    "FEBRERO":"02 FEBRERO",
                    "MARZO":"03 MARZO",
                    "ABRIL":"04 ABRIL",
                    "MAYO":"05 MAYO",
                    "JUNIO":"06 JUNIO",
                    "JULIO":"07 JULIO",
                    "AGOSTO":"08 AGOSTO",
                    "SEPTIEMBRE":"09 SEPTIEMBRE",
                    "OCTUBRE":"10 OCTUBRE",
                    "NOVIEMBRE":"11 NOVIEMBRE",
                    "DICIEMBRE":"12 DICIEMBRE",
                    }
        
        
        
        if name == "Ingresos":
            print("aquí haría algo")
            self.mes = ""
        else:
            self.excel_path = join(self.folder_year, folder_mes[name],"EGRESOS","huiini","resumen.xlsx")
            
            self.mes = name
            n = -1
            lc = ["Excel"]

            for i in range(6,self.tables[self.mes].columnCount()):
                try: 
                    f = float(self.tables[self.mes].item(0,i).text())
                    header = self.tables[self.mes].horizontalHeaderItem(i).text()
                    lc.append(header)
                except:
                    print("noesnumero")
            
            
            self.sumale()
        
    def setupTabMeses(self):
        self.tables[self.mes].setColumnCount(17)
        self.tables[self.mes].setColumnWidth(0,30)#pdf
        self.tables[self.mes].setColumnWidth(1,95)#fecha
        self.tables[self.mes].setColumnWidth(2,70)#uuid
        self.tables[self.mes].setColumnWidth(3,120)#receptor-nombre
        self.tables[self.mes].setColumnWidth(4,120)#emisor-rfc
        self.tables[self.mes].setColumnWidth(5,120)#concepto
        self.tables[self.mes].setColumnWidth(6,75)#Subtotal
        self.tables[self.mes].setColumnWidth(7,80)#Descuento
        self.tables[self.mes].setColumnWidth(8,80)#traslados-iva
        self.tables[self.mes].setColumnWidth(9,80)#traslados-ieps
        self.tables[self.mes].setColumnWidth(10,75)#retIVA
        self.tables[self.mes].setColumnWidth(11,75)#retISR
        self.tables[self.mes].setColumnWidth(12,80)#total
        self.tables[self.mes].setColumnWidth(13,74)#formaDePago
        self.tables[self.mes].setColumnWidth(14,77)#metodoDePago
        self.tables[self.mes].setColumnWidth(14,77)#carpetasCoi

        self.tables[self.mes].verticalHeader().setFixedWidth(35)
        header = self.tables[self.mes].verticalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.handleHeaderMenu)

        lc = ["Pdf","Fecha","UUID","Receptor","Emisor","Concepto","Subtotal","Descuento","Traslado\nIVA","Traslado\nIEPS","Retención\nIVA","Retención\nISR","Total","Forma\nPago","Método\nPago","Tipo","Carpetas Coi"]
        self.ponEncabezado(lc,self.mes)

        self.tables[self.mes].cellDoubleClicked.connect(self.meDoblePicaronXML)
        #self.tables[self.mes].horizontalHeader().sectionClicked.connect(self.reordena)
        self.tables[self.mes].setSortingEnabled(True)

#    def setupTabAnuales(self,tabName):


    def reordena(self, column):
        print("reodenaria")
        if column == 2:
            print("reodenaria con uuid")
            self.facturas[self.mes] = sorted(self.facturas[self.mes], key=lambda facturas: facturas.UUID)
        if column == 15:
            print("reodenaria con tipo")
            self.facturas[self.mes] = sorted(self.facturas[self.mes], key=lambda facturas: facturas.conceptos[0]['tipo'])

    def quitaCategoria(self):
        reply = QMessageBox.question(self, 'Message',"Estás seguro?", QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            curr_indexes = self.cats_dialog.myListWidget.selectedIndexes()
            if len(curr_indexes)>1:
                print("no")
            else:
                #confirmacion para maricas
                categoria = self.cats_dialog.myListWidget.currentItem().text().split(" (")[0]
                self.dicc_de_categorias.pop(categoria)
                with open(self.json_path, "w", encoding="utf-8") as jsonfile:
                    json.dump(self.dicc_de_categorias, jsonfile, indent=4, sort_keys=True)

                self.cats_dialog.myListWidget.takeItem(curr_indexes[0].row())

    def editaCategoria(self):
        curr_indexes = self.cats_dialog.myListWidget.selectedIndexes()
        if len(curr_indexes)>1:
            print("no")
        else:
            categoria = self.cats_dialog.myListWidget.currentItem().text().split(" (")[0]
            lista_de_empiezos = ", ".join(self.dicc_de_categorias[categoria])


            nombre, ok1 = QInputDialog().getText(self.cats_dialog, "Nombre de la Categoría",
                                        "Nombre de la categoría:", QLineEdit.Normal,categoria)
            claves_ps, ok2 = QInputDialog().getText(self.cats_dialog, "Lista de claves de producto o servicio",
                                         "clave_ps:", QLineEdit.Normal,
                                         lista_de_empiezos)

            if ok1 and ok2:
                if nombre != categoria:
                    self.dicc_de_categorias.pop(categoria)
                if nombre in self.dicc_de_categorias:
                    #lista_previa = self.dicc_de_categorias[nombre].copy()

                    #lista_previa.extend(claves_ps.strip().split(","))#el espacio no se ocupa
                    self.dicc_de_categorias[nombre] = claves_ps.replace(" ","").split(",")
                #self.lista_ordenada = sorted(self.lista_ordenada, key=lambda tup: tup[1])
                with open(self.json_path, "w", encoding="utf-8") as jsonfile:
                    json.dump(self.dicc_de_categorias, jsonfile, indent=4, sort_keys=True)
                self.cats_dialog.myListWidget.clear()
                self.enlista_categorias()

    def agregaCategoria(self):
        nombre, ok1 = QInputDialog().getText(self.cats_dialog, "Nombre de la Categoría",
                                     "Nombre de la categoría:", QLineEdit.Normal,"")
        claves_ps, ok2 = QInputDialog().getText(self.cats_dialog, "Lista de claves de producto o servicio",
                                     "clave_ps:", QLineEdit.Normal,
                                     "")
        claves_ps.strip()

        if ok1 and ok2:
            for clave in claves_ps.split(", "):
                pasa = True
                for categoria, lista in self.dicc_de_categorias.items():
                    for clave1 in lista:
                        if clave1.startswith(clave) or clave.startswith(clave1):
                            pasa = False
                            QMessageBox.information(self, "Advertencia", "El inicio de clave " + clave + " ya está considerado en la categoría " + categoria)
                if pasa:
                    if clave == "" or nombre == "":
                        print("no mames")
                    else:
                        self.dicc_de_categorias[nombre] = claves_ps.split(", ")

            #self.lista_ordenada = sorted(self.lista_ordenada, key=lambda tup: tup[1])
            with open(self.json_path, "w", encoding="utf-8") as jsonfile:
                json.dump(self.dicc_de_categorias, jsonfile, indent=4, sort_keys=True)
            self.cats_dialog.myListWidget.clear()
            self.enlista_categorias()

    def enlista_categorias(self):
        for key, value in self.dicc_de_categorias.items():
            if len(value) > 3:
                texto_claves = " ("+value[0]+", "+value[1]+", "+value[2]+"...)"
            else:
                texto_claves = " (" + ", ".join(value) + ")"
            i = QListWidgetItem(key+texto_claves)
            i.setToolTip("\n".join(value))
            # if "Default" in tupla[0]:
            #     i.setBackground(QtGui.QColor("#ababab"))
            self.cats_dialog.myListWidget.addItem(i)

    def abre_excel_anual(self):
        try:
            os.startfile(self.annual_xlsx_path)
            print("este guey me pico:"+self.annual_xlsx_path)
        except:
            print ("el sistema no tiene una aplicacion por default para abrir exceles")
            QMessageBox.information(self, "Information", "El sistema no tiene una aplicación por default para abrir exceles" )
    def edita_categorias(self):
        self.cats_dialog = categorias_widget()
        self.cats_dialog.remove_button.clicked.connect(self.quitaCategoria)
        self.cats_dialog.add_button.clicked.connect(self.agregaCategoria)
        self.cats_dialog.edit_button.clicked.connect(self.editaCategoria)
        folder_cliente = os.path.split(os.path.split(self.paths[0])[0])[0]
        self.json_path = join(folder_cliente, "categorias_dicc_huiini.json")
        if os.path.exists(self.json_path):
            with open(self.json_path, "r", encoding="utf-8") as jsonfile:
                self.dicc_de_categorias = json.load(jsonfile)
        else:
            self.dicc_de_categorias = {}


        # lista_de_tuplas.extend(lista_categorias_default)
        #self.lista_ordenada = sorted(lista_de_tuplas, key=lambda tup: tup[1])

        self.enlista_categorias()
        self.cats_dialog.exec()

    def as_text(self,value):
        if value is None:
            return ""
        return str(value)

    def style_ws(self, ws, columna_totales, sumas_row):
        cell_border = Border(left=Side(border_style='medium', color='FF000000'),
                     right=Side(border_style='medium', color='FF000000'),
                     top=Side(border_style='medium', color='FF000000'),
                     bottom=Side(border_style='medium', color='FF000000'))

        cell_border_sumas = Border(left=Side(border_style=None, color='FF000000'),
                     right=Side(border_style=None, color='FF000000'),
                     top=Side(border_style='thin', color='FF000000'),
                     bottom=Side(border_style='thin', color='FF000000'))

        for cell in ws["1:1"]:
            cell.fill = PatternFill(start_color="8ccbff", end_color="8ccbff", fill_type = "solid")
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            cell.border = cell_border

        for column_cells in ws.columns:
            #length = max(len(self.as_text(cell.value)) for cell in column_cells)
            length = len(self.as_text(column_cells[0].value))
            ws.column_dimensions[column_cells[0].column_letter].width = length+5

        ws.column_dimensions['A'].width = 12

        for cell in ws['A']:
            cell.font = Font(bold=True)


        for cell in ws[str(sumas_row)+":"+str(sumas_row)]:
            cell.border = cell_border_sumas
            cell.font = Font(bold=True)


        for i in range(2,sumas_row+1):
            for j in range(2,columna_totales+1):
                ws.cell(i,j).number_format = numbers.FORMAT_NUMBER_COMMA_SEPARATED1

        ws.cell(sumas_row,1).fill = PatternFill(start_color="4ac6ff", end_color="4ac6ff", fill_type = "solid")
        ws.cell(sumas_row,1).border = cell_border

    def style_ws_ingresos(self, ws, columna_totales, sumas_row):
        cell_border = Border(left=Side(border_style=None, color='FF000000'),
                     right=Side(border_style=None, color='FF000000'),
                     top=Side(border_style='medium', color='FF000000'),
                     bottom=Side(border_style='medium', color='FF000000'))

        cell_border_sumas = Border(left=Side(border_style=None, color='FF000000'),
                     right=Side(border_style=None, color='FF000000'),
                     top=Side(border_style='thin', color='FF000000'),
                     bottom=Side(border_style='thin', color='FF000000'))

        for column in range(1,18):
            cell = ws.cell(1,column)
            cell.fill = PatternFill(start_color="8ccbff", end_color="8ccbff", fill_type = "solid")
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            cell.border = cell_border

        ws.column_dimensions['A'].width = 10
        ws.column_dimensions['B'].width = 10
        ws.column_dimensions['C'].width = 40
        ws.column_dimensions['D'].width = 15
        ws.column_dimensions['E'].width = 20
        ws.column_dimensions['F'].width = 40
        ws.column_dimensions['G'].width = 9
        ws.column_dimensions['H'].width = 9
        ws.column_dimensions['I'].width = 9
        ws.column_dimensions['J'].width = 9
        ws.column_dimensions['K'].width = 9
        ws.column_dimensions['L'].width = 9
        ws.column_dimensions['M'].width = 9
        ws.column_dimensions['N'].width = 9

        # for cell in ws['A']:
        #     cell.font = Font(bold=True)



        for column in range(1,18):
            cell = ws.cell(sumas_row,column)
            cell.border = cell_border_sumas
            cell.font = Font(bold=True)


        for i in range(2,sumas_row+1):
            for j in range(8,14):
                ws.cell(i,j).number_format = numbers.FORMAT_NUMBER_COMMA_SEPARATED1

        for column in range(20,27):
            cell = ws.cell(3,column)
            cell.fill = PatternFill(start_color="8ccbff", end_color="8ccbff", fill_type = "solid")
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            cell.border = cell_border
            cell = ws.cell(20,column)
            cell.fill = PatternFill(start_color="8ccbff", end_color="8ccbff", fill_type = "solid")
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            cell.border = cell_border

        for column in range(20,27):
            cell = ws.cell(16,column)
            cell.border = cell_border_sumas
            cell.font = Font(bold=True)
            cell = ws.cell(33,column)
            cell.border = cell_border_sumas
            cell.font = Font(bold=True)

        ws.column_dimensions['T'].width = 12
        ws.column_dimensions['U'].width = 12
        ws.column_dimensions['V'].width = 12
        ws.column_dimensions['W'].width = 12
        ws.column_dimensions['X'].width = 12
        ws.column_dimensions['Y'].width = 12
        ws.column_dimensions['Z'].width = 12



    def calculaAgregados(self, df, ws_cats, variable):
        # for col in df.columns:
        #     print(col)
        print(df.head())
        por_categorias = df.groupby(['mes', 'tipo'], as_index=False).agg({variable:sum})
        por_categorias_wide = por_categorias.pivot_table(index="mes",columns=['tipo'],values=variable,fill_value= 0)
        por_categorias_wide.reset_index(inplace=True)
        por_categorias_wide['mes'] = pd.Categorical(por_categorias_wide['mes'], self.todos_los_meses)
        por_categorias_wide = por_categorias_wide.sort_values("mes")
        por_categorias_wide['mes'] = por_categorias_wide.mes.astype(str)
        for r in dataframe_to_rows(por_categorias_wide, index=False, header=True):
            ws_cats.append(r)
        #print(por_categorias_wide)

        if variable == "importeConcepto":
            col_sum = "G"

        if variable == "impuestos":
            col_sum = "J"



        self.numeroDeColumnas = len(por_categorias_wide.columns)
        self.columna_totales = self.numeroDeColumnas + 1
        self.sumas_row = len(por_categorias_wide.index)+2
        ws_cats.cell(1,self.columna_totales, "Total")
        ws_cats.cell(self.sumas_row,1,"Anual")

        for i in range(2,self.columna_totales):
            letra = get_column_letter(i)
            for j in range(2,self.sumas_row):
                ws_cats.cell(j,i,"=SUMIFS(Conceptos!"+col_sum+":"+col_sum+",Conceptos!L:L,"+letra+"1,Conceptos!A:A,A"+str(j)+',Conceptos!M:M,"Pagado")')



        for i in range(2,self.columna_totales):
            letra = get_column_letter(i)
            ws_cats.cell(self.sumas_row,i,"=SUM("+letra+ "2:"+letra+ str(self.sumas_row-1)+")")

        letra_final = get_column_letter(self.numeroDeColumnas)
        for i in range(2,self.sumas_row):
            ws_cats.cell(i,self.columna_totales,"=SUM(B"+str(i)+ ":"+letra_final+ str(i)+")")

        letra_sumas = get_column_letter(self.columna_totales)
        ws_cats.cell(self.sumas_row,self.columna_totales,"=SUM("+letra_sumas+"2:"+letra_sumas+str(self.sumas_row-1)  +")")

    def hazTabDeIngresos(self,paths):
        if len(self.listaDeFacturasIngresos) > 0:
            workbook = load_workbook(self.annual_xlsx_path)
            if not "Ingresos" in workbook.sheetnames:
                ws_ingresos = workbook.create_sheet("Ingresos")
            else:
                ws_ingresos = workbook["Ingresos"]

            if ws_ingresos.max_row == 1:
                ws_ingresos.cell(1, 1, "MesEmision")
                ws_ingresos.cell(1, 2,     "MesPago")
                ws_ingresos.cell(1, 3,     "uuid")
                ws_ingresos.cell(1, 4,     "FECHA")
                ws_ingresos.cell(1, 5,     "RFC (Receptor)")
                ws_ingresos.cell(1, 6,     "RAZON SOCIAL")
                ws_ingresos.cell(1, 7,     "DESCRIPCION")
                ws_ingresos.cell(1, 8,     "SUBTOTAL")
                ws_ingresos.cell(1, 9,     "I.V.A.")
                ws_ingresos.cell(1, 10,     "IMPORTE")
                ws_ingresos.cell(1, 11,     "RET ISR")
                ws_ingresos.cell(1, 12,     "RET IVA")
                ws_ingresos.cell(1, 13,     "T O T A L")
                ws_ingresos.cell(1, 14,     "M-Pago")
                ws_ingresos.cell(1, 15,     "Status")
                ws_ingresos.cell(1, 16,     "complementosDePago")
                ws_ingresos.cell(1, 17,     "Tipo")
                row = 1
            else:
                max_row_for_a = max((c.row for c in ws_ingresos['C'] if c.value is not None))
                row = max_row_for_a
                #row = ws_ingresos.max_row
            dv = DataValidation(type="list", formula1='"Pendiente,Pagado"', allowBlank=True)
            ws_ingresos.add_data_validation(dv)
            dv_mes = DataValidation(type="list", formula1='"ENERO,FEBRERO,MARZO,ABRIL,MAYO,JUNIO,JULIO,AGOSTO,SEPTIEMBRE,OCTUBRE,NOVIEMBRE,DICIEMBRE,--"', allow_blank=True)
            ws_ingresos.add_data_validation(dv_mes)

            for factura in self.listaDeFacturasIngresos:
                numeroDeMes = int(factura.fechaTimbrado.split("-")[1])
                este_mes = self.todos_los_meses[numeroDeMes-1]
                if not self.yaEstaba[este_mes]:
                    row += 1
                    
                    dv_mes.add(ws_ingresos.cell(row, 1))
                    dv_mes.add(ws_ingresos.cell(row, 2))
                    ws_ingresos.cell(row, 1, self.todos_los_meses[numeroDeMes-1])
                    if factura.metodoDePago == "PUE" or factura.tipoDeComprobante == "P":
                        ws_ingresos.cell(row, 2, self.todos_los_meses[numeroDeMes-1])
                    if factura.UUID in self.complementosDePago:
                        numeroDeMesP = int(self.complementosDePago[factura.UUID]["fechaUltimoPago"].split("-")[1])
                        ws_ingresos.cell(row, 2, self.todos_los_meses[numeroDeMesP-1])
                    ws_ingresos.cell(row, 3, factura.UUID)
                    ws_ingresos.cell(row, 4, factura.fechaTimbrado)
                    ws_ingresos.cell(row, 5, factura.ReceptorRFC)
                    ws_ingresos.cell(row, 6, factura.ReceptorNombre)
                    ws_ingresos.cell(row, 7, factura.conceptos[0]['descripcion'])
                    ws_ingresos.cell(row, 8, factura.subTotal)
                    ws_ingresos.cell(row, 9, factura.traslados["IVA"]["importe"])
                    ws_ingresos.cell(row, 10, factura.importe)
                    if factura.tipoDeComprobante == "N":
                        ws_ingresos.cell(row, 11, factura.RetencionesISRNomina)
                    else:
                        ws_ingresos.cell(row, 11, factura.retenciones["ISR"])
                    ws_ingresos.cell(row, 12, factura.retenciones["IVA"])
                    ws_ingresos.cell(row, 13, factura.total)
                    ws_ingresos.cell(row, 14, factura.metodoDePago)

                    status = "Pendiente"
                    if factura.metodoDePago == "PUE":
                        status = "Pagado"
                    if factura.metodoDePago == "PPD":
                        if factura.UUID in self.complementosDePago:
                            if factura.total - self.complementosDePago[factura.UUID]["suma"] < 0.5:
                                status = "Pagado"
                    if factura.tipoDeComprobante == "P":
                        status = "Pagado"

                    dv.add(ws_ingresos.cell(row, 15))
                    ws_ingresos.cell(row, 15, status)

                    if factura.UUID in self.complementosDePago:
                        ws_ingresos.cell(row, 16, self.complementosDePago[factura.UUID]["suma"])

                    if factura.tipoDeComprobante == "N":
                        ws_ingresos.cell(row, 17, "Nómina")
                    else:
                        ws_ingresos.cell(row, 17, "Facturado")


            ws_ingresos.cell(row+1, 8, "=SUM(H2:H"+str(row)+")")
            ws_ingresos.cell(row+1, 9, "=SUM(I2:I"+str(row)+")")
            ws_ingresos.cell(row+1, 10, "=SUM(J2:J"+str(row)+")")
            ws_ingresos.cell(row+1, 11, "=SUM(K2:K"+str(row)+")")
            ws_ingresos.cell(row+1, 12, "=SUM(L2:L"+str(row)+")")
            ws_ingresos.cell(row+1, 13, "=SUM(M2:M"+str(row)+")")

            ws_ingresos.cell(2, 23, "Facturado")#bajo protesta
            ws_ingresos.cell(3, 20, "Mes")
            ws_ingresos.cell(3, 21, "SUBTOTAL")
            ws_ingresos.cell(3, 22, "I.V.A.")
            ws_ingresos.cell(3, 23, "IMPORTE")
            ws_ingresos.cell(3, 24, "RET ISR")
            ws_ingresos.cell(3, 25, "RET IVA")
            ws_ingresos.cell(3, 26, "T O T A L")

            ws_ingresos.cell(4, 20, "ENERO")
            ws_ingresos.cell(5, 20, "FEBRERO")
            ws_ingresos.cell(6, 20, "MARZO")
            ws_ingresos.cell(7, 20, "ABRIL")
            ws_ingresos.cell(8, 20, "MAYO")
            ws_ingresos.cell(9, 20, "JUNIO")
            ws_ingresos.cell(10, 20, "JULIO")
            ws_ingresos.cell(11, 20, "AGOSTO")
            ws_ingresos.cell(12, 20, "SEPTIEMBRE")
            ws_ingresos.cell(13, 20, "OCTUBRE")
            ws_ingresos.cell(14, 20, "NOVIEMBRE")
            ws_ingresos.cell(15, 20, "DICIEMBRE")

            for renglonMes in range(4,16):
                ws_ingresos.cell(renglonMes, 21, '=SUMIFS(H:H,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Facturado")')
                ws_ingresos.cell(renglonMes, 22, '=SUMIFS(I:I,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Facturado")')
                ws_ingresos.cell(renglonMes, 23, '=SUMIFS(J:J,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Facturado")')
                ws_ingresos.cell(renglonMes, 24, '=SUMIFS(K:K,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Facturado")')
                ws_ingresos.cell(renglonMes, 25, '=SUMIFS(L:L,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Facturado")')
                ws_ingresos.cell(renglonMes, 26, '=SUMIFS(M:M,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Facturado")')

            ws_ingresos.cell(16, 21, "=SUM(U4:U15)")
            ws_ingresos.cell(16, 22, "=SUM(V4:V15)")
            ws_ingresos.cell(16, 23, "=SUM(W4:W15)")
            ws_ingresos.cell(16, 24, "=SUM(X4:X15)")
            ws_ingresos.cell(16, 25, "=SUM(Y4:Y15)")
            ws_ingresos.cell(16, 26, "=SUM(Z4:Z15)")


            ws_ingresos.cell(19, 23, "Nómina")
            ws_ingresos.cell(20, 20, "Mes")
            ws_ingresos.cell(20, 21, "SUBTOTAL")
            ws_ingresos.cell(20, 22, "I.V.A.")
            ws_ingresos.cell(20, 23, "IMPORTE")
            ws_ingresos.cell(20, 24, "RET ISR")
            ws_ingresos.cell(20, 25, "RET IVA")
            ws_ingresos.cell(20, 26, "T O T A L")

            ws_ingresos.cell(21, 20, "ENERO")
            ws_ingresos.cell(22, 20, "FEBRERO")
            ws_ingresos.cell(23, 20, "MARZO")
            ws_ingresos.cell(24, 20, "ABRIL")
            ws_ingresos.cell(25, 20, "MAYO")
            ws_ingresos.cell(26, 20, "JUNIO")
            ws_ingresos.cell(27, 20, "JULIO")
            ws_ingresos.cell(28, 20, "AGOSTO")
            ws_ingresos.cell(29, 20, "SEPTIEMBRE")
            ws_ingresos.cell(30, 20, "OCTUBRE")
            ws_ingresos.cell(31, 20, "NOVIEMBRE")
            ws_ingresos.cell(32, 20, "DICIEMBRE")

            for renglonMes in range(21,33):
                ws_ingresos.cell(renglonMes, 21, '=SUMIFS(H:H,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Nómina")')
                ws_ingresos.cell(renglonMes, 22, '=SUMIFS(I:I,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Nómina")')
                ws_ingresos.cell(renglonMes, 23, '=SUMIFS(J:J,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Nómina")')
                ws_ingresos.cell(renglonMes, 24, '=SUMIFS(K:K,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Nómina")')
                ws_ingresos.cell(renglonMes, 25, '=SUMIFS(L:L,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Nómina")')
                ws_ingresos.cell(renglonMes, 26, '=SUMIFS(M:M,B:B,T'+str(renglonMes)+',O:O,"Pagado",Q:Q,"Nómina")')

            ws_ingresos.cell(33, 21, "=SUM(U21:U32)")
            ws_ingresos.cell(33, 22, "=SUM(V21:V32)")
            ws_ingresos.cell(33, 23, "=SUM(W21:W32)")
            ws_ingresos.cell(33, 24, "=SUM(X21:X32)")
            ws_ingresos.cell(33, 25, "=SUM(Y21:Y32)")
            ws_ingresos.cell(33, 26, "=SUM(Z21:Z32)")

            self.style_ws_ingresos(ws_ingresos,17,row+1)

            workbook.save(self.annual_xlsx_path)

    def getDescription(self, clave):
        desc = ""
        try:
            desc = self.concepto[clave]
        except:
            desc = ""
        return desc

    def hazAgregados(self, paths):
        print(self.complementosDePago)



        workbook = load_workbook(self.annual_xlsx_path)
        if not "Conceptos" in workbook.sheetnames:
            ws_todos = workbook.create_sheet("Conceptos")
        else:
            ws_todos = workbook["Conceptos"]

        if "IVA_anual" in workbook.sheetnames:
            sheet1 = workbook["IVA_anual"]
            workbook.remove(sheet1)
        if "Importe_anual" in workbook.sheetnames:
            sheet1 = workbook["Importe_anual"]
            workbook.remove(sheet1)
        if "Categorias" in workbook.sheetnames:
            sheet1 = workbook["Categorias"]
            workbook.remove(sheet1)

        workbook.save(self.annual_xlsx_path)


        ws_cats = workbook.create_sheet("IVA_anual")
        ws_cats_importe = workbook.create_sheet("Importe_anual")
        ws_lista_cats = workbook.create_sheet("Categorias")
        r = 0
        for cat in self.lista_categorias_default:
            r += 1
            ws_lista_cats.cell(r, 1, cat)

        status_column = 0
        primer_mes = workbook[self.meses[0]]

        for i in range(1,primer_mes.max_column+1):
            if primer_mes.cell(1, i).value == "Status":
                status_column = i - 2
        for mes in self.meses:
            ws_mes = workbook[mes]
            for row in range(2,len(ws_mes["A"])):
                if ws_mes.cell(row, 12).value == "PPD":#11 H
                    print("ajustaria"+ ws_mes.cell(row, 3).value)
                    if ws_mes.cell(row, 3).value in self.complementosDePago:
                        ws_mes.cell(row, 16, self.complementosDePago[ws_mes.cell(row, 3).value]["suma"])
                        if ws_mes.cell(row, 10).value - self.complementosDePago[ws_mes.cell(row, 3).value]["suma"] < 0.5:
                            ws_mes.cell(row, 14, "Pagado")


        print("ws_todos.max_row................................................................",str(ws_todos.max_row))
        if ws_todos.max_row == 1:
            ws_todos.cell(1, 1, "mes")
            ws_todos.cell(1, 2, 'clave_concepto')
            ws_todos.cell(1, 3, 'concepto_sat')
            #self.concepto
            ws_todos.cell(1, 4, 'UUID')
            ws_todos.cell(1, 5, 'cantidad')
            ws_todos.cell(1, 6, 'descripcion')
            ws_todos.cell(1, 7, 'importeConcepto')
            ws_todos.cell(1, 8, 'descuento')
            ws_todos.cell(1, 9, 'subTotal')
            ws_todos.cell(1, 10, 'impuestos')
            ws_todos.cell(1, 11, 'total')
            ws_todos.cell(1, 12, 'tipo')
            ws_todos.cell(1, 13, 'status')
            ws_todos.column_dimensions['A'].width = 9
            ws_todos.column_dimensions['B'].width = 10
            ws_todos.column_dimensions['C'].width = 40
            ws_todos.column_dimensions['D'].width = 40
            ws_todos.column_dimensions['E'].width = 10
            ws_todos.column_dimensions['F'].width = 40
            ws_todos.column_dimensions['G'].width = 9
            ws_todos.column_dimensions['H'].width = 9
            ws_todos.column_dimensions['I'].width = 9
            ws_todos.column_dimensions['J'].width = 9
            ws_todos.column_dimensions['K'].width = 9
            ws_todos.column_dimensions['L'].width = 15
            ws_todos.column_dimensions['M'].width = 9
            row = 1
        else:
            row = ws_todos.max_row

        # for mes in meses:
        #     if mes in meses_folders:
        #         for concepto in self.conceptos[mes]:

        #dv_categorias = DataValidation(type="list", formula1='"{}"'.format(self.texto_para_validacion), allow_blank=True)
        dv_categorias = DataValidation(type="list", formula1="=Categorias!A$1:A$"+str(len(self.lista_categorias_default)), allow_blank=True)

        ws_todos.add_data_validation(dv_categorias)
        for concepto in self.conceptos:
            if not self.yaEstaba[concepto['mes']]:
                row += 1
                clave = concepto['clave_concepto']
                ws_todos.cell(row, 1, concepto['mes'])
                ws_todos.cell(row, 2, clave)
                ws_todos.cell(row, 3, self.getDescription(clave))
                ws_todos.cell(row, 4, concepto['UUID'])
                ws_todos.cell(row, 5, concepto['cantidad'])
                ws_todos.cell(row, 6, concepto['descripcion'])
                ws_todos.cell(row, 7, concepto['importeConcepto'])
                ws_todos.cell(row, 8, concepto['descuento'])
                ws_todos.cell(row, 9, concepto['importeConcepto'] - concepto['descuento'])
                ws_todos.cell(row, 10, concepto['impuestos'])
                ws_todos.cell(row, 11, (concepto['importeConcepto'] - concepto['descuento']) + concepto['impuestos'])
                dv_categorias.add(ws_todos.cell(row, 12))
                ws_todos.cell(row, 12, concepto['tipo'])
                ws_todos.cell(row, 13, "=VLOOKUP(D"+str(row)+","+concepto['mes']+"!C:Q,"+str(status_column)+",FALSE)")

        df = pd.DataFrame(self.conceptos)



        self.calculaAgregados(df, ws_cats, 'impuestos')
        self.style_ws(ws_cats, self.columna_totales, self.sumas_row)

        self.calculaAgregados(df, ws_cats_importe, 'importeConcepto')
        self.style_ws(ws_cats_importe, self.columna_totales, self.sumas_row)


        workbook.save(self.annual_xlsx_path)

    def agregaMes(self, mes):
        if os.path.isfile(self.annual_xlsx_path):
            workbook = load_workbook(self.annual_xlsx_path)
            if not mes in workbook.sheetnames:
                self.yaEstaba[mes] = False
                if "Conceptos" in workbook.sheetnames:
                    antesDeConceptos = workbook.worksheets.index(workbook['Conceptos'])
                else:
                    antesDeConceptos = 1
                ws_mes = workbook.create_sheet(mes, antesDeConceptos)
            else:
                self.yaEstaba[mes] = True
        else:
            workbook = Workbook()
            ws_mes = workbook.create_sheet(mes)
            sheet1_name = workbook.get_sheet_names()[0]
            sheet1 = workbook[sheet1_name]
            workbook.remove_sheet(sheet1)
            self.yaEstaba[mes] = False

        #TUA	IEPS	ISH

        if not self.yaEstaba[mes]:
            ws_mes.cell(1, 1, "clave_ps")
            ws_mes.cell(1, 2,     "Fecha")
            ws_mes.cell(1, 3,     "UUID")
            ws_mes.cell(1, 4,     "Nombre")
            ws_mes.cell(1, 5,     "RFC")
            ws_mes.cell(1, 6,     "Concepto")
            ws_mes.cell(1, 7,     "Sub")
            ws_mes.cell(1, 8,     "Descuento")
            ws_mes.cell(1, 9,     "IVA")
            ws_mes.cell(1, 10,     "TUA")
            ws_mes.cell(1, 11,     "ISH")
            ws_mes.cell(1, 12,     "IEPS")
            ws_mes.cell(1, 13,     "Total")
            ws_mes.cell(1, 14,     "F-Pago")
            ws_mes.cell(1, 15,     "M-Pago")
            ws_mes.cell(1, 16,     "Tipo")
            ws_mes.cell(1, 17,     "Status")
            ws_mes.cell(1, 18,     "TipoDeComprobante")
            ws_mes.cell(1, 19,     "complementosDePago")
            ws_mes.column_dimensions['A'].width = 10
            ws_mes.column_dimensions['B'].width = 20
            ws_mes.column_dimensions['C'].width = 40
            ws_mes.column_dimensions['D'].width = 35
            ws_mes.column_dimensions['E'].width = 16
            ws_mes.column_dimensions['F'].width = 30
            ws_mes.column_dimensions['G'].width = 9
            ws_mes.column_dimensions['H'].width = 9
            ws_mes.column_dimensions['I'].width = 9
            ws_mes.column_dimensions['J'].width = 9
            ws_mes.column_dimensions['K'].width = 9
            ws_mes.column_dimensions['L'].width = 9
            ws_mes.column_dimensions['M'].width = 9
            ws_mes.column_dimensions['N'].width = 20
            ws_mes.column_dimensions['O'].width = 7
            ws_mes.column_dimensions['P'].width = 20
            ws_mes.column_dimensions['Q'].width = 20
            ws_mes.column_dimensions['R'].width = 10
            ws_mes.column_dimensions['S'].width = 7

            dv = DataValidation(type="list", formula1='"Pendiente,Pagado"', allow_blank=True)
            ws_mes.add_data_validation(dv)

            row = 1
            for factura in self.facturas[self.mes]:
                row += 1
                ws_mes.cell(row, 1, factura.conceptos[0]['clave_concepto'])
                ws_mes.cell(row, 2, factura.fechaTimbrado)
                ws_mes.cell(row, 3, factura.UUID)
                ws_mes.cell(row, 4, factura.EmisorNombre)
                ws_mes.cell(row, 5, factura.EmisorRFC)
                ws_mes.cell(row, 6, factura.conceptos[0]['descripcion'])
                if factura.tipoDeComprobante == "E":
                    ws_mes.cell(row, 7, 0.0 - factura.subTotal)
                    ws_mes.cell(row, 8, 0.0 - factura.descuento)
                    ws_mes.cell(row, 9, 0.0 - factura.traslados["IVA"]["importe"])
                    ws_mes.cell(row, 10, 0.0)
                    ws_mes.cell(row, 11, 0.0)
                    ws_mes.cell(row, 12, 0.0)
                    ws_mes.cell(row, 13, 0.0 - factura.total)
                else:
                    ws_mes.cell(row, 7, factura.subTotal)
                    ws_mes.cell(row, 8, factura.descuento)
                    ws_mes.cell(row, 9, factura.traslados["IVA"]["importe"])
                    ws_mes.cell(row, 10, factura.trasladosLocales["TUA"]["importe"])
                    ws_mes.cell(row, 11, factura.trasladosLocales["ISH"]["importe"])
                    ws_mes.cell(row, 12, factura.traslados["IEPS"]["importe"])
                    ws_mes.cell(row, 13, factura.total)
                ws_mes.cell(row, 14, factura.formaDePagoStr)
                ws_mes.cell(row, 15, factura.metodoDePago)
                ws_mes.cell(row, 16, factura.conceptos[0]['tipo'])
                status = "Pendiente"
                if factura.metodoDePago == "PUE":
                    status = "Pagado"
                if factura.metodoDePago == "PPD":
                    if factura.UUID in self.complementosDePago:
                        if factura.total - self.complementosDePago[factura.UUID]["suma"] < 0.5:
                            status = "Pagado"
                if factura.tipoDeComprobante == "P":
                    status = "Pagado"

                dv.add(ws_mes.cell(row, 17))
                ws_mes.cell(row, 17, status)
                ws_mes.cell(row, 18, factura.tipoDeComprobante)
                if factura.UUID in self.complementosDePago:
                    ws_mes.cell(row, 19, self.complementosDePago[factura.UUID]["suma"])

                if factura.tipoDeComprobante == "P":
                    print("segun "+ factura.UUID + "del mes " +mes+ ", aqui buscaria en todos los meses el uuid "+factura.IdDocumento+" y si encuentra su factura modificaria, la columna 13 del renglon de esa factura en el mes que esté, a Pagado")

            workbook.save(self.annual_xlsx_path)

    def hazResumenDiot(self,currentDir):
        appdatapath = os.path.expandvars('%APPDATA%\huiini')
        workbook = load_workbook(os.path.join(appdatapath,"template_diot.xlsx"))
        ws_rfc = workbook[workbook.get_sheet_names()[0]]
        xlsx_path = os.path.join(currentDir,os.path.join("huiini","resumen.xlsx"))
        #workbook = xlsxwriter.Workbook(xlsx_path)
        #worksheet = workbook.add_worksheet("por_RFC")
        # workbook = Workbook()
        # ws_rfc = workbook.create_sheet("por_RFC")
        # sheet1_name = workbook.get_sheet_names()[0]
        # sheet1 = workbook[sheet1_name]
        # workbook.remove_sheet(sheet1)

        # ws_rfc.cell(1, 1,     "RFC")
        # ws_rfc.cell(1, 2,     "SUBTOTAL")
        # ws_rfc.cell(1, 3,     "DESCUENTO")
        # ws_rfc.cell(1, 4,     "IMPORTE")
        # ws_rfc.cell(1, 5,     "IVA")
        # ws_rfc.cell(1, 6,     "TOTAL")

        row = 5
        for key, value in self.sumaRFC[self.mes].items():
            row += 1
            if row > 9:
                ws_rfc.insert_rows(row)
                for c in range(1,23):
                    cell = ws_rfc.cell(row + 1, c)
                    new_cell = ws_rfc.cell(row, c)
                    new_cell._style = copy(cell._style)
            ws_rfc.cell(row, 3, key)
            ws_rfc.cell(row, 8, value['importeStr'])
            # ws_rfc.cell(row, 2, value['subTotal'])
            # ws_rfc.cell(row, 3, value['descuento'])
            # ws_rfc.cell(row, 4, value['trasladoIVA'])factura.EmisorNombre
            ws_rfc.cell(row, 5, value['nombre'])
            ##factura.EmisorNombre
            ws_rfc.cell(row, 20, value['trasladoIVAStr'])
            # ws_rfc.cell(row, 6, value['total'])
        ws_rfc.cell(row+2, 8, "=SUM(H6:H"+str(row)+")")
        ws_rfc.cell(row+2, 20, "=SUM(T6:T"+str(row)+")")


        #worksheet2 = workbook.add_worksheet("por_Factura")
        ws_factura = workbook.create_sheet("por_Factura")
        ws_factura.cell(1, 1, "clave_ps")
        ws_factura.cell(1, 2,     "Fecha")
        ws_factura.cell(1, 3,     "UUID")
        ws_factura.cell(1, 4,     "Nombre")
        ws_factura.cell(1, 5,     "RFC")
        ws_factura.cell(1, 6,     "Concepto")
        ws_factura.cell(1, 7,     "Sub")
        ws_factura.cell(1, 8,     "IVA")
        ws_factura.cell(1, 9,     "Total")
        ws_factura.cell(1, 10,     "F-Pago")
        ws_factura.cell(1, 11,     "M-Pago")
        ws_factura.cell(1, 12,     "Tipo")

        row = 1
        for factura in self.facturas[self.mes]:
            row += 1
            ws_factura.cell(row, 1, factura.conceptos[0]['clave_concepto'])
            ws_factura.cell(row, 2, factura.fechaTimbrado)
            ws_factura.cell(row, 3, factura.UUID)
            ws_factura.cell(row, 4, factura.EmisorNombre)
            ws_factura.cell(row, 5, factura.EmisorRFC)
            ws_factura.cell(row, 6, factura.conceptos[0]['descripcion'])
            ws_factura.cell(row, 7, factura.subTotal)
            ws_factura.cell(row, 8, factura.traslados["IVA"]["importe"])
            ws_factura.cell(row, 9, factura.total)
            ws_factura.cell(row, 10, factura.formaDePagoStr)
            ws_factura.cell(row, 11, factura.metodoDePago)
            ws_factura.cell(row, 12, factura.conceptos[0]['tipo'])

        row += 1
        ws_factura.cell(row, 7,     "=SUM(G2:G"+str(row-1)+")")
        ws_factura.cell(row, 8,     "=SUM(H2:H"+str(row-1)+")")
        ws_factura.cell(row, 9,     "=SUM(I2:I"+str(row-1)+")")

        workbook.save(xlsx_path)


    def hazListadeUuids(self):
        self.listadeUuids = []
        for renglon in range(self.numeroDeFacturasValidas[self.mes]):
            self.listadeUuids.append(self.tables[self.mes].item(renglon,1).text())


    def handleHeaderMenu(self, pos):
        menu = QMenu()
        deleteAction = QAction('&Delete', self)
        #deleteAction = QtGui.QAction("Delete")
        deleteAction.triggered.connect(lambda: self.quitaRenglon(self.tables[self.mes].verticalHeader().logicalIndexAt(pos)))
        menu.addAction(deleteAction)

        menu.exec_(QtGui.QCursor.pos())

    def quitaRenglon(self,row):
        elNombre = self.tables[self.mes].item(row,2).text()
        suRFC = ""
        for factura in self.facturas[self.mes]:
            if factura.UUID == elNombre:
                print("i found it!")
                suRFC = factura.EmisorRFC

                break


        suSubtotal = float(self.tables[self.mes].item(row,6).text())
        suDescuento = float(self.tables[self.mes].item(row,7).text())
        suTrasladoIVA = float(self.tables[self.mes].item(row,8).text())
        suImporte = float(self.tables[self.mes].item(row,6).text())-float(self.tables[self.mes].item(row,7).text())
        self.tables[self.mes].removeRow(row)

        if suRFC in self.sumaRFC[self.mes]:
            self.sumaRFC[self.mes][suRFC]['subTotal'] -= suSubtotal
            self.sumaRFC[self.mes][suRFC]['descuento'] -= suDescuento
            self.sumaRFC[self.mes][suRFC]['trasladoIVA'] -= suTrasladoIVA
            self.sumaRFC[self.mes][suRFC]['importe'] -= suImporte

            if math.fabs(self.sumaRFC[self.mes][suRFC]['subTotal']) < 0.0001 and math.fabs(self.sumaRFC[self.mes][suRFC]['descuento']) < 0.0001 and math.fabs(self.sumaRFC[self.mes][suRFC]['trasladoIVA']) < 0.0001 and math.fabs(self.sumaRFC[self.mes][suRFC]['importe']) < 0.0001:
                self.sumaRFC[self.mes].pop(suRFC,0)


        self.numeroDeFacturasValidas[self.mes] -= 1
        self.sumale(1)


        self.hazResumenDiot(self.esteFolder)

    def sumale(self, renglonResumen=0):
        total_col = 13
        
        for i in range(6,self.tables[self.mes].columnCount()):
            estaTabla = self.tables[self.mes]
            if estaTabla.horizontalHeaderItem(i).text() == "Total":
                total_col =  i
        print(str(self.numeroDeFacturasValidas[self.mes]))
        for columna in range(6,total_col+1):
            suma = 0
            for renglon in range(self.numeroDeFacturasValidas[self.mes]):
                try:
                    suma += float(self.tables[self.mes].item(renglon, columna).text().replace(",",""))
                except:
                    print("no puedo")

    def ponEncabezado(self,lista_columnas,tabName):
        n = -1
        for columna in lista_columnas:
            n += 1
            self.tables[tabName].setHorizontalHeaderItem (n, QTableWidgetItem(columna))

    def meDoblePicaronXML(self, row,column):
        print("me picaron en : " +str(row)+", " +str(column))

        tabName = self.tabWidget.tabText(self.tabWidget.currentIndex())
        print(tabName)
        folder_mes = ""
        for file in listdir(self.year_folder):
            if tabName in file:
                folder_mes = join(self.year_folder,file,"EGRESOS")
        if column == 2:
            esteUUID = self.tables[tabName].item(row, 2).text().lower()
            for root, dirs, files in os.walk(folder_mes, topdown=False):
                for name in files:
                    if esteUUID in name.lower() and name.endswith("xml"):
                        xmlpath = os.path.join(root, name)
            try:
                print("este guey me pico:"+xmlpath)
                os.startfile(xmlpath)
            except:
                print("el sistema no tiene una aplicacion por default para abrir xmls")
                print(xmlpath)
                QMessageBox.information(self, "Information", "El sistema no tiene una aplicación por default para abrir xmls" )

        if column == 0:
            pdf = join(join(folder_mes,"huiini"),self.tables[tabName].item(row, 2).text()+".pdf")
            try:
                print("este guey me pico:"+pdf)
                os.startfile(pdf)
            except:
                print ("el sistema no tiene una aplicacion por default para abrir pdfs")
                QMessageBox.information(self, "Information", "El sistema no tiene una aplicación por default para abrir pdfs" )


    def meDoblePicaronResumen(self, row,column):
        print("me picaron en : " +str(row)+", " +str(column))
        try:
            print("este guey me pico:"+self.excel_path)
            os.startfile(self.excel_path)
            
        except:
            print ("el sistema no tiene una aplicacion por default para abrir exceles")
            QMessageBox.information(self, "Information", "El sistema no tiene una aplicación por default para abrir exceles" )



    def cambiaImpresora(self):
        # self.tabWidget.setCurrentIndex(1)
        #self.listaDeImpresoras.setEnabled(True)
        self.impresoras = impresoras_widget()
        for (a,b,name,d) in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL):
            self.impresoras.lista.addItem(name)
        self.impresoras.exec()

    def cancelaImpresion(self):
        print("cancelaria")
        phandle = win32print.OpenPrinter(win32print.GetDefaultPrinter())

        print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
        for job in print_jobs:

            print(job['TotalPages'])

            if(job['TotalPages'] >= 1):
                print(type(job))
                win32print.SetJob(phandle, job['JobId'], 0, None, win32print.JOB_CONTROL_DELETE)

        win32print.ClosePrinter(phandle)



    def imprime(self):
        #objetosMagicosOrdenados = sorted(self.objetosMagicos, key=lambda objetosMagicos: objetosMagicos.fecha)
        self.actionCancelar_Impresi_n.setEnabled(True)
        tabName = self.tabWidget.tabText(self.tabWidget.currentIndex())
        print(tabName)
        folder_mes = ""
        for file in listdir(self.year_folder):
            if tabName in file:
                folder_mes = join(self.year_folder,file,"EGRESOS","huiini")

        # if tabName == "Ingresos":
        #     pdf_path1 = join(self.year_folder,file,"EGRESOS","huiini")
        #     pdf_path2 =

        for renglon in range(0,self.tables[tabName].rowCount()-1):
            uuid = self.tables[tabName].item(renglon,2).text()
            columnaTotal = 0
            for i in range(0,self.tables[tabName].columnCount()-1):
                esteHeaderItem = self.tables[tabName].horizontalHeaderItem(i)
                if esteHeaderItem.text() == "Total":
                    columnaTotal = i

            
            if float(self.tables[tabName].item(renglon,columnaTotal).text().replace(",","")) < 0.01:
                print("no imprimo facturas con total menores a 0")
            else:
                if self.tables[tabName].item(renglon,columnaTotal+2).text() == "None":
                    print("no imprimo pagos seño")
                else:
                    pdf_path = '"'+join(folder_mes, uuid+".pdf")+'"'
                    args = '"'+self.gswin64c_path+'" ' \
                            '-sDEVICE=mswinpr2 ' \
                            '-dBATCH ' \
                            '-dNOPAUSE ' \
                            '-dFitPage ' \
                            '-dQueryUser=3 '
                    ghostscript = args + pdf_path
                    call(ghostscript, shell=True)
        
        #hh = win32api.ShellExecute(0, "print", join(join(self.esteFolder,"huiini"), "resumenDiot.pdf") , None,  ".",  0)
    def esteItem(self, text, tooltip):
        item = QTableWidgetItem(text)
        item.setToolTip(tooltip)
        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
        return item

    def esteCenteredItem(self, text, tooltip):
        item = QTableWidgetItem(QtCore.QLocale().toString(float(text),'f', 2))
        #item.setStyleSheet("padding :15px")
        item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        QtCore.QLocale().toString(float(text),'f', 2)
        item.setToolTip(tooltip)
        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
        return item


    def hazPDFs(self):
        contador = -1
        pdf_folder = join(self.esteFolder,"huiini")
        for factura in self.facturas[self.mes]:
            contador += 1
            if factura.has_pdf == False:
                xml_name = basename(factura.xml_path)
                factura.conviertemeEnTex()
                factura.conviertemeEnPDF(pdfs_folder = pdf_folder)


                factura.has_pdf = True
                self.tables[self.mes].setCellWidget(contador,0, ImgWidgetPalomita(self))

                #     else:
                #         self.tableWidget_xml.setCellWidget(contador,0, ImgWidgetTache(self))
                # except:
                #     self.tableWidget_xml.setCellWidget(contador,0, ImgWidgetTache(self))
    def borraAuxiliares(self):
        for root, dirs, files in os.walk(self.esteFolder, topdown=False):
            for name in files:
                if name.endswith(".tex") or name.endswith(".log") or name.endswith(".aux"): 
                    elpath = os.path.join(root, name)
                    try:
                        os.remove(elpath)
                    except:
                        print("no pude borrar "+name)
        self.progressBar.hide()

    def cualCarpeta(self):
        #self.folder.hide()
        file_dialog = getFilesDlg()
        file_dialog.sendPaths.connect(self.procesaCarpetas)
        file_dialog.exec()

    def quitaColumnaVacias(self,ultima,primera,tabName):
        for columna in range(ultima,primera,-1):
            suma = 0
            for renglon in range(0,self.tables[tabName].rowCount()):
                try:
                    suma += float(self.tables[tabName].item(renglon,columna).text())
                except:
                    print("estaba vacio")

            if suma < 0.00000001:
                self.tables[tabName].removeColumn(columna)

    def procesaCarpetas(self,paths):
        self.paths = paths.copy()
        self.progressBar.show()
        self.progressBar.setValue(1)

        self.tabWidget.clear()

        folder_cliente = os.path.split(os.path.split(self.paths[0])[0])[0]
        self.folder_year = os.path.split(self.paths[0])[0]
        self.json_path = join(folder_cliente, "categorias_dicc_huiini.json")
        if os.path.exists(self.json_path):
            with open(self.json_path, "r", encoding="utf-8") as jsonfile:
                self.dicc_de_categorias = json.load(jsonfile)
        else:
            self.dicc_de_categorias = {}

        self.lista_categorias_default = []

        with open(join(scriptDirectory,"categorias_default.json"), "r", encoding="utf-8") as jf:
            self.lista_categorias_default = json.load(jf)
        for categoria, claves in self.dicc_de_categorias.items():
            if not categoria in self.lista_categorias_default:
                self.lista_categorias_default.append(categoria)

        self.despliega_cliente([folder_cliente])

        self.todos_los_meses = ["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]

        self.conceptos = []
        self.yaEstaba = {}
        self.complementosDePago = {}
        self.meses = []
        print(paths[0])
        self.year_folder = os.path.split(paths[0])[0]
        same_year = True
        no_son_meses = False

        huiini_home_folder = os.path.split(os.path.split(self.year_folder)[0])[0]
        print(huiini_home_folder)
        appdatapath = os.path.expandvars('%APPDATA%\huiini')
        with open(os.path.join(appdatapath,"huiini_home_folder_path.txt"), "w") as f:
            f.write(huiini_home_folder)
        meses = []
        for path in paths:
            mes = os.path.split(path)[1]
            mes = ''.join([i for i in mes if not i.isdigit()])
            mes = mes.strip()
            meses.append(mes)
            if not mes in self.todos_los_meses:
                no_son_meses = True
            if self.year_folder != os.path.split(path)[0]:
                same_year = False

        self.paths = [tuple[1] for x in self.todos_los_meses for tuple in zip(meses,self.paths) if tuple[0] == x]

        print(self.paths)

        if not same_year or no_son_meses:
            if no_son_meses:
                QMessageBox.information(self, "Información", "no son meses")
            else:
                QMessageBox.information(self, "Información", "no son el mismo año")
        else:
            print(self.year_folder)
            year = os.path.split(os.path.split(paths[0])[0])[1]
            client = os.path.split(os.path.split(os.path.split(paths[0])[0])[0])[1]
            print(client+"_"+year)
            self.respaldo_anual = False
            if self.tiene_pdflatex:
                reply = QMessageBox.question(self, 'Message',"Crear pdfs?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    self.hacerPDFs = True
                else:
                    self.hacerPDFs = False
            else:
                self.hacerPDFs = False

            self.annual_xlsx_path = os.path.join(self.year_folder, client+"_"+year + ".xlsx")
            if os.path.isfile(self.annual_xlsx_path):#borra el anterior

                reply = QMessageBox.question(self, 'Message',"Borrar información previa?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    self.respaldo_anual = True
                    hoy = str(datetime.now()).split(".")[0].replace(" ","T").replace("-","_").replace(":","_")
                    self.respaldo_anual_path = self.annual_xlsx_path.split(".xlsx")[0]+"respaldo_"+hoy+".xlsx"
                    os.rename(self.annual_xlsx_path,self.respaldo_anual_path)





           
            self.excel_path = join(self.paths[0],"EGRESOS","huiini","resumen.xlsx")

            self.listaDeFacturasIngresos = []

            p = 0
            for path in self.paths:
                p += 1
                progreso = int(100*(p/(len(self.paths)+2)))
                self.procesaEgresos(path)
                self.pon_categorias_custom_por_factura(self.paths)
                self.pon_categorias_custom_en_gui(self.paths)
                self.quitaColumnaVacias(12,5,self.mes)
                self.agregaMes(self.mes)
                self.procesaIngresos(path)
                self.aislaNomina(path)
                self.aislaReconocibles(path)
                self.progressBar.setValue(progreso)
                # if p == 1:
                #     self.tabWidget.removeTab(0)
                #     self.tabWidget.removeTab(0)


            self.hazTabDeIngresos(self.paths)

            p += 1
            progreso = int(100*(p/(len(paths)+2)))
            self.progressBar.setValue(progreso)
            self.pon_categorias_custom_por_concepto(self.paths)
            self.hazAgregados(self.paths)
            p += 1
            progreso = int(100*(p/(len(paths)+2)))
            self.progressBar.setValue(progreso)

            if len(self.listaDeFacturasIngresos) > 0:
                self.agregaTab("Ingresos")
                self.quitaColumnaVacias(12,6,"Ingresos")
            #self.agregaTab("Conceptos")
            #self.agregaTab("IVA_anual")
            #self.agregaTab("Importe_anual")



            self.action_editar_Categor_as.setEnabled(True)
            if self.tiene_gswin64c == True:
                self.actionImprimir.setEnabled(True)
            self.excel_anual_button.setEnabled(True)
            self.raise_()
            self.activateWindow()
            self.progressBar.hide()
            if self.respaldo_anual:
                if filecmp.cmp(self.annual_xlsx_path,self.respaldo_anual_path):
                    os.remove(self.respaldo_anual_path)
                else:
                    print("se respaldó el archivo existente y el nuevo no es igual")
            curr_index = self.tabWidget.currentIndex() 
            name = self.tabWidget.tabText(curr_index)
            self.mes = name       
            self.sumale()


        if name == "Ingresos":
            print("aquí haría algo")
        else:
            self.mes = name



    def agregaTab(self, tabName):

        # or



        workbook = load_workbook(self.annual_xlsx_path, data_only=True)
        ws = workbook[tabName]
        c_max = ws.max_column - 9
        r_max = 0
        for r in range(2, ws.max_row+1):
            if ws.cell(r,1).value == None:
                r_max = r
                break


        self.tables[tabName] = QTableWidget(r_max,c_max)
        self.tabWidget.addTab(self.tables[tabName], tabName)
        self.tables[tabName].setColumnCount(c_max)

        self.tables[tabName].verticalHeader().setFixedWidth(35)
        header = self.tables[tabName].verticalHeader()
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.handleHeaderMenu)

        lc = []
        for cell in ws[1]:
            lc.append(cell.value)

        self.ponEncabezado(lc,tabName)

        # self.tables[self.mes].cellDoubleClicked.connect(self.meDoblePicaronXML)
        # self.tables[self.mes].horizontalHeader().sectionClicked.connect(self.reordena)
        for r in range(2, r_max+1):
            for c in range(1, c_max+1):
                #print(str(r),str(c))
                valor = ws.cell(r,c).value
                self.tables[tabName].setItem(r-2,c-1,self.esteItem(str(valor),str(valor)))

    def pon_categorias_custom_por_factura(self,paths):

        folder_cliente = os.path.split(os.path.split(paths[0])[0])[0]
        json_path = join(folder_cliente,"categorias_dicc_huiini.json")
        hay_categorias_custom = False
        if os.path.exists(json_path):
            hay_categorias_custom = True
            with open(json_path, "r") as jsonfile:
                self.dicc_de_categorias = json.load(jsonfile)


        if hay_categorias_custom:
            for factura in self.facturas[self.mes]:
                for concepto in factura.conceptos:
                    clave = concepto["clave_concepto"]

                    for categoria, claves in self.dicc_de_categorias.items():
                        for clave1 in claves:
                            if clave.startswith(clave1):
                                concepto["tipo"] = categoria


    def pon_categorias_custom_por_concepto(self,paths):
        folder_cliente = os.path.split(os.path.split(paths[0])[0])[0]
        json_path = join(folder_cliente,"categorias_dicc_huiini.json")
        hay_categorias_custom = False
        if os.path.exists(json_path):
            hay_categorias_custom = True
            with open(json_path, "r") as jsonfile:
                self.dicc_de_categorias = json.load(jsonfile)


        if hay_categorias_custom:
            for concepto in self.conceptos:
                clave = concepto["clave_concepto"]
                for categoria, claves in self.dicc_de_categorias.items():
                    for clave1 in claves:
                        if clave.startswith(clave1):
                            concepto["tipo"] = categoria

    def pon_categorias_custom_en_gui(self, paths):

        folder_cliente = os.path.split(os.path.split(paths[0])[0])[0]
        json_path = join(folder_cliente,"categorias_dicc_huiini.json")
        hay_categorias_custom = False
        if os.path.exists(json_path):
            hay_categorias_custom = True
            with open(json_path, "r") as jsonfile:
                self.dicc_de_categorias = json.load(jsonfile)


        if hay_categorias_custom:
            r = 0
            for factura in self.facturas[self.mes]:
                
                tooltipTipo = "\n".join(x['tipo'] for x in factura.conceptos)
                self.tables[self.mes].setItem(r,15,self.esteItem(factura.conceptos[0]['tipo'],tooltipTipo))
                r+=1

    def procesaIngresos(self, path):
        self.esteFolder = join(path,"INGRESOS")
        if os.path.isdir(self.esteFolder):
            if not os.path.exists(join(self.esteFolder, "huiini")):
                os.makedirs(join(self.esteFolder, "huiini"))
            self.mes = os.path.split(path)[1]
            self.mes = ''.join([i for i in self.mes if not i.isdigit()])
            self.mes = self.mes.strip()
            cuantosDuplicados = 0
            self.listaDeDuplicados = []
            self.listaDeFacturas = []
            self.listaDeUUIDs = []
            contador = 0
            for archivo in os.listdir(self.esteFolder):
                if archivo.endswith(".xml"):
                    try:
                        laFactura = Factura(join(self.esteFolder + os.sep,archivo))
                        if laFactura.sello == "SinSello":
                            print("Omitiendo xml sin sello "+laFactura.xml_path)
                        else:
                            if laFactura.version:
                                if laFactura.UUID in self.listaDeUUIDs:

                                    cuantosDuplicados+=1
                                    self.listaDeDuplicados.append(laFactura.UUID)
                                else:
                                    self.listaDeUUIDs.append(laFactura.UUID)
                                    contador += 1
                                    self.listaDeFacturas.append(laFactura)
                    except:
                        QMessageBox.information(self, "Information", "La factura : " + join(self.esteFolder + os.sep,archivo) + " está corrupta")

            self.facturas[self.mes] = sorted(self.listaDeFacturas, key=lambda listaDeFacturas: listaDeFacturas.fechaTimbrado)
            if cuantosDuplicados > 0:
                mensaje = "En ingresos hay "+str(cuantosDuplicados)+" duplicados\n"
                chunks = []
                for esteDuplicado in self.listaDeDuplicados:
                    chunks.append(str(esteDuplicado)+"\n")
                mensaje2 = "".join(chunks)
                mensaje = mensaje + mensaje2
                QMessageBox.information(self, "Information", mensaje)

            # for t in range(0,5):
            #     time_old.sleep(0.05*len(self.facturas[self.mes]))
            #     self.pd.setValue(self.pd.value() + ( (100 - self.pd.value()) / 2))
            contador = 0

            los_facturas = self.facturas[self.mes].copy()
            self.listaDeFacturasIngresos.extend(los_facturas)
            for factura in self.facturas[self.mes]:
                #self.pd.setValue(50*((contador + 1)/len(self.facturas[self.mes])))
                factura.setFolio(contador + 1)
                if factura.tipoDeComprobante == "P":
                    if factura.IdDocumento in self.complementosDePago:
                        self.complementosDePago[factura.IdDocumento]["suma"] += factura.ImpPagado
                    else:
                        self.complementosDePago[factura.IdDocumento] = {}
                        self.complementosDePago[factura.IdDocumento]["suma"] = factura.ImpPagado

                    self.complementosDePago[factura.IdDocumento]["fechaUltimoPago"] = factura.fechaTimbrado

            if self.hacerPDFs:
                self.hazPDFs()
                #time_old.sleep(0.1*len(self.facturas[self.mes]))
                self.borraAuxiliares()

    def aislaNomina(self, path):
        esteFolder = join(path,"EGRESOS")
        # esteFolderIngresos = join(path,"INGRESOS")
        # if not os.path.exists(esteFolderIngresos):
        #     os.makedirs(esteFolderIngresos)

        for archivo in os.listdir(esteFolder):
            if archivo.endswith(".xml"):
                try:
                    laFactura = Factura(join(esteFolder + os.sep,archivo))
                    if laFactura.tipoDeComprobante == "N":
                        if not os.path.exists(join(esteFolder, "Nomina")):
                            os.makedirs(join(esteFolder, "Nomina"))
                        try:
                            os.rename(join(esteFolder + os.sep,archivo), join(esteFolder, "Nomina",archivo))

                        except:
                            print("no pude mover una nómina")
                except:
                    print("--------------------------------------------------")

    def aislaReconocibles(self, path):
        esteFolder = join(path,"EGRESOS")
        # esteFolderIngresos = join(path,"INGRESOS")
        # if not os.path.exists(esteFolderIngresos):
        #     os.makedirs(esteFolderIngresos)

        for archivo in os.listdir(esteFolder):
            if archivo.endswith(".xml"):
                try:
                    laFactura = Factura(join(esteFolder + os.sep,archivo))
                    if laFactura.tipoDeComprobante == "P":
                        if not os.path.exists(join(esteFolder, "COMPLEMENTO_PAGO")):
                            os.makedirs(join(esteFolder, "COMPLEMENTO_PAGO"))
                        try:
                            os.rename(join(esteFolder + os.sep,archivo), join(esteFolder, "COMPLEMENTO_PAGO",archivo))

                        except:
                            print("no pude mover una COMPLEMENTO_PAGO")

                    if laFactura.tipoDeComprobante == "E":
                        if not os.path.exists(join(esteFolder, "INGRESOS_NEGATIVOS")):
                            os.makedirs(join(esteFolder, "INGRESOS_NEGATIVOS"))
                        try:
                            os.rename(join(esteFolder + os.sep,archivo), join(esteFolder, "INGRESOS_NEGATIVOS",archivo))

                        except:
                            print("no pude mover una INGRESOS_NEGATIVOS")

                    if laFactura.conceptos[0]["clave_concepto"] == "78111808":
                        if not os.path.exists(join(esteFolder, "UBER")):
                            os.makedirs(join(esteFolder, "UBER"))
                        try:
                            os.rename(join(esteFolder + os.sep,archivo), join(esteFolder, "UBER",archivo))

                        except:
                            print("no pude mover una UBER")

                    
                except:
                    print("--------------------------------------------------")

    def mueveAcarpetaCoi(self, xml_path, renglon, sender):
        print("me pico ",renglon,xml_path,sender.currentText())
        xml_dir, xml_name= os.path.split(xml_path)
        print("el xml es", xml_name)
        if os.path.split(xml_dir)[1] == "EGRESOS":
            mes_folder = xml_dir
        else:
            mes_folder = os.path.split(xml_dir)[0]
        print("el folder de egresos es ", mes_folder)
        
        for (dirpath, dirnames, filenames) in os.walk(mes_folder):
            for filename in filenames:
                if filename == xml_name: 
                    print("estaba en ", join(dirpath, filename), "y lo movere a ", join(mes_folder, sender.currentText()))
                    if sender.currentText() == "--":
                        try:
                            os.rename(join(dirpath, filename), join(mes_folder, filename))

                        except:
                            print("no pude mover el xml : ",filename ," a ",mes_folder)
                    else:
                        if not os.path.exists(join(mes_folder, sender.currentText())):
                            os.makedirs(join(mes_folder, sender.currentText()))
                        try:
                            os.rename(join(dirpath, filename), join(mes_folder, sender.currentText(),filename))

                        except:
                            print("no pude mover el xml : ",filename ," a ",sender.currentText())


    def procesaEgresos(self, path):
        #self.folder.setText("Procesando: " + u'\n' + path)
        #self.folder.show()
        self.esteFolder = join(path,"EGRESOS")
        folder_cliente = os.path.split(os.path.split(path)[0])[0]
        coi_json_path = join(folder_cliente, "carpetas_coi.json")
        if os.path.exists(coi_json_path):
            with open(coi_json_path, "r", encoding="utf-8") as jsonfile:
                lista_carpetas_coi = json.load(jsonfile)
        else:
            lista_carpetas_coi = ["--","UBER","Nomina","COMPLEMENTO_PAGO","INGRESOS_NEGATIVOS"]
        self.mes = os.path.split(path)[1]
        self.mes = ''.join([i for i in self.mes if not i.isdigit()])
        self.mes = self.mes.strip()
        self.meses.append(self.mes) # aqui si self.mes no se puede formar correctamantre deberia dar un error y ventanita que lo explique
        #self.conceptos[self.mes] = []
        self.tables[self.mes] = QTableWidget(10,20)
        self.setupTabMeses()
        self.tabWidget.addTab(self.tables[self.mes], self.mes)

        if not os.path.exists(join(self.esteFolder, "huiini")):
            os.makedirs(join(self.esteFolder, "huiini"))
        self.tables[self.mes].clear()
        lc = ["Pdf","Fecha","UUID","Receptor","Emisor","Concepto","Subtotal","Descuento","Traslado\nIVA","Traslado\nIEPS","Retención\nIVA","Retención\nISR","Total","Forma\nPago","Método\nPago","Tipo","Carpeta Coi"]
        self.ponEncabezado(lc,self.mes)
        self.tables[self.mes].setRowCount(13)
        self.tables[self.mes].repaint()
        self.delegate = PaddingDelegate()
        self.tables[self.mes].setItemDelegate(self.delegate)
        cuantosDuplicados = 0
        self.listaDeDuplicados= []
        self.listaDeFacturas = []
        self.listaDeUUIDs = []

        listaDePathsXMLS = []
        for root, dirs, files in os.walk(self.esteFolder, topdown=False):
            for name in files:
                if name.endswith(".xml"):
                    listaDePathsXMLS.append(os.path.join(root, name))
           
        contador = 0
        for xml_path in listaDePathsXMLS:
            try:
                laFactura = Factura(xml_path)
                if laFactura.sello == "SinSello":
                    print("Omitiendo xml sin sello "+laFactura.xml_path)
                else:
                    if laFactura.version:
                        if laFactura.UUID in self.listaDeUUIDs:

                            cuantosDuplicados+=1
                            self.listaDeDuplicados.append(laFactura.UUID)
                        else:
                            #if laFactura.tipoDeComprobante != "N":
                            self.listaDeUUIDs.append(laFactura.UUID)
                            contador += 1
                            self.listaDeFacturas.append(laFactura)
            except:
                QMessageBox.information(self, "Information", "El xml " + xml_path + " no está bien formado")
                print("El xml " + xml_path + " no está bien formado")

        if contador > 13:
            self.tables[self.mes].setRowCount(contador)

 
        
        self.facturas[self.mes] = sorted(self.listaDeFacturas, key=lambda listaDeFacturas: listaDeFacturas.fechaTimbrado)
        
        
        print(self.facturas[self.mes])



        if cuantosDuplicados > 0:
            mensaje = "En egresos hay "+str(cuantosDuplicados)+" duplicados\n"
            chunks = []
            for esteDuplicado in self.listaDeDuplicados:
                chunks.append(str(esteDuplicado)+"\n")
            mensaje2 = "".join(chunks)
            mensaje = mensaje + mensaje2
            QMessageBox.information(self, "Information", mensaje)

        contador = 0
          
        listacombos = []
        self.sumaRFC[self.mes] = {}
        for factura in self.facturas[self.mes]:
            listacombos.append(QComboBox())
            listacombos[contador].addItems (lista_carpetas_coi)
            xml_dir, xml_name= os.path.split(factura.xml_path)
            
            if os.path.split(xml_dir)[1] == "EGRESOS":
                mes_folder = xml_dir
            else:
                mes_folder, carpeta_actual = os.path.split(xml_dir)
                listacombos[contador].setCurrentText(carpeta_actual)
    
            #listacombos[contador].setStyleSheet("QComboBox{margin:3px};")
            listacombos[contador].currentIndexChanged.connect(lambda state, xml_path=factura.xml_path, renglon=contador, combo=listacombos[contador] : self.mueveAcarpetaCoi(xml_path,renglon,combo))
            factura.setFolio(contador + 1)
            los_conceptos = factura.conceptos.copy()
            for concepto in los_conceptos:
                concepto["mes"] = self.mes
                concepto["UUID"] = factura.UUID
                if concepto["impuestos"]:
                    concepto["impuestos"] = float(concepto['impuestos'])
                else:
                    concepto["impuestos"] = 0
                if factura.tipoDeComprobante == "E":
                    concepto["importeConcepto"] = 0.0 - float(concepto['importeConcepto'])
                    concepto["descuento"] = 0.0 - float(concepto['descuento'])
                    #concepto["subTotal"] = 0.0 - float(concepto['subTotal'])
                    concepto["impuestos"] = 0.0 - float(concepto['impuestos'])
                    #concepto["total"] = 0.0 - float(concepto['total'])

            if factura.tipoDeComprobante != "N":
                self.conceptos.extend(los_conceptos)


            if factura.tipoDeComprobante == "P":
                if factura.IdDocumento in self.complementosDePago:
                    self.complementosDePago[factura.IdDocumento]["suma"] += factura.ImpPagado
                else:
                    self.complementosDePago[factura.IdDocumento] = {}
                    self.complementosDePago[factura.IdDocumento]["suma"] = factura.ImpPagado

                self.complementosDePago[factura.IdDocumento]["fechaUltimoPago"] = factura.fechaTimbrado

            if factura.tipoDeComprobante == "N":
                self.listaDeFacturasIngresos.append(factura)

            xml_path = factura.xml_path

            files = {'files': open(xml_path , 'rb')}

            self.tables[self.mes].setItem(contador,1,self.esteItem(factura.fechaTimbrado,factura.fechaTimbrado))
            self.tables[self.mes].setItem(contador,2,self.esteItem(factura.UUID,factura.UUID))
            self.tables[self.mes].setItem(contador,3,self.esteItem(factura.ReceptorRFC,factura.ReceptorNombre))
            self.tables[self.mes].setItem(contador,4,self.esteItem(factura.EmisorRFC,factura.EmisorNombre))
            mesage = ""
            for concepto in factura.conceptos:
                mesage += self.concepto[concepto["clave_concepto"]] + u'\n'
            self.tables[self.mes].setItem(contador,5, self.esteItem(factura.conceptos[0]['descripcion'],mesage))
            self.tables[self.mes].setItem(contador,6,self.esteCenteredItem(str(factura.subTotal),""))
            self.tables[self.mes].setItem(contador,7,self.esteCenteredItem(str(factura.descuento),""))
            self.tables[self.mes].setItem(contador,8,self.esteCenteredItem(str(factura.traslados["IVA"]["importe"]),""))
            self.tables[self.mes].setItem(contador,9,self.esteCenteredItem(str(factura.traslados["IEPS"]["importe"]),""))
            self.tables[self.mes].setItem(contador,10,self.esteCenteredItem(str(factura.retenciones["IVA"]),""))
            self.tables[self.mes].setItem(contador,11,self.esteCenteredItem(str(factura.retenciones["ISR"]),""))
            self.tables[self.mes].setItem(contador,12,self.esteCenteredItem(str(factura.total),""))
            self.tables[self.mes].setItem(contador,13,self.esteItem(factura.formaDePagoStr,""))
            self.tables[self.mes].setItem(contador,14, self.esteItem(factura.metodoDePago,factura.metodoDePago))
            tooltipTipo = "\n".join(x['tipo'] for x in factura.conceptos)
            self.tables[self.mes].setItem(contador,15, self.esteItem(factura.conceptos[0]['tipo'],tooltipTipo))
            self.tables[self.mes].setCellWidget(contador,16,listacombos[contador])
           
            pdf_dir = os.path.join(self.esteFolder,"huiini")
            pdf_name = os.path.split(factura.tex_path)[1].replace("tex","pdf")
            pdf_path = os.path.join(pdf_dir, pdf_name)
            if os.path.exists(pdf_path):
                self.tables[self.mes].setCellWidget(contador,0, ImgWidgetPalomita(self))
            
            if factura.EmisorRFC in self.sumaRFC[self.mes]:
                self.sumaRFC[self.mes][factura.EmisorRFC]['subTotal'] += float(factura.subTotal)
                self.sumaRFC[self.mes][factura.EmisorRFC]['descuento'] += float(factura.descuento)
                self.sumaRFC[self.mes][factura.EmisorRFC]['trasladoIVA'] += float(factura.traslados['IVA']['importe'])
                self.sumaRFC[self.mes][factura.EmisorRFC]['importe'] += float(factura.subTotal)-float(factura.descuento)
                self.sumaRFC[self.mes][factura.EmisorRFC]['total'] += float(factura.total)
                self.sumaRFC[self.mes][factura.EmisorRFC]['importeStr'] += "+"+str(float(factura.subTotal)-float(factura.descuento))
                self.sumaRFC[self.mes][factura.EmisorRFC]['trasladoIVAStr'] += "+"+str(factura.traslados['IVA']['importe'])
                print("sumale " + str(factura.subTotal) )
            else:
                self.sumaRFC[self.mes][factura.EmisorRFC] = {'subTotal': float(factura.subTotal),
                                                              'descuento': float(factura.descuento),
                                                              'trasladoIVA': float(factura.traslados['IVA']['importe']),
                                                              'importe': float(factura.subTotal)-float(factura.descuento),
                                                              'total': float(factura.total),
                                                              'importeStr': "="+str(float(factura.subTotal)-float(factura.descuento)),
                                                              'trasladoIVAStr': "="+str(factura.traslados['IVA']['importe']),
                                                              'nombre': factura.EmisorNombre
                                                            }
                print("crealo con " + str(factura.subTotal))

            contador += 1

        if self.hacerPDFs:
            self.hazPDFs()
            #time_old.sleep(0.2*len(self.facturas[self.mes]))
            self.borraAuxiliares()


        contador = -1

        # time_old.sleep(0.5*len(self.facturas[self.mes]))

        self.numeroDeFacturasValidas[self.mes] = len(self.facturas[self.mes])


        self.sumale()

        self.hazResumenDiot(self.esteFolder)
        #if len(paths)>2:
        #obtener los warnings de las facturas
        mensajeAlerta =""
        for factura in self.facturas[self.mes]:
            if not factura.mensaje == "":
                mensajeAlerta += factura.UUID + factura.mensaje + r'\n'
        if not mensajeAlerta == "":
            QMessageBox.information(self, "Information", mensajeAlerta)




        #self.folder.setText("Carpeta Procesada: " + u'\n' + self.esteFolder)
        #self.folder.show()

        

class WheelEventFilter(QtCore.QObject):
    def eventFilter(self, obj, ev):
        if obj.inherits("QComboBox") and ev.type() == QtCore.QEvent.Wheel:
            return True
        return False
class PaddingDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, padding=5, parent=None):
        super(PaddingDelegate, self).__init__(parent)
        self._padding = ' ' * max(1, padding)


    def is_num(self,s):
        try:
            float(s.replace(',',''))
        except ValueError:
            return False
        else:
            return True

    def displayText(self, text, locale):
        if self.is_num(text):
            return text + self._padding
        else:
            return self._padding + text

    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        margins = editor.textMargins()
        padding = editor.fontMetrics().width(self._padding) + 1
        margins.setLeft(margins.left() + padding)
        editor.setTextMargins(margins)
        return editor




#app = QtWidgets.QApplication.instance()
app = QtWidgets.QApplication(sys.argv)
filter = WheelEventFilter()
app.installEventFilter(filter)
app.setStyleSheet("QMessageBox { messagebox-text-interaction-flags: 5; }")
form = Ui_MainWindow()
form.show()


app.exec_()
