


#Importan!
#Pleae note that the referred error (sh: 1: cls: not found ) on my submit ion feedback is related to an Os issue, 
# 'cls' is a command that exist in Windows. If you are running this script on Linux or Mac the 'cls' command needs 
# to be replaced with 'clear', please read the following article related : https://www.pythonanywhere.com/forums/topic/1758/




#=====importing libraries===========
'''This is the section where you will import libraries'''
import os
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Create an object with the information contained in "user.txt"
f = open("user.txt","r")

#Create a list what will contain the users and passwords
user_password=[]

#Create a variable to save the username of the person that is using the program
user_on_use=""

#Create for loop to read the content the users and passwords extracted form "user.txt", strip and split the information in the list "user_password"
for line in f:

    user_password.append(line.strip("\n"))

f.close()

#Declare a Boolean variable to mark the end of the loop when it's necessary
a = True

#Start a while loop that will keep repeating unless the right username and pasword are entered
while a == True:
  user = input("Enter your user name: ")
  password=input("Enter your password: ")
  
  for i in range(0,len(user_password)):

    if user_password[i] == user+", "+password:
      os.system('cls')
      print("Welcome " + user+"\n")
      user_on_use = user
      a = False
      break

    elif i == len(user_password)-1:
      os.system('cls')
      print("Invalid User/Password!, try again"+"\n")

#Start a for loop to allow the user to navigate on the options available on the main Manu 
while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise, you present a relevant message.'''

        os.system('cls')
        
        # Open the file "user.txt" in the write mode 
        f=open("user.txt","a")

        #Create a variable "user" to save the new username entered in the console
        user=(input("Enter the new user's Name: "))

        #Start a for loop to compare and verify if the password entered by the user matches with the password verification, if this condition 
        #is met, then the new username and password will be added to the "user.txt" file and the loop will break out
        while True:

            password1 = input("Enter the new user's Password: ")
            password2 = input("Confirm the new Password: ")

            if password1 == password2:
                password=password1
                f.write("\n")
                f.write(user+", "+password)
                user_password.append(user+", "+password)
                os.system('cls')
                print ("New user registered successfully!")
                break

            else:
                os.system('cls')
                print("The password doesn't match, Try again")

        f.close()
        

    elif menu == 'a':

        os.system("cls")

        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        
        #Open the "tasks.txt" file on write mode to allow adding information
        f = open("tasks.txt","a")

        #Declare a control variable with initial Boolean value true
        a = True

        #Start a while loop to compare if the user entered exists in the list "user_password". If the user exists in the list, then request the task details,
        #if the user doesn't exist print out unexisting user message an repeat the loop
        while a == True:
            
            user = input("Who is the task assigned to?: ")
               
            for i in range (0,len(user_password)):
                user1=user_password[i].split(", ")
                user2 = user1[0]
                if user.upper() == user2.upper():
                    f.write("\n")
                    f.write(user1[0]+", ")
                    a = False
                    break

                elif i == len(user_password)-1:
                    os.system("cls")
                    print("Unexiting user, Try again\n")
        
        #Request and write in "task.txt" file the task details
        f.write(input("Enter the task title:")+", ")
        f.write(input("Enter the task description: ")+", ")
        f.write(input("Enter the task due date (format example. 10 Oct 2019 ):")+", ")
        f.write(datetime.datetime.now().strftime("%d %b %Y")+", ") 
        f.write("No")
        
        f.close()

    elif menu == 'va':

        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        
        #Opent the file "tasks.txt" on read mode 
        f=open("tasks.txt","r")
        os.system("cls")

        #Start a for loop to read each line in the file opened and print the information on the required format
        for i in f:

            tasks=i.split(", ")
            print(f"""________________________________________________________________\n
Task:                {tasks[1]}\n
Assigned to:         {tasks[0]}\n
Date assigned:       {tasks[4]}\n
Due date:            {tasks[3]}\n
Task complete?       {tasks[5]}\n
Task description:    {tasks[2]}\n
""")
        
        f.close()
        

    elif menu == 'vm':
        
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        
        #Open "tasks.txt" in read mode
        f=open("tasks.txt","r")

        #Declare a control variable to determinate if the for loop reached the end
        b=0

        #Start a for loop to read the content in each line of "tasks.txt" and append the values in the list tasks to access and manipulate the information
        for i in f:

            tasks = i.split(", ")

            #Verify if the user that has logged in exists in the list of tasks
            if tasks[0] == user_on_use:

                b = 1
                os.system("cls")

                #If the user exists in the list of tasks then print the task details in the format required
                print(f"""________________________________________________________________\n
Task:                {tasks[1]}\n
Assigned to:         {tasks[0]}\n
Date assigned:       {tasks[4]}\n
Due date:            {tasks[3]}\n
Task complete?       {tasks[5]}\n
Task description:    {tasks[2]}\n
""")
        #If the user doesn’t appear on the list of task then print out the respective message
        if b==0:

            os.system("cls")
            print("You don't have any tasks assigned!\n")
        
        f.close()

    elif menu == 'e':

        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


