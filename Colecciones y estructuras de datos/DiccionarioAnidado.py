# Diccionario inicial con información sobre una persona
persona = {
    "Nombre": "Juan Pérez",
    "Edad": 30,
    "Contacto": {
        "Email": "juan.perez@example.com",
        "Teléfono": "123-456-7890"
    },
    "Dirección": {
        "Calle": "Calle Falsa 123",
        "Ciudad": "Ciudad Ejemplo",
        "País": "País Ejemplo"
    }
}

# Añadir información adicional directamente
persona["Ocupación"] = "Ingeniero de Software"
persona["Hobbies"] = ["Leer", "Correr", "Programar"]

# Crear un segundo diccionario con información adicional
informacion_adicional = {
    "Redes Sociales": {
        "LinkedIn": "linkedin.com/in/juanperez",
        "Twitter": "@juanperez"
    },
    "Educación": {
        "Grado": "Ingeniería Informática",
        "Universidad": "Universidad Ejemplo"
    }
}

# Actualizar el diccionario inicial con la información adicional
persona.update(informacion_adicional)

# Imprimir el diccionario actualizado
print("\nDiccionario actualizado con información sobre la persona:")
for clave, valor in persona.items():
    if isinstance(valor, dict):
        print(f"\n{clave}:")
        for subclave, subvalor in valor.items():
            print(f"  {subclave}: {subvalor}")
    else:
        print(f"\n{clave}: {valor}")