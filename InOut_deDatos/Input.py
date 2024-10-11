# Solicitar el nombre del usuario
def presentate():
    nombre = input("\nPor favor, introduce tu nombre: ")
    edad = int(input("\n y ahora diga su edad: "))  # Para el input por defecto es un string --> pasarlo a int si es adecuado
    # Mostrar un mensaje de bienvenida
    print(f"\t [+] Hola, {nombre} usted cumplirá {edad+1} años el siguiente año!")

# Para hacer un bucle y se obtenga 
def presentate_bucle():
    while True:  # Bucle infinito
        try:
            presentate()
            break
        except ValueError:
            print("\n[i] ERROR, Intentalo de nuevo!")

#presentate_bucle()

from getpass import getpass

pwd = getpass("Introduce su contraseña --> ") #getpass --> Para evitar q se muestre la cosas que se escriben en terminal
print(f"Esta es su pwd --> {pwd}")