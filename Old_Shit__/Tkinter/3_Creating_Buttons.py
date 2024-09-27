from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look I  clicked a Button")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myClick, fg= "blue", bg= "red")  
# suports hex color formate.
# state= DISABLED, padx=5, pady=5.
myButton.pack()

root.mainloop()
