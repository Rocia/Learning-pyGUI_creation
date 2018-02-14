#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:05:36 2017

@author: rocia
"""

import tkinter

canvas_width = 500
canvas_height = 150

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

master = tkinter.Tk()
master.title( "Painting using Ovals" )
w = tkinter.Canvas(master, width=canvas_width, height=canvas_height)

w.pack(expand = True, fill = 'both')
w.bind( "<B1-Motion>", paint )

message = tkinter.Label( master, text = "Press and Drag the mouse to draw" )
message.pack(side = 'bottom')
    
master.mainloop()