"""
Global Variables :-

Variables that are created outside of a function (as in all of the examples above) 
are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

MyName = "Yugen May" # its a Global Variable

def Fuck():
        print("My Name is " ,MyName) # '+' and ',' Both work here same
        
Fuck()

"""
If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, 
global and with the original value.
"""

myname = "May Yugen" # its a global variable , used inside and outside function

def fuck():
    myname = "Jack" # Its a Local variable , only used inside the function , value change here
    print("my name is ", myname) # inside function
    
fuck()

print("my name is " ,myname)# Outside the function

"""
The global Keyword :- 

Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

def fuck1():
    global a # global Keyword
    a = "Jack May" #Inside Function Gloabal Variable 
    print("My name is" , a)

fuck1()

print("my name is :" ,a)

"""
Also, use the global keyword if you want to change a global variable inside a function.
"""

a = " Cool" # Global variable

def fuck():
    global a # Inside function change global variable value
    a = "awesome"
    
fuck()
print("Python is" ,a)