def bubble_sort(a, size, swapped):
    if swapped==False:
        return a
    swapped=False
    for i in range(size-1):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
            swapped=True
    bubble_sort(a,size,swapped)
 
a=[8,9,1,1,7,6,3]
z=len(a)
bubble_sort(a,z,True)
print(a)