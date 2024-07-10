# Task 3: Class for Managing a Product Inventory
# Create a Python class called Product that represents a product in an inventory with the following attributes:
# product_id (private): A unique product identifier.
# product_name (public): The name of the product.
# price (protected): The price of the product.
# quantity_in_stock (protected): The quantity of the product in stock.
# Implement the following methods:
# sell(quantity): Decreases the quantity in stock by the specified quantity.
# restock(quantity): Increases the quantity in stock by the specified quantity.
# get_stock_status(): Returns a string indicating the stock status of the product (e.g., "In stock," "Low stock," "Out of stock").
# __str__(): Returns a string representation of the product.
# __lt__(other): Custom comparison based on product name (less than).
# __eq__(other): Custom equality comparison based on product ID.

class Product:
    def __init__(self, product_id, product_name, price, quantity_in_stock):
        self.__product_id = product_id
        self.product_name = product_name
        self._price = price
        self._quantity_in_stock = quantity_in_stock
    
    def get_product_id(self):
        return self.__product_id
    
    def get_product_name(self):
        return self.product_name
    
    def get_price(self):
        return self._price
    
    def get_quantity_in_stock(self):
        return self._quantity_in_stock
    
    def set_product_id(self, new_product_id):
        if new_product_id > 0:
            self.__product_id = new_product_id
        else:
            print("Id can't be zero or negative number!")
        
    def set_product_name(self, new_product_name):
        if len(new_product_name) > 0:
            self.product_name = new_product_name
        else:
            print("Product name can't be nothing!")

    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Price can't be zero or negative number!")
    
    def set_quantity_in_stock(self, new_quantity_in_stock):
        if new_quantity_in_stock > 0:
            self._quantity_in_stock = new_quantity_in_stock
        else:
            print("Quantity can't be zero or negative number!")
    
    def sell(self,quantity):
        self._quantity_in_stock -= quantity
    
    def restock(self,quantity):
        self._quantity_in_stock += quantity
    
    def get_stock_status(self):
        if self._quantity_in_stock == 0:
            return "Out of stock"
        elif self._quantity_in_stock <= 50:
            return "Low stock"
        else:
            return "In stock"

    def __str__(self):
        return f"Product name: {self.get_product_name()}, Price: {self.get_price()} ,Quantity: {self.get_quantity_in_stock()}"

    def __lt__(self, other):
        return self.product_name < other.product_name
    
    def __eq__(self, other):   
        return self.__product_id == other.__product_id

# self, product_id, product_name, price, quantity_in_stock
product = Product("1", "Banana", 3.5, 50)

print(product.get_product_name())
print(product.get_price())
print(product.get_quantity_in_stock())

print(product)
print("-------------")
products = [
    Product("1", "Banana", 3.5, 50),
    Product("2", "Melon", 0.5, 25),
    Product("3", "Potato", 2.5, 100),
    Product("4", "Cherry", 1.5, 0),
    Product("1", "Banana", 3.5, 50)
]

orderedProducts = sorted(products)

for product in orderedProducts:
    print(product)