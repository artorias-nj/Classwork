import random
import time
def selection(a):
    for i in range(len(a)): 
     
        min_idx = i 
        for j in range(i+1, len(a)): 
            if a[min_idx] > a[j]: 
                min_idx = j        
        a[i], a[min_idx] = a[min_idx], a[i] 


f1=[]
array=[]
for i in range(10):
    array.append(random.randrange(1,101))
ta=0
for l in range(100):
    ta1=time.time()
    selection(array)
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
    selection(array)
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
    selection(array)
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
    selection(array)
    ta2=time.time()
    ta+=(ta2-ta1)
ta=(ta/100)
f1.append(ta)

print(f1)