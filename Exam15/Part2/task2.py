
# Task 2: Create a Python dictionary representing a shopping cart with items and their prices.
# Add the following items to the cart:
# Item: "Apples", Price: 1.99
# Item: "Bananas", Price: 0.99
# Item: "Chocolates", Price: 2.49
# Calculate and print the total cost of the items in the shopping cart.

shopping_cart = {
    "Apples": 1.99,
    "Banana":0.99,
    "Chocolate":2.49
}

sum =0;
for key,value in shopping_cart.items():
    sum += value;

print("{:.2f}".format(sum))
