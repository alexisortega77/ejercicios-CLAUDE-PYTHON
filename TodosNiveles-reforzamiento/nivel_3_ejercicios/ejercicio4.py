# ------------------------------------------------------------
# EJERCICIO 4 — Medio
# Crea tres funciones:
# - es_bisiesto(año) → True/False
# - dias_en_mes(mes, año) → número de días
# - validar_fecha(dia, mes, año) → True/False
# ------------------------------------------------------------
# Output esperado:
# es_bisiesto(2024)  → True
# es_bisiesto(2023)  → False
# es_bisiesto(1900)  → False
# es_bisiesto(2000)  → True
#
# dias_en_mes(2, 2024) → 29
# dias_en_mes(2, 2023) → 28
# dias_en_mes(4, 2024) → 30
#
# validar_fecha(29, 2, 2024) → True
# validar_fecha(29, 2, 2023) → False
# validar_fecha(31, 4, 2024) → False
# validar_fecha(15, 6, 2024) → True
#
# Pista año bisiesto: divisible entre 4, excepto siglos
# a menos que sean divisibles entre 400.

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_on_month(month, year):
    days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
            7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # Febrero especial
    if month == 2 and is_leap(year):
        return 29
    return days[month]

def validate_date(day, month, year):
    if not 1 <= month <= 12:
        return False
    return 1 <= day <= day_on_month(month, year)
   
print(is_leap(2024))   
print(is_leap(2023))   
print(is_leap(1900))   
print(is_leap(2000))   

print(day_on_month(2,2024))   
print(day_on_month(2,2023))   
print(day_on_month(4,2024))   

print(validate_date(29,2,2024))   
print(validate_date(29,2,2023))   
print(validate_date(31,4,2024))  
print(validate_date(15,6,2024))    