import argparse

# Crear el parser principal
parser = argparse.ArgumentParser(description="Sistema de gestión de usuarios")

# Argumento global (afectará a todos los comandos)
parser.add_argument("--verbose", action="store_true", help="Muestra información detallada")

# Crear subparsers para los comandos específicos
subparsers = parser.add_subparsers(dest="comando", help="Comando a ejecutar")

# Subcomando 'agregar' (añadir usuario)
parser_agregar = subparsers.add_parser("agregar", help="Agrega un nuevo usuario")
parser_agregar.add_argument("nombre", type=str, help="Nombre del usuario")
parser_agregar.add_argument("--edad", type=int, default=18, help="Edad del usuario")

# Subcomando 'eliminar' (eliminar usuario)
parser_eliminar = subparsers.add_parser("eliminar", help="Elimina un usuario")
parser_eliminar.add_argument("nombre", type=str, help="Nombre del usuario a eliminar")

# Obtener los argumentos ingresados por el usuario
args = parser.parse_args()

# Lógica según el comando ingresado
if args.comando == "agregar":
    print(f"✅ Usuario '{args.nombre}' agregado con {args.edad} años.")
    if args.verbose:
        print("ℹ Se ha registrado un nuevo usuario en la base de datos.")

elif args.comando == "eliminar":
    print(f"❌ Usuario '{args.nombre}' eliminado.")
    if args.verbose:
        print("ℹ Se ha eliminado un usuario de la base de datos.")

else:
    print("⚠ No se proporcionó un comando válido.")
    parser.print_help()
