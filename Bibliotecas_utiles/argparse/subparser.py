import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="comando")

# Subcomando "saludar"
subparser_saludar = subparsers.add_parser("saludar", help="Saludar a una persona")
subparser_saludar.add_argument("nombre", type=str, help="Nombre de la persona")

# Subcomando "despedir"
subparser_despedir = subparsers.add_parser("despedir", help="Despedir a una persona")
subparser_despedir.add_argument("nombre", type=str, help="Nombre de la persona")

args = parser.parse_args()

if args.comando == "saludar":
    print(f"¡Hola, {args.nombre}!")
elif args.comando == "despedir":
    print(f"¡Adiós, {args.nombre}!")
else:
    print("Comando no reconocido")
