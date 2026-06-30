class Students:
    
    
    def __init__(self, fname="", lname=""):
        self.__fname=fname
        self.__lname=lname
        self.__dob="jj"
        self.__married=""
        self.__address=""
        self.__college="Adrian"
        self.__classes=[]
    
    def get_dob(self):
        return self.__dob
        
        
    def get_fname(self):
        return self.__fname
        
    def get_lname(self):
        return self.__lname
        
    def get_marriedB(self):
        return self.__married
        
    def get_address(self):
       return self.__address
        
    def get_college(self):
        return self.__college
        
    def get_classes(self):
        return self.__classes
    
              
    def set_dob(self, x,):
        self.__dob=x
        
    def set_fname(self, x,):
        self.__fname=x
        
    def set_lname(self, x,):
        self.__lname=x
        
    def set_married(self, x,):
        self.__married=x
        
    def set_address(self, x,):
        self.__adress=x
        
    def set_college(self, x,):
        self.__college=x
        
    def set_classes(self, x,):
        self.__classes=x
        
    def get_married(self):
        self.__married="Married"
    
    def movedto(self, x):
        self.__address=x
    
    def enrolls(self, x):
        self.__classes.append(x)
    
    def drops(self, x):
        self.__classes.remove(x)
        
x=Students("John", "Doe")
test=x.get_fname()
test2=x.get_lname()
print(test+" "+test2)


x.set_dob("01,20,2000")
test=x.get_dob()
print(test)

x.get_married()
test=x.get_marriedB()
print(test)

x.movedto("MI")
test=x.get_address()
print(test)

x.enrolls("CC102")
test=x.get_classes()
print(test)

x.drops("CC102")
test=x.get_classes()
print(test)