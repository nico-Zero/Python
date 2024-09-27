from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Opendilog")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))
root.geometry("400x400")

def graph():
    house_p = np.random.normal(200000,25000,5000)
    plt.hist(house_p, 300)
    plt.show()

gr = Button(root,text="graph",command=graph)
gr.pack()

root.mainloop()
