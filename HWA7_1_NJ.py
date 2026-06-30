import random
import time
import math
def insertionSort(arr):
    n = len(arr)  
      
    if n <= 1:
        return  
 
    for i in range(1, n):  
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]:  
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 

def selection(a):
    for i in range(len(a)): 
     
        min_idx = i 
        for j in range(i+1, len(a)): 
            if a[min_idx] > a[j]: 
                min_idx = j        
        a[i], a[min_idx] = a[min_idx], a[i] 

def minIndex( a , i , j ):
    if i == j:
        return i
    k = minIndex(a, i + 1, j)
    return (i if a[i] < a[k] else k)
     
def selection_sort(a, n, i):
 
    if i == n:
        return -1
    k = minIndex(a, i, n-1)
    if k != i:
        a[k], a[i] = a[i], a[k]
    selection_sort(a, n, i + 1)

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
               
def merge(src, result, start, inc):
    end1 = start+inc 
    end2 = min(start+2*inc, len(src)) 
    x, y, z = start, start+inc, start 
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]; x += 1 
        else:
            result[z] = src[y]; y += 1 
        z += 1 
    if x < end1:
        result[z:end2] = src[x:end1] 
    elif y < end2:
        result[z:end2] = src[y:end2] 

def merge_sort(S):
    n = len(S)
    logn = math.ceil(math.log(n,2))
    src, dest = S, [None]*n 
    for i in (2**k for k in range(logn)): 
        for j in range(0, n, 2*i): 
            merge(src, dest, j, i)
        src, dest = dest, src 
    if S is not src:
        S[0:n] = src[0:n] 

def merge_rec(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i] 
            i += 1
        else:
            S[i+j] = S2[j] 
            j += 1
 
def merge_sort_rec(S):
    n = len(S)
    if n < 2:
        return 
    mid = n // 2
    S1 = S[0:mid] 
    S2 = S[mid:n] 
    merge_sort_rec(S1) 
    merge_sort_rec(S2) 
    merge_rec(S1, S2, S) 

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



insertionSort_time=[]
array=[]
for i in range(10000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    insertionSort(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
insertionSort_time.append(ta)
array=[]
for i in range(50000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    insertionSort(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
insertionSort_time.append(ta)
array=[]
for i in range(100000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    insertionSort(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
insertionSort_time.append(ta)

selection_nonrec_time=[]
array=[]
for i in range(10000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
selection_nonrec_time.append(ta)
array=[]
for i in range(50000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
selection_nonrec_time.append(ta)
array=[]
for i in range(100000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
selection_nonrec_time.append(ta)

selection_sort_rec_time=[]
array=[]
for i in range(10000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection_sort(array,len(array),0)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
selection_sort_rec_time.append(ta)
array=[]
for i in range(50000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection_sort(array,len(array),0)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
selection_sort_rec_time.append(ta)
array=[]
for i in range(100000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection_sort(array,len(array),0)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
selection_sort_rec_time.append(ta)

bubble_sort_time=[]
array=[]
for i in range(10000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    bubble_sort(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
bubble_sort_time.append(ta)
array=[]
for i in range(50000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    bubble_sort(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
bubble_sort_time.append(ta)
array=[]
for i in range(100000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    bubble_sort(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
bubble_sort_time.append(ta)

merge_sort_time=[]
array=[]
for i in range(10000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    merge_sort(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
merge_sort_time.append(ta)
array=[]
for i in range(50000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    merge_sort(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
merge_sort_time.append(ta)
array=[]
for i in range(100000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    merge_sort(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
merge_sort_time.append(ta)

merge_sort_rec_time=[]
array=[]
for i in range(10000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    merge_sort_rec(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
merge_sort_rec_time.append(ta)
array=[]
for i in range(50000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    merge_sort_rec(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
merge_sort_rec_time.append(ta)
array=[]
for i in range(100000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    merge_sort_rec(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
merge_sort_rec_time.append(ta)

rec_quick_time=[]
array=[]
for i in range(10000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    rec_quick(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
rec_quick_time.append(ta)
array=[]
for i in range(50000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    rec_quick(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
rec_quick_time.append(ta)
array=[]
for i in range(100000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    rec_quick(array,len(array))
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
rec_quick_time.append(ta)

print("insertionSort times "+str(insertionSort_time))
print("selection nonrec times "+str(selection_nonrec_time))
print("selection_sort rec times "+str(selection_sort_rec_time))
print("bubble_sort times"+str(bubble_sort_time))
print("merge_sort times"+str(merge_sort_time))
print("merge_sort_rec times"+str(merge_sort_rec_time))
print("rec_quick_time"+str(rec_quick_time))