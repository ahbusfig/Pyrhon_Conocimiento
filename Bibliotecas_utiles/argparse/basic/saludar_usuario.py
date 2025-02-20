import argparse
import datetime
parser = argparse.ArgumentParser(description="Saludar a usuario")
parser.add_argument("nombre",type=str, help="Nombre del usuario")
args = parser.parse_args()

def saludar_user():
    hora = int(datetime.datetime.now().strftime("%H"))
    if 6 <= hora < 16:
        print(f"Hola buenos dias {args.nombre}")
    elif 16 <= hora < 19:
        print(f"Hola buenas tardes {args.nombre}")
    else:
        print(f"Hola buenas noches {args.nombre}")

saludar_user()