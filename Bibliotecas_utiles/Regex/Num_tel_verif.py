import re
from termcolor import colored

def validar_num_tel():
    while True:
        num = input("Introduzca su número de teléfono (formato (6/7)XX-XXX-XXX) --> ")
        patron = r"^(6|7)\d{2}-\d{3}-\d{3}$"
        patron2 = r"^(6|7)\d{8}$"
        if re.match(patron, num) or re.match(patron2, num):
            print(colored(f"El formato del número --> {num} es correcto", 'green'))
            break
        else:
            print(colored(f"El formato del número --> {num} es incorrecto", 'red'))

validar_num_tel()
