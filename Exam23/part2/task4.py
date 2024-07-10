# Task 4: Create two classes, Parent1 and Parent2, each with a method called show_info.
#  Create a subclass Child that inherits from both Parent1 and Parent2. 
# Override the show_info method in Child to call both parent methods.
#  Create an instance of Child and call its show_info method.

class Parent1:
    def show_info():
        return "parent 1 info"


class Parent2:
    def show_info():
        return "parent 2 info"

class Child(Parent1, Parent2):

    def show_info(self):
        return Parent1.show_info() + " / " + Parent2.show_info()

child = Child()
temp = child.show_info()
print(child.show_info())