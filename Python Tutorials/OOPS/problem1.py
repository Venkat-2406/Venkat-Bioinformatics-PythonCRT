#Program to create a mobile class and declare the states of mobile like color..price..brand..series..features..storages…battery capacity..create 10 objects and intialise using constructor and print the individual using function
class Mobile():
  def __init__(self,color,price,brand,series,storage,batterycapacity):
    self.mcolor=color
    self.mprice=price
    self.mbrand=brand
    self.mseries=series
    self.mstorage=storage
    self.mbattery=batterycapacity
def Mobile_details(self):
  print("Mobile_Details")
  print(f"Color of mobile {self.mcolor}")
  print(f"price of mobile {self.mprice}")
  print(f"brand of mobile {self.mbrand}")
  print(f"series of mobile {self.mseries}")
  print(f"storage of mobile {self.mstorage}")
  print(f"battery of mobile {self.mbattery}")
M1=Mobile("Black","23000","Iqoo","Z7","128GB","4500mah")
M2=Mobile("white","25000","Apple","14","256GB","5000mah")
M3=Mobile("red","30000","MI","note 4","1TB","6500mah")
Mobile_details(M1)
print()
Mobile_details(M2)
print()
Mobile_details(M3)