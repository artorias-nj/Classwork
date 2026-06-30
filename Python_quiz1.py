
#inputs
dn=input("What is your name: ")
da=input("What is your age: ")
md1=input("Please enter your miles driven in digits: ")
mpg1=input("Please enter your car's miles per gallon in digits: ")
gppg1=input("Please enter the gas price per gallon in digits: ")

#making sure digits are used
try:
    md2=float(md1)
    mpg2=float(mpg1)
    gppg2=float(gppg1)
except:
    print("Error: input is not a numerical value")
    quit()

#calulating cost
cost=md2/mpg2
cost=cost*gppg2

#print answer
print(str(dn)+", your commute costs you "+str(cost))
