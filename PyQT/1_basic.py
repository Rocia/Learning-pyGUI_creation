#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)  #resizes window to dimensions specified in the parameters
    w.move(300, 300)    #move the window to the position on the screen specified by these co-ordinates
    w.setWindowTitle('Simple App')  #Title of the window
    w.show()
    
    sys.exit(app.exec_())