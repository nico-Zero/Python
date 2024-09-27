import sqlite3 as sl

# con = sl.connect(":memory:")
con = sl.connect("customer.db")

# cteating a cuesor.
c = con.cursor()

# Create a Table

c.execute(
    """
    CREATE TABLE customers (
        id INTEGER PRIMARY  KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT,
        email TEXT
    )
    """
)

con.commit()
con.close()