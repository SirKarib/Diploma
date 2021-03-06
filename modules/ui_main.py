# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainLZRMUy.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 680)
        MainWindow.setMinimumSize(QSize(1100, 680))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "\n"
                                      "SET APP STYLESHEET - FULL STYLES HERE\n"
                                      "DARK THEME - DRACULA COLOR BASED\n"
                                      "\n"
                                      "///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
                                      "\n"
                                      "QWidget{\n"
                                      "	color: rgb(221, 221, 221);\n"
                                      "	font: 10pt \"Segoe UI\";\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Tooltip */\n"
                                      "QToolTip {\n"
                                      "	color: #ffffff;\n"
                                      "	background-color: rgba(33, 37, 43, 180);\n"
                                      "	border: 1px solid rgb(44, 49, 58);\n"
                                      "	background-image: none;\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 2px solid rgb(255, 121, 198);\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 8px;\n"
                                      "	margin: 0px;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Bg App */\n"
                                      "#bgApp {	\n"
                                      "	background"
                                      "-color: rgb(40, 44, 52);\n"
                                      "	border: 1px solid rgb(44, 49, 58);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Left Menu */\n"
                                      "#leftMenuBg {	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "}\n"
                                      "#topLogo {\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	background-image: url(:/images/images/images/PyDracula.png);\n"
                                      "	background-position: centered;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "}\n"
                                      "#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
                                      "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
                                      "\n"
                                      "/* MENUS */\n"
                                      "#topMenu .QPushButton {	\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid transparent;\n"
                                      "	background-color: transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "}\n"
                                      "#topMenu .QPushButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#topMenu .QPushButton:pressed {	\n"
                                      "	background-color: rgb(18"
                                      "9, 147, 249);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton {	\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 20px solid transparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton:pressed {	\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "#leftMenuFrame{\n"
                                      "	border-top: 3px solid rgb(44, 49, 58);\n"
                                      "}\n"
                                      "\n"
                                      "/* Toggle Button */\n"
                                      "#toggleButton {\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 20px solid transparent;\n"
                                      "	background-color: rgb(37, 41, 48);\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "	color: rgb(113, 126, 149);\n"
                                      "}\n"
                                      "#toggleButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#toggleButton:pressed {\n"
                                      "	background-color: rgb("
                                      "189, 147, 249);\n"
                                      "}\n"
                                      "\n"
                                      "/* Title Menu */\n"
                                      "#titleRightInfo { padding-left: 10px; }\n"
                                      "\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Extra Tab */\n"
                                      "#extraLeftBox {	\n"
                                      "	background-color: rgb(44, 49, 58);\n"
                                      "}\n"
                                      "#extraTopBg{	\n"
                                      "	background-color: rgb(189, 147, 249)\n"
                                      "}\n"
                                      "\n"
                                      "/* Icon */\n"
                                      "#extraIcon {\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	background-image: url(:/icons/images/icons/icon_settings.png);\n"
                                      "}\n"
                                      "\n"
                                      "/* Label */\n"
                                      "#extraLabel { color: rgb(255, 255, 255); }\n"
                                      "\n"
                                      "/* Btn Close */\n"
                                      "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                      "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
                                      "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
                                      "\n"
                                      "/* Extra Content */\n"
                                      "#extraContent{\n"
                                      "	border"
                                      "-top: 3px solid rgb(40, 44, 52);\n"
                                      "}\n"
                                      "\n"
                                      "/* Extra Top Menus */\n"
                                      "#extraTopMenu .QPushButton {\n"
                                      "background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid transparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "}\n"
                                      "#extraTopMenu .QPushButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#extraTopMenu .QPushButton:pressed {	\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Content App */\n"
                                      "#contentTopBg{	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "}\n"
                                      "#contentBottom{\n"
                                      "	border-top: 3px solid rgb(44, 49, 58);\n"
                                      "}\n"
                                      "\n"
                                      "/* Top Buttons */\n"
                                      "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                      "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                                      "le: solid; border-radius: 4px; }\n"
                                      "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
                                      "\n"
                                      "/* Theme Settings */\n"
                                      "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
                                      "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
                                      "\n"
                                      "/* Bottom Bar */\n"
                                      "#bottomBar { background-color: rgb(44, 49, 58); }\n"
                                      "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
                                      "\n"
                                      "/* CONTENT SETTINGS */\n"
                                      "/* MENUS */\n"
                                      "#contentSettings .QPushButton {	\n"
                                      "	background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid transparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "}\n"
                                      "#contentSettings .QPushButton:hover {\n"
                                      "	background-color: rgb(40, 44, 52);\n"
                                      "}\n"
                                      "#contentSettings .QPushButton:pressed {	\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "	color: rgb"
                                      "(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "QTableWidget */\n"
                                      "QTableWidget {	\n"
                                      "	background-color: transparent;\n"
                                      "	padding: 10px;\n"
                                      "	border-radius: 5px;\n"
                                      "	gridline-color: rgb(44, 49, 58);\n"
                                      "	border-bottom: 1px solid rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::item{\n"
                                      "	border-color: rgb(44, 49, 60);\n"
                                      "	padding-left: 5px;\n"
                                      "	padding-right: 5px;\n"
                                      "	gridline-color: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::item:selected{\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "}\n"
                                      "QHeaderView::section{\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	max-width: 30px;\n"
                                      "	border: 1px solid rgb(44, 49, 58);\n"
                                      "	border-style: none;\n"
                                      "    border-bottom: 1px solid rgb(44, 49, 60);\n"
                                      "    border-right: 1px solid rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::horizontalHeader {	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "}\n"
                                      "QHeaderView::section:horizontal\n"
                                      "{\n"
                                      "    border: 1px solid rgb(33, 37, 43);\n"
                                      "	background-co"
                                      "lor: rgb(33, 37, 43);\n"
                                      "	padding: 3px;\n"
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "}\n"
                                      "QHeaderView::section:vertical\n"
                                      "{\n"
                                      "    border: 1px solid rgb(44, 49, 60);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "LineEdit */\n"
                                      "QLineEdit {\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(33, 37, 43);\n"
                                      "	padding-left: 10px;\n"
                                      "	selection-color: rgb(255, 255, 255);\n"
                                      "	selection-background-color: rgb(255, 121, 198);\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "PlainTextEdit */\n"
                                      "QPlainTextEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	padding: 10px;\n"
                                      "	selection-color: rgb(255, 255, 255);\n"
                                      "	selection-background-c"
                                      "olor: rgb(255, 121, 198);\n"
                                      "}\n"
                                      "QPlainTextEdit  QScrollBar:vertical {\n"
                                      "    width: 8px;\n"
                                      " }\n"
                                      "QPlainTextEdit  QScrollBar:horizontal {\n"
                                      "    height: 8px;\n"
                                      " }\n"
                                      "QPlainTextEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QPlainTextEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "ScrollBars */\n"
                                      "QScrollBar:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    height: 8px;\n"
                                      "    margin: 0px 21px 0 21px;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal {\n"
                                      "    background: rgb(189, 147, 249);\n"
                                      "    min-width: 25px;\n"
                                      "	border-radius: 4px\n"
                                      "}\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      "	border-top-right-radius: 4px;\n"
                                      "    border-bottom-right-radius: 4px;\n"
                                      "    subcontrol-position: right;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      ""
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      "	border-top-left-radius: 4px;\n"
                                      "    border-bottom-left-radius: 4px;\n"
                                      "    subcontrol-position: left;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      " QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 8px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      " }\n"
                                      " QScrollBar::handle:vertical {	\n"
                                      "	background: rgb(189, 147, 249);\n"
                                      "    min-height: 25px;\n"
                                      "	border-radius: 4px\n"
                                      " }\n"
                                      " QScrollBar::add-line:vertical {\n"
                                      "     border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "     height: 20px;\n"
                                      "	border-bottom-left-radius: 4px;\n"
                                      "    border-bottom-right-radius: 4px;\n"
                                      "     subcontrol-position: bottom;\n"
                                      "     su"
                                      "bcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::sub-line:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "     height: 20px;\n"
                                      "	border-top-left-radius: 4px;\n"
                                      "    border-top-right-radius: 4px;\n"
                                      "     subcontrol-position: top;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "CheckBox */\n"
                                      "QCheckBox::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "    background: 3px solid rgb(52, 59, 72);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "	back"
                                      "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "RadioButton */\n"
                                      "QRadioButton::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QRadioButton::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QRadioButton::indicator:checked {\n"
                                      "    background: 3px solid rgb(94, 106, 130);\n"
                                      "	border: 3px solid rgb(52, 59, 72);	\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "ComboBox */\n"
                                      "QComboBox{\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(33, 37, 43);\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subco"
                                      "ntrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-left-width: 3px;\n"
                                      "	border-left-color: rgba(39, 44, 54, 150);\n"
                                      "	border-left-style: solid;\n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      " }\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: rgb(255, 121, 198);	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: rgb(39, 44, 54);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Sliders */\n"
                                      "QSlider::groove:horizontal {\n"
                                      "    border-radius: 5px;\n"
                                      "    height: 10px;\n"
                                      "	margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:horizontal:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal {\n"
                                      "    background-color: rgb(189, 147, 249);\n"
                                      "    border: none;\n"
                                      "    h"
                                      "eight: 10px;\n"
                                      "    width: 10px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:hover {\n"
                                      "    background-color: rgb(195, 155, 255);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:pressed {\n"
                                      "    background-color: rgb(255, 121, 198);\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:vertical {\n"
                                      "    border-radius: 5px;\n"
                                      "    width: 10px;\n"
                                      "    margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:vertical:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:vertical {\n"
                                      "    background-color: rgb(189, 147, 249);\n"
                                      "	border: none;\n"
                                      "    height: 10px;\n"
                                      "    width: 10px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QSlider::handle:vertical:hover {\n"
                                      "    background-color: rgb(195, 155, 255);\n"
                                      "}\n"
                                      "QSlider::handle:vertical:pressed {\n"
                                      "    background-color: rgb(255, 121, 198);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "CommandLinkButton */\n"
                                      "QCommandLi"
                                      "nkButton {	\n"
                                      "	color: rgb(255, 121, 198);\n"
                                      "	border-radius: 5px;\n"
                                      "	padding: 5px;\n"
                                      "	color: rgb(255, 170, 255);\n"
                                      "}\n"
                                      "QCommandLinkButton:hover {	\n"
                                      "	color: rgb(255, 170, 255);\n"
                                      "	background-color: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCommandLinkButton:pressed {	\n"
                                      "	color: rgb(189, 147, 249);\n"
                                      "	background-color: rgb(52, 58, 71);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Button */\n"
                                      "#pagesContainer QPushButton {\n"
                                      "	border: 2px solid rgb(52, 59, 72);\n"
                                      "	border-radius: 5px;	\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "#pagesContainer QPushButton:hover {\n"
                                      "	background-color: rgb(57, 65, 80);\n"
                                      "	border: 2px solid rgb(61, 70, 86);\n"
                                      "}\n"
                                      "#pagesContainer QPushButton:pressed {	\n"
                                      "	background-color: rgb(35, 40, 49);\n"
                                      "	border: 2px solid rgb(43, 50, 61);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuBg.sizePolicy().hasHeightForWidth())
        self.leftMenuBg.setSizePolicy(sizePolicy)
        self.leftMenuBg.setMinimumSize(QSize(200, 0))
        self.leftMenuBg.setMaximumSize(QSize(200, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_portfolio = QPushButton(self.topMenu)
        self.btn_portfolio.setObjectName(u"btn_portfolio")
        sizePolicy1.setHeightForWidth(self.btn_portfolio.sizePolicy().hasHeightForWidth())
        self.btn_portfolio.setSizePolicy(sizePolicy1)
        self.btn_portfolio.setMinimumSize(QSize(0, 45))
        self.btn_portfolio.setFont(font)
        self.btn_portfolio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_portfolio.setLayoutDirection(Qt.LeftToRight)
        self.btn_portfolio.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-briefcase.png);")

        self.verticalLayout_8.addWidget(self.btn_portfolio)

        self.btn_processing = QPushButton(self.topMenu)
        self.btn_processing.setObjectName(u"btn_processing")
        sizePolicy1.setHeightForWidth(self.btn_processing.sizePolicy().hasHeightForWidth())
        self.btn_processing.setSizePolicy(sizePolicy1)
        self.btn_processing.setMinimumSize(QSize(0, 45))
        self.btn_processing.setFont(font)
        self.btn_processing.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_processing.setLayoutDirection(Qt.LeftToRight)
        self.btn_processing.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-code.png);")

        self.verticalLayout_8.addWidget(self.btn_processing)

        self.btn_graphs = QPushButton(self.topMenu)
        self.btn_graphs.setObjectName(u"btn_graphs")
        sizePolicy1.setHeightForWidth(self.btn_graphs.sizePolicy().hasHeightForWidth())
        self.btn_graphs.setSizePolicy(sizePolicy1)
        self.btn_graphs.setMinimumSize(QSize(0, 45))
        self.btn_graphs.setFont(font)
        self.btn_graphs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_graphs.setLayoutDirection(Qt.LeftToRight)
        self.btn_graphs.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_8.addWidget(self.btn_graphs)

        self.toggleBox = QFrame(self.topMenu)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_recommended = QPushButton(self.toggleBox)
        self.btn_recommended.setObjectName(u"btn_recommended")
        sizePolicy1.setHeightForWidth(self.btn_recommended.sizePolicy().hasHeightForWidth())
        self.btn_recommended.setSizePolicy(sizePolicy1)
        self.btn_recommended.setMinimumSize(QSize(0, 45))
        self.btn_recommended.setFont(font)
        self.btn_recommended.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recommended.setLayoutDirection(Qt.LeftToRight)
        self.btn_recommended.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-thumb-up.png);")

        self.verticalLayout_4.addWidget(self.btn_recommended)


        self.verticalLayout_8.addWidget(self.toggleBox)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-description.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 0, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_creators = QPushButton(self.extraTopMenu)
        self.btn_creators.setObjectName(u"btn_creators")
        sizePolicy1.setHeightForWidth(self.btn_creators.sizePolicy().hasHeightForWidth())
        self.btn_creators.setSizePolicy(sizePolicy1)
        self.btn_creators.setMinimumSize(QSize(0, 45))
        self.btn_creators.setFont(font)
        self.btn_creators.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_creators.setLayoutDirection(Qt.LeftToRight)
        self.btn_creators.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_11.addWidget(self.btn_creators)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.themeModeSlider = QSlider(self.leftBox)
        self.themeModeSlider.setObjectName(u"themeModeSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.themeModeSlider.sizePolicy().hasHeightForWidth())
        self.themeModeSlider.setSizePolicy(sizePolicy3)
        self.themeModeSlider.setMinimumSize(QSize(25, 35))
        self.themeModeSlider.setMaximumSize(QSize(25, 16777215))
        self.themeModeSlider.setFont(font)
        self.themeModeSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.themeModeSlider.setMaximum(1)
        self.themeModeSlider.setPageStep(2)
        self.themeModeSlider.setValue(0)
        self.themeModeSlider.setSliderPosition(0)
        self.themeModeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.themeModeSlider)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy4)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
                                "background-position: center;\n"
                                "background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.portfolio = QWidget()
        self.portfolio.setObjectName(u"portfolio")
        self.portfolio.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.portfolio)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_portfolio = QFrame(self.portfolio)
        self.frame_portfolio.setObjectName(u"frame_portfolio")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_portfolio.sizePolicy().hasHeightForWidth())
        self.frame_portfolio.setSizePolicy(sizePolicy5)
        self.frame_portfolio.setMinimumSize(QSize(0, 550))
        self.frame_portfolio.setFrameShape(QFrame.StyledPanel)
        self.frame_portfolio.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_portfolio)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_import_file = QFrame(self.frame_portfolio)
        self.frame_div_import_file.setObjectName(u"frame_div_import_file")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_div_import_file.sizePolicy().hasHeightForWidth())
        self.frame_div_import_file.setSizePolicy(sizePolicy6)
        self.frame_div_import_file.setMinimumSize(QSize(0, 110))
        self.frame_div_import_file.setMaximumSize(QSize(16777215, 110))
        self.frame_div_import_file.setFrameShape(QFrame.NoFrame)
        self.frame_div_import_file.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_import_file)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_importFile = QFrame(self.frame_div_import_file)
        self.frame_title_importFile.setObjectName(u"frame_title_importFile")
        self.frame_title_importFile.setMaximumSize(QSize(16777215, 35))
        self.frame_title_importFile.setFrameShape(QFrame.StyledPanel)
        self.frame_title_importFile.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_importFile)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.importFileLabel = QLabel(self.frame_title_importFile)
        self.importFileLabel.setObjectName(u"importFileLabel")
        self.importFileLabel.setFont(font)
        self.importFileLabel.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.importFileLabel)


        self.verticalLayout_17.addWidget(self.frame_title_importFile)

        self.frame_import_file = QFrame(self.frame_div_import_file)
        self.frame_import_file.setObjectName(u"frame_import_file")
        self.frame_import_file.setFrameShape(QFrame.NoFrame)
        self.frame_import_file.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_import_file)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.importFileLayout = QGridLayout()
        self.importFileLayout.setObjectName(u"importFileLayout")
        self.importFileLayout.setContentsMargins(-1, -1, -1, 0)
        self.importFileDescriptionLabel = QLabel(self.frame_import_file)
        self.importFileDescriptionLabel.setObjectName(u"importFileDescriptionLabel")
        self.importFileDescriptionLabel.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.importFileDescriptionLabel.setLineWidth(1)
        self.importFileDescriptionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.importFileLayout.addWidget(self.importFileDescriptionLabel, 1, 0, 1, 2)

        self.filePathLineEdit = QLineEdit(self.frame_import_file)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setMinimumSize(QSize(0, 30))
        self.filePathLineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.importFileLayout.addWidget(self.filePathLineEdit, 0, 0, 1, 1)

        self.importTickersFileButton = QPushButton(self.frame_import_file)
        self.importTickersFileButton.setObjectName(u"importTickersFileButton")
        self.importTickersFileButton.setMinimumSize(QSize(150, 30))
        self.importTickersFileButton.setFont(font)
        self.importTickersFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.importTickersFileButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importTickersFileButton.setIcon(icon4)

        self.importFileLayout.addWidget(self.importTickersFileButton, 0, 1, 1, 1)


        self.horizontalLayout_9.addLayout(self.importFileLayout)


        self.verticalLayout_17.addWidget(self.frame_import_file)


        self.verticalLayout_16.addWidget(self.frame_div_import_file, 0, Qt.AlignTop)

        self.frame_div_buttons_load_start = QFrame(self.frame_portfolio)
        self.frame_div_buttons_load_start.setObjectName(u"frame_div_buttons_load_start")
        sizePolicy6.setHeightForWidth(self.frame_div_buttons_load_start.sizePolicy().hasHeightForWidth())
        self.frame_div_buttons_load_start.setSizePolicy(sizePolicy6)
        self.frame_div_buttons_load_start.setMinimumSize(QSize(0, 50))
        self.frame_div_buttons_load_start.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.frame_div_buttons_load_start)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.loadTickersFromFileButton = QPushButton(self.frame_div_buttons_load_start)
        self.loadTickersFromFileButton.setObjectName(u"loadTickersFromFileButton")
        self.loadTickersFromFileButton.setMinimumSize(QSize(230, 40))
        self.loadTickersFromFileButton.setMaximumSize(QSize(16777215, 16777215))
        self.loadTickersFromFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loadTickersFromFileButton.setIcon(icon5)

        self.horizontalLayout_11.addWidget(self.loadTickersFromFileButton)

        self.pushButton = QPushButton(self.frame_div_buttons_load_start)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 40))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.horizontalLayout_11.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_div_buttons_load_start)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(150, 40))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_11.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_div_buttons_load_start)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(140, 40))
        self.pushButton_2.setCursor(QCursor(Qt.OpenHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)

        self.horizontalLayout_11.addWidget(self.pushButton_2)


        self.verticalLayout_16.addWidget(self.frame_div_buttons_load_start, 0, Qt.AlignLeft)

        self.frame_div_select_tickers = QFrame(self.frame_portfolio)
        self.frame_div_select_tickers.setObjectName(u"frame_div_select_tickers")
        sizePolicy4.setHeightForWidth(self.frame_div_select_tickers.sizePolicy().hasHeightForWidth())
        self.frame_div_select_tickers.setSizePolicy(sizePolicy4)
        self.frame_div_select_tickers.setMinimumSize(QSize(0, 200))
        self.frame_div_select_tickers.setSizeIncrement(QSize(0, 0))
        self.frame_div_select_tickers.setBaseSize(QSize(0, 0))
        self.importAndSelectTickersHorizontalLayout = QHBoxLayout(self.frame_div_select_tickers)
        self.importAndSelectTickersHorizontalLayout.setObjectName(u"importAndSelectTickersHorizontalLayout")
        self.importAndSelectTickersHorizontalLayout.setContentsMargins(0, 10, 0, 10)
        self.importedTickersListLayout = QVBoxLayout()
        self.importedTickersListLayout.setObjectName(u"importedTickersListLayout")
        self.importedTickersListLayout.setContentsMargins(-1, 0, -1, 0)
        self.importedTickersListWidget = QListWidget(self.frame_div_select_tickers)
        self.importedTickersListWidget.setObjectName(u"importedTickersListWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.importedTickersListWidget.sizePolicy().hasHeightForWidth())
        self.importedTickersListWidget.setSizePolicy(sizePolicy7)
        self.importedTickersListWidget.setMinimumSize(QSize(0, 80))
        self.importedTickersListWidget.setSizeIncrement(QSize(0, 0))
        self.importedTickersListWidget.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setItalic(False)
        self.importedTickersListWidget.setFont(font4)
        self.importedTickersListWidget.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
                                                     "border: 2px solid #343B48;")
        self.importedTickersListWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.importedTickersListWidget.setMovement(QListView.Static)
        self.importedTickersListWidget.setResizeMode(QListView.Fixed)

        self.importedTickersListLayout.addWidget(self.importedTickersListWidget)


        self.importAndSelectTickersHorizontalLayout.addLayout(self.importedTickersListLayout)

        self.buttonsForSelectVerticalLayout = QVBoxLayout()
        self.buttonsForSelectVerticalLayout.setSpacing(80)
        self.buttonsForSelectVerticalLayout.setObjectName(u"buttonsForSelectVerticalLayout")
        self.buttonsForSelectVerticalLayout.setContentsMargins(20, 25, 20, 270)
        self.trackButton = QPushButton(self.frame_div_select_tickers)
        self.trackButton.setObjectName(u"trackButton")
        sizePolicy3.setHeightForWidth(self.trackButton.sizePolicy().hasHeightForWidth())
        self.trackButton.setSizePolicy(sizePolicy3)
        self.trackButton.setMinimumSize(QSize(40, 40))
        self.trackButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.trackButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chevron-right.png);\n"
                                       "background-repeat: no-repeat;\n"
                                       "background-position: center;")

        self.buttonsForSelectVerticalLayout.addWidget(self.trackButton, 0, Qt.AlignHCenter)

        self.untrackButton = QPushButton(self.frame_div_select_tickers)
        self.untrackButton.setObjectName(u"untrackButton")
        sizePolicy3.setHeightForWidth(self.untrackButton.sizePolicy().hasHeightForWidth())
        self.untrackButton.setSizePolicy(sizePolicy3)
        self.untrackButton.setMinimumSize(QSize(40, 40))
        self.untrackButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.untrackButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chevron-left.png);\n"
                                         "background-repeat: no-repeat;\n"
                                         "background-position: center;")

        self.buttonsForSelectVerticalLayout.addWidget(self.untrackButton, 0, Qt.AlignHCenter)

        self.trackAllButton = QPushButton(self.frame_div_select_tickers)
        self.trackAllButton.setObjectName(u"trackAllButton")
        sizePolicy3.setHeightForWidth(self.trackAllButton.sizePolicy().hasHeightForWidth())
        self.trackAllButton.setSizePolicy(sizePolicy3)
        self.trackAllButton.setMinimumSize(QSize(40, 40))
        self.trackAllButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.trackAllButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chevron-double-right.png);\n"
                                          "background-repeat: no-repeat;\n"
                                          "background-position: center;")

        self.buttonsForSelectVerticalLayout.addWidget(self.trackAllButton, 0, Qt.AlignHCenter)

        self.untrackAllButton = QPushButton(self.frame_div_select_tickers)
        self.untrackAllButton.setObjectName(u"untrackAllButton")
        sizePolicy3.setHeightForWidth(self.untrackAllButton.sizePolicy().hasHeightForWidth())
        self.untrackAllButton.setSizePolicy(sizePolicy3)
        self.untrackAllButton.setMinimumSize(QSize(40, 40))
        self.untrackAllButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.untrackAllButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chevron-double-left.png);\n"
                                            "background-repeat: no-repeat;\n"
                                            "background-position: center;")

        self.buttonsForSelectVerticalLayout.addWidget(self.untrackAllButton, 0, Qt.AlignHCenter)


        self.importAndSelectTickersHorizontalLayout.addLayout(self.buttonsForSelectVerticalLayout)

        self.selectedTickersListLayout = QVBoxLayout()
        self.selectedTickersListLayout.setObjectName(u"selectedTickersListLayout")
        self.selectedTickersListLayout.setContentsMargins(-1, 0, -1, 0)
        self.selectedTickersListWidget = QListWidget(self.frame_div_select_tickers)
        self.selectedTickersListWidget.setObjectName(u"selectedTickersListWidget")
        sizePolicy7.setHeightForWidth(self.selectedTickersListWidget.sizePolicy().hasHeightForWidth())
        self.selectedTickersListWidget.setSizePolicy(sizePolicy7)
        self.selectedTickersListWidget.setMinimumSize(QSize(0, 80))
        self.selectedTickersListWidget.setSizeIncrement(QSize(0, 0))
        self.selectedTickersListWidget.setBaseSize(QSize(0, 0))
        self.selectedTickersListWidget.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
                                                     "border: 2px solid #343B48;")
        self.selectedTickersListWidget.setResizeMode(QListView.Fixed)

        self.selectedTickersListLayout.addWidget(self.selectedTickersListWidget)


        self.importAndSelectTickersHorizontalLayout.addLayout(self.selectedTickersListLayout)


        self.verticalLayout_16.addWidget(self.frame_div_select_tickers)


        self.verticalLayout.addWidget(self.frame_portfolio, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.portfolio)
        self.processing = QWidget()
        self.processing.setObjectName(u"processing")
        self.verticalLayout_20 = QVBoxLayout(self.processing)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_processing = QFrame(self.processing)
        self.frame_processing.setObjectName(u"frame_processing")
        self.frame_processing.setFrameShape(QFrame.StyledPanel)
        self.frame_processing.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_processing)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.row_2 = QFrame(self.frame_processing)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.row_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_2 = QCheckBox(self.row_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.checkBox_2, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.row_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.radioButton_2, 0, 1, 1, 1)

        self.verticalSlider_2 = QSlider(self.row_2)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setStyleSheet(u"")
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.gridLayout_3.addWidget(self.verticalSlider_2, 0, 2, 3, 1)

        self.verticalScrollBar_2 = QScrollBar(self.row_2)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
                                               " QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar_2.setOrientation(Qt.Vertical)

        self.gridLayout_3.addWidget(self.verticalScrollBar_2, 0, 4, 3, 1)

        self.scrollArea_2 = QScrollArea(self.row_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u" QScrollBar:vertical {\n"
                                        "    background: rgb(52, 59, 72);\n"
                                        " }\n"
                                        " QScrollBar:horizontal {\n"
                                        "    background: rgb(52, 59, 72);\n"
                                        " }")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 274, 218))
        self.scrollAreaWidgetContents_2.setStyleSheet(u" QScrollBar:vertical {\n"
                                                      "	border: none;\n"
                                                      "    background: rgb(52, 59, 72);\n"
                                                      "    width: 14px;\n"
                                                      "    margin: 21px 0 21px 0;\n"
                                                      "	border-radius: 0px;\n"
                                                      " }")
        self.horizontalLayout_13 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(200, 200))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_13.addWidget(self.plainTextEdit_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 5, 3, 1)

        self.comboBox_2 = QComboBox(self.row_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_2.setIconSize(QSize(16, 16))
        self.comboBox_2.setFrame(True)

        self.gridLayout_3.addWidget(self.comboBox_2, 1, 0, 1, 2)

        self.horizontalScrollBar_2 = QScrollBar(self.row_2)
        self.horizontalScrollBar_2.setObjectName(u"horizontalScrollBar_2")
        sizePolicy1.setHeightForWidth(self.horizontalScrollBar_2.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_2.setSizePolicy(sizePolicy1)
        self.horizontalScrollBar_2.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
                                                 " QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar_2.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalScrollBar_2, 1, 3, 1, 1)

        self.commandLinkButton_2 = QCommandLinkButton(self.row_2)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton_2.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_2.setIcon(icon8)

        self.gridLayout_3.addWidget(self.commandLinkButton_2, 1, 6, 1, 1)

        self.horizontalSlider_3 = QSlider(self.row_2)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setStyleSheet(u"")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_3, 2, 0, 1, 2)


        self.verticalLayout_22.addLayout(self.gridLayout_3)


        self.verticalLayout_23.addWidget(self.row_2)

        self.row_3 = QFrame(self.frame_processing)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy7.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy7)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        #endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        #endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        #endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_23.addWidget(self.row_3)


        self.verticalLayout_20.addWidget(self.frame_processing)

        self.stackedWidget.addWidget(self.processing)
        self.graphs = QWidget()
        self.graphs.setObjectName(u"graphs")
        self.verticalLayout_21 = QVBoxLayout(self.graphs)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_graphs = QFrame(self.graphs)
        self.frame_graphs.setObjectName(u"frame_graphs")
        sizePolicy7.setHeightForWidth(self.frame_graphs.sizePolicy().hasHeightForWidth())
        self.frame_graphs.setSizePolicy(sizePolicy7)
        self.frame_graphs.setMinimumSize(QSize(500, 0))
        self.frame_graphs.setFrameShape(QFrame.StyledPanel)
        self.frame_graphs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_graphs)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.graphsHorizontalLayout = QHBoxLayout()
        self.graphsHorizontalLayout.setSpacing(0)
        self.graphsHorizontalLayout.setObjectName(u"graphsHorizontalLayout")
        self.leftGraphsVerticalLayout = QVBoxLayout()
        self.leftGraphsVerticalLayout.setSpacing(15)
        self.leftGraphsVerticalLayout.setObjectName(u"leftGraphsVerticalLayout")
        self.labelTickers = QLabel(self.frame_graphs)
        self.labelTickers.setObjectName(u"labelTickers")
        self.labelTickers.setStyleSheet(u"font: 500 12pt \"Segoe UI\";")

        self.leftGraphsVerticalLayout.addWidget(self.labelTickers)

        self.graphsList = QListWidget(self.frame_graphs)
        self.graphsList.setObjectName(u"graphsList")
        sizePolicy7.setHeightForWidth(self.graphsList.sizePolicy().hasHeightForWidth())
        self.graphsList.setSizePolicy(sizePolicy7)
        self.graphsList.setMinimumSize(QSize(150, 0))
        self.graphsList.setMaximumSize(QSize(16777215, 16777215))
        self.graphsList.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
                                      "border: 2px solid #343B48;")

        self.leftGraphsVerticalLayout.addWidget(self.graphsList)


        self.graphsHorizontalLayout.addLayout(self.leftGraphsVerticalLayout)

        self.graphsVerticalLayout = QVBoxLayout()
        self.graphsVerticalLayout.setSpacing(30)
        self.graphsVerticalLayout.setObjectName(u"graphsVerticalLayout")
        self.graphsVerticalLayout.setContentsMargins(30, 40, 30, 200)
        self.showDefaultGraphButton = QPushButton(self.frame_graphs)
        self.showDefaultGraphButton.setObjectName(u"showDefaultGraphButton")
        self.showDefaultGraphButton.setMinimumSize(QSize(300, 50))
        self.showDefaultGraphButton.setMaximumSize(QSize(300, 50))
        self.showDefaultGraphButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.graphsVerticalLayout.addWidget(self.showDefaultGraphButton)

        self.showLogarithmicGraphButton = QPushButton(self.frame_graphs)
        self.showLogarithmicGraphButton.setObjectName(u"showLogarithmicGraphButton")
        self.showLogarithmicGraphButton.setMinimumSize(QSize(300, 50))
        self.showLogarithmicGraphButton.setMaximumSize(QSize(300, 50))
        self.showLogarithmicGraphButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.graphsVerticalLayout.addWidget(self.showLogarithmicGraphButton)

        self.showBetaDistributionGraphButton = QPushButton(self.frame_graphs)
        self.showBetaDistributionGraphButton.setObjectName(u"showBetaDistributionGraphButton")
        self.showBetaDistributionGraphButton.setMinimumSize(QSize(300, 50))
        self.showBetaDistributionGraphButton.setMaximumSize(QSize(300, 50))
        self.showBetaDistributionGraphButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.graphsVerticalLayout.addWidget(self.showBetaDistributionGraphButton)

        self.saveSelectedGraphButton = QPushButton(self.frame_graphs)
        self.saveSelectedGraphButton.setObjectName(u"saveSelectedGraphButton")
        self.saveSelectedGraphButton.setMinimumSize(QSize(300, 50))
        self.saveSelectedGraphButton.setMaximumSize(QSize(300, 50))
        self.saveSelectedGraphButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.graphsVerticalLayout.addWidget(self.saveSelectedGraphButton)

        self.saveAllGraphsButton = QPushButton(self.frame_graphs)
        self.saveAllGraphsButton.setObjectName(u"saveAllGraphsButton")
        self.saveAllGraphsButton.setMinimumSize(QSize(300, 50))
        self.saveAllGraphsButton.setMaximumSize(QSize(300, 50))
        self.saveAllGraphsButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.graphsVerticalLayout.addWidget(self.saveAllGraphsButton)


        self.graphsHorizontalLayout.addLayout(self.graphsVerticalLayout)


        self.verticalLayout_24.addLayout(self.graphsHorizontalLayout)


        self.verticalLayout_21.addWidget(self.frame_graphs)

        self.stackedWidget.addWidget(self.graphs)
        self.recommended = QWidget()
        self.recommended.setObjectName(u"recommended")
        self.stackedWidget.addWidget(self.recommended)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_settings_recommendations = QPushButton(self.topMenus)
        self.btn_settings_recommendations.setObjectName(u"btn_settings_recommendations")
        sizePolicy1.setHeightForWidth(self.btn_settings_recommendations.sizePolicy().hasHeightForWidth())
        self.btn_settings_recommendations.setSizePolicy(sizePolicy1)
        self.btn_settings_recommendations.setMinimumSize(QSize(0, 45))
        self.btn_settings_recommendations.setFont(font)
        self.btn_settings_recommendations.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_recommendations.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings_recommendations.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-thumb-up.png);")

        self.verticalLayout_14.addWidget(self.btn_settings_recommendations)

        self.btn_settings_styles = QPushButton(self.topMenus)
        self.btn_settings_styles.setObjectName(u"btn_settings_styles")
        sizePolicy1.setHeightForWidth(self.btn_settings_styles.sizePolicy().hasHeightForWidth())
        self.btn_settings_styles.setSizePolicy(sizePolicy1)
        self.btn_settings_styles.setMinimumSize(QSize(0, 45))
        self.btn_settings_styles.setFont(font)
        self.btn_settings_styles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_styles.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings_styles.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_14.addWidget(self.btn_settings_styles)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"CalliduStocks", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u043a\u043e\u0442\u0438\u0440\u043e\u0432\u043e\u043a", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.btn_portfolio.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u044b", None))
        self.btn_processing.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.btn_graphs.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.btn_recommended.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        #if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
        #endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f", None))
        self.btn_creators.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u044b", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                       "p, li { white-space: pre-wrap; }\n"
                                                                       "</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                                       "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#ff79c6;\">CalliduStocks</span></p>\n"
                                                                       "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">\u0422\u0440\u0435\u0439\u0434\u0435\u0440\u0441\u043a\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0431\u0438\u0440\u0436\u0435\u0432\u044b\u0445 \u0434\u0430\u043d\u043d"
                                                                       "\u044b\u0445, \u0441\u043e\u0437\u0434\u0430\u043d\u043e \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e Python \u0438 PySide, \u0442\u0435\u043c\u0430 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0430 \u043d\u0430 \u0446\u0432\u0435\u0442\u0430\u0445 \u0442\u0435\u043c\u044b Dracula, \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u043e\u0439 Zeno Rocha.</span></p>\n"
                                                                       "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">MIT License</span></p>\n"
                                                                       "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#bd93f9;\">\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u0438: SirKarib &amp; Alxymitr</span></p>\n"
                                                                       "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                                                                       "0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#ff79c6;\">\u0421\u043f\u0440\u0430\u0432\u043a\u0430</span></p>\n"
                                                                       "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u0432\u044b\u0448\u0435 \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u043f\u0440\u0430\u0432\u043a\u0443 \u043f\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u0439.</span></p>\n"
                                                                       "<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#ff79c6;\">\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430</span></p>\n"
                                                                       "<p align=\"center\" style="
                                                                       "\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">\u0421\u0432\u044f\u0436\u0438\u0442\u0435\u0441\u044c \u0441 \u0430\u0432\u0442\u043e\u0440\u0430\u043c\u0438 \u0435\u0441\u043b\u0438 \u0436\u0435\u043b\u0430\u0435\u0442\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0438\u0442\u044c \u0441\u0432\u043e\u044e \u043f\u043e\u043c\u043e\u0449\u044c.</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        #if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
        #endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
        #if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        #endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
        #if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        #endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
        #if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        #endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.importFileLabel.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u0441\u043e \u0441\u043f\u0438\u0441\u043a\u043e\u043c \u0442\u0438\u043a\u0435\u0440\u043e\u0432", None))
        self.importFileDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f .txt, \u043a\u0430\u0436\u0434\u044b\u0439 \u0442\u0438\u043a\u0435\u0440 \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 \u0422\u0438\u043a\u0435\u0440-\u0412\u0430\u043b\u044e\u0442\u0430, \u043f\u0440\u0438\u043c\u0435\u0440: BTC-USD</p></body></html>", None))
        self.filePathLineEdit.setText("")
        self.filePathLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
        self.importTickersFileButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.loadTickersFromFileButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0438\u043a\u0435\u0440\u044b \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0438\u043a\u0435\u0440", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0438\u043a\u0435\u0440", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.trackButton.setText("")
        self.untrackButton.setText("")
        self.trackAllButton.setText("")
        self.untrackAllButton.setText("")
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton_2.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.labelTickers.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0418\u041a\u0415\u0420\u042b", None))
        self.showDefaultGraphButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u0431\u0435\u0437 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.showLogarithmicGraphButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043b\u043e\u0433\u0430\u0440\u0438\u0444\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.showBetaDistributionGraphButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a \u0411\u0435\u0442\u0430-\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.saveSelectedGraphButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0434\u043b\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0442\u0438\u043a\u0435\u0440\u0430", None))
        self.saveAllGraphsButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u0442\u0438\u043a\u0435\u0440\u043e\u0432", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0438\u0442\u044c \u043e \u0431\u0430\u0433\u0435", None))
        self.btn_settings_recommendations.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438", None))
        self.btn_settings_styles.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: SirKarib", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

