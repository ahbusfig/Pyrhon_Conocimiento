import argparse

def validar_numero(valor):
    valor = int(valor)
    if valor <= 0:
        raise argparse.ArgumentTypeError("El número debe ser mayor que 0")
    return valor

parser = argparse.ArgumentParser(description="Validar número positivo")
parser.add_argument("numero", type=validar_numero, help="Número positivo")

args = parser.parse_args()
print(f"Número válido: {args.numero}")
