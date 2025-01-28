"""
Output Variables:-

The Python print() function is often used to output variables.
"""

x = "Python is a Programming Language"
print (x) # Output of the variable

# In the print() function, you output multiple variables, separated by a comma:

a = "Python"
b = "is a"
c = "programming"
d = "language !"

print(a ,b ,c ,d)# Output of maltiple variable

# You can also use the + operator to output multiple variables:

q = "Python "
w = "is a "
e = "programming "
r = "language !"

print(q + w + e + r)

#Notice the space character after "Python " and "is ", 
# without them the result would be "Pythonisawesome".


#For numbers, the + character works as a mathematical operator:
a = 5
b = 10
print(a + b)


# In the print() function, 
# when you try to combine a string and a number with the + operator, 
# Python will give you an error:
a = "hello"
b = 20
#print(a+b) It will give you an error


# The best way to output multiple variables in the print() 
# function is to separate them with commas, 
# which even support different data types:
a = "hello"
b = 20
print(a,b)# Seperated by comma
