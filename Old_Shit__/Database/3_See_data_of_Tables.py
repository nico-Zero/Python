import sqlite3 as sl

# con = sl.connect(":memory:")
con = sl.connect("customer.db")

# cteating a cuesor.
c = con.cursor()

c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany()
print((c.fetchall()))

print("\nCommand executed successfully...")
con.commit()
con.close()
