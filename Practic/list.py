print("-----User input in list-----")
print("-------Method No.1-------")
list1 = []
for i in range(5):
    list2 = int(input("Enter Value:"))
    list1.append(list2)
    list1.sort()

print("List:",list1)
print("Min Value:"),print(min(list1))
print("Max Value:"),print(max(list1))

print("Even Values: ")
for num in list1:
    if num % 2 == 0:
        print(num)

print("Odd Values: ")
for num in list1:
    if num % 2 != 0:
        print(num)

print("-------Method No.2-------")
list3 = []
val1 = int(input("Enter How many values you want: "))

for i in range(val1):
    list4 = int(input("Enter Values: "))
    list3.append(list4)
    list3.sort()

print("List :",list3)
print("Min Value:"),print(min(list3))
print("Max Value:"),print(max(list3))

print("Even Values:")
for num in list3:
    if num % 2 == 0:
        print(num)

print("Odd Values: ")
for num in list1:
    if num % 2 != 0:
        print(num)



