"""
Ejercicio 6 — Medio
Crea una jerarquía de empleados. Clase base Employee con nombre, id y salario base.
 Clases hijas: FullTime (con bono anual), PartTime (con horas trabajadas y tarifa por hora) 
 y Contractor (con tarifa diaria y días trabajados). Cada uno calcula su pago mensual diferente.
e1 = FullTime("Ana", "E001", 25000, annual_bonus=5000)
e2 = PartTime("Luis", "E002", hours=120, rate=150)
e3 = Contractor("María", "E003", daily_rate=800, days=22)

e1.monthly_pay()  → 25416.67  (salario + bono/12)
e2.monthly_pay()  → 18000     (horas * tarifa)
e3.monthly_pay()  → 17600     (días * tarifa)

print(e1)  → FullTime: Ana | Monthly: $25416.67
print(e2)  → PartTime: Luis | Monthly: $18000.00
print(e3)  → Contractor: María | Monthly: $17600.00

"""
class Employe:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class FullTime(Employe):
    def __init__(self, name, id, salary_base,annual_bonus):
        super().__init__(name, id)
        self.salary_base = salary_base
        self.annual_bonus = annual_bonus
    def monthly_pay(self):
        
        return round(self.salary_base + self.annual_bonus/12,2)
    def __str__(self):
        return f"Fulltime: {self.name} | Monthly: ${self.monthly_pay():}"
    
class PartTime(Employe):
    def __init__(self, name, id, hours,rate):
        super().__init__(name, id)
        self.hours = hours
        self.rate = rate
    def monthly_pay(self):
        return  self.hours * self.rate
    def __str__(self):
        return f"PartTime: {self.name} | Monthly: ${self.monthly_pay()}"
 
class Contractor(Employe):
    def __init__(self, name, id,daily_rate,days):
        super().__init__(name, id)
        self.daily_rate = daily_rate
        self.days = days
    def monthly_pay(self):
        return self.daily_rate * self.days
    def __str__(self):
        return f"Contractor: {self.name} | Monthly: ${self.monthly_pay()}"

e1 = FullTime("Ana", "E001", 25000, annual_bonus=5000)
e2 = PartTime("Luis", "E002", hours=120, rate=150)
e3 = Contractor("María", "E003", daily_rate=800, days=22)
print(e1.monthly_pay())
print(e2.monthly_pay())
print(e3.monthly_pay())
print(e1)        
print(e2)  
print(e3)  

#FORMA MEJOR DE HACERLO SIN REPETIR STR POR CADA HIJO
"""
class Employee:
    def __init__(self, name, emp_id):
        self.name   = name
        self.emp_id = emp_id

    def monthly_pay(self):
        raise NotImplementedError("Subclasses must implement monthly_pay()")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} | Monthly: ${self.monthly_pay():.2f}"


class FullTime(Employee):
    def __init__(self, name, emp_id, salary_base, annual_bonus):
        super().__init__(name, emp_id)
        self.salary_base  = salary_base
        self.annual_bonus = annual_bonus

    def monthly_pay(self):
        return round(self.salary_base + self.annual_bonus / 12, 2)


class PartTime(Employee):
    def __init__(self, name, emp_id, hours, rate):
        super().__init__(name, emp_id)
        self.hours = hours
        self.rate  = rate

    def monthly_pay(self):
        return self.hours * self.rate


class Contractor(Employee):
    def __init__(self, name, emp_id, daily_rate, days):
        super().__init__(name, emp_id)
        self.daily_rate = daily_rate
        self.days       = days

    def monthly_pay(self):
        return self.daily_rate * self.days


e1 = FullTime("Ana",   "E001", 25000, annual_bonus=5000)
e2 = PartTime("Luis",  "E002", hours=120, rate=150)
e3 = Contractor("María", "E003", daily_rate=800, days=22)

print(e1.monthly_pay())   # 25416.67
print(e2.monthly_pay())   # 18000
print(e3.monthly_pay())   # 17600
print(e1)                 # FullTime: Ana | Monthly: $25416.67
print(e2)                 # PartTime: Luis | Monthly: $18000.00
print(e3)                 # Contractor: María | Monthly: $17600.00
"""
        
        