from matplotlib.figure import Figure
from matplotlib import animation
import numpy as np
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

class PlotGraphics(QtWidgets.QMainWindow):
    def __init__(self, algorithm, lb, ub):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        self.fig = Figure(figsize=(5, 5))
        self.canvas1 = FigureCanvas(self.fig)

        layout.addWidget(self.canvas1)
        self.addToolBar(NavigationToolbar(self.canvas1, self))
        self.setup(algorithm, lb, ub)

    def setup(self, algorithm, lb, ub):
        agents = algorithm.get_agents()
        x = np.array([j[0] for j in agents[0]])
        y = np.array([j[1] for j in agents[0]])

        self.ax1 = self.fig.subplots()
        self.ax1.set_aspect('equal')
        self.ax1.grid(True, linestyle='-')
        self.ax1.set_xlim([lb, ub])
        self.ax1.set_ylim([lb, ub])
        self.scat1 = self.ax1.scatter(x, y, color='black')

        def updateAnimation(i):
            x = np.array([j[0] for j in agents[i]])
            y = np.array([j[1] for j in agents[i]])
            self.scat1.set_offsets(list(zip(x, y)))

        self.ani = animation.FuncAnimation(self.fig, updateAnimation, frames=len(agents) - 1)