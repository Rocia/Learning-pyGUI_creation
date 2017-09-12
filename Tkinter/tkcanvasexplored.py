#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:09:28 2017

@author: rocia
"""

import tkinter
master = tkinter.Tk()

#canvas line
canvas_width = 80
canvas_height = 40
w = tkinter.Canvas(master, width=canvas_width,height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")

			  
#tk2 rectangles and lines explored
x = tkinter.Canvas(master, width=200, height=100)
x.pack()

x.create_rectangle(50, 20, 150, 80, fill="#476042")
x.create_rectangle(65, 35, 135, 65, fill="yellow")
x.create_line(0, 0, 50, 20, fill="#476042", width=3)
x.create_line(0, 100, 50, 80, fill="#476042", width=3)
x.create_line(150,20, 200, 0, fill="#476042", width=3)
x.create_line(150, 80, 200, 100, fill="#476042", width=3)
master.mainloop()

