from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/__/Python/Tkinter/wifi-router.png'))
# root.iconbitmap("@/media/zero/Software/__/Python/Tkinter/png icon/icons8-vk-com-500.xbm")
# root.iconphoto(True,PhotoImage("/media/zero/Software/__/Python/Tkinter/wifi-router.png"))

img = ImageTk.PhotoImage(Image.open("/media/zero/Software/__/Python/Tkinter/wifi-router.png"))
lable = Label(image=img)
lable.pack()

button_quit = Button(root, text="Exit", command= root.quit)
button_quit.pack()


root.mainloop()
