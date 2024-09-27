from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3


root = Tk()
root.title("Opendilog")
root.call(
    "wm",
    "iconphoto",
    PhotoImage(file="/media/zero/Software/__/Python/Tkinter/wifi-router.png"),
)
root.geometry("400x550")

# Database

con = sqlite3.connect("data.db")
c = con.cursor()


def clear():
    f_name.delete(0, END)
    l_name.delete(0, END)
    mobile.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    d.delete(0,END)


def insert(x):
    con = sqlite3.connect("data.db")
    c = con.cursor()
    l = {
        "f_name": f_name.get(),
        "l_name": l_name.get(),
        "mobile": mobile.get(),
        "address": address.get(),
        "city": city.get(),
        "state": state.get(),
        "zipcode": zipcode.get(),
    }

    if all(list(l.values())):
        pass
    else:
        clear()
        return

    if x != "":
        c.execute(f"SELECT rowid FROM test")
        t = []
        for i in c.fetchall():
            t.append(str(i[0]))
            # print(t)

        if x in t:
            pass
        else:
            c.execute(
                f"""INSERT INTO test 
                VALUES(:f_name,
                    :l_name,
                    :mobile,
                    :address,
                    :city,
                    :state,
                    :zipcode
                    )
                """,
                l,
            )
        
            c.execute(f"""
                    UPDATE test 
                    SET rowid = {x}
                    WHERE First_name = :f_name
                    """,l)
    else:
        c.execute(
            """INSERT INTO test 
            VALUES(
                :f_name,
                :l_name,
                :mobile,
                :address,
                :city,
                :state,
                :zipcode
                )
            """,
            l,
        )

    clear()

    c.execute("SELECT * FROM test")
    print(*(c.fetchall()), sep="\n")

    con.commit()
    con.close()


def show(x):
    con = sqlite3.connect("data.db")
    c = con.cursor()

    if x != "":
        c.execute(f"SELECT rowid,* FROM test WHERE rowid = {x}")
        r = c.fetchone()
        l = ["Id","First_name","Last_name","Address","City","State","Zipcode"]
        
        for i,j in zip(r,l):
            Label(root, text=f"{j} = {i}").grid(column=0, columnspan=2, padx=(10, 0))
        d.delete(0,END)
    else:
        c.execute("SELECT rowid, * FROM test")
        r = c.fetchall()
        for i in r:
            Label(root, text=i).grid(column=0, columnspan=2, padx=(10, 0))
    # print(*(c.fetchall()),sep="\n")
    con.commit()
    con.close()


def delete(i):
    if i != "":
        con = sqlite3.connect("data.db")
        c = con.cursor()
        d.delete(0, END)
        c.execute(f"DELETE FROM test WHERE rowid={i}")

        con.commit()
        con.close()
    else:
        pass


def update(i):
    if i != "":
        new = Tk()
        new.title("Update test")
        new.geometry("400x280")

        f_name_u = Entry(new, width=30)
        f_name_u.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))
        Label(new, text="First_name:-").grid(row=0, padx=(10, 0), column=0, pady=(10, 0))
        l_name_u = Entry(new, width=30)
        l_name_u.grid(row=1, column=1, padx=(10, 0))
        Label(new, text="Last_name:-").grid(row=1, column=0, padx=(10, 0))
        mobile_u = Entry(new, width=30)
        mobile_u.grid(row=2, column=1, padx=(10, 0))
        Label(new, text="Mobile:-").grid(row=2, column=0, padx=(10, 0))
        address_u = Entry(new, width=30)
        address_u.grid(row=3, column=1, padx=(10, 0))
        Label(new, text="Address:-").grid(row=3, column=0, padx=(10, 0))
        city_u = Entry(new, width=30)
        city_u.grid(row=4, column=1, padx=(10, 0))
        Label(new, text="City:-").grid(row=4, column=0, padx=(10, 0))
        state_u = Entry(new, width=30)
        state_u.grid(row=5, column=1, padx=(10, 0))
        Label(new, text="State:-").grid(row=5, column=0, padx=(10, 0))
        zipcode_u = Entry(new, width=30)
        zipcode_u.grid(row=6, column=1, padx=(10, 0))
        Label(new, text="Zipcode:-").grid(row=6, column=0, padx=(10, 0))

        def save(x):
            con = sqlite3.connect("data.db")
            c = con.cursor()
            l = {
                "f_name_u": f_name_u.get(),
                "l_name_u": l_name_u.get(),
                "mobile_u": mobile_u.get(),
                "address_u": address_u.get(),
                "city_u": city_u.get(),
                "state_u": state_u.get(),
                "zipcode_u": zipcode_u.get(),
            }

            c.execute(
                f"""
                UPDATE test 
                SET First_name = :f_name_u, 
                Last_name = :l_name_u,
                Address = :address_u,
                City = :city_u,
                State = :state_u,
                Zipcode = :zipcode_u 
                WHERE rowid = {x}""",
                l,
            )
            # print(*(c.fetchall()),sep="\n")
            r = c.fetchall()
            for i in r:
                Label(root, text=i).grid(column=0, columnspan=2, padx=(10, 0))

            con.commit()
            con.close()
            f_name_u.delete(0, END)
            l_name_u.delete(0, END)
            mobile_u.delete(0, END)
            address_u.delete(0, END)
            city_u.delete(0, END)
            state_u.delete(0, END)
            zipcode_u.delete(0, END)


        def set(x):
            con = sqlite3.connect("data.db")

            c = con.cursor()
            c.execute(f"SELECT * FROM test WHERE rowid = {x}")
            fa = list(*(c.fetchall()))
            f_name_u.insert(0, fa[0])
            l_name_u.insert(0, fa[1])
            mobile_u.insert(0, fa[2])
            address_u.insert(0, fa[3])
            city_u.insert(0, fa[4])
            state_u.insert(0, fa[5])
            zipcode_u.insert(0, fa[6])

            con.commit()
            con.close()

        def dis():
            new.destroy()
        set(i)
        Button(new, text="Save", command=lambda: save(i)).grid(row=7,
            column=1,ipadx=30,pady=(5,0), padx=(150, 0)
        )
        Button(new, text="Quit", command=dis).grid(row=8,
            column=1,ipadx=30,pady=(5,0), padx=(150, 0)
        )
        
    else:
        pass


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))
Label(root, text="First_name:-").grid(row=0, padx=(10, 0), column=0, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=(10, 0))
Label(root, text="Last_name:-").grid(row=1, column=0, padx=(10, 0))
mobile = Entry(root, width=30)
mobile.grid(row=2, column=1, padx=(10, 0))
Label(root, text="Mobile:-").grid(row=2, column=0, padx=(10, 0))
address = Entry(root, width=30)
address.grid(row=3, column=1, padx=(10, 0))
Label(root, text="Address:-").grid(row=3, column=0, padx=(10, 0))
city = Entry(root, width=30)
city.grid(row=4, column=1, padx=(10, 0))
Label(root, text="City:-").grid(row=4, column=0, padx=(10, 0))
state = Entry(root, width=30)
state.grid(row=5, column=1, padx=(10, 0))
Label(root, text="State:-").grid(row=5, column=0, padx=(10, 0))
zipcode = Entry(root, width=30)
zipcode.grid(row=6, column=1, padx=(10, 0))
Label(root, text="Zipcode:-").grid(row=6, column=0, padx=(10, 0))

Label(root, text="Submit ID:- ").grid(row=7, column=0, pady=(10, 0), padx=(10, 0))
d = Entry(root, width=30, justify=LEFT)
d.grid(row=7, column=1, pady=(10, 0), padx=(10,0))

Button(root, text="Insert", command=lambda : insert(d.get())).grid(
    row=8, column=0, columnspan=2, pady=(10, 0), padx=(17, 0), ipadx=145
)
Button(root, text="Show Records", command=lambda : show(d.get())).grid(
    row=9, column=0, columnspan=2, pady=(5, 0), padx=(17, 0), ipadx=118
)

Button(root, text="Delete", command=lambda: delete(d.get())).grid(
    row=10, column=0, pady=(5, 0), columnspan=2, padx=(17, 0), ipadx=141
)

Button(root, text="Update", command=lambda: update(d.get())).grid(
    row=11, column=0, columnspan=2, pady=(5, 0), padx=(17, 0), ipadx=139
)

# c.execute("SELECT * FROM test")
# print(*(c.fetchall()),sep="\n")

con.commit()
# con.close()
root.mainloop()
