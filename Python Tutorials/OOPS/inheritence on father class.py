class Father:
  def __init__(self):
    pass
  @staticmethod
  def Work():
    print("Handworking Father")
class Son(Father):
  def __init__(self):
    super().__init__()
  @staticmethod
  def Work():
    print("Enjoying Son")
Father.Work()
Son.Work()