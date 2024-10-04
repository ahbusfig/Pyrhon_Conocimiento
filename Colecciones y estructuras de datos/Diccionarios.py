"""
Diccionarios propiedades:
    Clave-Valor: Almacenan pares de clave y valor. 
                 Cada clave es única y se utiliza para acceder a su valor correspondiente.
   
    Mutable: Se puede modificar después de su creacion.
    
    No Ordenado: en versiones anteriores a 3.7.

    Claves Inmutables: Las claves deben ser de un tipo de datos inmutable (p.e:números, cadenas, tuplas). 
                       Los valores pueden ser de cualquier tipo.
    
    Acceso Rápido: Proporcionan acceso rápido a los valores mediante sus claves, 
                   utilizando una estructura de datos hash.
"""

# Ejemplo de diccionario con temática de hacking
hacking_tools = {
    "Nmap": "Herramienta de escaneo de red",
    "Metasploit": "Framework de explotación",
    "Wireshark": "Analizador de tráfico de red",
    "John the Ripper": "Cracker de contraseñas",
    "Hydra": "Herramienta de fuerza bruta"
}
herramienta = "Nmap"
print("\n Obtener un elemento usando get --> ",hacking_tools.get(herramienta,"No se ha encontrado la herramienta"))
# Acceso rápido a los valores mediante sus claves
print("\n Descripción de Nmap:", hacking_tools["Nmap"])  # Salida: Herramienta de escaneo de red

# Añadir un nuevo par clave-valor
hacking_tools["Burp Suite"] = "Herramienta de prueba de seguridad web"
print("\n Añadido Burp Suite:", hacking_tools)

# Modificar un valor existente
hacking_tools["John the Ripper"] = "Herramienta de cracking de contraseñas"
print("\n Modificado John the Ripper:", hacking_tools)

# Eliminar un par clave-valor
del hacking_tools["Hydra"]
print("\n Eliminado Hydra:", hacking_tools)

# Verificar si una clave existe en el diccionario
herramienta = "Metasploit"
if herramienta in hacking_tools:
    print("\n Metasploit está en el diccionario")
else:
    print("\n Esta clave no existe en el diccionario.")

# Iterar sobre las claves y valores del diccionario
for herramienta, descripcion in hacking_tools.items():
    print(f"\n Herramienta: {herramienta}, Descripción: {descripcion}")

# Para saber long de un diccionario
print(f"\n La longitud del diccionario es --> {len(hacking_tools)}") #5 herramientas


#Forma compacta de crear un diccionario
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)


# Crear un segundo diccionario de herramientas de hacking
additional_tools = {
    "Burp Suite": "Herramienta de prueba de seguridad web",
    "Aircrack-ng": "Suite de herramientas para auditoría de redes inalámbricas",
    "SQLmap": "Herramienta de inyección SQL",
    "Nikto": "Escáner de vulnerabilidades web"
}

# Actualizar el primer diccionario con los elementos del segundo
hacking_tools.update(additional_tools)
print("\n Diccionario actualizado de herramientas de hacking:")
for herramienta, descripcion in hacking_tools.items():
    print(f"\n Herramienta: {herramienta}, Descripción: {descripcion}")

# Añadir una herramienta nueva que no se repita
hacking_tools["ZAP"] = "Herramienta de prueba de seguridad web"
print("\n Herramienta 'ZAP' añadida directamente:")
for herramienta, descripcion in hacking_tools.items():
    print(f"\n Herramienta: {herramienta}, Descripción: {descripcion}")