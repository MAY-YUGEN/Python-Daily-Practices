#Basic Data Types
name = "Yugen" # string
age = 22 #int
Doing_job = True # Bool
salary = 100000.00 # Float

#Collection Data Types:
All_infomartion1 = [name,age,Doing_job,salary] #List
All_infomartion2 = (name,age,Doing_job,salary) #tuple
All_infomartion3 = {name,age,Doing_job,salary} # set
All_infomartion4 = {"Name": name,"Age": age,"At Job": Doing_job,"Salary": salary} #dict

print("List:", All_infomartion1 ,"\nTuple:",All_infomartion2,"\nSet:",All_infomartion3,"\nDict:",All_infomartion4)

#Type Checking
print (type(salary))

# Type Conversion

salary = int(salary)

print(salary)