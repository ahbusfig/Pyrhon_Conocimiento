import re
import os
text = "Hoy estamos a fecha 10/10/2023 xd, mañana será 11/10/2023 xd"

######################################################################
#####################Buscar coincidencias#############################
######################################################################

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
# Buscar los correos electronicos
text = "Los users pueden contactarnos a soporte@hack4u.io o a info@hack4u.tech"
matches = re.findall("(\w+)@(\w+\.\w{2,})", text)
print(matches)

#################################################################################
 ##################################Substituin###################################
  #############################################################################
"""texto= []
for i in range(1,6):
    texto.append(f"campo {i}")
print(str(texto))
"""

texto = "campo1,campo2,campo3,campo4,campo5"
texto = re.split(",",texto) #Lo transforma en lista !!
print((texto[1]))


"""
#################################################################################
 #############################validador de correos##############################
  #############################################################################
 """

def validador_correo(correo):
    patron = r"\b[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}\b"

    if re.findall(patron,correo):
        return True
    else:
        return False
    
correo = "alaingh37@gmail.com"
print(validador_correo(correo))

#Repasar regex es complejo !!