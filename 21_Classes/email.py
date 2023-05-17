#An Email Simulation

#Declare the class "Email" to define all the object properties and methods 
class Email():
    #Define the class properties
    def __init__(self,from_address, email_contents):
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address
    
    #Define the class methods
    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True  

#Declare an empty list that will contain the objects "Email" declared by the user   
inbox=[]

#Define the functions to be implemented in the main menu

#Define a function to create and append new objects (Emails) to the empty list "inbox", 
# the function gets as input the sender's email address and the email content
def add_email(sender,contents):
    new_email = Email(sender,contents)
    inbox.append(new_email)

#Define a function to determinate how many objects exist in the list "inbox"
def get_count():
    return len(inbox)

#Define a function to get an Email from the inbox, the function gets an email's index as input
def get_email(i):
    inbox[i].mark_as_read()
    print(f"From:{inbox[i].from_address} Content: {inbox[i].email_contents}")

#Define a function to get the unread emails
def get_unread_emails():
    print('Unread Emails:')
    b=0

    for i in inbox:
        if i.has_been_read == False:
            print(f"From:{i.from_address} Content: {i.email_contents}")
            b=1

    if b == 0:
        print("You don't have unread emails")

# Define a function to get the spam emails
def get_spam_emails():
    print('Spam Mailbox:')
    b = 0
    for i in inbox:

        if i.is_spam == True:
            print(f"From:{i.from_address} Content: {i.email_contents}")
            b=1

    if b == 0:
        print("You don't have Spam emails!")
        
# Define a fuction to delete Emails from the inbox list, the function gets an email's index as input
def delete(i):
    del inbox[i]
    print(f'The email with index {a} has been deleted')

user_choice = ""

#Start a while loop to perform a task based on the user's input
while user_choice != "quit":

    #Display the menu options and request to input an option
    user_choice = input("What would you like to do - add email / read emails / show unread emails / mark spam / show spam / delete / quit?: ")
    
    #if the user selects add email, call the function add_email and request to the user to enter the function's input information
    if user_choice == "add email":
        contents = input("Enter the email content: ")
        sender = input("Enter the sender's email address: ")
        add_email(sender,contents)
    
    #if the user selects read emails, call the function get_email and request to the user to enter the function's input information
    elif user_choice == "read emails":
            while True:

                try:
                    a=int(input("Enter the email index: "))
                    get_email(a)
                    break

                except:
                    print("Invalid email index, try again!")
    

    #if the user selects show unread emails, call the function get_unread_emails, no input information is needed for this function
    elif user_choice == "show unread emails":
        get_unread_emails()
    

    #if the user selects mark spam, request to the user to enter the Email's index and 
    # call the class method mark_as_spam to modify the Email Spam property to True
    elif user_choice == "mark spam":
        while True:

                try:
                    a=int(input("Enter the email index: "))
                    inbox[a].mark_as_spam()
                    print(f'The email with index {a} has been marked as spam')
                    break

                except:
                    print("Invalid email index, try again!")
    
    #if the user selects show spam, call the function ge_spam_emails, no input information is needed for this function
    elif user_choice == "show spam":
        get_spam_emails()

    #if the user selects delete, call the function delete and request to the user to enter the Email's index to be deleted
    elif user_choice == "delete":
        while True:

                try:
                    a=int(input("Enter the email index: "))
                    delete(a)
                    break

                except:
                    print("Invalid email index, try again!")

    #if the user selects quit, then print out the goodbye message, this option also breaks the loop
    elif user_choice == "quit":
        print("Goodbye")
    
    #if the user selects any other option that doesn't exist in the menu then print out the respective message
    else:
        print("Oops - incorrect input")


