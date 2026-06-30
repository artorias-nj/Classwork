import random
def bs(a,t,lo,hi):
    if lo==hi:
        if a[lo]==t:
            index=lo
        else: 
            index=-1
    else:
        mid=int(lo+((hi-lo)/2))
        if t==a[mid]:
            index=mid
        elif t>a[mid]:
            lo=mid+1
            index=bs(a,t,lo,hi)
        else: 
            hi=mid-1
            index=bs(a,t,lo,hi)
    return index

array=[]
for i in range(100):
    array.append(random.randrange(1,101,1))
t=random.randrange(1,101,1)
array.sort()
x=len(array)-1
y=bs(array,t,0,x)
print(t)
print("index is "+str(y))
