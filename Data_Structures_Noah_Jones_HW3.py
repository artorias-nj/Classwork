#Data Structures Noah Jones homework 3

#assign class
class queue:
  def __init__(self):
    self.items = []
    
  def isEmpty(self):
    return self.items == []
    
  def addfront(self, item):
    self.items.append(item)
    
  def addRear(self, item):
    self.items.insert(0, item)
    
  def removeFront(self):
    return self.items.pop()
    
  def removeRear(self):
    return self.items.pop(0)
    
  def size(self):
    return len(self.items)
    

#create palindrome checker
def palchecker(aString):
  chardeque = queue()
  
  for ch in aString:
    chardeque.addRear(ch)
    
  stillEqual = True
  
  while chardeque.size() > 1 and stillEqual:
    first = chardeque.removeFront()
    last = chardeque.removeRear()
    if first != last:
      stillEqual = False
      
  return stillEqual

#Test
print("Data Structures Noah Jones homework 3")
print("qwerty")
print(palchecker("qwerty"))
print("able was I ere I saw elba")
print(palchecker("able was I ere I saw elba"))
print("father")
print(palchecker("father"))
print("dad")
print(palchecker("dad"))