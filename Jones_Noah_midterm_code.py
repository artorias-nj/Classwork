#cacluate BMI
def bmi(x,y): 
    score = x * 703
    score = score/(y*y)
    return score

#Check weight stastus.
def status(x):
    if x < 25:
        return 0
    elif x >= 30:
        return 1
    else:
        return 2


#makes lists
people = ["Steve", "Tony", "Natasha", "Bruce", "Peter", "Bucky"]
bmis=[]
#assign weight and height
for name in people: 
    w = float(input("Please input weight for "+name+": "))
    h = float(input("Please input height for "+name+": "))
    temp = bmi(w,h)
    bmis.append(temp)

#make global variables
global under
under = 0
global normal
normal = 0
global over
over = 0

#see how many are in each group
for i in bmis:
    temp = status(i)
    if temp == 0:
        under = under+1
    if temp == 1: 
        over = over+1
    if temp == 2:
        normal = normal+1    
        
#print results
print("There are "+str(under)+" underweight people, "+str(over)+" overweight people, and "+str(normal)+" normal weight people.")

