class Graduation():
  def __init__(self):
    pass
  @staticmethod
  def Graduate():
    print("Congratulations you are a graduate now")

#First sub classes
class CSE():
  def __init__(self):
    pass
  @staticmethod
  def Graduate():
    print("Congratulations you are a CSE graduate now")
  
#second sub class
class BI():
  def __init__(self):
    pass
  @staticmethod
  def Graduate():
    print("Congratulations you are a BI graduate now")

#third sub class
class IT():
  def __init__(self):
    pass
  @staticmethod
  def Graduate():
    print("Congratulations you are a IT graduate now")
Graduation.Graduate()
CSE.Graduate()
BI.Graduate()
IT.Graduate()
