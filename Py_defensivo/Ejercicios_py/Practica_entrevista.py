"""
                    1.Invertir una cadena sin usar [::-1]
Ejercicio: Implementa una función que invierta una cadena sin usar slicing.
"""
def invertir_cadena(cadena):
    res = ""
    # for caracter in cadena:
    #     res = caracter + res

    for caracter in reversed(cadena):
        res+= caracter

    return res

# print(invertir_cadena("python"))  # "nohtyp"

# texto = "hola"
# print(texto[::-1])

"""
                2. Detectar un número repetido en una lista
Ejercicio: Escribe una función que devuelva el primer número repetido en una lista.
"""

def primer_numero_repetido(lista):
    vistos = set()

    for num in lista:

        if num in vistos:
            return num
        vistos.add(num)
    
    return "No se ha encontrado ningun numero repetido"

# print(primer_numero_repetido([1, 2, 3, 4, 2, 5]))  # 2


"""
        3. Contar la frecuencia de palabras en un texto
Ejercicio: Dado un string, cuenta cuántas veces aparece cada palabra.
"""

def contar_palabras(texto):
    res = texto.lower().split()
    contador = 0
    for pal in res:
        contador +=1 
    return contador

# print(contar_palabras("Hola mundo hola mundo hola"))  


"""
                        4. Validar una dirección IP
Ejercicio: Escribe una función que valide si una cadena es una dirección IP válida.
"""
import re

def validar_ip(ip):

    patron = r"^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$"
    return bool(re.match(patron, ip))

# print(validar_ip("192.168.1.1"))  # True
# print(validar_ip("999.999.999.999"))  # False

"""
                        5. Verificar si una cadena es un palíndromo
Ejercicio: Escribe una función que verifique si una cadena es un palíndromo.
"""

def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

# Ejemplos de uso:
# print(es_palindromo("Anita lava la tina"))  # True
# print(es_palindromo("python"))  # False

"""
                        8. Encontrar el número faltante en una secuencia
Ejercicio: Dada una lista de números del 1 al n con un número faltante, encuentra el número perdido.
    p.e --> print(numero_faltante([1, 2, 4, 5, 6]))  # 3
"""

def numero_faltante(secuencia):
    n = len(secuencia) + 1
    suma_esperada = n * (n + 1) // 2
    suma_real = sum(secuencia)

    return suma_esperada - suma_real

print(numero_faltante([1, 2, 4, 5, 6]))  # 3

