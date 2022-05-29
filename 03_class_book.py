class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book_1 = Book("Steve Jobs", "me", 22)
print(book_1.name)