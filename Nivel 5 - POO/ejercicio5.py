"""

**Ejercicio 5 — Medio**
Crea una clase `Stack` que implemente la estructura LIFO. Métodos: `push()`, `pop()`, `peek()`, `is_empty()`, `size()` y `__str__`.
```
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.peek()       → 3
s.pop()        → 3
s.size()       → 2
s.is_empty()   → False
print(s)       → Stack: [1, 2] | Top: 2
```

"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        if self.is_empty():
            return "Stack: [] | Empty"
        return f"Stack: {self._items} | Top: {self.peek()}"


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())      # 3
print(s.pop())       # 3
print(s.size())      # 2
print(s.is_empty())  # False
print(s)             # Stack: [1, 2] | Top: 2