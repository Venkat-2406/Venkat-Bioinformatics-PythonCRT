class Queue:
  def __init__(self):
    self.items=[]
  #add to rear
  def enqueue(self,item):
    self.items.append(item)
  #Empty or not
  def is_empty(self):
    return len(self.items)==0
  #Remove and return front items
  def dequeue(self):
    if self.is_empty():
      return None
    return self.items.pop(0)
  #Look at front item without removing
  def peek_front(self):
    if self.is_empty():
      return None
    return self.items[-1]
  def size(self):
    return len(self.items)
  


