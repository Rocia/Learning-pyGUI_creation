#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:08:23 2017

@author: root
"""
import tkinter
root = tkinter.Tk()
#listbox 1
'''
listbox = tkinter.Listbox(root)
listbox.pack()

for i in range(20):
    listbox.insert('end', str(i))
'''	
	
#listbox 2	
#'''
listbox = tkinter.Listbox(root)
listbox.pack(fill="both", expand=True)

for i in range(20):
    listbox.insert('end', str(i))
#'''
root.mainloop()