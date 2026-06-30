import random
def rec_quick(a,s):
    if s==1 or s==0:
        return a
    else:
        pidx=s//2
        p=a[pidx]
        i1=0
        i2=0
        a1=[]
        a2=[]
        for i in range(s):
            if a[i]>=p and i!=pidx:
                a2.append(a[i])
                i2=i2+1
            elif a[i]<p:
                a1.append(a[i])
                i1=i1+1
        x=rec_quick(a1,i1)
        y=rec_quick(a2,i2)
        ap=[p]
        a=x+ap+y
        return a

a=[3,2,2,1]
s=len(a)
a=rec_quick(a,s)
print(a)