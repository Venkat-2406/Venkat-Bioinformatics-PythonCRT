class Mobile:
  def __init__(self):
    print("Objected is created")
  @classmethod
  def Display(a):
    print("I'm class method")
    print("I will work irrespective of object creation")
Mobile.Display()
M1=Mobile()
M1.Display()