import sqlite3
db = sqlite3.connect('database_main_db')
cursor = db.cursor()  # Get a cursor object

#Create a table called python_programming.

cursor.execute('''CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT,
                   	grade INTEGER)
''')
db.commit()

#Insert the following new rows into the python_programming table:

cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (55, "Carl Davis", 61))
print('inserted')

cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (66, "Dennis Fredrickson", 88))
print('inserted')

cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (77, "Jane Richards", 78))
print('inserted')

cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (12, "Peyton Sawyer", 45))
print('inserted')

cursor.execute('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', (2, "Lucas Brooke", 99))
print('inserted')

db.commit()

#Select all records with a grade between 60 and 80.

cursor.execute('''SELECT id, name, grade FROM python_programming  WHERE grade >= 60 AND grade <= 80''')
records = cursor.fetchall()
print("All records with a grade between 60 and 80")
for record in records: print(record)
print("\n")

#Change Carl Davis’s grade to 65.

cursor.execute('''UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis"''')
db.commit()

cursor.execute('''SELECT * FROM python_programming''')
records = cursor.fetchall()
print("Change Carl Davis's grade to 65")
for record in records: print(record)
print("\n")

#Delete Dennis Fredrickson’s row.

cursor.execute('''DELETE FROM python_programming WHERE name = "Dennis Fredrickson" ''')
db.commit()

cursor.execute('''SELECT * FROM python_programming''')
records = cursor.fetchall()
print("Delete Dennis Fredrickson's row")
for record in records: print(record)
print("\n")

#Change the grade of all people with an id below than 55.

cursor.execute('''UPDATE python_programming SET grade = 66 WHERE id < 55 ''')
db.commit()

cursor.execute('''SELECT * FROM python_programming''')
records = cursor.fetchall()
print("Change the grade of all people with an id below than 55 with grade = 66")
for record in records: print(record)
