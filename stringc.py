
x=input("Please input a word: ")
y=input("Please input a word: ")
if (x>y):
    print(y)
    print(x)
elif(y>x):
    print(x)
    print(y)
else:
    print(x,"==",y)
print(x.upper())
print(y.upper())
print(x.lower())
print(x.lower())
if(x.islower()):
    x=x.swapcase()
    y=y.swapcase()
print(x)
print(y)
x=x.strip()
y=y.strip()
print(x)
print(y)
