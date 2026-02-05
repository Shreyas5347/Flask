import sqlite3

conn=sqlite3.connect("test.db")
c=conn.cursor()

#c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
#c.execute("INSERT INTO users (name, age) VALUES ('shreyas', 20)")
c.execute("SELECT * FROM users")
print(c.fetchall())
conn.commit()
conn.close()