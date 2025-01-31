#Control Flow 1)if, 2)elif, 3)else

#Age = int(input("Enter Your Age:"))

Age = 20

if Age < 18:
    print("You are Minor!")
elif Age == 18:
    print("You become An Adult!")
elif Age !=18:
    print("You are an adult!")
else:
    print("Please Enter You age")
    
#loops 1) while, 2) for 

#loops 1) while
count = 1

while count < 11:
    print(count)
    count += 1
    
#loops 2) for 

for condition in range(10):
    if condition == 5:
        continue
    print(condition)
    
    
print("Even Number from 1 to 20")


sum_of_evens = 0

for condition in range(1,21):
    if condition % 2 == 0:
        print(condition)
    sum_of_evens += condition

print("Sum Of Even Numbers from 1 to 20:",sum_of_evens)  


print("Multiplication Table:")

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i * j}")

    



