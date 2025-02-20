import re
from datetime import datetime

# Expresión regular para formato DD/MM/YYYY o DD-MM-YYYY
patron = r"^(0[1-9]|[12][0-9]|3[01])[/-](0[1-9]|1[0-2])[/-](\d{4})$"

def es_bisiesto(anio):
    """Devuelve True si el año es bisiesto, False en caso contrario."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar_fecha(fecha):
    """Verifica si la fecha es válida considerando días, meses y años bisiestos."""
    # Verifica si la fecha cumple el formato correcto
    match = re.match(patron, fecha)
    if not match:
        return False
    
    # Extrae día, mes y año de la fecha
    dia, mes, anio = map(int, match.groups())

    # Días máximos por mes
    dias_por_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Si el año es bisiesto, febrero tiene 29 días
    if mes == 2 and es_bisiesto(anio):
        dias_por_mes[2] = 29
    
    # Verifica si el día es válido para el mes correspondiente
    return dia <= dias_por_mes[mes]

# 🔍 Pruebas
fechas = [
    "29/02/2024",  # ✅ Año bisiesto, válido
    "29/02/2023",  # ❌ No es bisiesto, inválido
    "31/04/2024",  # ❌ Abril solo tiene 30 días
    "15-08-2000",  # ✅ Fecha válida
    "32/01/2022",  # ❌ Día inválido
    "12/13/2025",  # ❌ Mes inválido
    "01/01/0001",  # ✅ Fecha válida
]

for fecha in fechas:
    print(f"{fecha}: {'✅ Válida' if validar_fecha(fecha) else '❌ Inválida'}")
