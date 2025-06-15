#function---A block of code used to perform a specific task     ()----represents memorary allocation

def job_goal():
  print("Success")
  print("Consistency")
  print("determination")
job_goal()
job_goal()
job_goal()

# Types of functions
def display():
  return "Hey..! I'm the zero arg function"
res=display()
print(res)

def displaynamed(name):
  return f"Hey..! I'm the zero arg function called by {name}"
res1=displaynamed("Kavya")
print(res1)