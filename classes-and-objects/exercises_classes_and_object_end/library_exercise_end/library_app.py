from library_tools.library import Library
from library_tools.book import Book

if __name__ == '__main__':
    print("Welcome to our library App")
    print("--------------------------")
    # create a library
    library = Library("Edmonton Public Library")
    print(library)
    # let's call the list books to observe that we have no books
    library.list_books()

    # a few books
    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000)
    bookTwo = Book("The Wheel of Time", "Robert Jordan", 690)
    bookThree = Book("The Way of Kings", "Brandon Sanderson", 1200)
    bookFour = Book("Mistborn", "Brandon Sanderson", 640)

    # add the books to our library
    library.add_book(book)
    library.add_book(bookTwo)
    library.add_book(bookThree)
    library.add_book(bookFour)
    
    # let's call the list books to see that we have one book!
    library.list_books()

    library.checkout_book(book)

    library.list_books()