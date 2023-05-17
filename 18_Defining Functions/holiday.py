#Define a function to calculate and return the cost of the accommodation. Use the number of nights of the stay as input argument
def hotel_cost(nights):
  cost = nights*200
  return cost

#Define a function to calculate and return the cost of the airplane ticked based on the destination entered as argument
def plane_cost(city):
  if city.upper()== "CANCUN":
    
    cost = 700
  
  elif city.upper()== "BARCELONA":
    cost = 80
  
  elif city.upper()== "MADRID":
    cost= 30
  
  elif city.upper()== "ROME":
    cost = 50
  
  elif city.upper()== "ROME":
    cost = 45
  
  else:
    cost="Invalid city"
  
  return cost

#Define a function to calculate and return the cost of the car rental based on the days the car will be rented as the function’s input argument
def car_rental(days):
    cost=days*90
    return cost

#Define a function to calculate and return total cost for the holidays receiving as input arguments the cost for the accommodation, plane tickets, and car rental. 
def  holiday_cost(p, c, h):
  
   total = p+c+h
   
   print(f"The total price for your holidays in {city.upper()}, with {nights} nights accommodation and rented car for {days} days is {total}£")

#Declare the input values for each function
nights=4
city="Rome"
days=5

#Call each function inserting the corresponding input arguments
hotel=hotel_cost(nights)
plane = plane_cost(city)
car = car_rental(days)
holiday_cost(plane,car,hotel)



