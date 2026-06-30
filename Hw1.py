import random
import time
def accumulate(array):
    sum=0
    size=len(array)
    for i in range(size):
        sum+=array[i]
    return sum

def partial_sum(array,ps):
    size=len(array)
    for i in range(size):
        for j in range(i,size):
            ps[i]+=array[j]

f1=[]
f2=[]

array=[1,4,16,20,11]
a2=[]
for i in array:
    a2.append(0)

x=accumulate(array)
partial_sum(array,a2)

array=[]
for i in range(10):
    array.append(random.randrange(1,101))
a2=[]
for i in array:
    a2.append(0)
    
ta=0
tb=0
for l in range(100):
    ta1=time.time()
    x=accumulate(array)
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    partial_sum(array,a2)
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
    a2.append(0)

ta=0
tb=0
for l in range(100):
    ta1=time.time()
    x=accumulate(array)
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    partial_sum(array,a2)
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
    a2.append(0)

ta=0
tb=0
for l in range(100):
    ta1=time.time()
    x=accumulate(array)
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    partial_sum(array,a2)
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
    a2.append(0)

ta=0
tb=0
for l in range(5):
    ta1=time.time()
    x=accumulate(array)
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    partial_sum(array,a2)
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
    a2.append(0)

ta=0
tb=0
for l in range(2):
    ta1=time.time()
    x=accumulate(array)
    ta2=time.time()
    ta+=(ta2-ta1)
    tb1=time.time()
    partial_sum(array,a2)
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