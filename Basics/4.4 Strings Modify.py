#Modify Strings


# Python has a set of built-in methods that you can use on strings.

"""
1. Upper Case

the upper() method returnthe string in upper case:
"""

a = "Hello, world!"
print(a.upper())


"""
2. Lower Case

The lower() method return the string in lower case:
"""

a = "Hello,world!"
print(a.lower())

"""
3. Remove Whitespaces
Whitespace is the space before and/or after the actual text, and very foten you want to remove this space.

the strip() method removes any whitespace from the beginning or the end:
"""

a = "          Hello, world!                "
print(a.strip())

"""
4. Peplace String

The replace() method replaces a string with another string:

"""

a = "Hello, world!"
print(a.replace("H", "K"))
print(a.replace("w", "K"))


"""
5. Split String

the split() method return a list where the text between the specified separator becomes the list items.

The split() method splits the string into substring if it finds instances of the separator.
"""

a = "hello world!"
print(a.split(","))