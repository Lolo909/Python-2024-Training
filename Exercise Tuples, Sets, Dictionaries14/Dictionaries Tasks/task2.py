# Dictionary Manipulation: Create a dictionary representing a simple inventory system for a store.
#  Perform the following operations:
# add items - item and quantity;
# remove items - totally remove item; reduce the quantity;
# check the stock of an item - check the quantity;
# calculate the total value of the inventory - create a new dictionary - item:
#  price and calculate what is the value of the whole inventory


store = {"banana": 999, "apple": 100, "watermelon": 50}

store["carrot"] = 200

store.pop("watermelon")
store["banana"] = store["banana"] - 99

print("The banana quantity is", store["banana"])


priceOfProducts = {"banana": 2.99, "apple":1.99, "carrot":3.99}
totalSum = 0;
for key,value in store.items():
    totalSum += value * priceOfProducts[key]


print(totalSum)

