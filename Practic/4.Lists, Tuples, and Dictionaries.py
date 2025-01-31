
print("List related Tasks:")
fruits = ["Apple","Mango","Banana"]

fruits.append("Berry")

print(fruits)
print("Lenth of List:",len(fruits))

fruits.remove("Banana")

print(fruits)

print(fruits[1])

print("Lenth of List:",len(fruits))

print(fruits[-1])

fruits.sort()

print(fruits)



fruits.append(input("Enter Fruits Name:"))
print(fruits)

fruits.remove(input("Enter Fruits Name:"))
print(fruits)


print("Tuples related Tasks:")

Numbers = (1,2,3,4,5)

print(Numbers)

print(Numbers[2])

print(Numbers[-2])

print("Dictionaries related Tasks:")

Infro = {"name":"Yugen","age":22}

print(Infro)

Infro["name"] = input("Enter Your Name:")

print(Infro)

Infro["age"] = input("Enter Your Age:")

print(Infro)

Infro["Grade"] = input("Enter Your Grade:")

print(Infro)

del Infro["age"]

print(Infro)

print("Write a program that asks for a list of 5 numbers, sorts them, and calculates their sum.")


Numbers = []
print("Enter Five Number")

for Number in range(5):
    Numbers.append(int(input(f"Enter {Numbers}  Numbers:")))
   
print("Unsorted List:",Numbers,"\n")

Numbers.sort()
print("Sorted List:",Numbers,"\n")

Numbers = sum(Numbers)
print("Sum of List:",Numbers,"\n")

print("Create a dictionary that stores the marks of 3 subjects and calculate the total and average marks.")

subject = {"English":"","Math":"","Science":""}

subject["English"] = int(input("Enter Your Marks For English:"))
subject["Math"] = int(input("Enter Your Marks For Math:"))
subject["Science"] = int(input("Enter Your Marks For Science:"))

print(subject)

sum = sum(subject.values())

print("Sum of 3 Subject:",sum)

avg = sum / len(subject)

print("Average of 3 Subject:",avg)

