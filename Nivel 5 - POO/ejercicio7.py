"""

**Ejercicio 7 — Desafío**
Crea un sistema de biblioteca con clases `Book`, `User` y `Library`. 
`Library` gestiona préstamos y devoluciones. 
Implementa historial de préstamos por usuario.
```
lib  = Library()
book = Book("El principito", "Saint-Exupéry", "978-0")
user = User("Manuel", "USR001")

lib.add_book(book)
lib.borrow(user, "978-0")    → "El principito borrowed by Manuel."
lib.borrow(user, "978-0")    → "El principito is not available."
lib.return_book(user, "978-0") → "El principito returned by Manuel."
lib.user_history(user)
→ Manuel's history:
  - El principito: borrowed and returned
```
"""
class Book:
    def __init__(self, title, author, isbn):
        self.title     = title
        self.author    = author
        self.isbn      = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} | {status}"


class User:
    def __init__(self, name, user_id):
        self.name    = name
        self.user_id = user_id
        self.history = []

    def __str__(self):
        return f"User: {self.name} | ID: {self.user_id}"


class Library:
    def __init__(self):
        self._books = {}
        self._users = {}

    def add_book(self, book):
        self._books[book.isbn] = book
        return f"'{book.title}' added to library."

    def add_user(self, user):
        self._users[user.user_id] = user
        return f"User '{user.name}' registered."

    def borrow(self, user, isbn):
        book = self._books.get(isbn)
        if not book:
            return "Book not found."
        if not book.available:
            return f"{book.title} is not available."
        book.available = False
        user.history.append((book.title, "borrowed"))
        return f"{book.title} borrowed by {user.name}."

    def return_book(self, user, isbn):
        book = self._books.get(isbn)
        if not book:
            return "Book not found."
        if book.available:
            return f"{book.title} was not borrowed."
        book.available = True
        user.history.append((book.title, "returned"))
        return f"{book.title} returned by {user.name}."

    def user_history(self, user):
        print(f"{user.name}'s history:")
        if not user.history:
            print("  No activity yet.")
            return
        for title, action in user.history:
            print(f"  - {title}: {action}")


lib  = Library()
book = Book("El principito", "Saint-Exupéry", "978-0")
user = User("Manuel", "USR001")

print(lib.add_book(book))
print(lib.borrow(user, "978-0"))      # El principito borrowed by Manuel.
print(lib.borrow(user, "978-0"))      # El principito is not available.
print(lib.return_book(user, "978-0")) # El principito returned by Manuel.
lib.user_history(user)