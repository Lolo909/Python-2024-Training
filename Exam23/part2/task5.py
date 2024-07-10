# Task 5: Create a Python class called Book with attributes title, author, and ISBN. 
# Implement a class Library with a dictionary to store books. 
# Add methods to add books to the library and search for books by title or author.

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    
    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_author(self):
        return self.author
    
    def set_author(self, new_author):
        self.author = new_author
    
    def get_ISBN(self):
        return self.ISBN
    
    def __str__(self):
        return f"Title: {str(self.get_title())}, Author: {self.get_author()}"
    
class Library:
    def __init__(self, books):
        self.books = books
    
    def add_book(self,new_book):
        listWithBooks = self.books
        listWithBooks.append(new_book)
        self.books = listWithBooks

    def find_book_by_title(self, title_to_search):
        for book in self.books:
            if book.get_title() == title_to_search:
                return book
        else:
            return "Book not found! With this title!"
        
    def find_book_by_author(self, author_to_search):
        isAnyBookfound = False
        listWithBooks = []
        for book in self.books:
            if book.get_author() == author_to_search:
                isAnyBookfound = True
                listWithBooks.append(book)
                            
        if not isAnyBookfound:
            listWithBooks.append("Books not found! With this author!")

        return listWithBooks
        
    
book1 = Book("Shark", "Pesho", 1234567890)
book2 = Book("Shark2", "Pesho", 2234567890)
book3 = Book("Zzz", "Minka", 3234567890)
library = Library([book1, book2, book3])

book4 = Book("NEWBOOK", "NEWAUTHOR", 4234567890)
library.add_book(book4)

print(library.find_book_by_title("Shark"))
print(library.find_book_by_title("NEWBOOK"))
print(library.find_book_by_title("NOTHING"))

print("------------")
for book in library.find_book_by_author("Pesho"):
    print(book)
print("------------")
for book in library.find_book_by_author("NOONE"):
    print(book)

