import os
import sys
import platform
import random

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (
    QSlider,
    QLabel,
    QWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QApplication,
    QDialog,
    QFileDialog
)

from modules import *
from widgets import *

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class Matplotlib(QDialog):
    def __init__(self, parent=None):
        super(Matplotlib, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure' it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvasQTAgg(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding toolbar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # setting layout to the main window
        self.setLayout(layout)

        self.plot()

    # function for draw graph
    def plot(self):
        # random data
        data = [random.random() for i in range(10)]

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.matplotlib_graph = Matplotlib(self)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "CalliduStocks"

        # APPLY TEXTS
        self.setWindowTitle(title)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # widgets.tableWidget.horizontalHeader().setStretchLastSection(True)
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        ###################################################
        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_portfolio.clicked.connect(self.buttonClick)
        widgets.btn_processing.clicked.connect(self.buttonClick)
        widgets.btn_graphs.clicked.connect(self.buttonClick)
        widgets.btn_recommended.clicked.connect(self.buttonClick)

        # SLIDER FOR CHANGING THEME
        widgets.horizontalSlider_2.valueChanged.connect(self.changeTheme)

        # OPEN TICKERS FILE BUTTON
        widgets.importTickersFileButton.clicked.connect(self.buttonClick)

        # LOAD TICKERS FROM FILE BUTTON
        widgets.loadTickersFromFileButton.clicked.connect(self.buttonClick)

        # PORTFOLIO PAGE BUTTONS
        widgets.trackButton.clicked.connect(self.buttonClick)
        widgets.untrackButton.clicked.connect(self.buttonClick)
        widgets.trackAllButton.clicked.connect(self.buttonClick)
        widgets.untrackAllButton.clicked.connect(self.buttonClick)

        # GRAPHS PAGE BUTTONS
        widgets.showDefaultGraphButton.clicked.connect(self.buttonClick)
        widgets.showLogarithmicGraphButton.clicked.connect(self.buttonClick)
        widgets.showBetaDistributionGraphButton.clicked.connect(self.buttonClick)
        widgets.saveSelectedGraphButton.clicked.connect(self.buttonClick)
        widgets.saveAllGraphsButton.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        self.show()

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def changeTheme(self, value):
        """
        Change theme mode realization.\n
        :param value: Value of slider, 0 - Dark mode, 1 - Light mode
        """

        if value == 0:
            mode = "Dark Mode"
        elif value == 1:
            mode = "Light Mode"
        UIFunctions.theme(self, mode)
        widgets.titleRightInfo.setText(mode)  # SET TEXT DESCRIPTION
        AppFunctions.setThemeHack(self, mode)  # SET HACKS

    @staticmethod
    def load_data_to_table():
        quotes = [
            {"ticker": "AAPL", "currency": "USD", "period": 300},
            {"ticker": "MCD", "currency": "USD", "period": 300}
        ]
        widgets.tableWidget.setItem(2, 0, QTableWidgetItem("Ticker"))

    def import_tickers_list(self):
        file_path = widgets.filePathLineEdit.text()
        with open(file_path, 'r', encoding='utf-8') as tickers_file:
            tickers = tickers_file.read().split()
            for ticker in tickers:
                widgets.importedTickersListWidget.addItem(ticker)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # PAGES ###################################
        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHER BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # SHOW PORTFOLIO PAGE
        if btnName == "btn_portfolio":
            widgets.stackedWidget.setCurrentWidget(widgets.portfolio)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHER BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # SHOW PROCESSING PAGE
        if btnName == "btn_processing":
            widgets.stackedWidget.setCurrentWidget(widgets.processing)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHER BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # SHOW GRAPHS PAGE
        if btnName == "btn_graphs":
            widgets.stackedWidget.setCurrentWidget(widgets.graphs)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHER BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # SHOW RECOMMENDED PAGE
        if btnName == "btn_recommended":
            widgets.stackedWidget.setCurrentWidget(widgets.recommended)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHER BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        ###############################################################
        # OPEN FILE DIALOG
        if btnName == "importTickersFileButton":
            file_path = QFileDialog.getOpenFileName(self, 'Open', filter='Текстовые файлы (*.txt)')
            widgets.filePathLineEdit.setText(file_path[0])

        # IMPORT TICKERS FROM FILE FROM PATH
        if btnName == "loadTickersFromFileButton":
            file_path = widgets.filePathLineEdit.text()
            try:
                with open(file_path, 'r', encoding='utf-8') as tickers_file:
                    # CHECK TXT FILE IS EMPTY
                    tickers_file.seek(0, os.SEEK_END)  # go to end of file
                    if tickers_file.tell():  # if current position is true (i.e != 0)
                        tickers_file.seek(0)  # rewind the file for later use
                    else:
                        QtWidgets.QMessageBox().about(self, "Ошибка", "Файл пуст.")
                    # IF FILE ISN'T EMPTY -> IMPORT TICKERS TO LISTBOX
                    self.import_tickers_list()
            except FileNotFoundError:
                QtWidgets.QMessageBox().about(self, "Ошибка", "Некорректный путь к файлу.")

        # PORTFOLIO PAGE BUTTON >
        if btnName == "trackButton":
            current_row = widgets.importedTickersListWidget.currentRow()
            selected_ticker = widgets.importedTickersListWidget.takeItem(current_row)
            widgets.selectedTickersListWidget.addItem(selected_ticker)

        # PORTFOLIO PAGE BUTTON <
        if btnName == "untrackButton":
            current_row = widgets.selectedTickersListWidget.currentRow()
            selected_ticker = widgets.selectedTickersListWidget.takeItem(current_row)
            widgets.importedTickersListWidget.addItem(selected_ticker)

        # PORTFOLIO PAGE BUTTON >>
        if btnName == "trackAllButton":
            selected_tickers = []
            for item in range(widgets.importedTickersListWidget.count()):
                items = widgets.importedTickersListWidget.item(item)
                selected_tickers.append(items.text())
            for ticker in selected_tickers:
                widgets.selectedTickersListWidget.addItem(ticker)
            widgets.importedTickersListWidget.clear()

        # PORTFOLIO PAGE BUTTON <<
        if btnName == "untrackAllButton":
            selected_tickers = []
            for item in range(widgets.selectedTickersListWidget.count()):
                items = widgets.selectedTickersListWidget.item(item)
                selected_tickers.append(items.text())
            for ticker in selected_tickers:
                widgets.importedTickersListWidget.addItem(ticker)
            widgets.selectedTickersListWidget.clear()

        # GRAPHS PAGE BUTTONS
        if btnName == "showDefaultGraphButton":
            self.matplotlib_graph.show()

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
