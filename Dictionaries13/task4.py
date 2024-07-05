# Task 4: Given two dictionaries, find the common key-value pairs between them. For example, 
# if you have dictionaries representing two people's favorite foods, find the foods they both like.
# # Example dictionaries of favorite foods
# person1_favorites = {
#     "fruit": "apple",
#     "dessert": "chocolate",
#     "drink": "coffee"
# }

# person2_favorites = {
#     "dessert": "chocolate",
#     "drink": "tea",
#     "snack": "chips"
# }


person1_favorites = {
    "fruit": "apple",
    "dessert": "chocolate",
    "drink": "coffee"
}

person2_favorites = {
    "dessert": "chocolate",
    "drink": "tea",
    "snack": "chips"
}

listWithCommonKeys = []

for key,value in person1_favorites.items():
    if key in person2_favorites:
        listWithCommonKeys.append(key)
print("List with commons keys:")
print(listWithCommonKeys)
print("--------------------")
listWithFoodTheyBothLike = []

for key in listWithCommonKeys:
    if person1_favorites[key] == person2_favorites[key]:
        listWithFoodTheyBothLike.append(person1_favorites[key])

print("List with food they bth like:")
print(listWithFoodTheyBothLike)