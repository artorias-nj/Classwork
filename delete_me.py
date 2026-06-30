import os
import sys
def cap(x):
    x=x.capitalize()
    return x
def swap(x):
    x=x.swapcase()
    return x
def count(x):
    z=0
    x=x.strip()
    for i in x:
        if (i==" "):
            z=z+1
    z=z+1
    z=z+flags
    return z
def find(x,y):
    z=0
    n=[]
    for i in x:
        if(i==y):
           n.append(z)
        z=z+1
    return n
def extract(x,y,z):
    try:
        flag=0
        y=int(y)
        flag=1
        z=int(z)
    except:
        if(flag==0):
            print("The Start should be a numeric value")
        else:
            print("The end should be a numeric value")
    return x[y:z]
def ucase(x):
    x=x.upper()
    return x
def lcase(x):
    x=x.lower()
    return x
while True:
    x=" "
    flags=0
    print("MENU")
    print("1. Enter string")
    print("2. Swapcase the string")
    print("3. Count the number of words in the string")
    print("4. Find the positions in the string of a particular word or character")
    print("5. Extract a slice")
    print("6. Capitalize the string")
    print("7. Convert every letter to uppercase")
    print("8. Convert every lettter to lowercase")
    print("9. Exit enter")
    print("")
    while True:
        y=input("Enter command: ")
        if (y=="6"):
            os.system('cls')
            var1=cap(x)
            print("MENU")
            print("1. Enter string")
            print("2. Swapcase the string")
            print("3. Count the number of words in the string")
            print("4. Find the positions in the string of a particular word or character")
            print("5. Extract a slice")
            print("6. Capitalize the string")
            print("7. Convert every letter to uppercase")
            print("8. Convert every lettter to lowercase")
            print("9. Exit enter")
            print("")
            print(var1)
            continue
        elif(y=="2"):
            os.system('cls')
            var2=swap(x)
            print("MENU")
            print("1. Enter string")
            print("2. Swapcase the string")
            print("3. Count the number of words in the string")
            print("4. Find the positions in the string of a particular word or character")
            print("5. Extract a slice")
            print("6. Capitalize the string")
            print("7. Convert every letter to uppercase")
            print("8. Convert every lettter to lowercase")
            print("9. Exit enter")
            print("")
            print(var2)
            continue
        elif(y=="3"):
            os.system('cls')
            var3=count(x)
            print("MENU")
            print("1. Enter string")
            print("2. Swapcase the string")
            print("3. Count the number of words in the string")
            print("4. Find the positions in the string of a particular word or character")
            print("5. Extract a slice")
            print("6. Capitalize the string")
            print("7. Convert every letter to uppercase")
            print("8. Convert every lettter to lowercase")
            print("9. Exit enter")
            print("")
            print(var3)
            continue
        elif(y=="4"):
            os.system('cls')
            y=input("Please input text you would like to find: ")
            var4=find(x,y)
            print("MENU")
            print("1. Enter string")
            print("2. Swapcase the string")
            print("3. Count the number of words in the string")
            print("4. Find the positions in the string of a particular word or character")
            print("5. Extract a slice")
            print("6. Capitalize the string")
            print("7. Convert every letter to uppercase")
            print("8. Convert every lettter to lowercase")
            print("9. Exit enter")
            print("")
            for i in var4:
                print(i)
            continue
        elif(y=="5"):
            os.system('cls')
            y=input("Please input start: ")
            z=input("Please input end: ")
            var5=extract(x,y,z)
            print("MENU")
            print("1. Enter string")
            print("2. Swapcase the string")
            print("3. Count the number of words in the string")
            print("4. Find the positions in the string of a particular word or character")
            print("5. Extract a slice")
            print("6. Capitalize the string")
            print("7. Convert every letter to uppercase")
            print("8. Convert every lettter to lowercase")
            print("9. Exit enter")
            print("")
            print(var5)
            continue
        elif(y=="1"):
            if(x==" "):
                print("")
                x=sys.stdin.readline()
            else:
                flags=flags+1
                y=sys.stdin.readline()
                x=x+y+""
                os.system('cls')
                print("MENU")
                print("1. Enter string")
                print("2. Swapcase the string")
                print("3. Count the number of words in the string")
                print("4. Find the positions in the string of a particular word or character")
                print("5. Extract a slice")
                print("6. Capitalize the string")
                print("7. Convert every letter to uppercase")
                print("8. Convert every lettter to lowercase")
                print("9. Exit enter")
                print("")
                print(x)
            continue
        elif(y=="9"):
            os.system('cls')
            print("Goodbye user!")
            quit()
        elif(y=="7"):
            os.system('cls')
            var6=ucase(x)
            print("MENU")
            print("1. Enter string")
            print("2. Swapcase the string")
            print("3. Count the number of words in the string")
            print("4. Find the positions in the string of a particular word or character")
            print("5. Extract a slice")
            print("6. Capitalize the string")
            print("7. Convert every letter to uppercase")
            print("8. Convert every lettter to lowercase")
            print("9. Exit enter")
            print("")
            print(var6)
            continue
        elif(y=="8"):
            os.system('cls')
            var8=lcase(x)
            print("MENU")
            print("1. Enter string")
            print("2. Swapcase the string")
            print("3. Count the number of words in the string")
            print("4. Find the positions in the string of a particular word or character")
            print("5. Extract a slice")
            print("6. Capitalize the string")
            print("7. Convert every letter to uppercase")
            print("8. Convert every lettter to lowercase")
            print("9. Exit enter")
            print("")
            print(var8)
            continue
        else:
            os.system('cls')
            print("MENU")
            print("1. Enter string")
            print("2. Swapcase the string")
            print("3. Count the number of words in the string")
            print("4. Find the positions in the string of a particular word or character")
            print("5. Extract a slice")
            print("6. Capitalize the string")
            print("7. Convert every letter to uppercase")
            print("8. Convert every lettter to lowercase")
            print("9. Exit enter")
            print("")
            print("ERROR DO NOT RECOGNIZE COMMMAND")
            continue
