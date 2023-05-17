#Request to the user to enter their full name 
full_name=input('Please enter your full name:\n') 
#Create a loop to reiterate the process until the full name is entered correctly 
while (True): 
#Compare the length of the variable that contains the information requested to the user 
#If the information is longer or shorter than the expected, request the user to enter the information again 
#If the information requested is in the right format break the loop 
     
    if len(full_name)==0: 
        print("You haven't entered anything. Please enter your full name:\n") 
        full_name=input('Please enter your full name:\n') 
     
    if len(full_name)<4: 
        print("You have entered less than 4 characters. Please make sure that you have entered your name and surname:\n") 
        full_name=input('Please enter your full name:\n') 

    if len(full_name)>25: 
        print("You have entered more than 25 characters. Please make sure that you have only entered your full name:\n") 
        full_name=input('Please enter your full name:\n') 

    if len(full_name)>4 and len(full_name)<25: 
        print("Thank you for entering your name\n") 
        break 

         

 

 
 

 