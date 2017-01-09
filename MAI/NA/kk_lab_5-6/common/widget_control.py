from PySide import QtGui
from PySide import QtCore
from PySide import QtUiTools
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def get_widget_from_ui(path):
    loader = QtUiTools.QUiLoader()
    file = QtCore.QFile(path)
    file.open(QtCore.QFile.ReadOnly)
    widget = loader.load(file)
    file.close()
    return widget


def set_line_edit_color(line_edit, rgb_color):
    line_edit.setStyleSheet('''
    QLineEdit {{
        color: rgb{};
    }}'''.format(tuple(rgb_color)))


# def get_message_box(title, msg)

class MatplotCanvasWidget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, frameon=False)
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(True)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.axes.tick_params(axis='both', which='major', labelsize=6)
        # self.fig.subplots_adjust(left=0.05, right=0.98, top=0.98, bottom=0.05)
        self.fig.subplots_adjust(left=0.1, right=0.98, top=0.85, bottom=0.05)

        self.h = []
        self.l = []

    def add(self, x, y, label='', **kwargs):
        n = min(len(x), len(y))
        self.h.append(self.axes.plot(x[:n], y[:n], **kwargs)[0])
        self.l.append(label)

    def plot(self):
        self.axes.legend(self.h, self.l, prop={'size': 6}, bbox_to_anchor=(0.2, 1.00, 1., .102), loc=3, ncol=3,
                         borderaxespad=0.)
        # self.axes.legend(h, l, prop={'size': 6})
        self.draw()
        self.h = []
        self.l = []

    def clear(self):
        self.axes.cla()
        self.axes.grid()
        self.h = []
        self.l = []
