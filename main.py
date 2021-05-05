#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
MP3 player
 
author: Mculover666
version: v2.0.0
"""
 
import sys
from MP3Player import MP3Player
from PyQt5.QtWidgets import (QApplication)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MP3Player()
    sys.exit(app.exec_())