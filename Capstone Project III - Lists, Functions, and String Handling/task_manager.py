#Importan!
#Pleae note that the referred error (sh: 1: cls: not found) on my submit ion feedback is related to an Os issue, 
# 'cls' is a command that exist in Windows. If you are running this script on Linux or Mac the 'cls' command needs 
# to be replaced with 'clear', please read the following article related : https://www.pythonanywhere.com/forums/topic/1758/



#=====importing libraries===========
'''This is the section where you will import libraries'''
import os
import datetime

f=open("tasks.txt","r")

#Declare a control variable to determinate if the for loop reached the end
c = 0
tasks = {}

#Start a for loop to read the content in each line of "tasks.txt" and append the values in the list tasks to access and manipulate the information
for i in f:

    task = i.split(", ")
    tasks[c] = task
    c += 1

f.close()


# Create an object with the information contained in "user.txt"
f = open("user.txt","r")

#Create a list what will contain the users and passwords
user_password = []

#Create a variable to save the username of the person that is using the program
user_on_use = ""

#Create for loop to read the content the users and passwords extracted form "user.txt", strip and split the information in the list "user_password"
for line in f:

    user_password.append(line.strip("\n"))

f.close()



#Declare a Boolean variable to mark the end of the loop when it's necessary
a = True

#Start a while loop that will keep repeating unless the right username and password are entered
while a == True:
  user = input("Enter your user name: ")
  password = input("Enter your password: ")
  
  for i in range(0,len(user_password)):
    
    #if the user and password exist in the "user.txt" then go to the main menu
    if user_password[i] == user+", "+password:

      os.system('cls')
      print("Welcome " +  user+"\n")
      user_on_use = user
      a = False
      break

    #if the user and password don't exist in "user.txt" print out the respective message
    elif i == len(user_password)-1:

      os.system('cls')
      print("Invalid User/Password!, try again"+"\n")

# Define a function that every time is called updates the tasks in the document "tasks.txt"
def refresh_tasks():
  
  #open "tasks.txt" file on read mode
  f = open("tasks.txt","r")
  
  #Declare an empty dictionary that will contain the information contained in "tasks.txt" 
  tasks = {}

  #Declare variable which value will represent the key value for each task in "tasks.txt"
  c = 0
 
  #Start a for loop to read the content on each line in "tasks.txt" and append the tasks in the dictionary "tasks"
  for i in f:
    
      task = i.split(", ")
      tasks[c] = task
      
      #After each iteration the variable c will increase one unit
      c += 1

  f.close()

  #Return a dictionary with the information contained in the file "tasks.txt"
  return tasks

# Define a function to register a new user
def reg_user():
  os.system('cls')

  usernames = "".join(user_password)
  usernames = usernames.split(",")

  # Open the file "user.txt" in the write mode 
  f = open("user.txt","a")

  #Create a variable "user" to save the new username entered in the console
  user = (input("Enter the new user's Name: "))
  
  
  #Start a for loop to compare and verify if the password entered by the user matches with the password verification, if this condition 
  #is met, then the new username and password will be added to the "user.txt" file and the loop will break out
  while True:
    
    if user in usernames:

      user = (input(f"The user '{user}' already exists on the system, please try again with a different username: "))
      
    else:

      password1 = input("Enter the new user's Password: ")
      password2 = input("Confirm the new Password: ")
      if password1 == password2:
        password = password1
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


# Define a function to add a new task to the file "tasks.txt"
def add_task():

  #Open the "tasks.txt" file on write mode to allow adding information
  f = open("tasks.txt","a")

  #Declare a control variable with initial Boolean value to end the for loop when is necessary
  a = True

  #Start a while loop to compare if the user entered exists in the list "user_password". If the user exists in the list, then request the task details,
  #if the user doesn't exist print out unexciting user message an repeat the loop
  while a == True:

    user = input("Who is the task assigned to?: ")
    
    for i in range (0,len(user_password)):

      user1 = user_password[i].split(", ")
      user2 = user1[0]

      if user.upper() == user2.upper():

         f.write("\n")
         f.write(user1[0]+", ")
         a = False
         break

      elif i == len(user_password)-1:

         os.system("cls")
         print("Unexiting user!, Try again\n")
    

        
  #Request and write in "tasks.txt" file the task details
  f.write(input("Enter the task title:")+", ")
  f.write(input("Enter the task description: ")+", ")
  f.write(input("Enter the task due date (format example. 10 Oct 2019 ):")+", ")
  f.write(datetime.datetime.now().strftime("%d %b %Y")+", ") 
  f.write("No")
  f.close()

#Define a new function to view all the tasks
def view_all():

  os.system("cls")

  #Opent the file "tasks.txt" on read mode 
  f=open("tasks.txt","r")
  

  #Start a for loop to read each line in the file opened and print out the information on the required format
  for i in range(0,len(tasks)):
    
    print(f"""________________________________________________________________\n
Task num:            {i}\n
Task:                {tasks[i][1]}\n
Assigned to:         {tasks[i][0]}\n
Date assigned:       {tasks[i][4]}\n
Due date:            {tasks[i][3]}\n
Task complete?       {tasks[i][5]}\n
Task description:    {tasks[i][2]}\n
""")
        
  f.close()
        

#Define a function to view the user's tasks 
def view_mine():

  os.system("cls")
  
  #start a for loop to read the all the tasks contained in the directory "tasks"
  for i in tasks:
    
    #if the user exists in the tasks’ dictionary then print out their tasks
    if tasks[i][0] == user_on_use:
        print(f'''________________________________________________________________\n
Task num:            {i}\n
Task:                {tasks[i][1]}\n
Assigned to:         {tasks[i][0]}\n
Date assigned:       {tasks[i][4]}\n
Due date:            {tasks[i][3]}\n
Task complete?       {tasks[i][5]}\n
Task description:    {tasks[i][2]}\n
''')

  """Allow the user to select either a specific task (by entering a number)
or input '-1' to return to the main menu.
o If the user selects a specific task, they should be able to choose to
either mark the task as complete or edit the task. If the user
chooses to mark a task as complete, the 'Yes'/'No' value that
describes whether the task has been completed or not should be
changed to 'Yes'. When the user chooses to edit a task, the
username of the person to whom the task is assigned or the due
date of the task can be edited. The task can only be edited if it has
not yet been completed."""

  while True:
    try:

      option=int(input('''Select a task entering the task number.\n
Enter -1 to get back to the main menu:\n'''))
    
      if option in tasks:

        while True:

          option1=input('''Select an option:\n
m - Mark as complete\n
e - Edith\n''')

          if option1=="m":

            tasks[option][5]=("Yes\n")
            break

          elif option1=="e":

            print(tasks[option][5])

            if tasks[option][5]=="No\n":

              tasks[option][0]=(input("Who is the task assigned to?:"))
              tasks[option][3]=(input("Enter the task due date (format example. 10 Oct 2019 ):"))
              break

            else:

              print("The task entered has been marked as completed, you can't edith it!\n")

          else:

            print("You haven't entered a valid option\n")
        break  

      elif(option== -1):
        break

      else:

        print("You haven't entered a valid task number!\n")

    except ValueError:

      print("You haven't entered a valid task number!\n")

  f=open("tasks.txt","w")
  for i in tasks:
    f.write(", ".join(tasks[i]))
  f.close

  """Add a function to generate reports to the main menu of the application.
When the user chooses to generate reports, two text files, called
task_overview.txt and user_overview.txt, should be generated. Both
these text files should output data in a user-friendly, easy to read manner.
o task_overview.txt should contain:
▪ The total number of tasks that have been generated and
tracked using the task_manager.py.
▪ The total number of completed tasks.
▪ The total number of uncompleted tasks.
▪ The total number of tasks that haven't been completed and
that are overdue.
▪ The percentage of tasks that are incomplete.
▪ The percentage of tasks that are overdue.
 """
def gen_reports():
  total_comp_tasks = 0
  total_uncom_tasks = 0
  actual_date = datetime.datetime.now().strftime("%d %b %Y")
  over_due_tasks = 0

  for i in tasks:

    if tasks[i][5].strip("\n") == "Yes":
      total_comp_tasks += 1

    elif tasks[i][5].strip("\n") == "No":
      total_uncom_tasks += 1

      if tasks[i][3] > actual_date:

        over_due_tasks += 0
  

  f = open("task_overview.txt","w+")
  
  f.write(f'''_______________________________Tasks overview_______________________________\n

Total of tasks:                  {len(tasks)}\n
Tasks completed:                {total_comp_tasks}\n
Tasks uncompleted:               {total_uncom_tasks}\n
Overdue tasks:                   {over_due_tasks}\n
Percent of tasks uncompleted:    {round(total_uncom_tasks*100/len(tasks),2)}\n
Percent of tasks overdue:        {round(over_due_tasks*100/len(tasks),2)}\n
''')

  f.close
  print("Report generated successfully!\n")

  f1 = open("user_overview.txt","w+")
  
  f1.write(f'''_______________________________Users overview_______________________________\n
Total of users registered:          {len(user_password)}\n
Tasks registered:                   {len(tasks)}\n''')

  
  user1 = ", ".join(user_password)
  user1 = user1.split(", ")
  user2 = []
  tasks_counter = 0
  total_task_percent = 0
  task_comp_counter = 0
  task_comp_percent = 0
  actual_date=datetime.datetime.now().strftime("%d %b %Y")
  task_overdue_counter = 0
  task_overdue_percent = 0

  for i in range (0,len(user1)):

    if i%2 == 0:

      user2.append(user1[i])

  for i in range(0,len(user2)):

    for j in tasks:

      if user2[i] == tasks[j][0]:

        tasks_counter += 1

        if tasks[j][5].strip("\n") == "Yes":

          task_comp_counter += 1

        elif tasks[j][5].strip("\n") == "No" and tasks[j][3] > actual_date:

          task_overdue_counter +=1
          

    try:

      total_task_percent = round(tasks_counter*100/len(tasks),2)
      task_comp_percent = round(task_comp_counter*100/tasks_counter,2)
      task_overdue_percent = round(task_overdue_counter*100/tasks_counter,2)

    except ValueError:

      total_task_percent = 0

      task_comp_percent = 0

      task_overdue_percent = 0

    f1.write(f'''_______________________________{user2[i]}_______________________________\n
Tasks:                                        {tasks_counter}\n
Percentage of the total tasks assigned:       {total_task_percent}%\n
Percentage of task completed:                 {task_comp_percent}%\n
Percentage of task pending to be completed:  {100-task_comp_percent}%\n
Percentage of task overdue to be completed:  {task_overdue_percent}%\n
''')

    tasks_counter = 0
    task_comp_counter = 0
    task_overdue_counter = 0

  f1.close

def view_statiscs():

  gen_reports()
  f=open("task_overview.txt","r")

  for line in f:

    print(line)

  f.close

  f1=open("user_overview.txt","r")

  for line in f1:

    print(line)

  f1.close

      

#_________________________________________________________________________________________________

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''


#Start a for loop to allow the user to navigate on the options available on the main Manu 
while True:

    #If the user logged in is the admin then execute a separated menu with more options
    if user_on_use == "admin":
        #presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        menu = input('''Select one of the following Options below:
r  - Registering a user
a  - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - Statistics
e  - Exit
: ''').lower()
        
        #if the user enters the option statistics call the function "view_statiscs"
        if menu == "ds":

            os.system("cls")
            
            view_statiscs()

    #if the user on user is not the admin display a different menu
    else:

        #presenting the menu to the user and 
        # # making sure that the user input is converted to lower case.
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    
    #If the "admin" has logged to register a new user, call the function "reg_user"
    if menu == 'r' and user_on_use == "admin":

      os.system("cls")

      reg_user()
    
    
    
    #If the user requesting to register a new user and is not the admin who is logged in then print out the corresponding message
    elif menu == 'r' and user_on_use != "admin":
        os.system('cls')
        print("You don't have permission to register a new user!\n")

    #if the user enters the option add a new task then call the functions "add_task" and "refresh_tasks"
    elif menu == 'a':

        os.system("cls")
        add_task()
        tasks=refresh_tasks()
        
    #if the user enters the option view all the tasks then call the function "view_all"
    elif menu == 'va':

      view_all()

    #if the user enters the option view my then call the functions "view_mine" and "refresh_tasks"
    elif menu == 'vm':

      view_mine()
      tasks=refresh_tasks()

    #if the user enters the option generate reports then call the function "gen_reports"
    elif menu == "gr":
      gen_reports()

    #if the user enteres the option exit then print out the good bye message and finish the program
    elif menu == 'e':

        print('Goodbye!!!')
        exit()
    
    
    #if the user enters a no valid option then print out the respective message
    else:
      if menu != "ds":
        print("You havn't entered a valid option!, Please Try again")

