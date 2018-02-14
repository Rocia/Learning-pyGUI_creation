#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:27:29 2017

@author: rocia
"""
#Python tkinter program to capture clicks within a window

import tkinter

root = tkinter.Tk()

def callback(event):
    print ("clicked at", event.x, event.y)

frame = tkinter.Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()



'''
Output:
	clicked at 53 30
clicked at 22 40
clicked at 32 31
clicked at 71 72
clicked at 49 46
clicked at 49 46
clicked at 41 30
clicked at 41 30
clicked at 41 30
'''