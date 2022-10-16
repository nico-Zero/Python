from itertools import chain
from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, justify = RIGHT)
e.grid(row=0, columnspan=4, padx=10, pady=10)
e1 = Entry(root, width=50, justify = RIGHT)
e1.grid(row=1, columnspan=4, padx=10, pady=10)

call_v = 0

def Count():
    l = ["+","-","/","*","%","^"]
    Current()
    global count
    count = sum(now_e.count(i) for i in l)

def Clear_e():
    e.delete(0, END)

def Clear_e1():
    e1.delete(0, END)

def Clear():
    global now_e
    global now_e1
    Clear_e()
    Clear_e1()
    global call_v
    call_v = 0
    now_e = 0
    now_e1 = 0

def Buttons(x):
    Current()
    Clear_e()
    e.insert(0, now_e +  str(x))
    Count()
    

def Helper_(x):
    global help
    help = now_e + x

def Current():
    now_E = e.get()
    now_E1 = e1.get()

    global now_e
    global now_e1
    
    now_e = now_E
    now_e1 = now_E1[1:]

def Orignal():
    number = e.get()
    global num
    num = number[::-1]
    
def Check(x):
    now = now_e[::-1]
    global __check
    l = ["+","-","/","*","%","^"]
    j = []
    for i in l :
        try:
            j.append(now.index(i))
        except:
            pass
    try:
        __check = now[min(j)]
    except ValueError:
        __check = x

def Core(x : str):
    n = "1234567890"
    Current()
    if call_v > 0:
        for i in n:
            if i == now_e[-1]:
                Helper_(x)
                Now()
                After()
                Clear_e()
                e.insert(0, now_e + x)
                Clear_e1()
                Brain(x)
            else:
                pass
    else:
        Helper_(x)
        Now()
        After()
        Clear_e()
        e.insert(0, now_e + x)
        Clear_e1()
        Brain(x)

def Brain(x = "+"):
    global call_v
    global now_ex
    global num_1x
    global num_2x

    try:
        now_ex = int(now_e1)
    except:
        try:
            now_ex = float(now_e1)
        except:
            now_ex = 0
    try:
        num_1x = int(num_1)
    except:
        num_1x = float(num_1)
        
    try:
        num_2x = int(num_2)
    except:
        try:
            num_2x = float(num_2)
        except:
            num_2x = 0

    if call_v > 2:
        Check(x)
        global now_e
        if now_e =="":
            now_e = 0
            
        try:
            match __check:
                case "+":
                    if call_v > 4:
                        e1.insert(0,"=" + str((now_ex + num_1x)))

                    elif call_v >= 2 and call_v <= 4:
                        e1.insert(0,"=" + str((num_1x + num_2x)))
                        
                case "-":
                    if call_v > 4:
                        e1.insert(0,"=" + str((now_ex - num_1x)))

                    elif call_v >= 2 and call_v <= 4:
                        e1.insert(0,"=" + str((num_1x - num_2x)))
                        
                case "*":
                    if call_v > 4:
                        e1.insert(0,"=" + str((now_ex * num_1x)))

                    elif call_v >= 2 and call_v <= 4:
                        e1.insert(0,"=" + str((num_1x * num_2x)))
                        
                case "/":    
                    if call_v > 4:
                        e1.insert(0,"=" + str((now_ex / num_1x)))

                    elif call_v >= 2 and call_v <= 4:
                        e1.insert(0,"=" + str((num_1x / num_2x)))
    
                case "^":    
                    if call_v > 4:
                        e1.insert(0,"=" + str((now_ex ** num_1x)))

                    elif call_v >= 2 and call_v <= 4:
                        e1.insert(0,"=" + str((num_1x ** num_2x)))
        except ValueError:
            Clear()

    call_v += 1

def Now(x = "!"):
    global call_v
    global num_1
    global new_
    # global help
    l = ["+","-","/","*","%","^"]
    n = "1234567890"
    m = []
    mx = []
    if x != "!":
        help_ = x[::-1]
    else:
        help_ = help[::-1]
    if call_v >= 0:
        for i in n:
            for j in help_:
                if i == j:
                    m.append(help_.index(j))
                    break
                else:
                    pass
        new_ = help_[min(m):]
        for i in l:
            for j in new_:
                if i == j:
                    mx.append(new_.index(j))
                    break
                else:
                    pass
        try:
            num_1 = "".join(reversed(new_[:min(mx)]))
        except:
            num_1 = "".join(reversed(new_[::1]))    
    call_v += 1
    
def After():
    global call_v
    global num_2
    l = ["+","-","/","*","%","^"]
    mx = []
    if call_v > 1 :
        for j in l:
            if new_.count(j):
                x = [i for i in range(len(new_)) if new_[i] == j]
                mx.append(x)
        mx = list(chain(*mx))
        if len(mx) > 1:
            mx = new_[min(mx)+1:sorted(mx)[1]]
        elif len(mx) == 1 :
            mx = new_[min(mx)+1:]
        num_2 = "".join(reversed(mx))
        
    # call_v += 1

def Dot():
    Current()
    l = ["+","-","/","*","%","^"]
    c = sum(now_e.count(i) for i in l)
    for i in l:
        if c == 0:
            if now_e.count(".") == 0 and now_e[-1] != i:
                Clear_e()
                e.insert(0, now_e + ".")
        else:
            if now_e.count(".") <= c and now_e[-1] != i:
                Clear_e()
                e.insert(0, now_e + ".")
def Ans():
    Current()
    Count()
    Clear_e()
    Clear_e1()
    global call_v
    Now(now_e)
    global num_1
    After()
    global num_2
    Brain()
    call_v = 0
    if count != 0:
        num_1 = ""
        num_2 = ""

    
def Delete():
    global call_v
    Count()
    x = e.get()
    l = len(x)

    if len(x) > 0:
        x = x[: l - 1]
        if l != 1:
            o = x[-1]
        try:
            if o == ".":
                x = x[: l - 2]
            o = ""
        except UnboundLocalError:
            Clear()
    else:
        pass
    Clear_e()
    if count == 1:
        call_v = 2
    else:
        pass

    e.insert(0, x)
    
def Add(x : str):
    Current()
    if len(now_e) != 0:
        Core(x)
    else:
        pass
def Subs(x: str):
    Current()
    if len(now_e) != 0:
        Core(x)
    else:
        pass

def Multi(x: str):
    Current()
    if len(now_e) != 0:
        Core(x)
    else:
        pass

def Divi(x: str):
    Current()
    if len(now_e) != 0:
        Core(x)
    else:
        pass

def Power(x: str):
    Current()
    if len(now_e) != 0:
        Core(x)
    else:
        pass

def Perc():
    Ans()
    Helper_("%")
    Now()
    global num_1
    
    if count == 0:
        n = num_1
        try: 
            n = int(n)
        except:
            n = float(n)

    Current()
    
    global call_v
    global nx
    call_v = 0

    Brain()
    Clear_e1()
        
    if count == 0:
        e.insert(0,str(n / 100))
    else:
        if call_v >= 1:
            e.insert(0,str(now_ex / 100))
        else:
            pass
    n = 0
    num_1 = ""

       
button_0 = Button(root, text="0", padx=50, pady=20,command= lambda : Buttons(0))
button_1 = Button(root, text="1", padx=50, pady=20,command= lambda : Buttons(1))
button_2 = Button(root, text="2", padx=50, pady=20,command= lambda : Buttons(2))
button_3 = Button(root, text="3", padx=50, pady=20,command= lambda : Buttons(3))
button_4 = Button(root, text="4", padx=50, pady=20,command= lambda : Buttons(4))
button_5 = Button(root, text="5", padx=50, pady=20,command= lambda : Buttons(5))
button_6 = Button(root, text="6", padx=50, pady=20,command= lambda : Buttons(6))
button_7 = Button(root, text="7", padx=50, pady=20,command= lambda : Buttons(7))
button_8 = Button(root, text="8", padx=50, pady=20,command= lambda : Buttons(8))
button_9 = Button(root, text="9", padx=50, pady=20,command= lambda : Buttons(9))
button_dot = Button(root, text=".", padx=52, pady=20,command= Dot)

button_add = Button(root, text="+", padx=49, pady=20, command= lambda: Add("+"))
button_subs = Button(root, text="-", padx=51, pady=20, command= lambda: Subs("-"))
button_multi = Button(root, text="*", padx=51, pady=20, command= lambda: Multi("*"))
button_divi = Button(root, text="/", padx=51, pady=20, command= lambda: Divi("/"))
button_power = Button(root, text="^", padx=49, pady=20, command= lambda: Power("^"))
button_perc = Button(root, text="%", padx=48, pady=20, command= Perc)

button_delete = Button(root, text="<-", padx=46, pady=20, command= Delete)
button_clear = Button(root, text="Clear", padx=37, pady=20,command= Clear)
button_ans = Button(root, text="=", padx=49, pady=20, command= Ans)

# put the button on the sereen
button_clear.grid(row=2, column=0)
button_delete.grid(row=2, column=1)
button_perc.grid(row=2, column=2)
button_divi.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multi.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_subs.grid(row=4, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_add.grid(row=5, column=3)

button_power.grid(row=6, column=1)
button_0.grid(row=6, column=0)
button_dot.grid(row=6, column=2)
button_ans.grid(row=6, column=3)

root.mainloop()
 