#!/usr/bin/python3.5

import sys
from PySide import QtGui
from common.widget_control import get_widget_from_ui
import lab_5_1.gui.main_window
import lab_5_2.gui.main_window
import lab_5_3.gui.main_window
# import lab_5_4.gui.main_window


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_menu = get_widget_from_ui('./gui/ui_forms/main_menu.ui')

    lab_5_1_widget = lab_5_1.gui.main_window.MainWindow(parent=main_menu)
    main_menu.pushButton_parabolic.clicked.connect(lab_5_1_widget.showMaximized)

    lab_5_2_widget = lab_5_2.gui.main_window.MainWindow(parent=main_menu)
    main_menu.pushButton_hyperbolic.clicked.connect(lab_5_2_widget.showMaximized)

    lab_5_3_widget = lab_5_3.gui.main_window.MainWindow(parent=main_menu)
    main_menu.pushButton_elliptical.clicked.connect(lab_5_3_widget.showMaximized)

    main_menu.pushButton_parabolic2D.setEnabled(False)
    # lab_5_4_widget = lab_5_4.gui.main_window.MainWindow(parent=main_menu)
    # main_menu.pushButton_parabolic2D.clicked.connect(lab_5_4_widget.showMaximized)

    main_menu.show()
    sys.exit(app.exec_())
