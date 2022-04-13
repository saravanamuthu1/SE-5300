from PyQt5 import QtCore, QtGui, QtWidgets
from plotter import Ui_dialog as form


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 250)
        self.col='#ffffff'
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(128)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.colx = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colx.sizePolicy().hasHeightForWidth())
        self.colx.setSizePolicy(sizePolicy)
        self.colx.setStyleSheet("QComboBox{\n"
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
        self.colx.setObjectName("colx")
        self.horizontalLayout_2.addWidget(self.colx)
        self.coly = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coly.sizePolicy().hasHeightForWidth())
        self.coly.setSizePolicy(sizePolicy)
        self.coly.setStyleSheet("QComboBox{\n"
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
        self.coly.setObjectName("coly")
        self.horizontalLayout_2.addWidget(self.coly)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
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
        self.color.clicked.connect(self.colorpicker)
        self.horizontalLayout_3.addWidget(self.color)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plot = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setStyleSheet("background-color: blue;\n"
                                "color: white;\n"
                                "border-radius: 5px;\n"
                                "padding: 8px 16px 8px 16px;")
        self.plot.setObjectName("plot")
        self.plot.clicked.connect(self.showplot)
        self.horizontalLayout.addWidget(self.plot)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Column for X axis:"))
        self.label_2.setText(_translate("Dialog", "Column for Y axis:"))
        self.plot.setText(_translate("Dialog", "Plot"))
        self.color.setText(_translate("Dialog", "Choose Color"))

    def setdata(self, dataframe, name, Dialog):
        _translate = QtCore.QCoreApplication.translate
        col_list = dataframe.columns.values.tolist()
        self.colx.addItems(col_list)
        self.coly.addItems(col_list)
        self.df = dataframe
        self.name = name
        if name == 'Line Plot':
            Dialog.setWindowTitle(_translate("Dialog", "Line Plot"))
            Dialog.setWindowIcon(QtGui.QIcon('Icons\\line-chart.png'))
        elif name == 'Scatter Plot':
            Dialog.setWindowTitle(_translate("Dialog", "Scatter Plot"))
            Dialog.setWindowIcon(QtGui.QIcon('Icons\\scatter-chart.png'))

    def showplot(self):
        str1 = str(self.colx.currentText())
        str2 = str(self.coly.currentText())
        if str1.__eq__(str2):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Please choose two different columns to plot.")
            msgBox.setWindowTitle("Plotter")
            msgBox.setWindowIcon(QtGui.QIcon('Icons\\icon.png'))
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.addButton(QtWidgets.QMessageBox.Yes)
            msgBox.exec_()
            return
        else:
            dialog = QtWidgets.QDialog()
            dialog.ui = form()
            dialog.setWindowIcon(QtGui.QIcon('Icons\\plot.png'))
            dialog.ui.setupUi(dialog)
            dialog.ui.plotdoubleaxis(self.name, str1, str2, self.df, self.col)
            dialog.exec_()
            dialog.show()

    def colorpicker(self):
        col1 = QtWidgets.QColorDialog.getColor()
        self.col = col1.name()
