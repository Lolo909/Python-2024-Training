# Task 1: Create a Python program that defines a base class Person with attributes name and age. 
# Then, create two subclasses, Student and Teacher, that inherit from the Person class.
#  Add a method introduce to both subclasses that prints a message introducing the person.
#  Create instances of both Student and Teacher and call their introduce methods.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduction():
        pass
    
class Student(Person):
    def introduction(self):
        return f"Hi, I'm student and my name is {self.name} and I'm {self.age} old."
    
        
class Teacher(Person):
    def introduction(self):
        return f"Hi, I'm teacher and my name is {self.name} and I'm {self.age} old."
    
student = Student("Pesho", 13)
teacher = Teacher("Gosho", 31)

print(student.introduction())

print(teacher.introduction())