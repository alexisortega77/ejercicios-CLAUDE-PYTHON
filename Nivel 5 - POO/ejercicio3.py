"""

**Ejercicio 3 — Fácil**
Crea una clase `Student` con nombre y lista de grades. Métodos: `add_grade()`, `average()`, `letter()`, `is_passing()` y `__str__`.
```
s = Student("Ana")
s.add_grade(85)
s.add_grade(92)
s.add_grade(78)
s.average()      → 85.0
s.letter()       → "B"
s.is_passing()   → True
print(s)         → Student: Ana | Average: 85.00 (B)
```
"""

class Student:
    def __init__(self, name):
        self.name   = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def letter(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def is_passing(self):
        return self.average() >= 60

    def __str__(self):
        return f"Student: {self.name} | Average: {self.average():.2f} ({self.letter()})"


s = Student("Ana")
s.add_grade(85)
s.add_grade(92)
s.add_grade(78)
print(s.average())     # 85.0
print(s.letter())      # B
print(s.is_passing())  # True
print(s)               # Student: Ana | Average: 85.00 (B)