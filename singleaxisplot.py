from PyQt5 import QtCore, QtGui, QtWidgets
from plotter import Ui_dialog as form


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 250)
        self.col='#ffffff'
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.colplot = QtWidgets.QComboBox(Dialog)
        self.colplot.setStyleSheet("QComboBox{\n"
                                   "background-color: white;\n"
                                   "color: blue;\n"
                                   "border: 1px solid blue;\n"
                                   "border-radius: 3px;\n"
                                   "}\n"
                                   "QComboBox::drop-down {\n"
                                   "    border-left-width: 1px;\n"
                                   "    border-left-color: blue;\n"
                                   "    border-left-style: solid;\n"
                                   "    border-top-right-radius: 3px;\n"
                                   "    border-bottom-right-radius: 3px;\n"
                                   "    width: 24px;\n"
                                   "}\n"
                                   "QComboBox::down-arrow {\n"
                                   "    image: url(Icons/arrow-blue.png);\n"
                                   "}"
                                   )
        self.colplot.setObjectName("colplot")
        self.horizontalLayout.addWidget(self.colplot)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.color = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("TW Cen MT")
        font.setPointSize(10)
        self.color.setFont(font)
        self.color.setStyleSheet("background-color: blue;\n"
                                 "color: white;\n"
                                 "border-radius: 5px;\n"
                                 "padding: 8px 16px 8px 16px;")
        self.color.setObjectName("color")
        self.horizontalLayout_3.addWidget(self.color)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plot = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.plot.setFont(font)
        self.plot.setStyleSheet("background-color: blue;\n"
                                "color: white;\n"
                                "border-radius: 5px;\n"
                                "padding: 8px 16px 8px 16px;")
        self.plot.setObjectName("plot")
        self.horizontalLayout_2.addWidget(self.plot)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.color.clicked.connect(self.colorpicker)
        self.plot.clicked.connect(self.showplot)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Column to be plotted:"))
        self.plot.setText(_translate("Dialog", "Plot"))
        self.color.setText(_translate("Dialog", "Choose Color"))

    def setdata(self, dataframe, name, Dialog):
        _translate = QtCore.QCoreApplication.translate
        col_list = dataframe.columns.values.tolist()
        self.colplot.addItems(col_list)
        self.df = dataframe
        self.name = name
        if name == 'Bar Plot':
            Dialog.setWindowTitle(_translate("Dialog", "Bar Plot"))
            Dialog.setWindowIcon(QtGui.QIcon('Icons\\bar-chart.png'))
        elif name == 'Histogram':
            Dialog.setWindowTitle(_translate("Dialog", "Histogram"))
            Dialog.setWindowIcon(QtGui.QIcon('Icons\\hist-chart.png'))
        elif name == 'Pie Chart':
            Dialog.setWindowTitle(_translate("Dialog", "Pie Chart"))
            Dialog.setWindowIcon(QtGui.QIcon('Icons\\pie-chart.png'))

    def colorpicker(self):
        col1 = QtWidgets.QColorDialog.getColor()
        self.col = col1.name()

    def showplot(self):
        str1 = str(self.colplot.currentText())
        dialog = QtWidgets.QDialog()
        dialog.ui = form()
        dialog.setWindowIcon(QtGui.QIcon('Icons\\plot.png'))
        dialog.ui.setupUi(dialog)
        dialog.ui.plotsingleaxis(self.name, str1, self.df, self.col)
        dialog.exec_()
        dialog.show()
