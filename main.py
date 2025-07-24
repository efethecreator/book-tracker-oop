class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        remaining_books = []
        for i in self.books:
            if i.title != book.title and i.author != book.author:
                remaining_books.append(i)
        self.books = remaining_books

    def search_books(self, search_string):
        matches = []
        search_lower = search_string.lower()
        for book in self.books:
            if search_lower in book.title.lower() or search_lower in book.author.lower():
                matches.append(book)
        return matches