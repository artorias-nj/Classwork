import os

def erase():
    os.system('cls')
    print("MENU")
    print("1. First 2 and last 2")
    print("2. Money")
    print("3. Swap word order")
    print("4. ing and ly")
    print("5. Exit")
    print("")

def f2l2():
    x=input("Please enter a string: ")
    z=-1
    for i in x:
        z=z+1
    if(z>1):
        y=x[0:2]
        y=y+x[z-1:z+1]
        erase()
        print(y)
        print("")
    else:
        erase()
        print("Empty Sting")
        print("")

def cash():
    x=input("Please enter a string: ")
    y=x[0:1]
    z=0
    n=0
    for i in x:
        if(z!=0):
            if(i==y):
                x= x[:n] + "$" + x[n+1:]
        z=z+1
        n=n+1
    erase()
    print(x)

def swap():
    x=input("Please enter a string: ")
    y=0
    z=""
    for i in x:
        if(i==" "):
         z=x[y+1:]
         z=z+" "
         z=z+x[0:y]
        y=y+1
    erase()
    print(z)

def ing():
    x=input("Please enter a string: ")
    n=0
    z=" "
    for i in x:
        n=n+1
    if(n>2):
        if(x[n-3:]=="ing"):
            z=x[0:n-3]
            z=z+"ly"
        else:
            z=x+"ing"
    erase()
    print(z)

erase()
while True:
    y=input("Enter command: ")
    match y:
        case "1":
            erase()
            f2l2()
        case "2":
            erase()
            cash()
        case "3":
            erase()
            swap()
        case "4":
            erase()
            ing()
        case "5":
            os.system('cls')
            print("Goodbye User!")
            quit()
        case _:
            erase()
            print("Command not recognized")
            print("")
            
