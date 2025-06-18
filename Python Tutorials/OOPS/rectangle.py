'''
program to create a rectangle class and intilize the variables length and breadth using constructor 
and access the values using mutator methods
'''
class Rectangle:
  def __init__(self,l,b):
    self.length=l
    self.breadth=b
  def set_details(self):
    self.length=6
    self.breadth=5
  def get_details(self):
    print(f"length of rectangle  is {self.length}")
    print(f"breadth of rectangle  is {self.breadth}")
m1=Rectangle(15,20)
m1.get_details()
print("After modification")
m1.set_details()
    