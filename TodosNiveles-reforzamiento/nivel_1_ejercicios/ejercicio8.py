# ------------------------------------------------------------
# EJERCICIO 8 — Desafío
# Pide un número de 4 dígitos y muestra cada dígito por separado
# y la suma de todos los dígitos.
# Pista: usa operaciones de división y módulo, no strings.
# ------------------------------------------------------------
# Input del usuario: 1234
# Output esperado:
# Número: 1234
# Millares: 1
# Centenas: 2
# Decenas:  3
# Unidades: 4
# Suma de dígitos: 10

numero=int(input("Ingresa numero de 4 digitos: "))

millares = numero // 1000
# Obtener centenas (resto de millares, dividido por 100)
centenas = (numero % 1000) // 100
# Obtener decenas (resto de centenas, dividido por 10)
decenas = (numero % 100) // 10
# Obtener unidades (resto de decenas)
unidades = numero % 10
suma = sum(int(digito) for digito in str(numero))
print(suma)  # Resultado: 18


print(f"Numero: {numero}")
print(f"millares: {millares}")
print(f"centenas: {centenas}")
print(f"decenas: {decenas}")
print(f"unidades: {unidades}")
print(f"suma de digitos: {suma}")