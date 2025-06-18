'''
program to create employee class decalre sales and create 5 objects using different constructors
'''
class Employee:
  def __init__(self,empname,empid,job,salary,location,dept):
    self.empname=empname
    self.empid=empid
    self.job=job
    self.salary=salary
    self.location=location
    self.dept=dept
    print("I am six parameterized constructor")
  def __init__(self,empname,empid,job,salary,location):
    self.empname=empname
    self.empid=empid
    self.job=job
    self.salary=salary
    self.location=location
    print("I am five parameterized constructor")
  def __init__(self,empname,empid,job,salary):
    self.empname=empname
    self.empid=empid
    self.job=job
    self.salary=salary
    print("I am four parameterized constructor")
  def __init__(self,empname,empid,job):
    self.empname=empname
    self.empid=empid
    self.job=job
    print("I am three parameterized constructor")
  def __init__(self,empname,empid):
    self.empname=empname
    self.empid=empid
    print("I am two parameterized constructor")
  def __init__(self,empname):
    self.empname=empname
    print("I am one parameterized constructor")
  def __init__(self):
    print("I am zero parameterized constructor")

