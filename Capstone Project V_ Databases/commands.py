import sqlite3

db = sqlite3.connect('library_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE stock(id TEXT PRIMARY KEY, Title TEXT, Author TEXT,
                   	Qty TEXT)
''')
db.commit()

cursor.execute('''INSERT INTO stock(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', ("3001", "A Tale of Two Cities", "Charles Dickens" , "30"))

cursor.execute('''INSERT INTO stock(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', ("3002", "Harry Potter and the Philosopher's Stone", "J.K. Rowling" , "40"))

cursor.execute('''INSERT INTO stock(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', ("3003", "The Lion, the Witch and the Wardrobe", "C. S. Lewis", "25"))

cursor.execute('''INSERT INTO stock(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', ("3004", "The Lord of the Rings", "J.R.R Tolkien", "37"))

cursor.execute('''INSERT INTO stock(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', ("3005", "Alice in Wondeland", "Lewis Carroll", "12"))
db.commit()