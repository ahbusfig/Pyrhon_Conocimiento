import argparse

#Crear el parser principal
parser = argparse.ArgumentParser(description="Calculadora que usa subcomandos")
#Agragar los subparser
subparser= parser.add_subparsers(dest="comando", help="Comando a ejecutar")

# Subcomando 'sumar'
parser_sumar = subparser.add_parser("sumar", help="Suma 2 numeros")
parser_sumar.add_argument("num1", type=int, help="Primer número")
parser_sumar.add_argument("num2",type=int, help="Segundo numero")

# Subcomando 'multiplicar'
parser_multiplicar = subparser.add_parser("multiplicar", help="Multiplica dos números")
parser_multiplicar.add_argument("num1", type=int, help="Primer número")
parser_multiplicar.add_argument("num2", type=int, help="Segundo número")

# Procesamos los argumentos
args = parser.parse_args()

# Lógica para ejecutar el comando correcto
if args.comando == "sumar":
    resultado = args.num1 + args.num2
    print(f"Resultado de la suma: {resultado}")
elif args.comando == "multiplicar":
    resultado = args.num1 * args.num2
    print(f"Resultado de la multiplicación: {resultado}")
else:
    parser.print_help()