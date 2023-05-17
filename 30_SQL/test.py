import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('example.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = '''CREATE TABLE EMPLOYEE(
        EmployeeID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Address varchar(255),
        PhoneNumber varchar(255),
        PRIMARY KEY (EmployeeID)
)'''

cursor.execute(sql)

conn.commit()
conn.close()