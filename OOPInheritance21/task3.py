# Task 3: Write a Python program that defines a custom exception called OutOfStockError. This exception should be raised when a user tries to purchase an item that is out of stock. Additionally, modify the program to check for negative quantities when making a purchase.
# HELP
# OutOfStockError Exception Class:
# This is a custom exception class that inherits from the built-in Exception class. It's used to handle situations where a user tries to purchase an item that is out of stock
# In the constructor __init__, it takes three parameters: item_name (the name of the item), requested_quantity (the quantity the user requested), and available_quantity (the quantity available in stock).
# The constructor calls the parent class constructor with a custom error message that indicates the item name and available quantity.
# NegativeQuantityError Exception Class:
# This is another custom exception class that inherits from Exception. It's used to handle situations where a user tries to purchase an item with a negative quantity, which is not allowed.
# In the constructor __init__, it takes two parameters: item_name (the name of the item) and quantity (the negative quantity requested).
# The constructor calls the parent class constructor with a custom error message indicating the item name and the invalid negative quantity.
# Store Class:
# This class represents a store and its available items. 
# It has an instance variable available_items, which is a dictionary storing item names as keys and their quantities as values.
# add_item(self, item_name, quantity) Method:
# This method allows adding items to the store's inventory.
# It takes two parameters: item_name (the name of the item) and quantity (the quantity of the item to add).
# It adds the item and its quantity to the available_items dictionary.
# purchase_item(self, item_name, quantity) Method:
# This method allows a user to purchase a certain quantity of an item.
# It takes two parameters: item_name (the name of the item to purchase) and quantity (the quantity the user wants to purchase).
# It first checks if the quantity parameter is negative. If it's negative, it raises a NegativeQuantityError exception with a user-friendly error message.
# If the item is in stock (i.e., item_name is in available_items), it checks if the requested quantity is available. If not, it raises an OutOfStockError exception with a user-friendly error message.
# If both checks pass, it deducts the purchased quantity from the available quantity and prints a success message.
# Using the Classes:
# In the code that follows the class definitions, we create an instance of the Store class (my_store) and add some items to its inventory using the add_item method.
# We then attempt to purchase items with various quantities, including valid and invalid cases (out of stock and negative quantity), and handle the exceptions raised with appropriate error messages.


class OutOfStockError(Exception):
    def __init__(self, message, item_name, requested_quantity, available_quantity):
        super().__init__(message)
        self.item_name = item_name
        self.requested_quantity = requested_quantity
        self.available_quantity = available_quantity
    
    def get_item_name(self):
        return self.item_name

    def error_message(self):
        return f"{self.item_name} has only {self.available_quantity} left. You wanted {self.requested_quantity}."

class NegativeQuantityError(Exception):
    def __init__(self, message, item_name, quantity):
        super().__init__(message)
        self.item_name = item_name
        self.quantity = quantity

    def get_item_name(self):
        return self.item_name
    
    def get_quantity(self):
        return self.quantity

    def error_message(self):
        return f"{self.item_name}'s quantity can't be negative: {self.quantity}."


class Store:
    def __init__(self, name, address, available_items):
        self.name = name
        self.address = address
        self.available_items = available_items


    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_available_items(self):
        return self.available_items
    
    def set_name(self, new_name):
        if len(new_name) > 0:
            self.name = new_name
        else:
            print("Name can't be nothing!")

    def set_address(self, new_address):
        if len(new_address) > 0:
            self.address = new_address
        else:
            print("Address can't be nothing!")
        
    def set_available_items(self, new_available_items):
        self.available_items = new_available_items
    
    def add_item(self, item_name, quantity):
            if quantity < 0:                
                raise NegativeQuantityError("Error:", item_name, quantity)
            else:
                items = {}
                items = self.get_available_items()
                items[item_name] = quantity
                print("You added successfully!")
    
    def purchase_item(self, item_name, quantity):
            if quantity < 0:
                raise NegativeQuantityError("Error:", item_name, quantity)
            elif quantity > self.available_items[item_name]:
                raise OutOfStockError("Error:", item_name, quantity, self.available_items[item_name])
            else:
                result = self.available_items[item_name] - quantity
                self.available_items[item_name] = result
                print("You purchased successfully!")


store = Store("StarMarket", "Somewhere 105", {"banana":30, "potato":200, "carrot":150})
try:
    store.add_item("cherry", -2)
except NegativeQuantityError:
     error = NegativeQuantityError("Error:", "cherry", -2)
     print(NegativeQuantityError.error_message(self=error))

store.add_item("cherry", 2)

try:
    store.purchase_item("cherry", -3)
except NegativeQuantityError:
    error = NegativeQuantityError("Error:", "cherry", -3)
    print(NegativeQuantityError.error_message(self=error))

try:
    store.purchase_item("cherry", 3)
except OutOfStockError:
     error = OutOfStockError("Error:","cherry", 3, store.available_items["cherry"])
     print(OutOfStockError.error_message(self=error))

for key,value in store.available_items.items():
    print(key,value)

store.purchase_item("cherry", 2)

for key,value in store.available_items.items():
    print(key,value)
