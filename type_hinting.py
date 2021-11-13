from typing import List  # Tuple, Set etc


# type hinting -> return type
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

# uncomment to test
#print(list_avg([1, 2, 3]))  # if int is passed python will suggest correction


class Book:
    TYPES = ("hardcover", "paperback")

    # example type hinting
    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<repr>Book {self.name}, {self.book_type}, weighing: {self.weight}g, "

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        """
        :rtype: object
        """
        return Book(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return Book(name, cls.TYPES[1], page_weight+100)


class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)}"

book1 = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
print(book1)
print(light)