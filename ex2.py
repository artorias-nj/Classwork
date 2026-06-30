
def add(x,y):
    z=x+y
    return z
def mult(x,y):
    m=x*y
    return m
def ab(x):
    if(x<0):
        x=x*-1
    return x
#main program
var1=input("Please enter number: ")
var2=input("Please enter number: ")
try:
   x=float(var1)
   y=float(var2)
except:
    print("Error: input is not a numerical value")
    quit()
print("The sum on the numbers is, "+str(add(x,y)))
print("The Multiplication of the numbers is, "+str(mult(x,y)))
print("The absloute vale of the first number is, "+str(ab(x)))
print("The absloute vale of the second number is, "+str(ab(y)))
