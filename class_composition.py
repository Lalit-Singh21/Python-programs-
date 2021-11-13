class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"<>Bookshelf with {len(self.books)} books."

#class Bookshelf instance
# shelf = Bookshelf(300)
# print(shelf)

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book : {self.name}"





if __name__ == "__main__":
    # class Book instance
    book = Book("Harry Potter")
    book2 = Book("Python 101")
    # print(book, book2)

    # composition
    shelf = Bookshelf(book, book2)
    print(shelf)
    print(shelf.books[0])