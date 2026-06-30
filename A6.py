
n=input("Please enter your name: ")
a=input("Please enter your age: ")
h=input("Please enter your height between 1.6 and 2.0 meters: ")
try:
    flag=0
    a=float(a)
    flag=1
    h=float(h)
except:
    if(flag==0):
        print("Age should be a numeric value")
    else:
        print("Height should be a numeric value")
    quit()
a=a+1
h=h+0.1
print(n," ",a," ",h)
