#Python Casting:
'''
Specify a Variable Type
There may be times when you want to specify a type on to a variable. 
This can be done with casting. 
Python is an object-orientated language,and as such it uses classes to define data types, 
including its primitive types.
'''

'''
Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, 
        a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, 
        a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, 
        including strings, integer literals and float literals
'''

print("Example of Integer\n")

x = int(5)      # x will be integer
y = int(10.5)   # y will be integer
z = int("15")   # z will be integer

print("All integer Value\n","X =",x,"Y =",y,"Z =",z)


print("\nExample of Float")

x = float(5)    # X will be 5.0
y = float(10.5) # y will be 10.5
z = float("15") # z will be 15.0


print("All Values are float\n","x =",x,"y =",y,"z =",z)

print("\nExample of String")

x = str("Hello") 
y = str("5")
z = str("10.5")

print("All values are String","\nX =",type(x),"\nY =",type(y),"\nZ =",type(z))