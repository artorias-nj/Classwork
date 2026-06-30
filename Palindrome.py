def checker(array): 
    y=0
    x=len(array)-1
    answer=True
    while y<=x and answer==True:
        if array[y]==array[x]:
            y=y+1
            x=x-1
        else:
            answer=False
    print(answer)

array=input("please enter a word:  ")
checker(array)