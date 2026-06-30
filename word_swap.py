def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
 
 
s = "rooks"
 

print(s)
s=reverse(s)
print(s)


def reverse(array,f,l):
    if l-f==0:
        return
    elif l-f==1:
        swap(array,f,l)
        return
    else:
        swap(array,f,l)
        reverse(array,f+1,l-1)
def swap(array,u,v):
    temp=array[u]
    array[u]=array[v]
    array[v]=temp

array=["H","e","l","l","o"]
x=len(array)-1
print(array)
reverse(array,0,x)
print(array)