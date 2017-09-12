import tkinter

top = tkinter.Tk()
C = tkinter.Canvas(top, bg="black", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=90, fill="green")
C.pack()

coordp = 10, 50, 240, 210
D = tkinter.Canvas(top, bg="black", height=250, width=300)
oval = D.create_polygon(coord,fill="yellow" )
D.pack()
top.mainloop()