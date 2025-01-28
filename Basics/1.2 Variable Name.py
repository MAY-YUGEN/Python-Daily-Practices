
"""
Python - Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 

Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

"""

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


"""
Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

"""

# Remember that variable names are case-sensitive.


"""
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:
"""

myVariableName = "Yugen" # Camel Case style  : Each word, except the first, starts with a capital letter
MyVariableName = "May"   # Pascal Case style : Each word starts with a capital letter
My_Variable_Name = 20    # Snake Case style  : Each word is separated by an underscore character

#This three are defferent

print("My Name is" ,myVariableName ,MyVariableName ,"and my age is" ,My_Variable_Name ,"years old") 