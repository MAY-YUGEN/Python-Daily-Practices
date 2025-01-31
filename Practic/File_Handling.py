import os
print("This file example.txt is in this location:",os.getcwd())


with open("example.txt","w") as file:
    file.write("Hello,")
    file.write("Yugen\n")
    file.write("How Are you!?")
  
with open("example.txt", "a") as file:
    file.write("\nI'm good")    
   
with open("example.txt","+r") as file:        
    content = file.read()
    print(content)
    file.write("\nAnd you!?\n") 
    
with open("example.txt","r") as file:
    content = file.read()
    print(content)
    

print ("Extra Challenge: Create a program that asks the user for their name and stores it in a file")
print ("Extra Challenge: Create another program that reads and displays all names stored in the file")

with open("example.txt","w") as file:
    file.write(input("Enter Your Name:"))
    
with open("example.txt","r") as file:
    content = file.read()
    print(content)
   
   
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())



