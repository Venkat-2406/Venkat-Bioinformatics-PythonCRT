class Mobile:
  def __init__(self):
    print("Objected is created")
  @staticmethod
  def Display():                                            # No calling
    print("I'm class method")
    print("I will work irrespective of object creation")
Mobile.Display()
