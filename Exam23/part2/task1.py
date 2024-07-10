# Task 1: Create a base class Vehicle with attributes make and model. 
# Create a subclass Car that inherits from Vehicle and adds an attribute year.
#  Create an instance of the Car class and print its make, model, and year.

class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def set_make(self,new_make):
        self.make = new_make
    
    def set_model(self,new_model):
        self.model = new_model

class Car(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model)
        self.year = year

    def get_year(self):
        return self.year
    def set_year(self,new_year):
        self.year = new_year
    
    def __str__(self):
        return f"Make: {self.get_make()}, Model: {self.get_model()}, Year: {self.get_year()}"

car = Car("None", "None", 1000)
car.set_make("Pesho made this car")
car.set_model("CoolModel")
car.set_year(2024)

print(car.get_make())
print(car.get_model())
print(car.get_year())

print(car)

    
