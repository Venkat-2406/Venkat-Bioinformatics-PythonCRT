class Vechicle:                 #super class
  def __init__(self):
    print("I am vachicle class constructor")
  @staticmethod
  def Start():
    print("Vechicle is started")
class Car(Vechicle):          #sub class
  def __init__(self):
    super().__init__()
    print("I am the class constructor")
  @staticmethod
  def Start():
    print("Car is Started")
c1=Car()
c1.Start()