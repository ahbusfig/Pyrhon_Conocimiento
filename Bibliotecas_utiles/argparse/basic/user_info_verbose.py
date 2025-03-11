import argparse

# Crear el objeto ArgumentParser
parser = argparse.ArgumentParser(description="Se imprime el nombre, la edad y la ciudad")

# Agregar argumentos
parser.add_argument("nombre", type=str, help="Nombre del usuario")
parser.add_argument("--e", "--edad", type=int, default=18, help="Edad del usuario")
parser.add_argument("--ciudad", type=str, default="Desconocida", help="Ciudad del usuario")
parser.add_argument("--verbose", action="store_true", help="Activa el modo detallado")

# Función que muestra la información
def mostrar_info():
    args = parser.parse_args()
   
    # Mostrar detalles adicionales si se activa la bandera --verbose
    if args.verbose:
        print("Modo verbose activado: Todos los datos han sido mostrados con éxito.")
    else:
        print(f"Nombre: {args.nombre}")
        print(f"Edad: {args.e}")
        print(f"Ciudad de origen: {args.ciudad}")
    

# Ejecutar la función si es el script principal
if __name__ == "__main__":
    mostrar_info()
