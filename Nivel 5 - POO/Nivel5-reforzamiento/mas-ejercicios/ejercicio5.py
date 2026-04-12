"""

Ejercicio 5 — Medio
Crea una clase Fraction que represente una fracción. 
Métodos: add(other), multiply(other), simplify() y __str__. 
Al mostrar la fracción siempre debe estar simplificada.
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

f1.add(f2)       → Fraction(5, 6)
f1.multiply(f2)  → Fraction(1, 6)
print(f1)        → 1/2
print(Fraction(4, 8))  → 1/2  (simplificada automáticamente)

💡 Para simplificar necesitas el MCD (Máximo Común Divisor).
 Puedes calcularlo con el algoritmo de Euclides: mcd(a,b) = mcd(b, a%b) hasta que b=0.
"""


# ── Fraction ──────────────────────────────────
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator   = numerator
        self.denominator = denominator

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def add(self, other):
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den).simplify()

    def multiply(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator).simplify()

    def __str__(self):
        s = self.simplify()
        return f"{s.numerator}/{s.denominator}"


        
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1.add(f2) )  # → Fraction(5, 6)
print(f1.multiply(f2))
print(Fraction(4, 8))