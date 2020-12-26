import sys
from PyQt5 import QtWidgets
import functions as tf
from batAlgorithm import ba
from cuckooSearchAlgorithm import cso
from beeAlgorithm import aba
import programPyQT
from PlotGraphics import PlotGraphics
import time

class MainApp(QtWidgets.QMainWindow, programPyQT.Ui_MainWindow):

    def getFunctionByIndex(self, index):
        if index == 0:
            return tf.sum_squares_function
        if index == 1:
            return tf.sum_of_different_powers_function
        else:
            return tf.easom_function

    def runCSOAlgorithm(self, n, functionIndex, lb, ub, dimension, iteration):
        # Запуск алгоритма поиска кукушки
        function = self.getFunctionByIndex(functionIndex)
        start = time.time()
        alh = cso(n, function, lb, ub, dimension, iteration)
        self.textBrowser.setText(str(time.time() - start))
        self.textBrowser_2.setText(str(alh.get_Gbest()))
        return alh
        # animation(alh.get_agents(), function, lb, ub)

    def runABAAlgorithm(self, n, functionIndex, lb, ub, dimension, iteration):
        # Запуск алгоритма пчелиной колонии
        function = self.getFunctionByIndex(functionIndex)
        start = time.time()
        alh = aba(n, function, lb, ub, dimension, iteration)
        self.textBrowser.setText(str(time.time() - start))
        self.textBrowser_2.setText(str(alh.get_Gbest()))
        return alh
        # animation(alh.get_agents(), function, lb, ub)

    def runBAAlgorithm(self, n, functionIndex, lb, ub, dimension, iteration):
        # Запуск алгоритма летучих мышей
        function = self.getFunctionByIndex(functionIndex)
        start = time.time()
        alh = ba(n, function, lb, ub, dimension, iteration)
        self.textBrowser.setText(str(time.time() - start))
        self.textBrowser_2.setText(str(alh.get_Gbest()))
        return alh
        # animation(alh.get_agents(), function, lb, ub)

    def getInputValues(self):
        n = int(self.lineEdit.text())
        function = self.comboBox.currentIndex()
        self.lb = int(self.lineEdit_3.text())
        self.ub = int(self.lineEdit_4.text())
        dimension = int(self.lineEdit_5.text())
        iteration = int(self.lineEdit_6.text())
        csoIsChecked = self.radioButton.isChecked()
        abaIsChecked = self.radioButton_2.isChecked()
        baIsChecked = self.radioButton_3.isChecked()
        if csoIsChecked:
            self.alh = self.runCSOAlgorithm(n, function, self.lb, self.ub, dimension, iteration)
        else:
            if abaIsChecked:
                self.alh = self.runABAAlgorithm(n, function, self.lb, self.ub, dimension, iteration)
            else:
                self.alh = self.runBAAlgorithm(n, function, self.lb, self.ub, dimension, iteration)
        self.plotAnimation()



    def plotAnimation(self):
        self.w = PlotGraphics(self.alh, self.lb, self.ub)
        self.w.show()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.getInputValues)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
