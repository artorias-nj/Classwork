import random
import time
def bubble_sort(a, size):
    swapped=True
    while(swapped):
        swapped=False
        for i in range(size-1):
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                swapped=True

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0     
    j = 0     
    k = l     
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 

f1=[]
f2=[]

array=[1,4,16,20,11]
a2=[]
for i in array:
    a2.append(random.randrange(1,101))

bubble_sort(array,len(array))
mergeSort(a2,0,(len(a2)-1))

array=[]
for i in range(10):
    array.append(random.randrange(1,101))
a2=[]
for i in array:
    a2.append(random.randrange(1,101))
    
ta=0
tb=0
for l in range(100):
    ta1=time.time()
    bubble_sort(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    mergeSort(a2,0,(len(a2)-1))
    tb2=time.time()
    tb+=(tb2-tb1)
ta=(ta/100)
tb=(tb/100)
f1.append(ta)
f2.append(tb)

array=[]
for i in range(50):
    array.append(random.randrange(1,101))
a2=[]
for i in array:
    a2.append(random.randrange(1,101))

ta=0
tb=0
for l in range(100):
    ta1=time.time()
    bubble_sort(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    mergeSort(a2,0,(len(a2)-1))
    tb2=time.time()
    tb+=(tb2-tb1)
ta=(ta/100)
tb=(tb/100)
f1.append(ta)
f2.append(tb)

array=[]
for i in range(100):
    array.append(random.randrange(1,101))
a2=[]
for i in array:
    a2.append(random.randrange(1,101))

ta=0
tb=0
for l in range(100):
    ta1=time.time()
    bubble_sort(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    mergeSort(a2,0,(len(a2)-1))
    tb2=time.time()
    tb+=(tb2-tb1)
ta=(ta/100)
tb=(tb/100)
f1.append(ta)
f2.append(tb)

array=[]
for i in range(1000):
    array.append(random.randrange(1,101))
a2=[]
for i in array:
    a2.append(random.randrange(1,101))

ta=0
tb=0
for l in range(5):
    ta1=time.time()
    bubble_sort(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    mergeSort(a2,0,(len(a2)-1))
    tb2=time.time()
    tb+=(tb2-tb1)
ta=(ta/5)
tb=(tb/5)
f1.append(ta)
f2.append(tb)

array=[]
for i in range(10000):
    array.append(random.randrange(1,101))
a2=[]
for i in array:
    a2.append(random.randrange(1,101))

ta=0
tb=0
for l in range(2):
    ta1=time.time()
    bubble_sort(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    mergeSort(a2,0,(len(a2)-1))
    tb2=time.time()
    tb+=(tb2-tb1)
ta=(ta/2)
tb=(tb/2)
f1.append(ta)
f2.append(tb)

tuplef1=((10,f1[0]),(50,f1[1]),(100,f1[2]),(1000,f1[3]),(10000,f1[4]))
tuplef2=((10,f2[0]),(50,f2[1]),(100,f2[2]),(1000,f2[3]),(10000,f2[4]))
print(tuplef1)
print(tuplef2)