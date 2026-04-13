"""
Ejercicio 5 — Medio
Lee el siguiente CSV y genera un reporte en consola y guárdalo en un archivo .txt.
python# El CSV tiene este formato:
# name,department,salary
# Ana,Sistemas,25000
# Luis,Ventas,18000
# ...
# reporte.txt:
Total employees: 8
Average salary: $22875.00

By department:
  Sistemas: 3 employees | Avg: $27666.67
  Ventas:   3 employees | Avg: $20333.33
  RRHH:     2 employees | Avg: $19500.00

Highest paid: Laura (Sistemas) - $30000
Lowest paid:  Luis (Ventas)    - $18000
"""
import csv


# Datos de empleados
workers = [
    ["Ana",    "Sistemas", 26000],
    ["Luis",   "Ventas",   18000],
    ["María",  "RRHH",     19000],
    ["Laura",  "Ventas",   20000],
    ["Javier", "Ventas",   25000],
    ["Miguel", "RRHH",     22000],
    ["Alexis", "Sistemas", 30000],
    ["Manuel", "Sistemas", 26000],
]

# Escribir CSV
with open("employes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "department", "salary"])
    writer.writerows(workers)

# Leer CSV
with open("employes.csv", "r") as f:
    employees = [
        {"name": row["name"], "department": row["department"], "salary": int(row["salary"])}
        for row in csv.DictReader(f)
    ]

# Procesar
def generate_report(employees):
    total     = len(employees)
    avg_salary = sum(e["salary"] for e in employees) / total
    highest   = max(employees, key=lambda e: e["salary"])
    lowest    = min(employees, key=lambda e: e["salary"])

    by_dept = {}
    for emp in employees:
        by_dept.setdefault(emp["department"], []).append(emp["salary"])

    lines = [
        f"Total employees: {total}",
        f"Average salary:  ${avg_salary:.2f}",
        "",
        "By department:",
    ]

    for dept, salaries in by_dept.items():
        avg = sum(salaries) / len(salaries)
        lines.append(f"  {dept}: {len(salaries)} employees | Avg: ${avg:.2f}")

    lines += [
        "",
        f"Highest paid: {highest['name']} ({highest['department']}) - ${highest['salary']}",
        f"Lowest paid:  {lowest['name']} ({lowest['department']}) - ${lowest['salary']}",
    ]

    return "\n".join(lines)

report = generate_report(employees)
print(report)

with open("report.txt", "w") as f:
    f.write(report)

print(f"\nReport saved to '{"report.txt"}'")