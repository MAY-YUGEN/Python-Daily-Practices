'''
from PIL import Image
image1 = Image.open("Data/Images/2.jpg")
image1.show()
'''

print("\nPyramid Patten Printing Using While loop")
i = 0
while i <= 10:
    print(i * "*")
    i = i+1

print("\n")
i = 10
while i >= 0:
    print(i * "*")
    i = i-1

print("Intended star pyramid pattern\n")

n = 10
i = 1

while i <= n:
    j = 1
    while j <= n - i:
        print(" ",end="")
        j = j + 1
    k = 1 
    while k <= 2 * i - 1:
        print("*",end="")
        k = k + 1
    print()
    i = i + 1
print("\n")
print("Inverted Star pyramid pattern\n")

n = 1
i = 10

while i >= n:
    j = 1 
    while j <= 10 - i:
        print(" ",end="")
        j = j + 1
    k = 1
    while k <= 2 * i - 1:
        print("*",end="")
        k = k + 1
    print()
    i = i - 1
print("\n")