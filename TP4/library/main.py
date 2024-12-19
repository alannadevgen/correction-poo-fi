from book import Book
from library import Library

# Créer les livres
book1 = Book("Normal People", "Sally Rooney", 2018)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book3 = Book("1984", "George Orwell", 1949)
book4 = Book("Pride and Prejudice", "Jane Austen", 1813)

# Créer la bibliothèque
library = Library("Bibliothèque Colette Vivier", "6 Rue Fourneyron, 75017 Paris")

# Ajouter les livres à la bibliothèque
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# Afficher la liste des livres
library.list_books()

# Supprimer le livre "1984"
library.remove_book(book3)

# Afficher la liste des livres après suppression
library.list_books()

# Afficher les informations du livre "Pride and Prejudice"
print("\nInformations sur 'Pride and Prejudice':")
print(book4)

# Afficher le titre du livre "Normal People"
print("\nTitre du livre 'Normal People':")
print(book1.get_title())
