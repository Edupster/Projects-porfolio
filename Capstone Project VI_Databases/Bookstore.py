import sqlite3
from tabulate import tabulate           # Import libraries
db = sqlite3.connect('library_db')
cursor = db.cursor()  # Get a cursor object

option =""
headers = ["ID", "Tittle", "Author", "Quantity"]

#Start a while loop to navigate in the menu, the loop will keep 
#repeating unless the option exit is entered
while option != "0":

    option = input("""Select an option from the option from the menu
1. Register a new book
2. Update book inf.
3. Delete book
4. Search book
5. See all books
0. Exit\n""")
    
    #If the option entered is Register a new book then request to enter
    #the new book details and register the new book in the database
    if option == "1":
        id = ( input( "Enter the book's id: "))
        
        cursor.execute('''SELECT * FROM stock WHERE id=? ''',(id,))
        record = cursor.fetchone()
        if record == None:
            Title = input( "Enter the book's Title: ")
            Author = input( "Enter the book's Author: ")
            Qty = ( input("Enter the Quantity available in stock: "))
            flag = 0
            while flag == 0:
                for i in Qty:
                    if i in ["0","1","2","3","4","5","6","7","8","9",]:
                        pass
                    else:
                        flag = 1
                if flag == 0:
                    break
                if flag == 1:
                    print("Please enter only integer numbers without spaces")
                    Qty = input("Enter the Quantity available in stock: ")
                    flag = 0
            
            cursor.execute('''INSERT INTO stock(id, Title, Author, Qty)
                  VALUES(?,?,?,?)''', (id, Title, Author, Qty))
            db.commit()
            print("The book has been registered successfully!")
        else:
            print("The book ID entered already exists in the database!")
        

    #If the option entered is update then request to enter the book id from
    #the list displayed list and request to select the data to be update.
    #Update the details entered in the database.

    if option == "2":
        cursor.execute('''SELECT * FROM stock''')
        records = cursor.fetchall()
        records = list( records )
        print( tabulate ( records, headers))
        while True:
            id = ( input ("Enter the ID of the book that you want to update: "))
            cursor.execute('''SELECT * FROM stock WHERE id=? ''',(id,))
            record = cursor.fetchone()
            if record != None:
                print ( record )
                id = record[0]
                Title = record[1]
                Author = record[2]
                Qty = record[3]
                print("\n")
                break
            else:
                print("Invalid book ID!, Try again")

        option1=("")
        while option1 != "5":
            option1=input("""Select the information that you'd like to update
1 - ID
2 - Title
3 - Author
4 - Qty
5 - Finish update \n""")
            if option1 == "1":
                id1 = ( input("Enter the new book's ID: "))
                cursor.execute('''SELECT id FROM stock''')
                ids = cursor.fetchall()
                ids2 = []
                for i in range ( 0, len( ids )):
                    ids2.append( ids[i][0] )
                if id1 in ids2:
                    print("The book Id entered already exists!, Try again with a non existing ID")
                else:
                    cursor.execute('''UPDATE stock SET id =? WHERE id = ? ''', (id1,id))
                    db.commit()
                    id = id1
                    print("The book's ID has been updated!")

            elif option1 == "2":
                Title = input("Enter the new book's Title: ")
                cursor.execute('''UPDATE stock SET Title = ? WHERE id = ? ''', (Title, id))
                db.commit()
                print("The book's Title has been updated!")
            
            elif option1 == "3":
                Author = ( input("Enter the new book's Author: "))
                cursor.execute('''UPDATE stock SET Author = ? WHERE id = ? ''', (Title, id))
                db.commit()
                print("The book's Title has been updated!")
            
            elif option1 == "4":
                Qty = input("Enter the new book's Qty: ")
                flag = 0
                while flag == 0:
                    for i in Qty:
                        if i in ["0","1","2","3","4","5","6","7","8","9",]:
                            pass
                        else:
                            flag = 1
                    if flag == 0:
                        break
                    if flag == 1:
                        print("Please enter only integer numbers without spaces")
                        Qty = input("Enter the new book's Qty: ")
                        flag = 0

                cursor.execute('''UPDATE stock SET Qty = ? WHERE id = ? ''', (Qty, id))
                db.commit()
                print("The book's Qty has been updated!")

            elif option1 == "5":
                pass
            elif option1 not in ["1","2","3","4","5"]:
                print("Invalid option!, Try again")

    
    #if the option entered is delete a book, request to enter the book id from the
    #list and then remove it from the database.
    if option == "3":
        cursor.execute('''SELECT * FROM stock''')
        records = cursor.fetchall()
        records = list( records )
        print( tabulate ( records, headers ))
        id = ( input("Enter the ID of the book that you want to delete: "))
        cursor.execute('''SELECT id FROM stock''')
        ids = cursor.fetchall()
        ids2 = []
        for i in range (0, len( ids )):
            ids2.append( ids[i][0] )
        if id in ids2:
            cursor.execute('''DELETE FROM stock WHERE id = ?''', (id,))
            db.commit()
            print(f"The book with id {id} has been Deleted!")
        else:
            print(f"The book with id {id} doesn't exist in the database!, try again")
            
    #if the option entered is search book, then request to select an option from the list 
    #of search by. request to the user to enter the search parameter and return the matching
    #  information found in the database 
    if option == "4":
        option2 = ""
        while option2 != "5":
            option2 = input("""Enter the type of search you would like to do
Search by
1 - ID
2 - Title
3 - Author
4 - Qty
5 - Exit\n""")
            if option2 == "1":
                id =  input("Enter the Book id: ")
                cursor.execute('''SELECT * FROM stock WHERE id=? ''', (id,))
                record = cursor.fetchone()
                if record != None:
                    record = [ list( record ) ]
                    print( tabulate( record, headers ))
                    print("\n")
                else:
                    print("Book ID not found!, Try again")

            
            elif option2 == "2":
                Title =  input("Enter the Book Title: ")
                cursor.execute('''SELECT * FROM stock WHERE Title LIKE ? ''',(Title+"%",))
                record = cursor.fetchone()
                if record != None:
                    record = [ list( record ) ]
                    print(tabulate( record, headers ))
                    print("\n")
                else:
                    print("Book Title not found!, Try again")

            
            elif option2 == "3":
                Author =  input("Enter the Book Author: ")
                cursor.execute('''SELECT * FROM stock WHERE Author LIKE ? ''',(Author+"%",))
                record = cursor.fetchone()
                if record != None:
                    record = [ list( record ) ]
                    print( tabulate( record, headers ))
                    print("\n")
                else:
                    print("Book Author not found!, Try again")

            
            elif option2 == "4":
                Qty =  input("Enter the Book Qty: ")
                flag = 0
                while flag == 0:
                    for i in Qty:
                        if i in ["0","1","2","3","4","5","6","7","8","9"]:
                            pass
                        else:
                            flag = 1
                    if flag == 0:
                        break
                    if flag == 1:
                        print("Please enter only integer numbers without spaces")
                        Qty = input("Enter the Book Qty:")
                        flag = 0

                cursor.execute('''SELECT * FROM stock WHERE Qty LIKE ? ''',(Qty+"%",))
                record = cursor.fetchone()
                if record != None:
                    record = [ list( record )]
                    print(tabulate( record, headers))
                    print("\n")
                else:
                    print("Book Qty not found!, Try again")


            elif option2 == "5":
                pass
            
            elif option2 not in ["1","2","3","4","5"]:
                print("Invalid option!, Try again")
    


    #if the option entered is see all the books then display all the information in the database
    elif option == "5":
        cursor.execute('''SELECT * FROM stock''')
        records = cursor.fetchall()
        records = list( records )
        print( tabulate ( records, headers ))
        print("\n")
        

    #if the option entered is exit then finish the loop and print a goodbye message
    elif option == "0":
        print("Goodbye!")
        db.close()

    #if the option doesn't exist in the menu then print out the respective message
    elif option not in ["0","1","2","3","4","5"]:
        print("Invalid option!, Try again")

