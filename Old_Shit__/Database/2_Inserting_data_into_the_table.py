import sqlite3 as sl

# con = sl.connect(":memory:")
con = sl.connect("customer.db")

# cteating a cuesor.
c = con.cursor()

# Create a Table
cus = [
    ('4', 'Rayli', 'Harda', 'R@gmail.com'),
    ('5', 'Hale', 'N', 'H@gmail.com'),
    ('6', 'Pici', 'Pop', 'P@gmail.com'),
    ('7', 'Sanar', 'Hord', 'S@gmail.com'),
    ('8', 'Rayli', 'Thomas', 'RT@gmail.com'),
    ('9', 'Nova', 'Smith', 'N@gmail.com'),
]


c.executemany("INSERT INTO customers VALUES (?,?,?,?)",cus)

print("Command executed successfully...")
con.commit()
con.close()
