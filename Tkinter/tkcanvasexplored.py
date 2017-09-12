#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
""" 
Created on Tue Sep 12 09:09:28 2017 
 
@author: rocia 
""" 
 
import tkinter 
master = tkinter.Tk() 
 
#canvas line 
canvas_width = 300 
canvas_height = 200 

'''w = tkinter.Canvas(master, width=canvas_width,height=canvas_height) 
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


colours = ("#476042", "yellow")
box=[]

for ratio in ( 0.2, 0.35 ):
   box.append( (canvas_width * ratio,
                canvas_height * ratio,
                canvas_width * (1 - ratio),
                canvas_height * (1 - ratio) ) )


w = tkinter.Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

for i in range(2):
   w.create_rectangle(box[i][0], box[i][1],box[i][2],box[i][3], fill=colours[i])

w.create_line(0, 0,                 # origin of canvas
              box[0][0], box[0][1], # coordinates of left upper corner of the box[0]
              fill=colours[0], 
              width=3)
w.create_line(0, canvas_height,     # lower left corner of canvas
              box[0][0], box[0][3], # lower left corner of box[0]
              fill=colours[0], 
              width=3)
w.create_line(box[0][2],box[0][1],  # right upper corner of box[0] 
              canvas_width, 0,      # right upper corner of canvas
              fill=colours[0], 
              width=3)
w.create_line(box[0][2], box[0][3], # lower right corner pf box[0]
              canvas_width, canvas_height, # lower right corner of canvas
              fill=colours[0], width=3)

w.create_text(canvas_width / 2,
              canvas_height / 2,
              text="Python")
			  
w = tkinter.Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline='green', 
            fill='yellow', width=3)		'''  
w = tkinter.Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

w.create_oval(10,10,300,200)
w.create_oval(20,20,290,190,outline="blue")
w.create_oval(30,30,280,180,outline="green",fill='yellow')


master.mainloop() 