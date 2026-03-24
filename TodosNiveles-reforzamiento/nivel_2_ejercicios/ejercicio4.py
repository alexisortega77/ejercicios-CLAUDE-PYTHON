
# ------------------------------------------------------------
# EJERCICIO 4 — Medio
# Pide números hasta que el usuario escriba 0.
# Muestra suma, promedio, positivos, negativos y el mayor.
# ------------------------------------------------------------
# Inputs: 5, -3, 8, -1, 4, 0
# Output esperado:
# Números ingresados: 5
# Suma:       13
# Promedio:   2.60
# Positivos:  3
# Negativos:  2
# Mayor:      8    

acum=[]
positivos=0
negativos=0
while True:
    
    num=int(input("Ingresa un numero: "))
    if num==0:
        break
    acum.append(num)
    if num>0:
        positivos+=1
    elif num<0:
        negativos+=1

   
    
mayor=max(acum)
suma=sum(acum)
prom=suma/len(acum)

print(f"Numeros ingresados: {len(acum)}")
print(f"Suma: {suma}")
print(f"promedio: {prom:.2f}")
print(f"positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Numero mayor: {mayor}")