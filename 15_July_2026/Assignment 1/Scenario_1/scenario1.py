# 1. Student Management System							
							
# Develop a Python application to manage student details using Object-Oriented Programming.							
							
# Requirements							
# Create a Student class with the following data members:							
# 	Roll Number						
# 	Name						
# 	Marks						
# Assign Grade based on marks:							
# 	A (Marks ≥ 90)						
# 	B (Marks ≥ 75)						
# 	C (Marks ≥ 60)						
# 	F (Marks < 60)						
# Create a College class.							
# Add student objects to the college.							

class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def assign_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'F'

    def __str__(self):
        return f"Roll Number: {self.roll_number}, Name: {self.name}, Marks: {self.marks}, Grade: {self.assign_grade()}"

class College:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"College: {self.name}")
        print("=" * 40)
        for student in self.students:
            print(student)
        print("=" * 40)

# Example usage
college = College("ABC Engineering College")
student1 = Student(101, "Rahul", 85)
student2 = Student(102, "Priya", 35)
college.add_student(student1)
college.add_student(student2)
college.display_students()  

