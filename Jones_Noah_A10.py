import os

def erase():
    os.system('cls')
    print("MENU")
    print("1. UPPER CASE")
    print("2. UPPER CASE new file")
    print("3. The Average")
    print("4. exit")
    print("")

def uppercase():
    for i in fh:
        i=i.rstrip()
        i=i.upper()
        print(i)

def newfile():
    nfh=open("mbox_short_upperc.txt","w")
    for i in fh:
        i=i.upper()
        nfh.write(i)
    nfh.close()

def average():
    count=0
    total=0.0
    for i in fh:
        if i.startswith('X-DSPAM-Confidence:') :
            count+=1
            x=i[19:]
            x=float(x)
            total+=x
    total=total/count
    print(total)

erase()
fh=open("Test_File","r")
while True:
    y=input("Enter command: ")
    match y:
        case "1":
            erase()
            uppercase()
        case "2":
            erase()
            newfile()
        case "3":
            erase()
            average()
            
        case "4":
            os.system('cls')
            print("Goodbye User!")
            quit()
        case _:
            erase()
            print("Command not recognized")
            print("")