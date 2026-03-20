#Ejercicio extra A
espar=False
numero=int(input("ingrese un numero: "))
while espar==False:
 if numero%2==0:
    espar=True
    print("Es par")
    for i in range(2,numero+1,2):
      print(i,end=' ')
    
 else:
  numero=int(input("ingrese un numero: "))

"""Crea un programa que pida una contraseña al usuario. 
La contraseña correcta es `"python123"`. Dale 
**3 intentos**. Si acierta, da la bienvenida. Si falla los 3, bloquea el acceso.
"""
#Ejercicio extra B
Intentos = 2
Contraseña_correcta='python'
contraseña=input("ingresa la contraseña: ")
if contraseña==Contraseña_correcta:
   print("Bienvenido!!")
while contraseña != Contraseña_correcta:
  Intentos-=1
  contraseña=input("ingresa la contraseña: ")
  if contraseña==Contraseña_correcta:
   print("Bienvenido!!")
  elif Intentos==0:
     print("Acceso bloqueado!")
     break
  
  