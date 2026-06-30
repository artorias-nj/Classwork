import socket

url=input("Please enter url: ")
host=url.split("/")
host=host[2]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = "GET "+str(url)+" HTTP/1.0\r\n\r\n"
cmd=cmd.encode()
mysock.send(cmd)
mylist=[]
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    x=data.decode()
    x=str(x)
    mylist.append(x)
    
mysock.close()
mylist=mylist[0].split("\r")
mylist2=[]
for i in mylist:
    temp=i.split("\n")
    mylist2.append(temp)
mylist=[]
for i in mylist2:
    for n in i:
        mylist.append(n)
        
     
val="" 
try:
    while True:
        mylist.remove(val)
except ValueError:
    pass

print("Data: "+mylist[2]+", "+mylist[3]+" "+mylist[6]+", "+mylist[10]+", "+mylist[11])