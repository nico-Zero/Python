from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))

img1 = ImageTk.PhotoImage(Image.open("/media/zero/Software/__/Python/Tkinter/full-battery.png"))
img2 = ImageTk.PhotoImage(Image.open("/media/zero/Software/__/Python/Tkinter/index.png"))
img3 = ImageTk.PhotoImage(Image.open("/media/zero/Software/__/Python/Tkinter/wifi-router.png"))
img4 = ImageTk.PhotoImage(Image.open("/media/zero/Software/__/Python/Tkinter/wireless-charger.png"))

i_list = [img1,img2,img3,img4]

lable = Label(image=i_list[0])
lable.grid(row = 0,column = 0, columnspan= 3)

count = 0
# Next Button Function
def Next():
    global lable
    global count

    if count == (len(i_list) - 2):
        button_next = Button(root, text=">>", state= DISABLED)
        button_next.grid(row = 1,column = 2)
    else:pass
    
    if count == 0:
        button_prev = Button(root, text="<<",command= Prev)
        button_prev.grid(row = 1,column = 0)
    else:pass

    count += 1
    lable.grid_forget()
    lable = Label(image=i_list[count])
    lable.grid(row = 0,column = 0, columnspan= 3)
    # Update status bar
    status = Label(root, text= f"Image {count+1} of {len(i_list)}",  bd = 1, relief= SUNKEN, anchor= E)
    status.grid(row = 2, column = 0, columnspan= 3, pady= 5, sticky= W+E)

# Prev Button Function 
def Prev():
    global lable
    global count
    
    if count == 1:
        button_prev = Button(root, text="<<", state= DISABLED)
        button_prev.grid(row = 1,column = 0)
    else:pass
    
    if count == (len(i_list) - 1):
        button_next = Button(root, text=">>", command= Next)
        button_next.grid(row = 1,column = 2)
    else:
        pass
    
    count -= 1
    lable.grid_forget()
    lable = Label(image=i_list[count])
    lable.grid(row = 0,column = 0, columnspan= 3)
    # Update status bar
    status = Label(root, text= f"Image {count+1} of {len(i_list)}",  bd = 1, relief= SUNKEN, anchor= E)
    status.grid(row = 2, column = 0, columnspan= 3, pady= 5, sticky= W+E)


button_prev = Button(root, text="<<", command= Prev, state= DISABLED)
button_quit = Button(root, text="Exit", command= root.quit)
button_next = Button(root, text=">>", command= Next)
status = Label(root, text= f"Image 1 of {len(i_list)}",  bd = 1, relief= SUNKEN, anchor= E)

button_prev.grid(row = 1,column = 0, pady= 10)
button_quit.grid(row = 1,column = 1, pady= 10)
button_next.grid(row = 1,column = 2, pady= 10)
status.grid(row = 2, column = 0, columnspan= 3, pady= 5, sticky= W+E)

root.mainloop()
