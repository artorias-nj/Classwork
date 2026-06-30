import random
import time
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
     
f1=[]
array=[]
for i in range(10):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection_sort(array,len(array),0)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
f1.append(ta)

array=[]
for i in range(100):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection_sort(array,len(array),0)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
f1.append(ta)

array=[]
for i in range(1000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection_sort(array,len(array),0)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
f1.append(ta)

array=[]
for i in range(5000):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection_sort(array,len(array),0)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
f1.append(ta)

print(f1)