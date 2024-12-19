from book import Book


class Library:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"The book '{self.name}' is not in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print(f"Books in the library '{self.name}':")
            for book in self.books:
                print(f" - {book}")
