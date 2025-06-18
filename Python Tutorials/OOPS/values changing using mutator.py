class Mobile:
  def __init__(self,P,C,B):
    self.Price=P
    self.Color=C
    self.Brand=B
    print("Object is Created")
    #mutator
  def set_color(self):
    self.Color='blue'
    #Accessor
  def Get_Details(self):
    print(f"color: {self.Color}")
    print(f"Brand: {self.Brand}")
    print(f"Price: {self.Price}")
m1=Mobile('black','Iqoo',25000)
m1.Get_Details()
print("After the update")    
m1.set_color()
m1.Get_Details()