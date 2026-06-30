intvar=1

floatvar=1.123456

strvar="Module variables"
def printing():
    print("The module has the following global variables: ")
    print("- an integer variable intvar = "+str(intvar))
    print("- a float variable floatvar = "+str(floatvar))
    print("- a string variable strvar = "+strvar)

def funct1():
    print("funct1")
    
def funct2(x):
    print("funct2")
    print(x)
    
def funct3(s):
    print("funct3")
    print(s.upper())
    return s.upper()
    
def funct4(x,s):
    print("funct4")
    intstr=str(x)+"_"+s
    print(str(x)+"_"+s)
    return intstr
    
def funct5(x,f,s):
    print("funct5")
    intfloatstr=str(x)+"_"+str('%.2f'%f)+"_"+s
    print(intfloatstr)
    return intfloatstr
    
    

