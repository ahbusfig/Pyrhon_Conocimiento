import re

text = "Hoy estamos a fecha 10/10/2023 xd, mañana será 11/10/2023 xd"

# Buscar coincidencias de "xd" en el texto
matches_xd = re.findall("xd", text)
print("Coincidencias de 'xd':", matches_xd)

# Buscar coincidencias de fechas en el formato dd/mm/yyyy en el texto
matches_fecha = re.findall(r"\d{2}/\d{2}/\d{4}", text)
print("Coincidencias de fechas:", matches_fecha)
"""
    \d{2}: Coincide con exactamente dos dígitos (0-9).
    
    La barra invertida \ se usa para escapar el /
    en la expresión regular.
    
    \d{4}: Coincide con exactamente
    cuatro dígitos (0-9).
"""