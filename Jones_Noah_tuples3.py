x=input("Please input file name: ")
y=open(x,"r")
d={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0,}
for z in y:
    words=z.split()
    for i in words:
        word=i.split()
        for t in word:
            temp=list(t)
            for n in temp:
                if n=="a"or n=="A":
                    d["A"]=d["A"]+1
                elif n=="b"or n=="B":
                    d["B"]=d["B"]+1
                elif n=="c"or n=="C":
                    d["C"]=d["C"]+1
                elif n=="d"or n=="D":
                    d["D"]=d["D"]+1
                elif n=="e"or n=="E":
                    d["E"]=d["E"]+1
                elif n=="f"or n=="F":
                    d["F"]=d["F"]+1
                elif n=="g"or n=="G":
                    d["G"]=d["G"]+1
                elif n=="h"or n=="H":
                    d["H"]=d["H"]+1
                elif n=="i"or n=="I":
                    d["I"]=d["I"]+1
                elif n=="j"or n=="J":
                    d["J"]=d["J"]+1
                elif n=="k"or n=="K":
                    d["K"]=d["K"]+1
                elif n=="l"or n=="L":
                    d["L"]=d["L"]+1
                elif n=="m"or n=="M":
                    d["M"]=d["M"]+1
                elif n=="n"or n=="N":
                    d["N"]=d["N"]+1
                elif n=="o"or n=="O":
                    d["O"]=d["O"]+1
                elif n=="p"or n=="P":
                    d["P"]=d["P"]+1
                elif n=="q"or n=="Q":
                    d["Q"]=d["Q"]+1
                elif n=="r"or n=="R":
                    d["R"]=d["R"]+1
                elif n=="s"or n=="S":
                    d["S"]=d["S"]+1
                elif n=="t"or n=="T":
                    d["T"]=d["T"]+1
                elif n=="u"or n=="U":
                    d["U"]=d["U"]+1
                elif n=="v"or n=="V":
                    d["V"]=d["V"]+1
                elif n=="w"or n=="W":
                    d["W"]=d["W"]+1
                elif n=="x"or n=="X":
                    d["X"]=d["X"]+1
                elif n=="y"or n=="Y":
                    d["Y"]=d["Y"]+1
                elif n=="z"or n=="Z":
                    d["Z"]=d["Z"]+1

li=list()
for key, val in d.items():
   li.append((val,key)) 
li=sorted(li, reverse=True)
print(li)