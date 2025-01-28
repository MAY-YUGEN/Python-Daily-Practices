"""
Casting:-
If you want to specify the data type of a variable, this can be done with casting.

"""

x = str(3)   # X is string '3' ,it can't be calculate 
y = int(4)   # Y is Intiger 4
z = float(5) # Z is floating  5

print("The values of" ,"X =",x,"Y =", y,"Z =", z)

print(x*y) # 4 time string
print(y*z) # Maltiplication 


"""
Get the Type:-
You can get the data type of a variable with the type() function.
"""

a = 5
b = "yugen"
c = 20.5

print("Type of" ,"A is" ,type(a) ,"B is" ,type(b) ,"C is" ,type(c))


"""
Single or Double Quotes:-
String variables can be declared either by using single or double quotes
"""

f_Name = 'Yugen'
l_Name = "May"
# Both are same

print("My name is" ,f_Name ,l_Name)

"""
Case-Sensitive :- 
Variable names are case-sensitive.
"""

Age = "Yugen"
age = 20
# Both variable are different 

print("My name is" ,Age ,"And age is" ,age ,"year old")