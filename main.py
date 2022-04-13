from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from singleaxisplot import Ui_Dialog as form
from doubleaxisplot import Ui_Dialog as form1
from tableview import Ui_Dialog as form2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color : lightgray;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("QComboBox{\n"
                                    "background-color: rgb(0, 0, 255);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "padding:5px 44px 5px 44px;\n"
                                    "border:1px solid white;\n"
                                    "border-radius:3px;\n"
                                    "}\n"
                                    "QComboBox::drop-down {\n"
                                    "    border-left-width: 1px;\n"
                                    "    border-left-color: white;\n"
                                    "    border-left-style: solid;\n"
                                    "    width: 24px;\n"
                                    "    border-top-right-radius: 3px;\n"
                                    "    border-bottom-right-radius: 3px;\n"
                                    "}\n"
                                    "QComboBox::down-arrow {\n"
                                    "    image: url(Icons/arrow.png);\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "    border: 1px solid blue;\n"
                                    "    selection-background-color: blue;\n"
                                    "    selection-color: white;\n"
                                    "}")
        self.comboBox.setEditable(False)
        self.comboBox.setIconSize(QtCore.QSize(16, 16))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated[str].connect(self.startwindow)
        self.comboBox.hide()
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(16, -1, 16, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setStyleSheet("border : 1px solid rgb(0, 0, 255);\n"
                                "background-color : #FFF;\n"
                                "border-radius : 2px;")
        self.path.setObjectName("path")
        self.horizontalLayout.addWidget(self.path)
        self.load = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load.sizePolicy().hasHeightForWidth())
        self.load.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.load.setFont(font)
        self.load.setStyleSheet("background-color : rgb(0, 0, 255);\n"
                                "color : rgb(255, 255, 255);\n"
                                "padding-left : 24px;\n"
                                "padding-right : 24px;\n"
                                "padding-top : 4px;\n"
                                "padding-bottom : 4px;\n"
                                "border-radius : 11px;\n"
                                "")
        self.load.setObjectName("load")
        self.load.clicked.connect(self.getpath)
        self.horizontalLayout.addWidget(self.load)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.list = QtWidgets.QListView(self.centralwidget)
        self.list.setStyleSheet("background-color : white;\n"
                                "border : 1px solid blue;\n"
                                "border-radius : 4px;\n"
                                "margin-top : 16px;\n"
                                "margin-bottom : 16px;")
        self.list.setObjectName("list")
        self.gridLayout.addWidget(self.list, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.showtable = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showtable.sizePolicy().hasHeightForWidth())
        self.showtable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("TW Cen MT")
        font.setPointSize(10)
        self.showtable.setFont(font)
        self.showtable.setStyleSheet("background-color: blue;\n"
                                 "color: white;\n"
                                 "border-radius: 5px;\n"
                                 "padding: 8px 16px 8px 16px;")
        self.showtable.setObjectName("showtable")
        self.showtable.clicked.connect(self.showtab)
        self.horizontalLayout_3.addWidget(self.showtable)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.showtable.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plotter"))
        self.label.setText(_translate("MainWindow", "Enter the file path to be loaded"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Plot a Graph"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Bar Plot"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Histogram"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Pie Chart"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Line Plot"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Scatter Plot"))
        self.load.setText(_translate("MainWindow", "Load"))
        self.showtable.setText(_translate("MainWindow", "Show Table"))

    def getpath(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(caption='Open File', directory='C:\\',
                                                         filter="CSV Files(*.csv)")
        self.path.setText(filepath[0])
        self.load.setDisabled(True)
        self.populatelist(filepath[0])

    def populatelist(self, file):
        self.df = pd.read_csv(file)
        self.load.setDisabled(False)
        model = QtGui.QStandardItemModel(self.list)
        list_item = self.df.columns.values.tolist()
        for item in list_item:
            litem = QtGui.QStandardItem(item)
            model.appendRow(litem)
        self.list.setModel(model)
        self.comboBox.show()
        self.showtable.show()

    def startwindow(self, name):
        if name == 'Plot a Graph':
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Please choose a graph type to plot.")
            msgBox.setWindowTitle("Plotter")
            msgBox.setWindowIcon(QtGui.QIcon('Icons\\icon.png'))
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.addButton(QtWidgets.QMessageBox.Yes)
            msgBox.exec_()
        elif name == 'Bar Plot' or name == 'Histogram' or name == 'Pie Chart':
            dialog=QtWidgets.QDialog()
            dialog.ui = form()
            dialog.ui.setupUi(dialog)
            dialog.ui.setdata(self.df, name, dialog)
            dialog.exec_()
            dialog.show()
        elif name == 'Line Plot' or name == 'Scatter Plot':
            dialog=QtWidgets.QDialog()
            dialog.ui = form1()
            dialog.ui.setupUi(dialog)
            dialog.ui.setdata(self.df, name, dialog)
            dialog.exec_()
            dialog.show()

    def showtab(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = form2()
        dialog.setWindowIcon(QtGui.QIcon('Icons\\table.png'))
        dialog.ui.setupUi(dialog)
        dialog.ui.getdata(self.df)
        dialog.exec_()
        dialog.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('Icons\icon.png'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
