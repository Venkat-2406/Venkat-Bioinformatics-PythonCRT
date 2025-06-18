'''
program to create a squareshape class & declare the property as
Length
Breadth
Height

i)Calculate the Area of square using instance methods
ii)check whether the sides of square are equal or not using instance methods
iii)calculate the perimeter of square using instance methods
iv)Find the Diagonals of square using instance methods
v)Find the length of square using instance methods
'''
class Squareshape:
  def __init__(self,l,b,h):
    self.sl=l
    self.sb=b
    self.sh=h
  def area(self):
        print("Area of the shape : ",self.sl*self.sb)
  def square(self):
        print("The shape is square or not : ",self.sl==self.sb)
  def perimeter(self):
      print("The Perimeter of the shape  : ",(2 *(self.sl+self.sb)))
  def diagonal(self):
      print("The Diagnol of permimeter", (self.sl*2 + self.sb*2) ** 0.5 )
  def sidesquare(self):
      print( (self.sl) if self.sl==self.sb else "Not Square" )                   
s1=Squareshape(5,5,5)
s1.area()
s1.square()
s1.perimeter()
s1.diagonal()
s1.sidesquare()
s2=Squareshape(5,2,1)
s2.area()
s2.square()
s2.perimeter()
s2.diagonal()
s2.sidesquare()


