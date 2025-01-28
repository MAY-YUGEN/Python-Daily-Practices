# Python Variable

# Variables are containers for storing data values.

# In Python, variables are created when you assign a value to it :-

x =5 
y = "Hello, Yugen !"

print("X and Y Values : ", x,y)

# Python has no command for declaring a variable


# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.

Z = 10 # Z is int type variable 
Z = "Hello" # Now Z value change because of re-diffinig 

print("Value of Z : " ,Z)


"""
In Python, variables are used to store  
values of different data types, like numbers, strings, lists, etc.

Variables are fundamental building blocks in programming. 
They allow you to store and manipulate data, making your code more dynamic and interactive.

"""

print("1. Variable Assignment :")
"""
Note : You can assign values to 
       variables using the assignment operator ('=').
"""






name = "Yugen"  #string
age  = 20       #intiger 
height = 5.4    #flout
                #bool = True and false
                
print(name, age, height)
                
"""

Dynamic Typing:
Python is dynamically typed, meaning you don't need to 
explicitly declare the data type of a variable. Python 
determines the data type automatically based on the value assigned to it.

"""


print("2. Type Conversion :")
"""
You can convert between data types using built-in functions like 
int(), float(), str(), and others.
"""
num_str = "42"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float

print(num_str)
print(num_int)
print(num_float)



print("3. Multiple Assignment :")
"""
Python allows you to assign multiple variables in a single line.
"""

x, y, z = 10, 20, 30

print (x)
print (y)
print (z)


print("4. Variable Reassignment :")

"""
You can change the value stored in a variable after it has been assigned.
"""

counter = 0
counter = counter + 3 # increment counter.
counter = counter + 2

print(counter)

print("5. Constants :")
"""
While Python doesn't have true constants, you can use uppercase 
variable names to indicate a constant value that should not be changed. 
It's a convention and not enforced by the language
"""

PI = 3.14159
print (PI)


print("6. None :")
"""
Python has a special value called 'None' that represents the 
absence of a value or a null value. It's often used to initialize 
variables before assigning real values.
"""

result = None

print(result)

print("7. String Formatting :")
"""
You can embed variables within strings using f-strings (formatted string literals)
"""
name = "Yugen"
age = 20

Massege = f"my name is {name} and my age is {age}" #Note : 'f' is compulsory to writte at the starting.

print(Massege)


