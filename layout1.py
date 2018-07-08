# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 19:46:43 2018

@author: Admin
"""
# https://gist.github.com/anonymous/9305da687ef674f1a2c33db10ba8620e
import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton('Push Me')
    l = QtWidgets.QLabel('Mirame')

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addLayout(h_box)

    w.setLayout(v_box)

    w.setWindowTitle('PyQt5 Lesson 4')
    w.show()

    sys.exit(app.exec_())

window()