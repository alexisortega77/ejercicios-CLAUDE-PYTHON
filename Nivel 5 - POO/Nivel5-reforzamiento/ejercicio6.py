"""
Ejercicio 6 — Medio
Crea una clase Matrix que represente una matriz 2x2. Métodos: add(other), multiply(other), transpose(), determinant() y __str__.
m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[5,6],[7,8]])

m1.add(m2)
→ [[6, 8], [10, 12]]

m1.multiply(m2)
→ [[19, 22], [43, 50]]

m1.transpose()
→ [[1, 3], [2, 4]]

m1.determinant()
→ -2

💡 Determinante de 2x2: (a*d) - (b*c) donde la matriz es [[a,b],[c,d]]

"""
class Matrix:
    def __init__(self, data):
        self.data = data

    def add(self, other):
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matrix(result)

    def multiply(self, other):
        a, b = self.data, other.data
        result = [
            [
                a[0][0]*b[0][0] + a[0][1]*b[1][0],
                a[0][0]*b[0][1] + a[0][1]*b[1][1]
            ],
            [
                a[1][0]*b[0][0] + a[1][1]*b[1][0],
                a[1][0]*b[0][1] + a[1][1]*b[1][1]
            ]
        ]
        return Matrix(result)

    def transpose(self):
        return Matrix([
            [self.data[0][0], self.data[1][0]],
            [self.data[0][1], self.data[1][1]]
        ])

    def determinant(self):
        a, b = self.data[0]
        c, d = self.data[1]
        return a*d - b*c

    def __str__(self):
        return "\n".join(f"  {row}" for row in self.data)


m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[5,6],[7,8]])

print("Suma:")
print(m1.add(m2))

print("Multiplicación:")
print(m1.multiply(m2))

print("Transpuesta:")
print(m1.transpose())

print("Determinante:", m1.determinant())
"""
class Matrix:
    def __init__(self, data):
        self.data = data

    def add(self, other):
        # list comprehension anidado — recorre filas y columnas
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(2)]
            for i in range(2)
        ])
# Para cada fila i y columna j del resultado:
#a[i][0]*b[0][j] + a[i][1]*b[1][j]

# i=0, j=0: a[0][0]*b[0][0] + a[0][1]*b[1][0] = 1*5 + 2*7 = 19
# i=0, j=1: a[0][0]*b[0][1] + a[0][1]*b[1][1] = 1*6 + 2*8 = 22
# i=1, j=0: a[1][0]*b[0][0] + a[1][1]*b[1][0] = 3*5 + 4*7 = 43
# i=1, j=1: a[1][0]*b[0][1] + a[1][1]*b[1][1] = 3*6 + 4*8 = 50
        
    def multiply(self, other):
        a, b = self.data, other.data
        # fórmula de multiplicación de matrices 2x2
        return Matrix([
            [a[i][0]*b[0][j] + a[i][1]*b[1][j] for j in range(2)]
            for i in range(2)
        ])

    def transpose(self):
        # intercambia filas por columnas
        return Matrix([
            [self.data[j][i] for j in range(2)]
            for i in range(2)
        ])

    def determinant(self):
        a, b = self.data[0]
        c, d = self.data[1]
        return a*d - b*c

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return "\n".join(f"  {row}" for row in self.data)


"""
