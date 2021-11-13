class TooManyPageReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __repr__(self):
        return (
            f"<repr> Book {self.name}: read {self.page_read} "
            f"pages out of {self.page_count}"
        )

    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise TooManyPageReadError(
                f"You tried to read {self.page_read+pages} pages"
                f"but this book has only {self.page_count} pages!"
            )
        self.page_read += pages
        print(f"now you have read {self.page_read}"
              f" pages out of {self.page_count}")

python101 = Book("Python101", 50)
print(python101)
try:
    python101.read(35)
    python101.read(50)
except TooManyPageReadError as e:
    print(e)

