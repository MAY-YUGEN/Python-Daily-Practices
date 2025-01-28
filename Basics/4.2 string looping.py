'''
Looping Through a String:

Since strings are arrays, 
we can loop through the characters in a string, 
with a for loop.
'''

for x in "Banana":
    print(x)
    
'''
String Length:
To get the length of a string, use the len() function.
'''

x = "Hello, world"

print(len(x))

'''
Check String:

To check if a certain phrase or character is present in a string, 
we can use the keyword in.

if character is present is string it will give you true or 
if not will will return false
'''

a = "The best things in life are free!"
print("best" in a)

# Use it in an if statement 

a = "The best things in life are free!"

if "Best" in a:
    print("Yes, 'best' is present")
else:
    print("Character is not Present in String")
    
    
'''
Check if NOT
To check if a certain phrase or character is NOT present in a string, 
we can use the keyword not in.
'''    

a = "The best things in life are free!"

print("Hello" not in a)

if "Hello" not in a:
    print("Not in string")
else:
    print("Avalable in string")