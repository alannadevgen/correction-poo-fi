class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' de {self.author}, paru en {self.year}"

    def get_title(self):
        return self.title
