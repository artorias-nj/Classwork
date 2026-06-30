
def pay(x,y):
    if(x>40):
        pay=add(mult(40,y),mult((sub(x,40)),(mult(1.5,y))))
    else:
        pay=(x*y)
    return pay
def add(x,y):
    z=x+y
    return z
def sub(x,y):
    z=x-y
    return z
def mult(x,y):
    m=x*y
    return m

var1=input("Enter Hours: ")
var2=input("Enter Rate: ")
try:
    flag=0
    var3=float(var1)
    flag=1
    var4=float(var2)
except:
    if(flag==0):
        print("Input Hours should be a numeric value")
    else:
        print("Input Rate should be a numeric value")
    quit()
print("Pay: $",pay(var3,var4))
