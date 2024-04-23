# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dspcalui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1301, 713)
        MainWindow.setMinimumSize(QSize(1301, 713))
        MainWindow.setStyleSheet(u"*{\n"
"	border: 0px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#line{\n"
"	border: 7px solid rgb(44, 49, 58);\n"
"}")
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"#main ,#page_main,#page_about{	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"\n"
"QLabel {color : white; }\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"/* Top Buttons */\n"
"#toprightbuttons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#toprightbuttons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#toprightbuttons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"\n"
"\n"
"/* MEnu Buttons */\n"
"#menubutton .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#menubutton .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#menubutton .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* ////////////////////////////////"
                        "/////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#page_composotion,#page_formula,#page_anangle,#page_multipleangle1,#page_multipleanangel3,#page_multipleanvalue2,#header_frame,#left_menu,#scrollAreaWidgetContents_7{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#label_3 { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#label_3 { font: 9pt \"Segoe UI\"; color: rgb(80, 177, 200); font-weight: bold;}\n"
"\n"
"#footerdesc QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
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
"    background: rgb(80, 177, 200);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBa"
                        "r::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
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
"	background: rgb(80, 177, 200);\n"
"    min-height: 25px;\n"
"	border-radiu"
                        "s: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
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
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb"
                        "(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(80, 177, 200);\n"
"}\n"
"\n"
"QHeaderView {\n"
"	background-color: transparent;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(17, 62, 104);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"	color: #fff;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(17, 62, 104);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(17, 62, 104);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(17, 62, 104);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border"
                        "-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"	background-color:rgba(0, 0, 0, 0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(80, 177, 200, 200);\n"
"	border-radius: 8px;\n"
"	color:rgba(255, 255, 255, 150);\n"
"	padding-bottom:7px;\n"
"}\n"
"\n"
"\n"
"QLineEdit::focus {\n"
"	color:rgba(255, 255, 255, 240);\n"
"}\n"
"\n"
"/*//////////////////////COMBOBOX/////////////////////////////////////*/\n"
"\n"
"QComboBox {\n"
"	border: 1px  solid #fff;\n"
"	color: #fff;\n"
"	background-color : rgba(80, 177, 200, 156);\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 13px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/guidata/cil-arrow-bottom.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	font"
                        "-size:12px;\n"
"	color : #fff;\n"
"	padding: 5px;\n"
"	border-radius: 0px;\n"
"	background-color : rgb(17, 62, 104);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.stylesheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.stylesheet)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(300, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.left_menu)
        self.slide_menu.setObjectName(u"slide_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_menu.sizePolicy().hasHeightForWidth())
        self.slide_menu.setSizePolicy(sizePolicy)
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.logoapp = QFrame(self.slide_menu)
        self.logoapp.setObjectName(u"logoapp")
        self.logoapp.setFrameShape(QFrame.StyledPanel)
        self.logoapp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.logoapp)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 8, 0)
        self.label_4 = QLabel(self.logoapp)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 20))
        self.label_4.setPixmap(QPixmap(u":/icons/guidata/dspcal-high-resolution-logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.label_3 = QLabel(self.logoapp)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setText(u"<font color='#113e68'>D</font><font color='#50b1c8'>ifferential</font><br><font color='#113e68'>S</font><font color='#50b1c8'>cattering</font><br><font color='#113e68'>P</font><font color='#50b1c8'>arameters</font><br><font color='#113e68'>Cal</font><font color='#50b1c8'>culator</font>")
        self.label_3.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.logoapp, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.slide_menu)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 282, 632))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy1)
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents_7)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 630))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(274, 306))
        self.frame_3.setMaximumSize(QSize(274, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(9)
        self.label_6.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_6, 0, Qt.AlignBottom)

        self.CmbChemical = QComboBox(self.frame_3)
        self.CmbChemical.addItem("")
        self.CmbChemical.addItem("")
        self.CmbChemical.setObjectName(u"CmbChemical")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CmbChemical.sizePolicy().hasHeightForWidth())
        self.CmbChemical.setSizePolicy(sizePolicy2)
        self.CmbChemical.setMinimumSize(QSize(0, 30))
        self.CmbChemical.setMaximumSize(QSize(16777215, 30))
        self.CmbChemical.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.CmbChemical.setLayoutDirection(Qt.LeftToRight)
        self.CmbChemical.setAutoFillBackground(False)
        self.CmbChemical.setInsertPolicy(QComboBox.InsertAfterCurrent)
        self.CmbChemical.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.CmbChemical.setDuplicatesEnabled(False)
        self.CmbChemical.setFrame(True)

        self.verticalLayout_6.addWidget(self.CmbChemical, 0, Qt.AlignVCenter)

        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(274, 223))
        self.stackedWidget.setLineWidth(1)
        self.page_formula = QWidget()
        self.page_formula.setObjectName(u"page_formula")
        self.verticalLayout_8 = QVBoxLayout(self.page_formula)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, -1, 145)
        self.label_7 = QLabel(self.page_formula)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setFont(font2)

        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignVCenter)

        self.LneChemicalFormula = QLineEdit(self.page_formula)
        self.LneChemicalFormula.setObjectName(u"LneChemicalFormula")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.LneChemicalFormula.sizePolicy().hasHeightForWidth())
        self.LneChemicalFormula.setSizePolicy(sizePolicy4)
        self.LneChemicalFormula.setMinimumSize(QSize(0, 30))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 150))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.LneChemicalFormula.setPalette(palette)
        self.LneChemicalFormula.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.LneChemicalFormula, 1, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_9)

        self.stackedWidget.addWidget(self.page_formula)
        self.page_composotion = QWidget()
        self.page_composotion.setObjectName(u"page_composotion")
        self.verticalLayout_10 = QVBoxLayout(self.page_composotion)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_6 = QFrame(self.page_composotion)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignTop)

        self.LneElements1 = QLineEdit(self.frame_6)
        self.LneElements1.setObjectName(u"LneElements1")
        sizePolicy4.setHeightForWidth(self.LneElements1.sizePolicy().hasHeightForWidth())
        self.LneElements1.setSizePolicy(sizePolicy4)
        self.LneElements1.setMinimumSize(QSize(0, 30))

        self.verticalLayout_11.addWidget(self.LneElements1, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_composotion)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_9.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(274, 305))
        self.frame_4.setMaximumSize(QSize(274, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_12)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_11)

        self.CmbEnergy = QComboBox(self.frame_4)
        self.CmbEnergy.addItem("")
        self.CmbEnergy.addItem("")
        self.CmbEnergy.addItem("")
        self.CmbEnergy.addItem("")
        self.CmbEnergy.setObjectName(u"CmbEnergy")
        self.CmbEnergy.setMinimumSize(QSize(0, 30))
        self.CmbEnergy.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_7.addWidget(self.CmbEnergy, 0, Qt.AlignVCenter)

        self.stackedWidget_2 = QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(282, 274))
        self.page_anangle = QWidget()
        self.page_anangle.setObjectName(u"page_anangle")
        self.verticalLayout_12 = QVBoxLayout(self.page_anangle)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 30)
        self.label_13 = QLabel(self.page_anangle)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setFont(font2)

        self.gridLayout_7.addWidget(self.label_13, 0, 0, 1, 1, Qt.AlignVCenter)

        self.LneEnergy = QLineEdit(self.page_anangle)
        self.LneEnergy.setObjectName(u"LneEnergy")
        sizePolicy4.setHeightForWidth(self.LneEnergy.sizePolicy().hasHeightForWidth())
        self.LneEnergy.setSizePolicy(sizePolicy4)
        self.LneEnergy.setMinimumSize(QSize(0, 30))
        self.LneEnergy.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.LneEnergy, 1, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_7)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, -1, -1, 30)
        self.label_14 = QLabel(self.page_anangle)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setFont(font2)

        self.gridLayout_8.addWidget(self.label_14, 0, 0, 1, 1, Qt.AlignVCenter)

        self.LneAngle = QLineEdit(self.page_anangle)
        self.LneAngle.setObjectName(u"LneAngle")
        sizePolicy4.setHeightForWidth(self.LneAngle.sizePolicy().hasHeightForWidth())
        self.LneAngle.setSizePolicy(sizePolicy4)
        self.LneAngle.setMinimumSize(QSize(0, 30))
        self.LneAngle.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_8.addWidget(self.LneAngle, 1, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_8)

        self.stackedWidget_2.addWidget(self.page_anangle)
        self.page_multipleangle1 = QWidget()
        self.page_multipleangle1.setObjectName(u"page_multipleangle1")
        self.verticalLayout_19 = QVBoxLayout(self.page_multipleangle1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 30)
        self.LneEnergy1 = QLineEdit(self.page_multipleangle1)
        self.LneEnergy1.setObjectName(u"LneEnergy1")
        sizePolicy4.setHeightForWidth(self.LneEnergy1.sizePolicy().hasHeightForWidth())
        self.LneEnergy1.setSizePolicy(sizePolicy4)
        self.LneEnergy1.setMinimumSize(QSize(0, 30))
        self.LneEnergy1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.LneEnergy1, 1, 0, 1, 1)

        self.label_19 = QLabel(self.page_multipleangle1)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)
        self.label_19.setFont(font2)

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1, Qt.AlignVCenter)


        self.verticalLayout_19.addLayout(self.gridLayout_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 30)
        self.label_16 = QLabel(self.page_multipleangle1)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setFont(font2)

        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1, Qt.AlignVCenter)

        self.label_17 = QLabel(self.page_multipleangle1)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setFont(font2)

        self.gridLayout_3.addWidget(self.label_17, 0, 1, 1, 1, Qt.AlignVCenter)

        self.label_18 = QLabel(self.page_multipleangle1)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)
        self.label_18.setFont(font2)

        self.gridLayout_3.addWidget(self.label_18, 0, 2, 1, 1, Qt.AlignVCenter)

        self.LneAngleFrom1 = QLineEdit(self.page_multipleangle1)
        self.LneAngleFrom1.setObjectName(u"LneAngleFrom1")
        sizePolicy4.setHeightForWidth(self.LneAngleFrom1.sizePolicy().hasHeightForWidth())
        self.LneAngleFrom1.setSizePolicy(sizePolicy4)
        self.LneAngleFrom1.setMinimumSize(QSize(0, 30))
        self.LneAngleFrom1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.LneAngleFrom1, 1, 0, 1, 1)

        self.LneAngleTo1 = QLineEdit(self.page_multipleangle1)
        self.LneAngleTo1.setObjectName(u"LneAngleTo1")
        sizePolicy4.setHeightForWidth(self.LneAngleTo1.sizePolicy().hasHeightForWidth())
        self.LneAngleTo1.setSizePolicy(sizePolicy4)
        self.LneAngleTo1.setMinimumSize(QSize(0, 30))
        self.LneAngleTo1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.LneAngleTo1, 1, 1, 1, 1)

        self.LneAngleSkip1 = QLineEdit(self.page_multipleangle1)
        self.LneAngleSkip1.setObjectName(u"LneAngleSkip1")
        sizePolicy4.setHeightForWidth(self.LneAngleSkip1.sizePolicy().hasHeightForWidth())
        self.LneAngleSkip1.setSizePolicy(sizePolicy4)
        self.LneAngleSkip1.setMinimumSize(QSize(0, 30))
        self.LneAngleSkip1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.LneAngleSkip1, 1, 2, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_3)

        self.stackedWidget_2.addWidget(self.page_multipleangle1)
        self.page_multipleanvalue2 = QWidget()
        self.page_multipleanvalue2.setObjectName(u"page_multipleanvalue2")
        self.verticalLayout_20 = QVBoxLayout(self.page_multipleanvalue2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 30)
        self.label_20 = QLabel(self.page_multipleanvalue2)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)
        self.label_20.setFont(font2)

        self.gridLayout_5.addWidget(self.label_20, 0, 0, 1, 1, Qt.AlignVCenter)

        self.LneEnergyFrom2 = QLineEdit(self.page_multipleanvalue2)
        self.LneEnergyFrom2.setObjectName(u"LneEnergyFrom2")
        sizePolicy4.setHeightForWidth(self.LneEnergyFrom2.sizePolicy().hasHeightForWidth())
        self.LneEnergyFrom2.setSizePolicy(sizePolicy4)
        self.LneEnergyFrom2.setMinimumSize(QSize(0, 30))
        self.LneEnergyFrom2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.LneEnergyFrom2, 1, 0, 1, 1)

        self.LneEnergyTo2 = QLineEdit(self.page_multipleanvalue2)
        self.LneEnergyTo2.setObjectName(u"LneEnergyTo2")
        sizePolicy4.setHeightForWidth(self.LneEnergyTo2.sizePolicy().hasHeightForWidth())
        self.LneEnergyTo2.setSizePolicy(sizePolicy4)
        self.LneEnergyTo2.setMinimumSize(QSize(0, 30))
        self.LneEnergyTo2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.LneEnergyTo2, 1, 1, 1, 1)

        self.LneEnergySkip2 = QLineEdit(self.page_multipleanvalue2)
        self.LneEnergySkip2.setObjectName(u"LneEnergySkip2")
        sizePolicy4.setHeightForWidth(self.LneEnergySkip2.sizePolicy().hasHeightForWidth())
        self.LneEnergySkip2.setSizePolicy(sizePolicy4)
        self.LneEnergySkip2.setMinimumSize(QSize(0, 30))
        self.LneEnergySkip2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.LneEnergySkip2, 1, 2, 1, 1)

        self.label_21 = QLabel(self.page_multipleanvalue2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setFont(font2)

        self.gridLayout_5.addWidget(self.label_21, 0, 1, 1, 1, Qt.AlignVCenter)

        self.label_32 = QLabel(self.page_multipleanvalue2)
        self.label_32.setObjectName(u"label_32")
        sizePolicy3.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy3)
        self.label_32.setFont(font2)

        self.gridLayout_5.addWidget(self.label_32, 0, 2, 1, 1, Qt.AlignVCenter)


        self.verticalLayout_20.addLayout(self.gridLayout_5)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 30)
        self.label_22 = QLabel(self.page_multipleanvalue2)
        self.label_22.setObjectName(u"label_22")
        sizePolicy3.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy3)
        self.label_22.setFont(font2)

        self.gridLayout_6.addWidget(self.label_22, 0, 0, 1, 1, Qt.AlignVCenter)

        self.LneAngle2 = QLineEdit(self.page_multipleanvalue2)
        self.LneAngle2.setObjectName(u"LneAngle2")
        sizePolicy4.setHeightForWidth(self.LneAngle2.sizePolicy().hasHeightForWidth())
        self.LneAngle2.setSizePolicy(sizePolicy4)
        self.LneAngle2.setMinimumSize(QSize(0, 30))
        self.LneAngle2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.LneAngle2, 1, 0, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_6)

        self.stackedWidget_2.addWidget(self.page_multipleanvalue2)
        self.page_multipleanangel3 = QWidget()
        self.page_multipleanangel3.setObjectName(u"page_multipleanangel3")
        self.verticalLayout_14 = QVBoxLayout(self.page_multipleanangel3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 30)
        self.label_23 = QLabel(self.page_multipleanangel3)
        self.label_23.setObjectName(u"label_23")
        sizePolicy3.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy3)
        self.label_23.setFont(font2)

        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1, Qt.AlignVCenter)

        self.LneEnergySkip3 = QLineEdit(self.page_multipleanangel3)
        self.LneEnergySkip3.setObjectName(u"LneEnergySkip3")
        sizePolicy4.setHeightForWidth(self.LneEnergySkip3.sizePolicy().hasHeightForWidth())
        self.LneEnergySkip3.setSizePolicy(sizePolicy4)
        self.LneEnergySkip3.setMinimumSize(QSize(0, 30))
        self.LneEnergySkip3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.LneEnergySkip3, 1, 2, 1, 1)

        self.LneEnergyTo3 = QLineEdit(self.page_multipleanangel3)
        self.LneEnergyTo3.setObjectName(u"LneEnergyTo3")
        sizePolicy4.setHeightForWidth(self.LneEnergyTo3.sizePolicy().hasHeightForWidth())
        self.LneEnergyTo3.setSizePolicy(sizePolicy4)
        self.LneEnergyTo3.setMinimumSize(QSize(0, 30))
        self.LneEnergyTo3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.LneEnergyTo3, 1, 1, 1, 1)

        self.label_25 = QLabel(self.page_multipleanangel3)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)
        self.label_25.setFont(font2)

        self.gridLayout_2.addWidget(self.label_25, 0, 2, 1, 1, Qt.AlignVCenter)

        self.LneEnergyFrom3 = QLineEdit(self.page_multipleanangel3)
        self.LneEnergyFrom3.setObjectName(u"LneEnergyFrom3")
        sizePolicy4.setHeightForWidth(self.LneEnergyFrom3.sizePolicy().hasHeightForWidth())
        self.LneEnergyFrom3.setSizePolicy(sizePolicy4)
        self.LneEnergyFrom3.setMinimumSize(QSize(0, 30))
        self.LneEnergyFrom3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.LneEnergyFrom3, 1, 0, 1, 1)

        self.label_24 = QLabel(self.page_multipleanangel3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)
        self.label_24.setFont(font2)

        self.gridLayout_2.addWidget(self.label_24, 0, 1, 1, 1, Qt.AlignVCenter)


        self.verticalLayout_14.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(-1, -1, -1, 30)
        self.label_26 = QLabel(self.page_multipleanangel3)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)
        self.label_26.setFont(font2)

        self.gridLayout.addWidget(self.label_26, 0, 0, 1, 1, Qt.AlignVCenter)

        self.label_28 = QLabel(self.page_multipleanangel3)
        self.label_28.setObjectName(u"label_28")
        sizePolicy3.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy3)
        self.label_28.setFont(font2)

        self.gridLayout.addWidget(self.label_28, 0, 1, 1, 1, Qt.AlignVCenter)

        self.label_27 = QLabel(self.page_multipleanangel3)
        self.label_27.setObjectName(u"label_27")
        sizePolicy3.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy3)
        self.label_27.setFont(font2)

        self.gridLayout.addWidget(self.label_27, 0, 2, 1, 1, Qt.AlignVCenter)

        self.LneAngleFrom3 = QLineEdit(self.page_multipleanangel3)
        self.LneAngleFrom3.setObjectName(u"LneAngleFrom3")
        sizePolicy4.setHeightForWidth(self.LneAngleFrom3.sizePolicy().hasHeightForWidth())
        self.LneAngleFrom3.setSizePolicy(sizePolicy4)
        self.LneAngleFrom3.setMinimumSize(QSize(0, 30))
        self.LneAngleFrom3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LneAngleFrom3, 1, 0, 1, 1)

        self.LneAngleTo3 = QLineEdit(self.page_multipleanangel3)
        self.LneAngleTo3.setObjectName(u"LneAngleTo3")
        sizePolicy4.setHeightForWidth(self.LneAngleTo3.sizePolicy().hasHeightForWidth())
        self.LneAngleTo3.setSizePolicy(sizePolicy4)
        self.LneAngleTo3.setMinimumSize(QSize(0, 30))
        self.LneAngleTo3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LneAngleTo3, 1, 1, 1, 1)

        self.LneAngleSkip3 = QLineEdit(self.page_multipleanangel3)
        self.LneAngleSkip3.setObjectName(u"LneAngleSkip3")
        sizePolicy4.setHeightForWidth(self.LneAngleSkip3.sizePolicy().hasHeightForWidth())
        self.LneAngleSkip3.setSizePolicy(sizePolicy4)
        self.LneAngleSkip3.setMinimumSize(QSize(0, 30))
        self.LneAngleSkip3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.LneAngleSkip3, 1, 2, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout)

        self.stackedWidget_2.addWidget(self.page_multipleanangel3)

        self.verticalLayout_7.addWidget(self.stackedWidget_2)


        self.verticalLayout_9.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout_21.addWidget(self.frame, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main = QFrame(self.stylesheet)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menubutton = QFrame(self.header_frame)
        self.menubutton.setObjectName(u"menubutton")
        self.menubutton.setFrameShape(QFrame.StyledPanel)
        self.menubutton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.menubutton)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.BtnLeftMenu = QPushButton(self.menubutton)
        self.BtnLeftMenu.setObjectName(u"BtnLeftMenu")
        icon = QIcon()
        icon.addFile(u":/icons/guidata/cil-expand-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnLeftMenu.setIcon(icon)
        self.BtnLeftMenu.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.BtnLeftMenu, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.menubutton, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy5)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.toprightbuttons = QFrame(self.header_frame)
        self.toprightbuttons.setObjectName(u"toprightbuttons")
        self.toprightbuttons.setFrameShape(QFrame.StyledPanel)
        self.toprightbuttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.toprightbuttons)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BtnMinimize = QPushButton(self.toprightbuttons)
        self.BtnMinimize.setObjectName(u"BtnMinimize")
        icon1 = QIcon()
        icon1.addFile(u":/icons/guidata/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnMinimize.setIcon(icon1)
        self.BtnMinimize.setIconSize(QSize(60, 30))

        self.horizontalLayout_4.addWidget(self.BtnMinimize)

        self.BtnMaximize = QPushButton(self.toprightbuttons)
        self.BtnMaximize.setObjectName(u"BtnMaximize")
        self.BtnMaximize.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(u":/icons/guidata/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnMaximize.setIcon(icon2)
        self.BtnMaximize.setIconSize(QSize(60, 30))

        self.horizontalLayout_4.addWidget(self.BtnMaximize)

        self.BtnClose = QPushButton(self.toprightbuttons)
        self.BtnClose.setObjectName(u"BtnClose")
        icon3 = QIcon()
        icon3.addFile(u":/icons/guidata/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnClose.setIcon(icon3)
        self.BtnClose.setIconSize(QSize(60, 30))

        self.horizontalLayout_4.addWidget(self.BtnClose)


        self.horizontalLayout_2.addWidget(self.toprightbuttons, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body = QFrame(self.main)
        self.main_body.setObjectName(u"main_body")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy6)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.main_body)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.stackedWidget_3 = QStackedWidget(self.main_body)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.verticalLayout_15 = QVBoxLayout(self.page_main)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_7 = QFrame(self.page_main)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_29)

        self.tableWidget_Chemical_Formula = QTableWidget(self.frame_7)
        if (self.tableWidget_Chemical_Formula.columnCount() < 1):
            self.tableWidget_Chemical_Formula.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Chemical_Formula.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget_Chemical_Formula.rowCount() < 4):
            self.tableWidget_Chemical_Formula.setRowCount(4)
        self.tableWidget_Chemical_Formula.setObjectName(u"tableWidget_Chemical_Formula")
        self.tableWidget_Chemical_Formula.setAutoFillBackground(False)
        self.tableWidget_Chemical_Formula.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_Chemical_Formula.setAutoScrollMargin(16)
        self.tableWidget_Chemical_Formula.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Chemical_Formula.setAlternatingRowColors(False)
        self.tableWidget_Chemical_Formula.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Chemical_Formula.setRowCount(4)
        self.tableWidget_Chemical_Formula.horizontalHeader().setVisible(True)
        self.tableWidget_Chemical_Formula.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Chemical_Formula.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Chemical_Formula.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_Chemical_Formula.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Chemical_Formula.verticalHeader().setVisible(True)
        self.tableWidget_Chemical_Formula.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Chemical_Formula.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_16.addWidget(self.tableWidget_Chemical_Formula)


        self.verticalLayout_15.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.page_main)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.verticalLayout_18.addWidget(self.label_30)

        self.tableWidget_Variables = QTableWidget(self.frame_8)
        if (self.tableWidget_Variables.columnCount() < 6):
            self.tableWidget_Variables.setColumnCount(6)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Variables.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Variables.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Variables.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_Variables.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_Variables.setHorizontalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_Variables.setHorizontalHeaderItem(5, __qtablewidgetitem6)
        if (self.tableWidget_Variables.rowCount() < 1):
            self.tableWidget_Variables.setRowCount(1)
        self.tableWidget_Variables.setObjectName(u"tableWidget_Variables")
        self.tableWidget_Variables.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Variables.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Variables.setRowCount(1)
        self.tableWidget_Variables.setColumnCount(6)
        self.tableWidget_Variables.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_18.addWidget(self.tableWidget_Variables)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.page_main)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_31)

        self.tableWidget_Results = QTableWidget(self.frame_9)
        if (self.tableWidget_Results.columnCount() < 6):
            self.tableWidget_Results.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        if (self.tableWidget_Results.rowCount() < 10):
            self.tableWidget_Results.setRowCount(10)
        self.tableWidget_Results.setObjectName(u"tableWidget_Results")
        self.tableWidget_Results.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Results.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Results.setRowCount(10)
        self.tableWidget_Results.setColumnCount(6)
        self.tableWidget_Results.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_17.addWidget(self.tableWidget_Results)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.page_main)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BtnCalculate = QPushButton(self.frame_10)
        self.BtnCalculate.setObjectName(u"BtnCalculate")

        self.horizontalLayout_7.addWidget(self.BtnCalculate)

        self.BtnDownload = QPushButton(self.frame_10)
        self.BtnDownload.setObjectName(u"BtnDownload")

        self.horizontalLayout_7.addWidget(self.BtnDownload)


        self.verticalLayout_15.addWidget(self.frame_10)

        self.stackedWidget_3.addWidget(self.page_main)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.stackedWidget_3.addWidget(self.page_about)

        self.verticalLayout_13.addWidget(self.stackedWidget_3)


        self.verticalLayout.addWidget(self.main_body)

        self.footer = QFrame(self.main)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.footerdesc = QFrame(self.footer)
        self.footerdesc.setObjectName(u"footerdesc")
        self.footerdesc.setFrameShape(QFrame.StyledPanel)
        self.footerdesc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.footerdesc)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.footerdesc)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.footerdesc, 0, Qt.AlignBottom)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(15, 15))
        self.size_grip.setMaximumSize(QSize(15, 15))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.size_grip)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.size_grip)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/guidata/cil-size-grip.png"))
        self.label.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Chemical formula or composition", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Which one you would like to compute DSP for ?", None))
        self.CmbChemical.setItemText(0, QCoreApplication.translate("MainWindow", u"A chemical formula", None))
        self.CmbChemical.setItemText(1, QCoreApplication.translate("MainWindow", u"A chemical composition", None))

        self.CmbChemical.setCurrentText(QCoreApplication.translate("MainWindow", u"A chemical formula", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Write the chemical formula.", None))
        self.LneChemicalFormula.setText(QCoreApplication.translate("MainWindow", u"H2O", None))
        self.LneChemicalFormula.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"The elements in the composition(e.g. HO, FeO, CHNOS.)", None))
        self.LneElements1.setText(QCoreApplication.translate("MainWindow", u"HO", None))
        self.LneElements1.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Energy and angle", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Whic one you would like to use ?", None))
        self.CmbEnergy.setItemText(0, QCoreApplication.translate("MainWindow", u"An energy value and an angle value", None))
        self.CmbEnergy.setItemText(1, QCoreApplication.translate("MainWindow", u"An energy value and multiple angle values", None))
        self.CmbEnergy.setItemText(2, QCoreApplication.translate("MainWindow", u"Multiple energy values and an angle value", None))
        self.CmbEnergy.setItemText(3, QCoreApplication.translate("MainWindow", u"Multiple energy values and multiple angle values", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Energy (keV)", None))
        self.LneEnergy.setText(QCoreApplication.translate("MainWindow", u"500.0", None))
        self.LneEnergy.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Energy (keV)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.LneAngle.setText(QCoreApplication.translate("MainWindow", u"45.0", None))
        self.LneAngle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.LneEnergy1.setText(QCoreApplication.translate("MainWindow", u"500.0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Energy (keV)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Angle from", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Angle to", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Angle skip", None))
        self.LneAngleFrom1.setText(QCoreApplication.translate("MainWindow", u"45.0", None))
        self.LneAngleTo1.setText(QCoreApplication.translate("MainWindow", u"90.0", None))
        self.LneAngleSkip1.setText(QCoreApplication.translate("MainWindow", u"5.0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Energy from\n"
" (keV)", None))
        self.LneEnergyFrom2.setText(QCoreApplication.translate("MainWindow", u"100.0", None))
        self.LneEnergyTo2.setText(QCoreApplication.translate("MainWindow", u"500.0", None))
        self.LneEnergySkip2.setText(QCoreApplication.translate("MainWindow", u"50.0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Energy to (keV)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Energy skip", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.LneAngle2.setText(QCoreApplication.translate("MainWindow", u"45.0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Energy from\n"
" (keV)", None))
        self.LneEnergySkip3.setText(QCoreApplication.translate("MainWindow", u"50.0", None))
        self.LneEnergyTo3.setText(QCoreApplication.translate("MainWindow", u"500.0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Energy skip", None))
        self.LneEnergyFrom3.setText(QCoreApplication.translate("MainWindow", u"100.0", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Energy to (keV)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Angle from", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Angle to", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Angle skip", None))
        self.LneAngleFrom3.setText(QCoreApplication.translate("MainWindow", u"45.0", None))
        self.LneAngleTo3.setText(QCoreApplication.translate("MainWindow", u"90.0", None))
        self.LneAngleSkip3.setText(QCoreApplication.translate("MainWindow", u"5.0", None))
        self.BtnLeftMenu.setText("")
        self.BtnMinimize.setText("")
        self.BtnMaximize.setText("")
        self.BtnClose.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Chemical Formula", None))
        ___qtablewidgetitem = self.tableWidget_Chemical_Formula.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Formula", None));
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Variables", None))
        ___qtablewidgetitem1 = self.tableWidget_Variables.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget_Variables.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Energy from (keV)", None));
        ___qtablewidgetitem3 = self.tableWidget_Variables.horizontalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Energy skip", None));
        ___qtablewidgetitem4 = self.tableWidget_Variables.horizontalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Angle from", None));
        ___qtablewidgetitem5 = self.tableWidget_Variables.horizontalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Angle to", None));
        ___qtablewidgetitem6 = self.tableWidget_Variables.horizontalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Angle skip", None));
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        ___qtablewidgetitem7 = self.tableWidget_Results.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Energy (keV)", None));
        ___qtablewidgetitem8 = self.tableWidget_Results.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Angle", None));
        ___qtablewidgetitem9 = self.tableWidget_Results.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Mom. Tra.", None));
        ___qtablewidgetitem10 = self.tableWidget_Results.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"KN", None));
        ___qtablewidgetitem11 = self.tableWidget_Results.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Th", None));
        ___qtablewidgetitem12 = self.tableWidget_Results.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"TMMDSC", None));
        self.BtnCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.BtnDownload.setText(QCoreApplication.translate("MainWindow", u"Download results", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"L. Aydinbakar, \"New software for calculating the differential scattering parameters for applications: DSPCal", None))
        self.label.setText("")
    # retranslateUi

