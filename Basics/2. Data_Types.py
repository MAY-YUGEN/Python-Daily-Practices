"""
Built-in Data Types :-

In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text Type      :	str
Numeric Types  :	int, float, complex
Sequence Types :	list, tuple, range
Mapping Type   :	dict
Set Types      :	set, frozenset
Boolean Type   :	bool
Binary Types   :	bytes, bytearray, memoryview
None Type      :	NoneType


"""

"""
Getting the Data Type:-
You can get the data type of any object by using the type() function:
"""

#Data Type:-

string_var = a = "Hello"
int_var = b  = 42
float_var = c = 3.14
list_var = d = [1, 2, 3]
tuple_var = e = (4, 5, 6)
dict_var = f = {"Name" : "yugen" ,"age" : 20 }
dict_var = g = {"Name" , "yugen" ,"age" , 20 }
frozenset = h = frozenset({"Name" ,"yugen" ,"age" ,20})
bool = i = True 
bytes = j = b"hello"
bytearray = k = bytearray(10)
None_ = l = None
complex = n = 1j # know more about complex data type


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(n))  


"""
Setting the Specific Data Type:-
If you want to specify the data type, you can use the following constructor functions
"""

m = str("Hello world !")
o = int(20)
p = float(10.5)
#q = complex(1j)
r = list(("Red" ,"Blue" ,"Black"))
s = tuple (("Red" ,"Blue" ,"Black"))
t = range(6)
u = dict(name = "yugen" ,age=20)
#v = bytearray(10)
w = set(("Red" ,"White" ,"Green"))
#x = frozenset(("Red" ,"White" ,"Green"))
#y = bool(5)
#z = bytes(10)

print(m)
print(o)
print(p)
#print(q)
print(r)
print(s)
print(t)
print(u)
#print(v)
print(w)
#print(x)
#print(y)
#print(z)


