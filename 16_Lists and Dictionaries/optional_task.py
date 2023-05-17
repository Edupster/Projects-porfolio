#Request to enter an abbreviation
abbrev=input("Enter the abbreviation you would like to know it's meaning: ")

#Declare a dictionary with the abbreviations as keys and the meaning of each abbreviation as value related
abbrev_dict={"NHS":"National Health Service",
             "BBC":"British Broadcasting Corporation",
             "KFC":"Kentucky Fried Chicken",
             "LED":"Light Emitting Diode",
             "HMRC":"Her Majesty's Revenue and Customs",
             "FIFA":"Federation Internationale de Football Association"}

#If the abbreviation entered by the user exist in the dictionary, then print the key and the value associated.
if abbrev in abbrev_dict:
    
    print(f"The meaning of the abbreviation \"{abbrev}\" is \"{abbrev_dict[abbrev]}\"")