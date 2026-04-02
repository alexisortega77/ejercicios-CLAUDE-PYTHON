"""

Ejercicio 5 — Medio
Crea una clase Fraction que represente una fracción. Métodos: add(other), multiply(other), simplify() y __str__. Al mostrar la fracción siempre debe estar simplificada.
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

f1.add(f2)       → Fraction(5, 6)
f1.multiply(f2)  → Fraction(1, 6)
print(f1)        → 1/2
print(Fraction(4, 8))  → 1/2  (simplificada automáticamente)

💡 Para simplificar necesitas el MCD (Máximo Común Divisor). Puedes calcularlo con el algoritmo de Euclides: mcd(a,b) = mcd(b, a%b) hasta que b=0.


"""