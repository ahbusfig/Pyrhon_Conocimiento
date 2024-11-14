#!/usr/bin/env python
from termcolor import colored

# ============================================================
# Acceder a elementos de una tupla
# ============================================================

def imprimir_tupla(tupla):
    i = 1
    for elemento in tupla:
        print(f"elemento {i} --> {elemento}")
        i += 1

# ============================================================
# Accede al segundo elemento de la tupla frutas.
# Intentar modificar una tupla
# ============================================================

def acceso_elemento_tupla(tupla1):
    print(colored(f"La tupla tiene un tamaño de {len(tupla1)} elementos", 'cyan'))
    while True:
        try:
            index = int(input(colored("Dime el indice (p.e 0...i)-->  ", 'yellow')))
            print(colored(f"\nEl elemento {index} --> {tupla1[index]}\n", 'green'))
            break
        except:
            print(colored("\nNo es un indice valido, intentalo de nuevo!\n", 'red'))

# ============================================================
# Intenta cambiar el valor del primer elemento de frutas a 
# "pera" y observa el resultado.
# ============================================================

def cambiar_valor_elemento_tupla(tupla1):
    lista1 = list(tupla1)
    print(colored(f"La tupla tiene un tamaño de {len(lista1)} elementos", 'cyan'))
    while True:
        try:
            index = int(input(colored("Dime el indice (p.e 0...i)-->  ", 'yellow')))
            elemento = input(colored("Dime por cual elemento lo cambiarás --> ", 'yellow'))
            lista1[index] = elemento
            tupla_modificada = tuple(lista1)
            print(colored(f"\nLa tupla modificada: {tupla_modificada}\n", 'green'))
            break
        except (ValueError, IndexError):
            print(colored("\nNo es un indice valido, intentalo de nuevo!\n", 'red'))
    return tupla_modificada
# ============================================================
# Concatenar dos tuplas
# ============================================================
def concatenar_2_tuplas(tupla1, tupla2):
    # Concatenar las dos tuplas directamente
    tupla_concatenada = tupla1 + tupla2
    
    # Imprimir las tuplas originales y la tupla resultante
    print(colored(f"Tupla 1 --> {tupla1}", 'yellow'))
    print(colored(f"Tupla 2 --> {tupla2}", 'yellow'))
    print(colored(f"Tupla concatenada --> {tupla_concatenada}", 'green'))
    
    return tupla_concatenada

# ============================================================
# Desempaquetar una tupla
# ============================================================
def desempaquetar_tupla(tupla1):
    variables = {}
    for i in range(len(tupla1)):
        var_name = f"var{i+1}"
        variables[var_name] = tupla1[i]
        print(colored(f"{var_name}: {tupla1[i]}", 'yellow'))
    print(variables)
    return variables
    #Forma con lista
    variables = []
    for i in range(len(tupla1)):
        variables.append(tupla1[i])
        print(colored(f"var{i+1}: {tupla1[i]}", 'yellow'))
    return variables

# ============================================================
# Convertir una tupla en una lista y modificarlas
# ============================================================
def modificar_tupla(tupla1):
    res = list(tupla1)
    while True:
        print(f"La tupla --> ({', '.join(res)})")
        try:
            indice = int(input(f"Dime el indice que quieres modificar (0 al {len(tupla1) - 1}) --> "))
            if indice < 0 or indice >= len(tupla1):
                print(colored("No es un indice valido!", 'red'))
                continue
            elemento = input("Dime por cual elemento lo cambiarás --> ")
            res[indice] = elemento
            print(colored("Se ha modificado correctamente!", 'green'))

            #---------Preguntar si quiero modificar otro elemento -------------
            while True:
                respuesta = input(f"Quieres modificar otro elemento --> (yes/no) ").strip().lower() #Strip elimina espacios en blanco a los lados o caracter puesto
                if respuesta == "no":
                    return print(tuple(res))
                elif respuesta == "yes":
                    break
                else:
                    print(colored("Introduce una respuesta valida!", 'red'))

        except ValueError:
            print(colored("Por favor, introduce un número entero válido!", 'red'))

        
"""--------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------Vamos a ejecutar las funciones-----------------------------------------------"""
"""--------------------------------------------------------------------------------------------------------------------"""
frutas = ("pera", "manzana","mandarina", "naranja")
verduras = ("Tomate", "Lechuga", "Zanahoria")
#imprimir_tupla(frutas)
#acceso_elemento_tupla(frutas)
#cambiar_valor_elemento_tupla(frutas)
#concatenar_2_tuplas(tupla1=frutas,tupla2=verduras)
#desempaquetar_tupla(frutas)
modificar_tupla(frutas)