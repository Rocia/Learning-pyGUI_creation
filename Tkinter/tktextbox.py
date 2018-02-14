#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:53:03 2017

@author: rocia
"""

import tkinter

top = tkinter.Tk()
L1 = tkinter.Label(top, text="User Name")
L1.pack( side = 'left')
E1 = tkinter.Entry(top, bd =5)

E1.pack(side = 'right')

top.mainloop()