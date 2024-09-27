from tkinter import *

w = Tk()

canvas = Canvas(w,height=500,width=500)
# canvas.create_line(0,0,500,500,fill="red",width=5)
# canvas.create_line(500,0,0,500,fill="green",width=5)
# canvas.create_line(0,250,500,250,fill="blue",width=5)
# canvas.create_rectangle(50,50,250,250,fill="pink",width=5)
# canvas.create_polygon(250,0,500,500,0,500,fill="pink",outline="pink")
# canvas.create_arc(0,0,500,500,start=90,extent=180)
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,start=180,fill="white",extent=180,width=10)
canvas.create_oval(200,200,300,300,fill="white",width=10)
canvas.create_oval(220,220,280,280,fill="white",width=5,outline="#f1e7e7")

canvas.pack()

w.mainloop()
# 8:50:28