import argparse

parser = argparse.ArgumentParser(description="Se imprime el nombre y la edad")
parser.add_argument("nombre", type=str, help="Nombre del user")
parser.add_argument("--e","--edad", type=int, default=18, help="edad del user")
parser.add_argument("--ciudad", type=str, default="Desconocida", help="Ciudad del usuario")

def mostrar_info():
    args = parser.parse_args()
    print(f"Nombre: {args.nombre}")
    print(f"Edad: {args.e}")
    print(f"Ciudad de origen: {args.ciudad} ")
if __name__ == "__main__":
    mostrar_info() 