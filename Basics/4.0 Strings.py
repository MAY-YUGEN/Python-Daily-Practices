'''
Python Strings

Strings in python are surrounded by either single quotation marks, 
or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function
'''

print("Hello")
print('Hello')

'''
Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by 
an equal sign and the string:
'''
a = "Hello"
print(a)

'''
Multiline Strings
You can assign a multiline string to a variable by using three quotes
Or three single quotes:
'''
# """ Multi-line String"""
# '''Multi-line String'''


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)