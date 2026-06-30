
go=True
while go:
    print("Please input information as requested, to stop enter 'none': ")
    ln=input("Please Input last name: ")
    if(ln == "none"):
        go=False
        continue
    fn=input("PLease Input first name: ")
    hn=input("Please Input house number: ")
    city=input("Please Input city name: ")
    stn=input("Please Input street name: ")
    state=input("Please Input state name: ")
    zipc=input("Please Input zip code: ")
    sem=input("Please Input amount of semester left to graduate (please use digits): ")
    gpa=input("Please Input GPA (please use digits): ")
    try:
        flag=0
        var3=float(zipc)
        flag=1
        var1=float(sem)
        flag=2
        var2=float(gpa)
    except:
        if(flag==0):
            print("Zip code should be a numeric value")
            continue
        elif(flag==1):
            print("Semesters left should be a numeric value")
            continue
        else:
            print("GPA should be a numeric value")
            continue
    flname=fn+" "+ln
    adress=hn+" "+stn+", "+city+", "+state+", "+zipc
    print(flname)
    print(adress)
    if(var1<3 and var2<3):
        print("Alert: GPA too low close to graduation")
print("Goodbye user!")
