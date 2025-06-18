class Grandfather():
  def __init__(self):
    pass
  @staticmethod       #method overriding
  def Properties():
    print("100 Acres of land")
class Father(Grandfather):
  def __init__(self):
    super().__init__()
  @staticmethod
  def Properties():
    print("50 Acres of land")
class Yourself(Father):
  def __init__(self):
    super().__init__()
  @staticmethod
  def Properties():
    print("B.Tech degree job")
Grandfather.Properties()
Father.Properties()
Yourself.Properties()
