# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calendar.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(944, 888)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 891, 591))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblMonday = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblMonday.setObjectName(_fromUtf8("lblMonday"))
        self.horizontalLayout.addWidget(self.lblMonday)
        self.lblTuesday = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblTuesday.setObjectName(_fromUtf8("lblTuesday"))
        self.horizontalLayout.addWidget(self.lblTuesday)
        self.lblWednesday = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblWednesday.setObjectName(_fromUtf8("lblWednesday"))
        self.horizontalLayout.addWidget(self.lblWednesday)
        self.lblThursday = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblThursday.setObjectName(_fromUtf8("lblThursday"))
        self.horizontalLayout.addWidget(self.lblThursday)
        self.lblFriday = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblFriday.setObjectName(_fromUtf8("lblFriday"))
        self.horizontalLayout.addWidget(self.lblFriday)
        self.lblSaturday = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblSaturday.setObjectName(_fromUtf8("lblSaturday"))
        self.horizontalLayout.addWidget(self.lblSaturday)
        self.lblSunday = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblSunday.setObjectName(_fromUtf8("lblSunday"))
        self.horizontalLayout.addWidget(self.lblSunday)
        self.lblWeekly = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblWeekly.setObjectName(_fromUtf8("lblWeekly"))
        self.horizontalLayout.addWidget(self.lblWeekly)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget_13 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_13.setObjectName(_fromUtf8("listWidget_13"))
        self.gridLayout.addWidget(self.listWidget_13, 1, 5, 1, 1)
        self.listWidget_19 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_19.setObjectName(_fromUtf8("listWidget_19"))
        self.gridLayout.addWidget(self.listWidget_19, 2, 4, 1, 1)
        self.listWidget_20 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_20.setObjectName(_fromUtf8("listWidget_20"))
        self.gridLayout.addWidget(self.listWidget_20, 2, 5, 1, 1)
        self.listWidget_21 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_21.setObjectName(_fromUtf8("listWidget_21"))
        self.gridLayout.addWidget(self.listWidget_21, 2, 6, 1, 1)
        self.listWidget_22 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_22.setObjectName(_fromUtf8("listWidget_22"))
        self.gridLayout.addWidget(self.listWidget_22, 3, 0, 1, 1)
        self.listWidget_23 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_23.setObjectName(_fromUtf8("listWidget_23"))
        self.gridLayout.addWidget(self.listWidget_23, 3, 1, 1, 1)
        self.listWidget_24 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_24.setObjectName(_fromUtf8("listWidget_24"))
        self.gridLayout.addWidget(self.listWidget_24, 3, 2, 1, 1)
        self.listWidget_25 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_25.setObjectName(_fromUtf8("listWidget_25"))
        self.gridLayout.addWidget(self.listWidget_25, 3, 3, 1, 1)
        self.listWidget_26 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_26.setObjectName(_fromUtf8("listWidget_26"))
        self.gridLayout.addWidget(self.listWidget_26, 3, 4, 1, 1)
        self.listWidget_27 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_27.setObjectName(_fromUtf8("listWidget_27"))
        self.gridLayout.addWidget(self.listWidget_27, 3, 5, 1, 1)
        self.listWidget_28 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_28.setObjectName(_fromUtf8("listWidget_28"))
        self.gridLayout.addWidget(self.listWidget_28, 3, 6, 1, 1)
        self.listWidget_29 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_29.setObjectName(_fromUtf8("listWidget_29"))
        self.gridLayout.addWidget(self.listWidget_29, 1, 7, 1, 1)
        self.listWidget_15 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_15.setObjectName(_fromUtf8("listWidget_15"))
        self.gridLayout.addWidget(self.listWidget_15, 2, 0, 1, 1)
        self.listWidget_16 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_16.setObjectName(_fromUtf8("listWidget_16"))
        self.gridLayout.addWidget(self.listWidget_16, 2, 1, 1, 1)
        self.listWidget_17 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_17.setObjectName(_fromUtf8("listWidget_17"))
        self.gridLayout.addWidget(self.listWidget_17, 2, 2, 1, 1)
        self.listWidget_18 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_18.setObjectName(_fromUtf8("listWidget_18"))
        self.gridLayout.addWidget(self.listWidget_18, 2, 3, 1, 1)
        self.listWidget_11 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_11.setObjectName(_fromUtf8("listWidget_11"))
        self.gridLayout.addWidget(self.listWidget_11, 1, 3, 1, 1)
        self.listWidget_14 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_14.setObjectName(_fromUtf8("listWidget_14"))
        self.gridLayout.addWidget(self.listWidget_14, 1, 6, 1, 1)
        self.listWidget_9 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_9.setObjectName(_fromUtf8("listWidget_9"))
        self.gridLayout.addWidget(self.listWidget_9, 1, 1, 1, 1)
        self.listWidget_2 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.gridLayout.addWidget(self.listWidget_2, 1, 0, 1, 1)
        self.listWidget_10 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_10.setObjectName(_fromUtf8("listWidget_10"))
        self.gridLayout.addWidget(self.listWidget_10, 1, 2, 1, 1)
        self.listWidget_12 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_12.setObjectName(_fromUtf8("listWidget_12"))
        self.gridLayout.addWidget(self.listWidget_12, 1, 4, 1, 1)
        self.vlayW1D1 = QtGui.QVBoxLayout()
        self.vlayW1D1.setObjectName(_fromUtf8("vlayW1D1"))
        self.lblW1D1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblW1D1.setObjectName(_fromUtf8("lblW1D1"))
        self.vlayW1D1.addWidget(self.lblW1D1)
        self.listW1D1 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listW1D1.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listW1D1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listW1D1.setObjectName(_fromUtf8("listW1D1"))
        item = QtGui.QListWidgetItem()
        self.listW1D1.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listW1D1.addItem(item)
        self.vlayW1D1.addWidget(self.listW1D1)
        self.gridLayout.addLayout(self.vlayW1D1, 0, 0, 1, 1)
        self.vlayW1Weekly = QtGui.QVBoxLayout()
        self.vlayW1Weekly.setObjectName(_fromUtf8("vlayW1Weekly"))
        self.lblW1Weekly = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblW1Weekly.setObjectName(_fromUtf8("lblW1Weekly"))
        self.vlayW1Weekly.addWidget(self.lblW1Weekly)
        self.listW1Weekly = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listW1Weekly.setObjectName(_fromUtf8("listW1Weekly"))
        self.vlayW1Weekly.addWidget(self.listW1Weekly)
        self.gridLayout.addLayout(self.vlayW1Weekly, 0, 7, 1, 1)
        self.widget_W1D2 = QtGui.QWidget(self.verticalLayoutWidget)
        self.widget_W1D2.setObjectName(_fromUtf8("widget_W1D2"))
        self.lblW1D2 = QtGui.QLabel(self.widget_W1D2)
        self.lblW1D2.setGeometry(QtCore.QRect(0, 0, 61, 21))
        self.lblW1D2.setObjectName(_fromUtf8("lblW1D2"))
        self.listW1D2 = QtGui.QListWidget(self.widget_W1D2)
        self.listW1D2.setGeometry(QtCore.QRect(0, 20, 91, 101))
        self.listW1D2.setObjectName(_fromUtf8("listW1D2"))
        self.gridLayout.addWidget(self.widget_W1D2, 0, 1, 1, 1)
        self.frame = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 2, 7, 1, 1)
        self.frame_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.listWidget = QtGui.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 0, 71, 111))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.frame_2, 4, 0, 1, 1)
        self.listWidget_8 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_8.setObjectName(_fromUtf8("listWidget_8"))
        self.gridLayout.addWidget(self.listWidget_8, 0, 6, 1, 1)
        self.listWidget_7 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_7.setObjectName(_fromUtf8("listWidget_7"))
        self.gridLayout.addWidget(self.listWidget_7, 0, 5, 1, 1)
        self.listWidget_6 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_6.setObjectName(_fromUtf8("listWidget_6"))
        self.gridLayout.addWidget(self.listWidget_6, 0, 4, 1, 1)
        self.listWidget_5 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))
        self.gridLayout.addWidget(self.listWidget_5, 0, 3, 1, 1)
        self.listWidget_4 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.gridLayout.addWidget(self.listWidget_4, 0, 2, 1, 1)
        self.listWidget_3 = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.gridLayout.addWidget(self.listWidget_3, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(230, 690, 264, 155))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.comboMonth = QtGui.QComboBox(self.centralwidget)
        self.comboMonth.setGeometry(QtCore.QRect(580, 720, 69, 22))
        self.comboMonth.setObjectName(_fromUtf8("comboMonth"))
        self.comboMonth.addItem(_fromUtf8(""))
        self.comboMonth.addItem(_fromUtf8(""))
        self.comboYear = QtGui.QComboBox(self.centralwidget)
        self.comboYear.setGeometry(QtCore.QRect(650, 720, 69, 22))
        self.comboYear.setObjectName(_fromUtf8("comboYear"))
        self.comboYear.addItem(_fromUtf8(""))
        self.comboYear.addItem(_fromUtf8(""))
        self.pushNextMonth = QtGui.QPushButton(self.centralwidget)
        self.pushNextMonth.setGeometry(QtCore.QRect(720, 720, 51, 22))
        self.pushNextMonth.setObjectName(_fromUtf8("pushNextMonth"))
        self.pushPrevMonth = QtGui.QPushButton(self.centralwidget)
        self.pushPrevMonth.setGeometry(QtCore.QRect(530, 720, 51, 22))
        self.pushPrevMonth.setObjectName(_fromUtf8("pushPrevMonth"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lblMonday.setText(_translate("MainWindow", "Monday", None))
        self.lblTuesday.setText(_translate("MainWindow", "Tuesday", None))
        self.lblWednesday.setText(_translate("MainWindow", "Wednesday", None))
        self.lblThursday.setText(_translate("MainWindow", "Thursday", None))
        self.lblFriday.setText(_translate("MainWindow", "Friday", None))
        self.lblSaturday.setText(_translate("MainWindow", "Saturday", None))
        self.lblSunday.setText(_translate("MainWindow", "Sunday", None))
        self.lblWeekly.setText(_translate("MainWindow", "Weekly", None))
        self.lblW1D1.setText(_translate("MainWindow", "01/02/2017", None))
        __sortingEnabled = self.listW1D1.isSortingEnabled()
        self.listW1D1.setSortingEnabled(False)
        item = self.listW1D1.item(0)
        item.setText(_translate("MainWindow", "Workout 1", None))
        item = self.listW1D1.item(1)
        item.setText(_translate("MainWindow", "Workout 2", None))
        self.listW1D1.setSortingEnabled(__sortingEnabled)
        self.lblW1Weekly.setText(_translate("MainWindow", "TextLabel", None))
        self.lblW1D2.setText(_translate("MainWindow", "TextLabel", None))
        self.comboMonth.setItemText(0, _translate("MainWindow", "January", None))
        self.comboMonth.setItemText(1, _translate("MainWindow", "February", None))
        self.comboYear.setItemText(0, _translate("MainWindow", "2016", None))
        self.comboYear.setItemText(1, _translate("MainWindow", "2017", None))
        self.pushNextMonth.setText(_translate("MainWindow", "Next", None))
        self.pushPrevMonth.setText(_translate("MainWindow", "Next", None))

