"""

**Ejercicio 7 — Desafío**
Crea un sistema de biblioteca con clases `Book`, `User` y `Library`. `Library` gestiona préstamos y devoluciones. Implementa historial de préstamos por usuario.
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