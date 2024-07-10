# Task 2: Class for Managing a Library Catalog
# Create a Python class called Book that represents a book with the following attributes:
# title (public): The title of the book.
# author (public): The author of the book.
# isbn (private): The ISBN (International Standard Book Number) of the book.
# Implement a method __str__() that returns a string representation of the book.
# Implement methods for custom comparisons (__lt__, __eq__) based on the title and author.


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_isbn(self):
        return self.__isbn
    
    def set_title(self, new_title):
        if len(new_title) > 0:
            self.title = new_title
        else:
            print("Title's name can't be nothing!")

    def set_author(self, new_author):
        if len(new_author) > 0:
            self.author = new_author
        else:
            print("Author's name can't be nothing!")

    def set_isbn(self, new_isbn):
        if len(new_isbn) == 13:
            self.__isbn = new_isbn
        else:
            print("ISBN must be 13 digits long!")

    def __str__(self):
        return f"Title: {str(self.get_title())}, Author: {self.get_author()}"
    
    def __lt__(self, other):
        if self.title != other.title:
            return self.title < other.title
        else:
            return self.author < other.author
        
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book = Book("Shark", "Pesho", 1234567890123)

print(book.get_author())
print(book.get_title())
print(book.get_isbn())

print(book)
print("-------------")
books = [
    Book("Shark2", "Pesho", 1234567890123),
    Book("Shark1", "Pesho", 1234567890123),
    Book("Shrek", "Tosh", 1234567890123),
    Book("Shrek", "Anna", 1234567890123),
    Book("Zzz", "Mitka", 1234567890123),
]

sortedBooks = sorted(books)

for book in sortedBooks:
    print(book)

