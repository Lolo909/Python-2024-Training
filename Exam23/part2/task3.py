# Task 3: Create a class Author with attributes name and books. 
# Create another class Book with attributes title and author. 
# Implement a relationship between Author and Book. ????????????????

class Author:
    def __init__(self,name,books):
        self.name = name
        self.books = books
    
    def get_name(self):
        return self.name
    
    def get_books(self):
        return self.books
    
    def set_name(self,new_name):
        self.name = new_name

    def set_books(self,new_books):
        self.books = new_books
    


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def set_title(self,new_title):
        self.title = new_title

    def set_author(self,new_author):
        self.author = new_author

    def __str__(self):
        name = self.author.get_name()
        return f"title: {self.title} - author name: {name}"

author = Author(name="Pesho", books=list())
book = Book(title="Shark", author=author)

listWithBooks = author.get_books()
listWithBooks.append(book)
author.set_books(listWithBooks)

for book in author.get_books():
    print(book)