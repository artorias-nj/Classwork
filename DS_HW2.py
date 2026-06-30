class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
        
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
        
    def printLinkedList (self):
        self.printLinkedList_helper(self.head)
 
    def printLinkedList_helper(self, current):
        if current is None:
            return
 
        print(current.data, end = ' ')
        self.printLinkedList_helper(current.next)


mylist = OrderedList()
mylist.add(100)
mylist.add(50)
mylist.add(100)
mylist.add(5)
mylist.add(20)
mylist.add(75)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
mylist.printLinkedList()