#!/usr/bin/env python3
import datetime

# Crear una fecha específica
fecha = datetime.date(2023, 6, 14)  # AA:MM:DD
print("Fecha específica:", fecha)

# Crear una hora específica
hora = datetime.time(14, 15, 44)  # hh:mm:ss
print("Hora específica:", hora)

# Obtener la fecha y hora actual
ahora = datetime.datetime.now()
print("Fecha y hora actual:", ahora)

# Calcular la diferencia entre dos fechas
fecha1 = datetime.date(2023, 6, 14)
fecha2 = datetime.date(2023, 7, 14)
diferencia = fecha2 - fecha1
print("Días de diferencia:", diferencia.days)

# Combinar fecha y hora en un solo objeto
fecha_hora_combinada = datetime.datetime.combine(fecha, hora)
print("Fecha y hora combinadas:", fecha_hora_combinada)

###################################################################
########Usar variables para la fecha y hora#######################
#################################################################
ahora = datetime.datetime.now()

# Crear variables para día, mes, año, hora, minuto y segundo
dia = ahora.day
mes = ahora.month
año = ahora.year
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second

# Crear un objeto de fecha y hora utilizando las variables
fecha = datetime.date(año, mes, dia)
hora = datetime.time(hora, minuto, segundo)
fecha_hora = datetime.datetime.combine(fecha, hora)

# Formatear la fecha y hora en una representación legible
fecha_hora_formateada = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha y hora formateadas:", fecha_hora_formateada)