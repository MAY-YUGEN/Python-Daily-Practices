'''
Slicing Strings:-

You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.


'''

#Get the characters from position 2 to position 5 (not included):


print("Example of Slicing :")
b = "Hello, World!"
print(b[2:5],"\n")

'''
Slice From the Start:
By leaving out the start index, the range will start at the first character:
'''

print("Example of Slice From the Start :")

#Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5],"\n")

'''
Slice To the End:
By leaving out the end index, the range will go to the end.
'''

print("Example of Slice To the End:")

b = "hello, world!\n"
print(b[2:],"\n")

'''
Negative Indexing:
Use negative indexes to start the slice from the end of the string
'''

print("Example of Negative Indexing:")

'''
From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2)
'''

b = "Hello, World!"
print(b[-5:-2])