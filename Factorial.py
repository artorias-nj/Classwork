def factorial(n):
    if n==0:
        return 1
    else:
        return n *factorial(n-1)

def fact(n):
    ret=1
    for i in range(1,n):
        ret=ret*i
    return ret


x=factorial(983)
print(x)
x=fact(999)
print(x)