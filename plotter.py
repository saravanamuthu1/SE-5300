from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Plot"))

    def plotsingleaxis(self, plottype, column, dataframe, color):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor(color)
        data = dataframe[column]
        if plottype == 'Bar Plot':
            index = np.arange(len(data))
            ax.bar(index, data)
        elif plottype == 'Histogram':
            ax.hist(data)
        elif plottype == 'Pie Chart':
            ax.pie(data)
        self.canvas.draw()

    def plotdoubleaxis(self, plottype, colx, coly, dataframe, color):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor(color)
        x = dataframe[colx]
        y = dataframe[coly]
        if plottype == 'Line Plot':
            ax.plot(x, y)
        elif plottype == 'Scatter Plot':
            ax.scatter(x, y)
        self.canvas.draw()
