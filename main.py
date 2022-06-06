import os
import sys
import platform

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (
    QSlider,
    QLabel,
    QWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QApplication
)

from modules import *
from widgets import *

import pandas as pd
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # QMainWindow.__init__(self)

        # Create the matplotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        # sc = MplCanvas(self, width=5, height=4, dpi=100)
        # sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # self.vertical_layout = QVBoxLayout()
        #
        # self.widget_matplotlib = QWidget()
        # self.widget_matplotlib.set_layout(self.vertical_layout)

        # Instead of calling .setCentralWidget(),
        # we call it by its snake-case name...
        # self.set_central_widget(self.widget_matplotlib)

        # self.setCentralWidget(sc)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # widget_matplotlib = self.ui.widget

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "CalliduStocks"
        description = "CalliduStocks - Trading App"

        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        ###################################################
        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_portfolio.clicked.connect(self.buttonClick)
        widgets.btn_processing.clicked.connect(self.buttonClick)
        widgets.btn_graphs.clicked.connect(self.buttonClick)
        widgets.btn_recommended.clicked.connect(self.buttonClick)
        widgets.btn_no_recommended.clicked.connect(self.buttonClick)
        widgets.btn_recent.clicked.connect(self.buttonClick)

        # SLIDER FOR CHANGING THEME
        widgets.horizontalSlider_2.valueChanged.connect(self.changeTheme)

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
            UIFunctions.theme(self, "dark")
            AppFunctions.setDarkThemeHack(self)  # SET HACKS
        elif value == 1:
            UIFunctions.theme(self, "light")
            AppFunctions.setLightThemeHack(self)  # SET HACKS

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

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

        # SHOW NO RECOMMENDED PAGE
        if btnName == "btn_no_recommended":
            widgets.stackedWidget.setCurrentWidget(widgets.no_recommended)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHER BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # SHOW RECENT PAGE
        if btnName == "btn_recent":
            widgets.stackedWidget.setCurrentWidget(widgets.recent)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHER BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

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
