num_days =int(input("How many days did you work this month?"))
pay_per_day =float(input("How much is your pay perday?"))
salary = num_days * pay_per_day
'print(f"My salary for the month is USD:{pay_per_day}")'
print("Youworked{1}thismonthandearned${0}perday".format(num_days,pay_per_day))