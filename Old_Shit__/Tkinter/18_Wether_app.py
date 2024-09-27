from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import requests
import json

root = Tk()
root.title("Opendilog")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/media/zero/Software/Python/Old_Shit__/Tkinter/wifi-router.png'))
root.geometry("200x50")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=87109&distance=25&API_KEY=3A9D8255-9564-4137-AB58-C5A4A4D162B0

def wether(x):
    try:
        api_r = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={x}&distance=25&API_KEY=3A9D8255-9564-4137-AB58-C5A4A4D162B0")
        api = json.loads(api_r.content)
        city = api[0]["ReportingArea"]
        aqi = api[0]["AQI"]
        q_n = api[0]["Category"]["Number"]
        quality = api[0]["Category"]["Name"]
        
        report =  city + " Air-Quality " + str(aqi) + " " + quality
        color = {1:"#00e400",2:"#ffff00",3:"#ff7e00",4:"#ff0000",5:"#8f3f97",6:"#7e0023"}
        print(report)

        new = Tk()
        new.title("Wether")
        new.configure(bg=color[q_n])
        x = Label(new,text=report,font=("Helvetica",15),bg=color[q_n])
        x.pack()
        
    except:
        messagebox.showerror("Error...", "")

        
w = Entry(root,width=10)
w.pack()
Button(root,text="Search",command= lambda: wether(w.get())).pack()

root.mainloop()
