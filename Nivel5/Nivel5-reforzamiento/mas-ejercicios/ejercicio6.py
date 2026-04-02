"""
Ejercicio 6 — Medio
Crea una jerarquía de empleados. Clase base Employee con nombre, id y salario base. Clases hijas: FullTime (con bono anual), PartTime (con horas trabajadas y tarifa por hora) y Contractor (con tarifa diaria y días trabajados). Cada uno calcula su pago mensual diferente.
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