"""
Ejercicio 6 — Medio
Crea una clase Calculator con historial de operaciones. Lanza excepciones específicas para cada tipo de error.
calc = Calculator()
calc.divide(10, 2)         → 5.0
calc.divide(10, 0)         → DivisionByZeroError: Cannot divide by zero
calc.sqrt(-4)              → NegativeNumberError: Cannot take square root of negative number
calc.log(0)                → InvalidInputError: Cannot take log of zero or negative
calc.history()
→ Operation
"""
class DivisionByZeroError(Exception):
    pass
class NegativeNumberError(Exception):
    pass
class InvalidInputError(Exception):
    pass
class Calculator:
    def __init__(self):
        self.op_history = []
    def divide(self, num_a, num_b):
        if num_b==0:
            raise DivisionByZeroError("Cannot divide by zero")
        result = num_a/num_b
        self.op_history.append({
            "type":"divide",
            "number_a":num_a,
            "number_b":num_b,
            "result":result
        })
        return result
    def sqrt(self, num_a):
        if num_a<0:
            raise NegativeNumberError ("Cannot take square root of negative number")
        result = num_a**0.5
        self.op_history.append({
            "type":"sqrt",
            "number_a":num_a,
            "result":result
        })
        return result
    def log(self,num_a):
        import math
        if num_a <= 0:
            raise InvalidInputError("Cannot take log of zero or negative")
        result = math.log(num_a)
        self.op_history.append({
            "type": "log",
            "number_a": num_a,
            "result": result
        })
        return result
    def history(self):
     for i, op in enumerate(self.op_history, 1):
        if op["type"] == "divide":
            print(f"{i}. divide({op['number_a']}, {op['number_b']}) = {op['result']}")
        
        elif op["type"] == "sqrt":
            print(f"{i}. sqrt({op['number_a']}) = {op['result']}")
        
        elif op["type"] == "log":
            print(f"{i}. log({op['number_a']}) = {op['result']}")
   
calc = Calculator()
calc.log(2)
calc.sqrt(2)

try:
    calc.divide(10, 2)
except DivisionByZeroError as e:
    print(f"DivisionByZeroError: {e}")

try:
    calc.divide(10, 0)
except DivisionByZeroError as e:
    print(f"DivisionByZeroError: {e}")

try:
    calc.sqrt(-4)
except NegativeNumberError as e:
    print(f"NegativeNumberError: {e}")

try:
    calc.log(0)
except InvalidInputError as e:
    print(f"InvalidInputError: {e}")

calc.history()