'''
  program to stimulate the behaviour of a web page or browsers back 
  button when a user Visits push to stack when user Click back pop the top page and go to previous
  '''
class Browser:
  def __init__(self):
    self.history=[]
  def visit(self,page):
    self.history.append(page)
    print(f"Visited page{page}")
  def undo(self):
    if len(self.history)>1:
      self.history.pop() 
      print(f"Back to {self.history[-1]}")
    else:
      print("No pages to comeback")
browser=Browser()
browser.visit("google.com")
browser.visit("Youtube.com")
browser.visit("Linkedin.com")
browser.undo()
browser.undo()
browser.undo()







