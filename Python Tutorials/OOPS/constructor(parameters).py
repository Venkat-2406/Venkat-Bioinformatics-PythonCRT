#constructor without parameter
class Mobile():
  def __init__(self):
    print("Mobile constructor Called")
realme=Mobile()

#without parameter
class Mobile():
  def __init__(self):
    self.model='RealMe X'
  def show_model(self):
    print("MOdel:",self.model)
    realme=Mobile()
    realme.show_model()
