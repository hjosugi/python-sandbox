import sqlite3

con = sqlite3.connect("mydatabase.db")
con.execute("CREATE TABLE IF NOT EXISTS users (id, name, email)")
con.execute("INSERT INTO users (id, name, email) VALUES (1, '(DB)John Doe', '')")
con.execute("INSERT INTO users (id, name, email) VALUES (2, '(DB)Jane Michael', '')")
con.execute("INSERT INTO users (id, name, email) VALUES (3, '(DB)Joe Bloggs', '')")
con.commit()
con.close()
