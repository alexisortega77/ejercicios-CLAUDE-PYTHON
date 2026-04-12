"""
Ejercicios extra — Nivel 3
Ejercicio 1 — Fácil
Crea una función celsius_a_fahrenheit que reciba una temperatura en Celsius y devuelva el equivalente en Fahrenheit.
 La fórmula es (celsius * 9/5) + 32. Llámala con 5 temperaturas diferentes e imprime los resultados con 2 decimales.
0°C   →  32.00°F
100°C →  212.00°F
37°C  →  98.60°F
-40°C → -40.00°F
25°C  →  77.00°F
"""
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32      # devuelve número puro

temperaturas = [0, 100, 37, -40, 25]
for temp in temperaturas:
    print(f"{temp}°C → {celsius_a_fahrenheit(temp):.2f}°F")



print(celsius_a_fahrenheit(0))
print(celsius_a_fahrenheit(100))
print(celsius_a_fahrenheit(37))
print(celsius_a_fahrenheit(-40))
print(celsius_a_fahrenheit(25))

"""
Ejercicio 2 — Fácil
Crea una función es_primo que reciba un número y devuelva True si es primo y False si no lo es. Luego imprima todos los números primos del 1 al 50.
Primos del 1 al 50:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

💡 Tip: un número es primo si solo es divisible entre 1 y él mismo. Recorre desde 2 hasta el número y checa si alguno lo divide exacto. Si encuentras uno, 
ya no es primo — usa return False inmediatamente.
"""
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

primos = []
for i in range(1, 51):
    if es_primo(i):
        primos.append(i)

print("Primos del 1 al 50:")
print(", ".join(str(n) for n in primos)) 

"""
Ejercicio 3 — Fácil
Crea una función repetir que reciba un texto y un número, y devuelva el texto repetido esa cantidad de veces separado por espacios.
repetir("hola", 3)   →  "hola hola hola"
repetir("Python", 2) →  "Python Python"
repetir("!", 5)      →  "! ! ! ! !"

💡 Tip: recuerda que puedes multiplicar strings en Python. Busca cómo usar .join() para separar con espacios.
"""
def repetir(texto, numero):
    return " ".join([texto]*numero)

print(repetir("!!!!!",12))

"""
Ejercicio 4 — Medio
Crea dos funciones. perimetro_rectangulo que reciba base y altura y devuelva el perímetro (base + altura) * 2. 
Y area_rectangulo que reciba base y altura y devuelva el área base * altura.
 Luego crea una tercera función describir_rectangulo que llame a las dos anteriores e imprima un reporte completo.
describir_rectangulo(5, 3)

Rectángulo de 5 x 3
Área:      15
Perímetro: 16
"""
def perimetro_rectangulo(base, altura):
    return (base + altura) * 2

def area_rectangulo(base, altura):
    return base * altura

def describir_rectangulo(base, altura):
    area      = area_rectangulo(base, altura)
    perimetro = perimetro_rectangulo(base, altura)

    # Guardas primero en variables, luego imprimes — más fácil de leer y depurar
    print(f"Rectángulo de {base} x {altura}")
    print(f"Área:      {area}")
    print(f"Perímetro: {perimetro}")

describir_rectangulo(5, 3)

"""
Ejercicio 5 — Medio
def clasificar_triangulo(a,b,c):
    if a+b>c and b+c>a and c+a>b:
         if a==b and b==c:
           return "equilatero"
         elif a==b or b==c or c==a:
          return "isosceles"
         else: 
          return "escaleno"
    else:
        return "No es un triangulo valido"
 """

         
 #SOLUCION OPTIMA
def clasificar_triangulo(a, b, c):
    if not (a + b > c and b + c > a and c + a > b):
        return "No es un triángulo válido"

    lados_unicos = len(set([a, b, c]))
    # set elimina duplicados — {3,3,3} tiene 1 elemento, {3,3,5} tiene 2, {3,4,5} tiene 3

    tipos = {1: "Equilátero", 2: "Isósceles", 3: "Escaleno"}
    return tipos[lados_unicos]
print(clasificar_triangulo(3, 3, 3)) 
print(clasificar_triangulo(3, 3, 5)) 
print(clasificar_triangulo(3, 4, 5))  
print(clasificar_triangulo(1, 2, 10))  

"""
Ejercicio 6 — Medio
"""
def adivina_numero(num_secreto, num_intentos):
    print(f"Tienes {num_intentos} intentos para adivinar el número.")

    for i in range(1, num_intentos + 1):
        numero = int(input(f"Intento {i}: "))

        if numero == num_secreto:
            print(f"¡Correcto! Ganaste en {i} intentos.")
            return True
        elif numero < num_secreto:
            print("Muy bajo.")
        else:
            print("Muy alto.")

    print(f"Perdiste. El número era {num_secreto}.")
    return False

adivina_numero(42, 5)   

#SOLUCION OPTIMA
"""
def adivina_numero(num_secreto, num_intentos):
    print(f"Tienes {num_intentos} intentos para adivinar el número.")

    for i in range(1, num_intentos + 1):
        numero = int(input(f"Intento {i}/{num_intentos}: "))

        if numero == num_secreto:
            print(f"¡Correcto! Ganaste en {i} intentos.")
            return True

        pista = "Muy bajo." if numero < num_secreto else "Muy alto."
        print(pista)
    else:
        print(f"Perdiste. El número era {num_secreto}.")
        return False

adivina_numero(42, 5)
"""
"""
Ejercicio 7 — Desafío

"""
def calcular_imc(peso, altura):
    return round(peso/altura**2,2)
def categoria_imc(imc):
    if imc <18.5:
     return "Bajo peso"
    elif imc<25:
        return "Peso normal"
    elif imc<30:
        return "Sobrepeso"
    else:
        return "Obesidad"   
    
def consejo(categoria):
    consejos = {
        "Bajo peso": "Aumenta tu ingesta calórica con alimentos nutritivos.",
        "Peso normal": "Mantén tus hábitos actuales, estás en un rango saludable.",
        "Sobrepeso": "Incorpora más actividad física y reduce alimentos procesados.",
        "Obesidad": "Consulta a un médico para un plan personalizado de salud."
    }
    return consejos.get(categoria, "Categoría no reconocida.") 


def reporte_imc(nombre, peso, altura):
 calculo_imc=calcular_imc(peso,altura)
 categoria=categoria_imc(calculo_imc)
 consejo_imc=consejo(categoria)
 print(f"Nombre: {nombre}")
 print(f"Peso: {peso}")
 print(f"Altura: {altura:.2f}")
 print(f"IMC: {calculo_imc}")
 print(f"Categoria: {categoria}")
 print(f"Consejo: {consejo_imc}")

print(calcular_imc(80,1.70))
print(categoria_imc(calcular_imc(80,1.70)))
print(consejo(categoria_imc(calcular_imc(80,1.70))))
reporte_imc("Manuel", 80,1.70)

"""
Ejercicio 8 — Desafío
"""
def es_palindromo(frase):
    frase=frase.lower().replace(" ", "")
        
    return frase==frase[::-1]
print(es_palindromo("Python"))
print(es_palindromo("Ana"))       
print(es_palindromo("racecar"))
print(es_palindromo("Anita lava la tina"))  
