'''
to create product class….name id price gst manufacture expirary date….create 5 obj…intilize using parameterized and access through parameterizd…declare the mutated methods
 for all properties and print it

'''
class Product:
  def __init__(self,name,price,gst,manufacture,expirary):
      self.pname=name
      self.pprice=price
      self.pgst=gst
      self.pmanufacture=manufacture
      self.pexpirary=expirary
      #mutator
  def Set_Details(self):
     self.pname='panner'
     self.pprice=200
     self.pgst=20
     self.pmanufacture='15 june'
     self.pexiprary='05 july'
  def Get_Details(self):
    print(f"name of product {self.pname}")
    print(f"price of product {self.pprice}")
    print(f"gst of product {self.pgst}")
    print(f"manufacture of product {self.pmanufacture}")
    print(f"exiprary of product {self.pexpirary}")
P1=Product('milk',30,24,'24 june','10 july')
P1.Get_Details()
print("After MOdification")
P1.Set_Details()
P1.Get_Details()         
     
    