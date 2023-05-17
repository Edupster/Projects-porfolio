#Request to the user to enter their job role (salesperson/manager)
role=input('Please enter your job role (salesperson/manager):\n')

#Determinate based on the user's answer the way that their salary will be calculate and save it in a variable
if role.upper()=='SALESPERSON':
    sales_month=float(input('Please enter your gross sales for the month:\n'))
    salary=(sales_month*0.08)+2000

elif role.upper()=='MANAGER':
    hours_week=float(input('Please enter the total of hours you worked this month:\n'))
    salary=hours_week*40

#Print out the user's salary 
print(f'Yor salary on your next payslip will be: {salary}£')