# Task 1: Create a Python dictionary representing a book with attributes like title, author, publication year, and genre. Perform the following operations:
# Create the dictionary.
# Print the dictionary.
# Add a new key-value pair to represent the number of pages.
# Update the author's name.
# Remove the publication year.
# Check if the genre exists in the dictionary.
# Print all the keys and values in the dictionary.




book = {
    "title": "The blue whale",
    "author": "Pesho",
    "year": 1999,
    "genre": "horor"
}

print(book)

book["pages"] = 2000
book["author"] = "Gosho"
book.pop("year")

print("genre" in book)

for key, value in book.items():
    print(key + " - " +str(value))
