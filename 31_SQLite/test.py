import sqlite3
db = sqlite3.connect('database_main_db')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''SELECT * FROM python_programming  WHERE grade >= 60 AND grade <= 80''')
records = cursor.fetchall()

for record in records: print(record)

cursor.execute('''UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis"''')

db.commit()

cursor.execute('''DELETE FROM python_programming WHERE name = "Dennis Fredrickson" ''')
db.commit()

cursor.execute('''SELECT * FROM python_programming''')
records = cursor.fetchall()
for record in records: print(record)

cursor.execute('''UPDATE python_programming SET grade = 66 WHERE id < 55 ''')

db.commit()

cursor.execute('''SELECT * FROM python_programming''')
records = cursor.fetchall()
for record in records: print(record)
