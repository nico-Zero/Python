import sqlite3 as sl

# con = sl.connect(":memory:")
con = sl.connect("customer.db")

# cteating a cuesor.
c = con.cursor()

c.execute("""
        SELECT * FROM customers
        WHERE First_name LIKE '%o%' AND rowid < 7
        ORDER BY First_name 
        LIMIT 1
          """)
# print(c.fetchone())
# print(c.fetchmany(4))

# for i in c.fetchall():
#     print(f"id:{i[0]}, name:{i[1]} {i[2]}, email:{i[3]}\n")

print(*(c.fetchall()),sep="\n")

print("\nCommand executed successfully...")
con.commit()
con.close()
