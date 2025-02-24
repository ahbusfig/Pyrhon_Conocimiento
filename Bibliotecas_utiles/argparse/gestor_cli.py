import argparse

parser = argparse.ArgumentParser(description="Gestor de tareas cli")
parser.add_argument("--v", type=str, help="activa el modo detallado")

# Subparsers
subparsers = parser.add_subparsers(dest="comando", help="Acciones disponibles")

# Las opciones del subparser
# ---------------------------Agregar una tarea-------------------------------
parser_add = subparsers.add_parser("agregar", help="Agrega una nueva tarea")
parser_add.add_argument("titulo",type=str, help="Titulo de la tarea")
parser_add.add_argument("--p","--prioridad",type=int, choices=[1,2,3], help="prioridad de la tarea", default=1)
# ---------------------------Listar las tareas-------------------------------
parser_list = subparsers.add_parser("listar", help="lista las tareas disponibles")
parser_list.add_argument("--completadas", type=str, help="Muestra las tareas completadas")
# ---------------------------Eliminar una tarea-------------------------------
parser_eliminar = subparsers.add_parser("eliminar", help="Elimina una tarea por título")
parser_eliminar.add_argument("titulo", type=str, help="Título de la tarea a eliminar")


# 🔹 Función principal
def main():
    args = parser.parse_args()

    if args.comando == "agregar":
        print(f"Tarea agregada: {args.titulo}, Prioridad: {args.p}")
    
    elif args.comando == "listar":
        filtro = "completadas" if args.completadas else "todas"
        print(f"Mostrando tareas {filtro}")
    
    elif args.comando == "eliminar":
        print(f"Eliminando tarea: {args.titulo}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()