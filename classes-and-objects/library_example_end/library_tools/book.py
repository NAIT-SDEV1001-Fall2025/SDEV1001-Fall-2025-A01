class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # representation of our object when
    # we print it out in a string.
    def __str__(self):
        return f"{self.title} by {self.author}"
