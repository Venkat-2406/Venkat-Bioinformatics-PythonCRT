'''
program to create a student class and declare the properties as name,id,branch,percentage,age,year of passout,no of certifications student as create 10 objects and intilize the values using mutator and acces through accessor….(Without Using Constructor)
'''
class Student:
    # Class attributes (default values)
    name = ""
    student_id = 0
    branch = ""
    percentage = 0.0
    age = 0
    year_of_passout = 0
    no_of_certifications = 0

    # Mutator methods (setters)
    def set_name(self, name):
        self.name = name

    def set_student_id(self, student_id):
        self.student_id = student_id

    def set_branch(self, branch):
        self.branch = branch

    def set_percentage(self, percentage):
        self.percentage = percentage

    def set_age(self, age):
        self.age = age

    def set_year_of_passout(self, year_of_passout):
        self.year_of_passout = year_of_passout

    def set_no_of_certifications(self, no_of_certifications):
        self.no_of_certifications = no_of_certifications

    # Accessor methods (getters)
    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def get_branch(self):
        return self.branch

    def get_percentage(self):
        return self.percentage

    def get_age(self):
        return self.age

    def get_year_of_passout(self):
        return self.year_of_passout

    def get_no_of_certifications(self):
        return self.no_of_certifications

# Creating student objects by taking input from the user
students = []
num_students = 2  # You can modify this value to take more or fewer students

for i in range(num_students):
    print(f"\nEnter details for Student {i+1}:")
    student = Student()
    student.set_name(input("Name: "))
    student.set_student_id(int(input("Student ID: ")))
    student.set_branch(input("Branch: "))
    student.set_percentage(float(input("Percentage: ")))
    student.set_age(int(input("Age: ")))
    student.set_year_of_passout(int(input("Year of Passout: ")))
    student.set_no_of_certifications(int(input("Number of Certifications: ")))
    students.append(student)

# Displaying student details using accessors
print("\nStudent Details:")
for student in students:
    print(f"Name: {student.get_name()}, ID: {student.get_student_id()}, Branch: {student.get_branch()}, "
          f"Percentage: {student.get_percentage()}%, Age: {student.get_age()}, "
          f"Year of Passout: {student.get_year_of_passout()}, Certifications: {student.get_no_of_certifications()}")


