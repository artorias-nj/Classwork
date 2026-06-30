#Data Structures Noah Jones homework 4 11/3/2023
def selectionSort(x):
   for fillslot in range(len(x)-1,0,-1):
       positionOfMin=0
       for location in range(1,fillslot+1):
           if x[location]<x[positionOfMin]:
               positionOfMin = location

       temp = x[fillslot]
       x[fillslot] = x[positionOfMin]
       x[positionOfMin] = temp
       print(x)

print("Data Structures, Noah Jones, homework 4, 11/3/2023")
x = [1,2,3,4,5,6,7,8,9,0]
selectionSort(x)
print(x)
