import os

import Jones_Noah_Module_P2

def erase():
    os.system('cls')
    print("MENU")
    print("1. Display Global Variables")
    print("2. Print ")
    print("3. Print Number ")
    print("4. Print String")
    print("5. Print Number and String")
    print("6. Print Number, Decimal, and String")
    print("7. exit")
    print("")

erase()
while True:
    y=input("Enter command: ")
    match y:
        case "1":
            erase()
            Jones_Noah_Module_P2.printing()
            
        case "2":
            erase()
            Jones_Noah_Module_P2.funct1()
            
        case "3":
            erase()
            Jones_Noah_Module_P2.funct2(Jones_Noah_Module_P2.intvar)
            
        case "4":
            erase()
            Jones_Noah_Module_P2.funct3(Jones_Noah_Module_P2.strvar)
            
        case "5":
            erase()
            Jones_Noah_Module_P2.funct4(Jones_Noah_Module_P2.intvar,Jones_Noah_Module_P2.strvar)
            
        case "6":
            erase()
            Jones_Noah_Module_P2.funct5(Jones_Noah_Module_P2.intvar,Jones_Noah_Module_P2.floatvar,Jones_Noah_Module_P2.strvar)
            
        case "7":
            os.system('cls')
            print("Goodbye User!")
            quit()
            
        case _:
            erase()
            print("Command not recognized")
            print("")