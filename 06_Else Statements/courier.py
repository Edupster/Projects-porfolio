#Request the user to enter the price of the package they would like to purchase and save it in a variable
package_price=float(input('Enter the price of the package you would like to purchase:\n'))
#Enter the total distance of the delivery in kms
distance_km=float(input("Enter the distance that your parcel will travel till the final destination (kilometers):\n"))
delivery_method=input('Enter your delivery method preferred, Air(0.36£ per km) Freight (0.25 per km):\n')
insurance=input('Enter your insurance selection Full(50£) Limited(£25):\n')
gift=input('Would you like to include a Gift? Yes(15£), No(0£):\n')
priority= input('Priority delivery? Yes(100£), No(20£):\n')

#Determinate the rate cost for each product/service depending on the information entered with if and elif statements
if delivery_method.upper()=='AIR':
    delivery_rate=0.36
elif delivery_method.upper()=='FREIGHT':
     delivery_rate=0.25     

if insurance.upper()=='FULL':
    insurance_rate=50
elif insurance.upper()=='LIMITED':
    insurance_rate=25

if gift.upper()=='YES':
    gift_rate=15
elif gift.upper()=='NO':
    gift_rate=0

if priority.upper()=='YES':
    priority_rate=100
elif priority.upper()=='NO':
    priority_rate=20                

#Calculate the total shipping cost
total_cost=package_price+(distance_km*delivery_rate)+insurance_rate+gift_rate+priority_rate

#Print out the shipping total price

print('The total cost for your shipping is:', total_cost)