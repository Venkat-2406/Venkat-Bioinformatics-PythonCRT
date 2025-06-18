class Employee():
  def __init__(self,empname,empID,designation,salary,deptname):
    print("Object is created")
    self.Empname=empname
    self.EmpID=empID
    self.Designation=designation
    self.Salary=salary
    self.Deptname=deptname
def Display_Details(self):
 print(f"Employee name :{self.Empname}")
 print(f"Employee ID:{self.EmpID}")
 print(f"Employee designation :{self.Designation}")
 print(f"Employee salary :{self.Salary}")
 print(f"Employee department :{self.Deptname}")
E1=Employee("Scott","101","security analyst","100000","Analysis")
Display_Details(E1)