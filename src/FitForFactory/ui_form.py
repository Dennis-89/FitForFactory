# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import pictures_rc

class Ui_FitForFactory(object):
    def setupUi(self, FitForFactory):
        if not FitForFactory.objectName():
            FitForFactory.setObjectName(u"FitForFactory")
        FitForFactory.resize(1174, 850)
        self.verticalLayout = QVBoxLayout(FitForFactory)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Header = QLabel(FitForFactory)
        self.Header.setObjectName(u"Header")
        self.Header.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Header.setTextFormat(Qt.TextFormat.AutoText)
        self.Header.setPixmap(QPixmap(u":/header.PNG"))
        self.Header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Header.setMargin(0)

        self.horizontalLayout.addWidget(self.Header)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(FitForFactory)
        self.tabWidget.setObjectName(u"tabWidget")
        self.new_user = QWidget()
        self.new_user.setObjectName(u"new_user")
        self.verticalLayout_2 = QVBoxLayout(self.new_user)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(6, -1, -1, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 3, 1, 1)

        self.register_button = QPushButton(self.new_user)
        self.register_button.setObjectName(u"register_button")

        self.gridLayout.addWidget(self.register_button, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 5, 1, 1)

        self.label = QLabel(self.new_user)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.user_info = QLabel(self.new_user)
        self.user_info.setObjectName(u"user_info")

        self.gridLayout.addWidget(self.user_info, 3, 4, 1, 1)

        self.user_name = QLineEdit(self.new_user)
        self.user_name.setObjectName(u"user_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_name.sizePolicy().hasHeightForWidth())
        self.user_name.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.user_name, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.new_user, "")
        self.weight = QWidget()
        self.weight.setObjectName(u"weight")
        self.verticalLayout_3 = QVBoxLayout(self.weight)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, -1, 6, 6)
        self.weight_table = QTableWidget(self.weight)
        if (self.weight_table.columnCount() < 2):
            self.weight_table.setColumnCount(2)
        self.weight_table.setObjectName(u"weight_table")
        self.weight_table.setColumnCount(2)
        self.weight_table.horizontalHeader().setCascadingSectionResizes(False)
        self.weight_table.horizontalHeader().setDefaultSectionSize(400)
        self.weight_table.horizontalHeader().setHighlightSections(True)
        self.weight_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.weight_table.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.weight_table, 2, 1, 1, 1)

        self.weight_button = QPushButton(self.weight)
        self.weight_button.setObjectName(u"weight_button")

        self.gridLayout_2.addWidget(self.weight_button, 4, 0, 1, 1)

        self.login_button = QPushButton(self.weight)
        self.login_button.setObjectName(u"login_button")

        self.gridLayout_2.addWidget(self.login_button, 3, 0, 1, 1)

        self.hello_user = QLabel(self.weight)
        self.hello_user.setObjectName(u"hello_user")

        self.gridLayout_2.addWidget(self.hello_user, 0, 1, 1, 1)

        self.logout_button = QPushButton(self.weight)
        self.logout_button.setObjectName(u"logout_button")

        self.gridLayout_2.addWidget(self.logout_button, 4, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.weight, "")
        self.overview = QWidget()
        self.overview.setObjectName(u"overview")
        self.overview.setMinimumSize(QSize(0, 638))
        self.chart = QChartView(self.overview)
        self.chart.setObjectName(u"chart")
        self.chart.setGeometry(QRect(0, 0, 1161, 641))
        self.tabWidget.addTab(self.overview, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(FitForFactory)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FitForFactory)
    # setupUi

    def retranslateUi(self, FitForFactory):
        FitForFactory.setWindowTitle(QCoreApplication.translate("FitForFactory", u"FitForFactory", None))
        self.Header.setText("")
        self.register_button.setText(QCoreApplication.translate("FitForFactory", u"Registrieren", None))
        self.label.setText(QCoreApplication.translate("FitForFactory", u"Bitte Name angeben", None))
        self.user_info.setText(QCoreApplication.translate("FitForFactory", u"Willkomen! Bitte registieren oder in der Benutzer-Lounge anmelden.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_user), QCoreApplication.translate("FitForFactory", u"Registrieren", None))
#if QT_CONFIG(tooltip)
        self.weight.setToolTip(QCoreApplication.translate("FitForFactory", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.weight_button.setText(QCoreApplication.translate("FitForFactory", u"Wiegen", None))
        self.login_button.setText(QCoreApplication.translate("FitForFactory", u"Anmelden", None))
        self.hello_user.setText(QCoreApplication.translate("FitForFactory", u"Willkommen, bitte anmelden!", None))
        self.logout_button.setText(QCoreApplication.translate("FitForFactory", u"Abmelden", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weight), QCoreApplication.translate("FitForFactory", u"Benutzer-Lounge", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overview), QCoreApplication.translate("FitForFactory", u"\u00dcbersicht aller Teilnehmer", None))
    # retranslateUi

