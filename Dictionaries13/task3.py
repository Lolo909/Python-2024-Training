# Task 3: Create a nested dictionary that represents a catalog of products in an online store.
#  Each product should have attributes like name, price, and description. Perform the following operations:
# Add multiple products to the catalog.
# Retrieve and print the details of a specific product.
# Update the price of one of the products.
# Remove a product from the catalog.


catalog = {   
    "product": {
        "name": "banana",
        "price": 2.99,
        "description": "yummy"
    },

    "product2": {
        "name": "apple",
        "price": 1.99,
        "description": "yummy"
    },
    
    "product3": {
        "name": "watermelon",
        "price": 0.99,
        "description": "juicy"
    }
}

print(catalog["product"])
print("------------------------")
catalog["product2"]["price"] = 1.50
print(catalog["product2"])

print("------------------------")
catalog.pop("product3")

print(catalog)
