def checker(array,i1,i2):
    if len(array)<=1:
        return True
    elif i1==i2 and i1!=0:
        return True
    elif i1+1==i2:
        if array[i1]==array[i2]:
            return True
        else:
            return False
    else: 
        if array[i1]!=array[i2]:
            return False
        else:
            return checker(array,i1+1,i2-1)

array=input("please enter a word:  ")
y=0
x=len(array)-1
print (checker(array,y,x))