class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
      self.Empname=empname
      self.EmpID=empID
      self.Designation=designation
      self.Salary=salary
      self.Deptname=deptname
    def Get_details(self):
       print(self.Empname) 
       print(self.EmpID)
       print(self.Designation)
       print(self.Salary)
       print(self.Deptname)
E1=Employee("Scott","101","security analyst","100000","Analysis")
E1.Get_details()