"""
Ejercicio 3 — Fácil
Crea una función read_positive_number(prompt) que siga pidiendo hasta obtener un número positivo mayor que cero.
Enter a number: -5
Error: must be greater than zero.
Enter a number: abc
Error: must be a valid number.
Enter a number: 0
Error: must be greater than zero.
Enter a number: 7.5
→ 7.5
"""
def read_positive_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                print(number)
                return number
            print("Error: must be greater than zero.")
        except ValueError:
            print("Error: must be a valid number.")

     
        
read_positive_number("Enter a number: ")