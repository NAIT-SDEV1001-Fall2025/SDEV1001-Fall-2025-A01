class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return f"{self.name}"
    
    # allows users to add books to our library
    def add_book(self, book):
        self.books.append(book)

    # allows users to list all the books in our library
    def list_books(self):
        print("Current books in our library:")
        if len(self.books) == 0:
            print("No books in our library")
        for book in self.books:
            print(F"- {book}")
