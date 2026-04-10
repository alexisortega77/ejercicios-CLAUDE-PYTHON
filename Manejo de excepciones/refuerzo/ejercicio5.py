"""
Ejercicio 5 — Medio
Crea un validador de formulario con excepciones personalizadas. Valida nombre, email y contraseña.
validate_form("Manuel", "manuel@mail.com", "Python123!")  → "Form valid!"
validate_form("", "manuel@mail.com", "Python123!")        → ValidationError: Name cannot be empty
validate_form("Manuel", "not-an-email", "Python123!")     → ValidationError: Invalid email format
validate_form("Manuel", "manuel@mail.com", "weak")        → ValidationError: Password too weak

💡 Un email válido debe tener exactamente un @ y un . después del @. Usa "@" in email y email.split("@").


"""

class ValidationError(Exception):
    pass


def validate_form(name, email, password):
    if name == "":
        raise ValidationError("Name cannot be empty")
    
    if email.count("@") != 1:
        raise ValidationError("Invalid email format")
    
    usuario, dominio = email.split("@")
    if "." not in dominio:
        raise ValidationError("Invalid email format")
    
    if len(password) < 8:
        raise ValidationError("Password too weak")
    
    return "Form valid!"

      

    
try:
 validate_form("Manuel", "manuel@mail.com", "Python123!") # → "Form valid!"
except ValidationError as e:
    print(f"ValidationError: {e}")
else:
   print("Form Valid!")
try:
  validate_form("", "manuel@mail.com", "Python123!")    
except ValidationError as e:
    print(f"ValidationError: {e}")    # ValidationError: Name cannot be empty
try:
  validate_form("Manuel", "not-an-email", "Python123!") 
except ValidationError as e:
    print(f"ValidationError: {e}")   # → ValidationError: Invalid email format
try:
 validate_form("Manuel", "manuel@mail.com", "weak")  
except ValidationError as e:
    print(f"ValidationError: {e}")