# Task 1: Implement an Abstract Base Class for Animals
# Define an abstract base class called Animal using the abc module. Declare abstract 
# methods speak and move in the Animal class. Create two concrete subclasses, Dog and Fish, that inherit from Animal. 
# Implement the speak and move methods in both Dog and Fish with appropriate behavior.
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def speak(self):
        return "Woof woof!!!"
    
    def move(self):
        return "walk"

class Fish(Animal):
    def speak(self):
        return "Buble buble o O"
     
    def move(self):
        return "swim"

dog = Dog()
print(dog.speak())
print(dog.move())

fish = Fish()
print(fish.speak())
print(fish.move())