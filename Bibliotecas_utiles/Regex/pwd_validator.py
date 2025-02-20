"""
Requisitos:

Al menos una minúscula ([a-z])
Al menos una mayúscula ([A-Z])
Al menos un número (\d)
Al menos un símbolo especial ([!@#$%^&*])
Mínimo 8 caracteres de longitud
"""
import re

def validar_contraseña(contraseña):
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$"
    return bool(re.match(patron, contraseña))

# Pruebas
print(validar_contraseña("Hola123!"))  # ✅ True (válida)
print(validar_contraseña("hola123!"))  # ❌ False (falta mayúscula)
print(validar_contraseña("HOLA123!"))  # ❌ False (falta minúscula)
print(validar_contraseña("HolaMundo!")) # ❌ False (falta número)
print(validar_contraseña("Hola1234"))   # ❌ False (falta símbolo)
