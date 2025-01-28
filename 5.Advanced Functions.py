print("Function Demonstration using **kwargs keyword")

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    
display_info(name="Yugen", age=22, course="MCA")

info = {}

info["roll_no"] = int(input("Enter your Roll no:")) 
    
display_info(**info)






"""
nums = []

print("Enter Five Number for Multiplication")
for i in range(1,6):
        num = int(input(f"Enter {i} numbers:"))
        nums.append(num)
              
def Multi_num(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(Multi_num(*nums))


nums = []
print("Enter Five Number for Sum")
for i in range(1,6):
        num = int(input(f"Enter{i} Num:"))
        nums.append(num)
              
def adding_num(*args): 
    return sum(args)

print(adding_num(*nums))

def greet(name):
    return f"Hello,{name}"

print(greet("Yugen"))

def greet(name = "Yugen"):
    return f"Hi,{name}"

print (greet())


def greet(a):
    print ("If we don't return arguments is will return:") 
    return 

print (greet("Yugen"))
"""