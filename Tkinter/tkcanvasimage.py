#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:40:08 2017

@author: root
"""
import tkinter
import PIL

#image = PIL.Image.open("roc.jpg")

master = tkinter.Tk()
canvas_width = 300
canvas_height =300

master = tkinter.Tk()

canvas = tkinter.Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()

img = tkinter.PhotoImage(PIL.Image.open("roc.jpg"))
canvas.create_image(20,20, anchor='nw', image=img)

master.mainloop