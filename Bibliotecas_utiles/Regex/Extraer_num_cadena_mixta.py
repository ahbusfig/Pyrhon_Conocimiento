import re 
from termcolor import colored

def extraer_num(texto):
    # Corregir el patrón para extraer números
    patron = r"\d+"
    return re.findall(patron, texto)

# Ejemplo de uso
texto = "La casa tiene 3 habitaciones y 2 baños y 1 living room."
numeros = extraer_num(texto)
i = 1

# Imprimir los números extraídos
print(colored(f"Numeros extraidos:", "yellow"))
for num in numeros:
    print(colored(f"Numero {i} --> {num}", 'green'))
    i +=1