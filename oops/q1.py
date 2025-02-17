# creat student class that take name and marks of 3 subjects as argument in constructor.
# the create a method that display average marks of student.

"""
class student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def display(self):
        return f"Name: {self.name}, Average Marks: {(self.marks1 + self.marks2 + self.marks3) / 3}"

student1 = student("Ali", 80, 90, 70)
print(student1.display())

"""

#  run this code with the help of loop to get sum all marks.
#  and also run this code with the help of loop to get average of all marks.
"""

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
         for val in self.marks:
            sum = 0
            sum += val
         return f"Name: {self.name}, Average Marks: {(sum) / 3}"

student1 = student("Ali", [80, 90, 70])
print(student1.display())

"""

