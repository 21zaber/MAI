from PySide import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import common.widget_control
from common.arithmetic_parser import FunctionFromStr
from lab_5_3.elliptic_pde import EllipticPDE


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Эллиптические уравнения')
        w = common.widget_control.get_widget_from_ui(path='./lab_5_3/gui/ui_forms/main_window.ui')
        self.setCentralWidget(w)

        self.main_args = None
        self.bound_1 = None
        self.bound_2 = None
        self.bound_3 = None
        self.bound_4 = None
        self.max_x = None
        self.max_y = None
        self.step_num_x = None
        self.step_num_y = None
        self.step_x = None
        self.step_y = None
        self.eps = None

        self.analytic_func = None
        self.solutions = None
        self.errors_analytic_numeric = None

        self.scheme_names = ['libman', 'seidel', 'sor']
        self.scheme_labels = ['Libman', 'Seidel', 'SOR']
        self.scheme_check_box = [w.checkBox_libman, w.checkBox_seidel, w.checkBox_sor]

        self.set_pixmaps()
        self.set_widgets_connections()

        self.canvas_solution_x = common.widget_control.MatplotCanvasWidget()
        self.toolbar_solution_x = NavigationToolbar(self.canvas_solution_x, self)
        w.verticalLayout_sol_x.addWidget(self.toolbar_solution_x)
        w.verticalLayout_sol_x.addWidget(self.canvas_solution_x)

        self.canvas_solution_y = common.widget_control.MatplotCanvasWidget()
        self.toolbar_solution_y = NavigationToolbar(self.canvas_solution_y, self)
        w.verticalLayout_sol_y.addWidget(self.toolbar_solution_y)
        w.verticalLayout_sol_y.addWidget(self.canvas_solution_y)

        self.canvas_error_x = common.widget_control.MatplotCanvasWidget()
        self.toolbar_error_x = NavigationToolbar(self.canvas_error_x, self)
        w.verticalLayout_err_x.addWidget(self.toolbar_error_x)
        w.verticalLayout_err_x.addWidget(self.canvas_error_x)

        self.canvas_error_y = common.widget_control.MatplotCanvasWidget()
        self.toolbar_error_y = NavigationToolbar(self.canvas_error_y, self)
        w.verticalLayout_err_y.addWidget(self.toolbar_error_y)
        w.verticalLayout_err_y.addWidget(self.canvas_error_y)

        self.save_args()

    def set_pixmaps(self):
        path_res = './lab_5_3/gui/resource/'
        self.centralWidget().label_pic.setPixmap(QtGui.QPixmap(path_res + 'pic.png'))

    def set_widgets_connections(self):
        w = self.centralWidget()

        w.tabWidget.currentChanged.connect(self.update_tab_page)

        w.spinBox_x.valueChanged.connect(self.plot_sol_for_x)
        w.spinBox_y.valueChanged.connect(self.plot_sol_for_y)

    def save_args(self):
        w = self.centralWidget()
        self.main_args = [w.doubleSpinBox_bx.value(),
                          w.doubleSpinBox_by.value(),
                          w.doubleSpinBox_c.value(),
                          FunctionFromStr(w.lineEdit_f.text())]
        f = self.main_args[3]
        f.set_args_name('x', 'y')
        f(0, 0)  # runtime check; check that f is func from x and t arguments
        # if not then field f.valid will be set to False

        self.bound_1 = [w.doubleSpinBox_alpha_1.value(),
                        w.doubleSpinBox_beta_1.value(),
                        FunctionFromStr(w.lineEdit_phi_1.text())]
        phi_1 = self.bound_1[2]
        phi_1.set_args_name('y')
        phi_1(0)

        self.bound_2 = [w.doubleSpinBox_alpha_2.value(),
                        w.doubleSpinBox_beta_2.value(),
                        FunctionFromStr(w.lineEdit_phi_2.text())]
        phi_2 = self.bound_2[2]
        phi_2.set_args_name('y')
        phi_2(0)

        self.bound_3 = [w.doubleSpinBox_alpha_3.value(),
                        w.doubleSpinBox_beta_3.value(),
                        FunctionFromStr(w.lineEdit_phi_3.text())]
        phi_3 = self.bound_3[2]
        phi_3.set_args_name('x')
        phi_3(0)

        self.bound_4 = [w.doubleSpinBox_alpha_4.value(),
                        w.doubleSpinBox_beta_4.value(),
                        FunctionFromStr(w.lineEdit_phi_4.text())]
        phi_4 = self.bound_4[2]
        phi_4.set_args_name('x')
        phi_4(0)

        if w.checkBox_analytic.isChecked():
            self.analytic_func = FunctionFromStr(w.lineEdit_analytic.text())
            self.analytic_func.set_args_name('x', 'y')
            self.analytic_func(0, 0)

        self.max_x = w.doubleSpinBox_max_x.value()
        self.max_y = w.doubleSpinBox_max_y.value()
        self.step_num_x = w.spinBox_nx.value()
        self.step_num_y = w.spinBox_ny.value()
        self.eps = 10 ** w.spinBox_eps.value()

        self.step_x = self.max_x / self.step_num_x
        self.step_y = self.max_y / self.step_num_y

    def update_tab_page(self, index):
        if index == 0:
            return
        self.save_args()
        if self.args_valid():
            w = self.centralWidget()
            w.spinBox_x.setMaximum(self.step_num_x)
            w.spinBox_y.setMaximum(self.step_num_y)
            self.calc_solutions()
            self.plot_sol_for_x()
            self.plot_sol_for_y()
            self.plot_err_x()
            self.plot_err_y()
        else:
            self.centralWidget().tabWidget.setCurrentIndex(0)
            QtGui.QMessageBox.warning(None, 'Achtung!', 'Условия заданы неверно')

    def args_valid(self):
        f = self.main_args[3]
        phi_1 = self.bound_1[2]
        phi_2 = self.bound_2[2]
        phi_3 = self.bound_3[2]
        phi_4 = self.bound_4[2]
        return (f.valid and
                phi_1.valid and phi_2.valid and phi_3.valid and phi_4.valid and
                self.analytic_func.valid)

    def calc_solutions(self):
        solver = EllipticPDE(*(self.main_args +
                               self.bound_1 +
                               self.bound_2 +
                               self.bound_3 +
                               self.bound_4 +
                               [self.max_x, self.max_y,
                                self.step_num_x, self.step_num_y]))

        w = self.centralWidget()
        sols = []
        print('=========================')
        def pr(s):
            print(s.final_eps)
            print(s.cur_iter_num)
            print('------------')
        if w.checkBox_libman.isChecked():
            s = solver.libman()
            sols.append(('Libman', s.solve(self.eps)))
            print('Libman')
            pr(s)
        if w.checkBox_seidel.isChecked():
            s = solver.seidel()
            sols.append(('Seidel', s.solve(self.eps)))
            print('Seidel')
            pr(s)
        if w.checkBox_sor.isChecked():
            s = solver.sor(w.doubleSpinBox_relax.value())
            sols.append(('SOR', s.solve(self.eps)))
            print('SOR')
            pr(s)
        if w.checkBox_analytic.isChecked():
            u = [[self.analytic_func(x * self.step_x, y * self.step_y) for y in range(self.step_num_y + 1)]
                 for x in range(self.step_num_x + 1)]
            sols.append(('Analytic', u))
        self.solutions = sols

    def plot_sol_for_x(self):
        self.canvas_solution_y.clear()
        y = [i * self.step_y for i in range(self.step_num_y + 1)]
        cur_x = self.centralWidget().spinBox_x.value()
        for s in self.solutions:
            self.canvas_solution_y.add(y, s[1][cur_x], label=s[0])
        self.canvas_solution_y.plot()

    def plot_sol_for_y(self):
        self.canvas_solution_x.clear()
        x = [i * self.step_x for i in range(self.step_num_x + 1)]
        cur_y = self.centralWidget().spinBox_y.value()
        for s in self.solutions:
            self.canvas_solution_x.add(x, [p[cur_y] for p in s[1]], label=s[0])
        self.canvas_solution_x.plot()

    def plot_err_x(self):
        analytic = None
        numeric = []
        for s in self.solutions:
            if s[0] == 'Analytic':
                analytic = s[1]
            else:
                numeric.append(s)
        if analytic is None:
            return
        self.canvas_error_x.clear()
        x = [i * self.step_x for i in range(self.step_num_x + 1)]
        tmp_lam = lambda a, b: max(map(lambda x, y: abs(x - y), a, b))
        err = [(s[0], [tmp_lam(analytic[i], s[1][i]) for i in range(len(analytic))]) for s in numeric]
        for e in err:
            self.canvas_error_x.add(x, e[1], label='err x ' + e[0])
        self.canvas_error_x.plot()

    def plot_err_y(self):
        analytic = None
        numeric = []
        for s in self.solutions:
            if s[0] == 'Analytic':
                analytic = s[1]
            else:
                numeric.append((s[0], list(zip(*s[1]))))
        if analytic is None:
            return
        self.canvas_error_y.clear()
        y = [i * self.step_y for i in range(self.step_num_y + 1)]
        tmp_lam = lambda a, b: max(map(lambda x, y: abs(x - y), a, b))
        analytic = list(zip(*analytic))
        err = [(s[0], [tmp_lam(analytic[i], s[1][i]) for i in range(len(analytic))]) for s in numeric]
        for e in err:
            self.canvas_error_y.add(y, e[1], label='err y ' + e[0])
        self.canvas_error_y.plot()


if __name__ == '__main__':
    pass
