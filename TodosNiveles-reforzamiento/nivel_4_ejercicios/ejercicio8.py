datos_empleados = """Ana,Sistemas,25000
Luis,Ventas,18000
María,Sistemas,28000
Carlos,RRHH,20000
Pedro,Ventas,22000
Laura,Sistemas,30000
Jorge,RRHH,19000
Sofia,Ventas,21000"""

# Parsear datos
employees = []
for line in datos_empleados.strip().split("\n"):
    parts = line.split(",")
    employees.append({
        "name":       parts[0],
        "department": parts[1],
        "salary":     int(parts[2])
    })

# Agrupar por departamento
by_department = {}
for emp in employees:
    dept = emp["department"]
    if dept not in by_department:
        by_department[dept] = []
    by_department[dept].append(emp)

# Estadísticas globales
highest_paid  = max(employees, key=lambda e: e["salary"])
lowest_paid   = min(employees, key=lambda e: e["salary"])
total_payroll = sum(e["salary"] for e in employees)

# Reporte
print(f"Total empleados: {len(employees)}")
print("\nPor departamento:")
for dept, members in by_department.items():
    avg = sum(e["salary"] for e in members) / len(members)
    print(f"  {dept:<10}: {len(members)} empleados | Salario promedio: ${avg:.2f}")

print(f"\nEmpleado mejor pagado:  {highest_paid['name']} ({highest_paid['department']}) - ${highest_paid['salary']}")
print(f"Empleado menor salario: {lowest_paid['name']} ({lowest_paid['department']}) - ${lowest_paid['salary']}")
print(f"Masa salarial total:    ${total_payroll}")