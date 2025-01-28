from datetime import datetime

DOB_input = input("Enter your Date Of Birth(DD-MM-YYYY):")
DOB = datetime.strptime(DOB_input,"%d-%m-%Y")


today = datetime.today()
age = today.year - DOB.year
if today.month < DOB.month or today.month == DOB.month and today.day < DOB.day:
    age -= 1

print("Today's date and time :",today)
print(f"Your current Age is : {age} years")

Future_year = int(input("Enter a Future year to know your age in the future what will be:"))

if Future_year < today.year or Future_year == today.year:
    print("Please Enter a Future Year")
else:
    Age_in_Future = Future_year - today.year
    Age_in_Future1 = age + Age_in_Future
    print(f"Your current Age is : {age} years")
    print(f"Your age in future will be : {Age_in_Future1} Year")
