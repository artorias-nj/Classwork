def copy(d,s,si,ei):
    k=0
    i=si
    while i >= si and i<=ei:
        d[k]=s[i]
        k=k+1
        i=i+1
    #print(d)



def merge(a,a1,a2):
    s1=len(a1)
    s2=len(a2)
    s=len(a)
    i1=0
    i2=0
    i=0
    print(a1)
    print(a2)
    while i1<s1 and i2<s2:
        if a1[i1]< a2[i2]:
            a[i]=a1[i1]
            i1=i1+1
        else:
            a[i]=a2[i2]
            i2=i2+1
        i=i+1
        
    print(a)
    print(i1)
    print(s1)
    if i1==s1:
        for k in range(i,s-1):
            a[i]=a2[i2]
            i=i+1
            i2=i2+1
    else:
        for k in range(i,s-1):
            a[i]=a1[i1]
            i=i+1
            i1=i1+1


def merge_sort(a):
    if len(a)==1:
        return a
    else:
        mid=len(a)//2
        a1=[0]*((mid-1)-0+1)
        #print(a1)
        a2=[0]*((len(a)-1)-mid+1)
        #print(a2)
        copy(a1,a,0,mid-1)
        copy(a2,a,mid,(len(a)-1))
        merge_sort(a1)
        merge_sort(a2)
        merge(a,a1,a2)
        return a

a=[0,7,5,9,4]
merge_sort(a)
print(a)