"""
Python Variables - Assign Multiple Values:-

Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""

a ,b ,c = "Yugen" ,'may' ,20
print("My name is" ,a ,b ,"And my age is" ,c ,"year old")

# Note: Make sure the number of variables matches the number of values, 
# or else you will get an error.


"""
One Value to Multiple Variables :
you can assign the same value to multiple variables in one line:
"""

x = y = z = "Myself" # One Value to Multiple Variables
print("I love" ,x ,",I Care for" ,y ,"and I Work for" ,z)

"""
Unpack a Collection:-

If you have a collection of values in a list, tuple etc.
Python allows you to extract the values into variables. 
This is called unpacking.
"""

Bio = ["Yugen" , "May" , 20]
name , surname , age = Bio

print("My name is" ,name ,",My Surname is" ,surname ,"and My age is" ,age ,"years old")