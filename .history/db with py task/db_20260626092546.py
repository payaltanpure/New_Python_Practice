import sqlite3

conn= sqlite3.connect("employee.db")
print("db connected ")

cursor= conn.cursor()

cursor.execute("""

create table if not exists emp(
               eid integer primary key autoincrement,
               name text not null
               sal integer)
""")

conn.commit()
print("Table created")