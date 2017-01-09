from PySide import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import common.widget_control
from common.arithmetic_parser import FunctionFromStr
from lab_5_2.hyperbolic_pde import HyperbolicPDE


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Гиперболические уравнения')
        w = common.widget_control.get_widget_from_ui(path='./lab_5_2/gui/ui_forms/main_window.ui')
        self.setCentralWidget(w)

        self.main_args = None
        self.left_boundary_args = None
        self.right_boundary_args = None
        self.initial_args = None
        self.min_x = None
        self.max_x = None
        self.max_t = None
        self.step_num_x = None
        self.step_num_t = None
        self.step_x = None
        self.step_t = None
        self.analytic_func = None

        self.analytic_solution = None
        self.solutions = None
        self.errors_analytic_numeric = None

        self.scheme_names = ['explicit', 'implicit']
        self.scheme_labels = ['Explicit', 'Implicit']
        self.scheme_check_box = [w.checkBox_explicit, w.checkBox_implicit]

        self.app_order_names = ['first_order_two_points', 'second_order_two_points', 'second_order_three_points']
        self.app_order_labels = ['1o2p', '2o2p', '2o3p']
        self.app_order_check_box = [w.checkBox_o1p2, w.checkBox_o2p2, w.checkBox_o2p3]

        self.init_order_names = [1, 2]
        self.init_order_labels = ['init 1 order', 'init 2 order']
        self.init_order_check_box = [w.checkBox_init_1, w.checkBox_init_2]

        self.set_pixmaps()
        self.set_widgets_connections()

        self.canvas_solution = common.widget_control.MatplotCanvasWidget()
        self.toolbar_solution = NavigationToolbar(self.canvas_solution, self)
        w.verticalLayout_plot_solution.addWidget(self.toolbar_solution)
        w.verticalLayout_plot_solution.addWidget(self.canvas_solution)

        self.canvas_error = common.widget_control.MatplotCanvasWidget()
        self.toolbar_error = NavigationToolbar(self.canvas_error, self)
        w.verticalLayout_plot_error.addWidget(self.toolbar_error)
        w.verticalLayout_plot_error.addWidget(self.canvas_error)

        self.save_args()

    def set_pixmaps(self):
        w = self.centralWidget()

        path_res = './lab_5_2/gui/resource/'

        pixmap_labels = [[w.label_1_1, w.label_1_2, w.label_1_3, w.label_1_4, w.label_1_5],
                         [w.label_2_1, w.label_2_2],
                         [w.label_3_1, w.label_3_2],
                         [w.label_4_1, w.label_4_2],
                         [w.label_5_1],
                         [w.label_6_1, w.label_6_2, w.label_6_3, w.label_6_4, w.label_6_5],
                         [w.label_7_1, w.label_7_2, w.label_7_3],
                         [w.label_8_1, w.label_8_2]]

        for i in range(len(pixmap_labels)):
            for j, l in enumerate(pixmap_labels[i]):
                pixmap_labels[i][j].setPixmap(QtGui.QPixmap(path_res + '{}_{}.png'.format(i + 1, j + 1)))

    def set_widgets_connections(self):
        w = self.centralWidget()

        w.tabWidget.currentChanged.connect(self.update_tab_page)

        def f():
            self.update_canvas_solution()
            self.update_canvas_error()

        checkbox_widgets = self.scheme_check_box + self.app_order_check_box + self.init_order_check_box
        for x in checkbox_widgets:
            x.stateChanged.connect(f)

        w.checkBox_show_analytic.stateChanged.connect(self.update_canvas_solution)
        w.spinBox_stept.valueChanged.connect(self.update_canvas_solution)

        w.lineEdit_analytic_solution.returnPressed.connect(self.update_analytic_solution)

        def value_changed_step_x():
            l1 = w.doubleSpinBox_l1.value()
            l2 = w.doubleSpinBox_l2.value()
            n = w.spinBox_nx.value()
            if l2 - l1 > 0 and n > 0:
                w.label_stepx.setText(str((l2 - l1) / n)[:10])
            else:
                w.label_stepx.setText('Error')

        w.doubleSpinBox_l1.valueChanged.connect(value_changed_step_x)
        w.doubleSpinBox_l2.valueChanged.connect(value_changed_step_x)
        w.spinBox_nx.valueChanged.connect(value_changed_step_x)

        def value_changed_step_t():
            T = w.doubleSpinBox_T.value()
            n = w.spinBox_nt.value()
            if T > 0 and n > 0:
                w.label_stept.setText(str(T / n)[:10])
            else:
                w.label_stept.setText('Error')

        w.doubleSpinBox_T.valueChanged.connect(value_changed_step_t)
        w.spinBox_nt.valueChanged.connect(value_changed_step_t)

    def update_analytic_solution(self):
        self.analytic_func = FunctionFromStr(self.centralWidget().lineEdit_analytic_solution.text())
        self.analytic_func.set_args_name('x', 't')
        self.analytic_func(0, 0)
        if not self.analytic_func.valid:
            QtGui.QMessageBox.warning(None, 'Achtung!', 'Аналитическая функция задана неверно')
            self.centralWidget().checkBox_show_analytic.setCheckable(False)
            self.errors_analytic_numeric = None
            self.canvas_error.clear()
            return
        self.analytic_solution = [
            [self.analytic_func(x * self.step_x, t * self.step_t) for x in range(self.step_num_x + 1)]
            for t in range(self.step_num_t + 1)]
        self.calculate_errors()
        self.update_canvas_error()
        self.centralWidget().checkBox_show_analytic.setCheckable(True)

    def save_args(self):
        w = self.centralWidget()
        self.main_args = [w.doubleSpinBox_a.value() ** 0.5,
                          w.doubleSpinBox_b.value(),
                          w.doubleSpinBox_c.value(),
                          w.doubleSpinBox_e.value(),
                          FunctionFromStr(w.lineEdit_f.text())]
        f = self.main_args[4]
        f.set_args_name('x', 't')
        f(0, 0)  # runtime check; check that f is func from x and t arguments
        # if not then field f.valid will be set to False

        self.left_boundary_args = [w.doubleSpinBox_alpha.value(),
                                   w.doubleSpinBox_beta.value(),
                                   FunctionFromStr(w.lineEdit_phi0.text())]
        phi_0 = self.left_boundary_args[2]
        phi_0.set_args_name('t')
        phi_0(0)

        self.right_boundary_args = [w.doubleSpinBox_gamma.value(),
                                    w.doubleSpinBox_delta.value(),
                                    FunctionFromStr(w.lineEdit_phi1.text())]
        phi_1 = self.right_boundary_args[2]
        phi_1.set_args_name('t')
        phi_1(0)

        self.initial_args = [FunctionFromStr(w.lineEdit_psi_1.text()),
                             FunctionFromStr(w.lineEdit_psi_2.text())]
        self.initial_args[0].set_args_name('x')
        self.initial_args[0](0)
        self.initial_args[1].set_args_name('x')
        self.initial_args[1](0)

        self.min_x = w.doubleSpinBox_l1.value()
        self.max_x = w.doubleSpinBox_l2.value()
        self.max_t = w.doubleSpinBox_T.value()
        self.step_num_x = w.spinBox_nx.value()
        self.step_num_t = w.spinBox_nt.value()

    def update_tab_page(self, index):
        if index == 0:
            return
        self.save_args()
        if self.args_valid():
            self.step_x = (self.max_x - self.min_x) / self.step_num_x
            self.step_t = self.max_t / self.step_num_t
            self.centralWidget().spinBox_stept.setValue(0)
            self.centralWidget().spinBox_stept.setMaximum(self.step_num_t)

            self.update_solutions()
            self.update_canvas_solution()
            sigma = self.main_args[0] ** 2 * self.step_t ** 2 / self.step_x ** 2
            if sigma >= 1:
                msg = 'sigma = {0}^2 * {1}^2 / {2}^2 = \n\t = {3} >= 1\nЯвная схема неустойчива'.format(
                    self.main_args[0],
                    self.step_t,
                    self.step_x,
                    sigma)
                QtGui.QMessageBox().information(None, 'Achtung!', msg)
            self.update_analytic_solution()
        else:
            self.centralWidget().tabWidget.setCurrentIndex(0)
            QtGui.QMessageBox.warning(None, 'Achtung!', 'Условия заданы неверно')

    def args_valid(self):
        a, b, c, e, f = self.main_args
        alpha, beta, phi_0 = self.left_boundary_args
        gamma, delta, phi_1 = self.right_boundary_args
        psi_1, psi_2 = self.initial_args
        return (a > 0 and
                f.valid and phi_0.valid and phi_1.valid and psi_1.valid and psi_2.valid and
                (alpha != 0 or beta != 0) and
                (gamma != 0 or delta != 0) and
                self.max_x > self.min_x and
                self.max_t > 0 and
                self.step_num_x > 0 and
                self.step_num_t > 0)

    def update_solutions(self):
        solver = HyperbolicPDE(*(self.main_args +
                                 self.left_boundary_args +
                                 self.right_boundary_args +
                                 self.initial_args +
                                 [self.min_x, self.max_x, self.max_t]))

        self.solutions = [[[None] * len(self.init_order_names)
                           for _ in range(len(self.app_order_names))]
                          for _ in range(len(self.scheme_names))]
        solve_progress_dialog = QtGui.QProgressDialog('Solving...', 'cancel', 0,
                                                      len(self.scheme_names) *
                                                      len(self.app_order_names) *
                                                      len(self.init_order_names))
        solve_progress_dialog.setMinimumDuration(0)
        solve_progress_dialog.setWindowTitle('Please wait')
        solve_progress_dialog.show()
        for i, s in enumerate(self.scheme_names):
            for j, a in enumerate(self.app_order_names):
                for k, init in enumerate(self.init_order_names):
                    solve_progress_dialog.setValue(i * len(self.scheme_names) + j)
                    solve_progress_dialog.setLabelText('Solving...\n{} {} {}'.format(s, a, init))
                    self.solutions[i][j][k] = solver.solve(step_x=self.step_x,
                                                           step_t=self.step_t,
                                                           scheme_type=s,
                                                           boundary_approximation_func=a,
                                                           initial_approximation_order=init)
                    if solve_progress_dialog.wasCanceled():
                        break

    def calculate_errors(self):
        self.errors_analytic_numeric = [[[None] * len(self.init_order_names)
                                         for _ in range(len(self.app_order_names))]
                                        for _ in range(len(self.scheme_names))]
        a = self.analytic_solution
        for i in range(len(self.scheme_names)):
            for j in range(len(self.app_order_names)):
                for k in range(len(self.init_order_names)):
                    self.errors_analytic_numeric[i][j][k] = [
                        max(map(lambda x, y: abs(x - y), a[cur], self.solutions[i][j][k][cur])) for cur in range(len(a))]

    def update_canvas_error(self):
        if self.errors_analytic_numeric is None:
            return
        scheme = list(zip(self.scheme_check_box, self.scheme_labels))
        app_order = list(zip(self.app_order_check_box, self.app_order_labels))
        init_order = list(zip(self.init_order_check_box, self.init_order_labels))

        t = [i * self.step_t for i in range(self.step_num_t + 1)]

        self.canvas_error.clear()

        for i, s in enumerate(scheme):
            if not s[0].isChecked():
                continue
            for j, a in enumerate(app_order):
                if not a[0].isChecked():
                    continue
                for k, init in enumerate(init_order):
                    if not init[0].isChecked():
                        continue
                    self.canvas_error.add(t, self.errors_analytic_numeric[i][j][k],
                                          label='err ' + s[1] + ' ' + a[1] + ' ' + init[1])
        self.canvas_error.plot()

    def update_canvas_solution(self):
        w = self.centralWidget()
        scheme = list(zip(self.scheme_check_box, self.scheme_labels))
        app_order = list(zip(self.app_order_check_box, self.app_order_labels))
        init_order = list(zip(self.init_order_check_box, self.init_order_labels))

        x = [self.min_x + i * self.step_x for i in range(self.step_num_x + 1)]
        cur_t = w.spinBox_stept.value()

        self.canvas_solution.clear()

        for i, s in enumerate(scheme):
            if not s[0].isChecked():
                continue
            for j, a in enumerate(app_order):
                if not a[0].isChecked():
                    continue
                for k, init in enumerate(init_order):
                    if not init[0].isChecked():
                        continue
                    self.canvas_solution.add(x, self.solutions[i][j][k][cur_t],
                                             label=s[1] + ' ' + a[1] + ' ' + init[1])

        if w.checkBox_show_analytic.isChecked():
            self.canvas_solution.add(x, self.analytic_solution[cur_t], label='analytic', linestyle='--')
        self.canvas_solution.plot()
        w.label_t.setText(str(cur_t * self.step_t)[:5])

if __name__ == '__main__':
    pass
