#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:09:11 2017

@author: root
"""

import tkinter
root = tkinter.Tk()
#tk widget
'''
w = tkinter.Label(root, text="Red", bg="red", fg="white")
w.pack()
w = tkinter.Label(root, text="Green", bg="green", fg="black")
w.pack()
w = tkinter.Label(root, text="Blue", bg="blue", fg="white")
w.pack()
'''

#tk widget 2
'''
w = tkinter.Label(root, text="Red", bg="red", fg="white")
w.pack(fill='x')
w = tkinter.Label(root, text="Green", bg="green", fg="black")
w.pack(fill='x')
w = tkinter.Label(root, text="Blue", bg="blue", fg="white")
w.pack(fill='x')
'''

#tk widget 3
'''
w = tkinter.Label(root, text="Red", bg="red", fg="white")
w.pack(side='left')
w = tkinter.Label(root, text="Green", bg="green", fg="black")
w.pack(side='left')
w = tkinter.Label(root, text="Blue", bg="blue", fg="white")
w.pack(side='left')
'''
root.mainloop()