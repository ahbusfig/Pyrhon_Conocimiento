#!/usr/bin/env python
from termcolor import colored
from collections import Counter

# ============================================================
# Ejercicio 1: Encontrar el índice de un elemento en una tupla
# ============================================================
# Dada una tupla de elementos, escribe una función que reciba la tupla y un elemento,
# y devuelva el índice del elemento en la tupla. 
# Si el elemento no está en la tupla, devuelve -1.
# ============================================================
def elemento_segun_indice(tupla):
    while True:
        try:
            #Preguntar el elemento que quieres comprobar
            elemento= input(colored(f"Que elemento buscas en la tupla --> ","yellow"))
            
            for item in tupla:
                if elemento == item:
                    indice = tupla.index(elemento)
                    return print(f"El indice es --> ",indice)
                            
        except ValueError:
            print(colored(f"No hay ningun elemento con ese nombre! --> -1", "red"))
        except Exception as e:
            print(f"Hubo un error: {e}")
#tupla = ("manzana", "banana", "cereza", "pera")
#elemento_segun_indice(tupla)
# ============================================================
# Ejercicio 2: Contar la frecuencia de un elemento en una tupla
# ============================================================
# Dada una tupla de elementos, escribe una función que reciba
# la tupla y un elemento, y devuelva la cantidad de veces que
# el elemento aparece en la tupla.
# ============================================================
def contador_elemento_in_tupla(tupla):
    while True:
        try:
            #Preguntar el elemento
            tupla_sin_rep = tuple(set(tupla))
            elemento = input(f"\nDime un elemento de la tupla {",".join(tupla_sin_rep)}--> ")
            
            contador = 0
            for item in tupla:
                if item == elemento:
                    contador+=1
            return print(f"{elemento} aparece {contador} vez/veces en la tupla")
        except:
            print(f"Hubo algun error!")

# tupla = ("manzana", "banana", "cereza", "pera", "banana", "banana")
# elemento = "banana"
# contador_elemento_in_tupla(tupla)

# ============================================================
# Ejercicio 3: Convertir una lista de tuplas en una tupla de listas
# ============================================================
# Dada una lista de tuplas, escribe una función que convierta
# esa lista en una tupla de listas.
# Ejemplo: [(1, 2), (3, 4)] -> ([1, 3], [2, 4])
# ============================================================
def lista_tuplas_to_tupla_listas(lista):
    res = []
    for item in lista:
        res.append(list(item))
    return print(f"La tupla resultante es --> {tuple(res)}")

# lista = [(1, 2), (3, 4)]
# lista_tuplas_to_tupla_listas(lista)

# ============================================================
# Ejercicio 4: Ordenar una tupla de tuplas por el segundo elemento
# ============================================================
# Dada una tupla de tuplas, escribe una función que ordene
# las tuplas internas por el segundo elemento de cada tupla.
# ============================================================
def tupla_de_tuplas_ordenar_por_2_elemento(tupla):
    lista = list(tupla)
    #Ordenamiento de burbuja
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j][1] > lista[j+1][1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    # Convertir la lista de nuevo en una tupla
    res = tuple(lista)
    print(colored(f"La tupla ordenada es: {res}", 'green'))
    return res
    """ -----------------Forma mas simple--------------------------
        res = sorted(tupla, key=lambda x: x[1])
        print(colored(f"La tupla ordenada es: {res}", 'green'))
        return res    
    --------------------------------------------------------------"""
# Ejemplo de uso
# tupla_de_tuplas = (("x", 4), ("y", 1), ("z", 3), ("w", 2))
# tupla_de_tuplas_ordenar_por_2_elemento(tupla_de_tuplas)

# ============================================================
# Ejercicio 5: Eliminar duplicados de una tupla
# ============================================================
# Dada una tupla de elementos, escribe una función que elimine
# los elementos duplicados y devuelva una tupla con los elementos
# únicos.res = set(tupla)
# ============================================================
def eliminar_elemento_duplicados_tupla(tupla):
    res = set(tupla)
    return tuple(res)
# tupla = ("manzana", "banana", "cereza", "pera", "banana", "manzana")
# res = eliminar_elemento_duplicados_tupla(tupla)
# print(res)

# ============================================================
# Ejercicio 6: Intercambiar el contenido de dos tuplas
# ============================================================
# Dadas dos tuplas, escribe una función que intercambie su
# contenido y devuelva las dos tuplas modificadas.
# ============================================================
def intercambiar_dos_tuplas(tupla1, tupla2):
    return tupla2,tupla1
# tupla1 = (1, 2, 3)
# tupla2 = (4, 5, 6)
# print(intercambiar_dos_tuplas(tupla1, tupla2))
# ============================================================
# Ejercicio 7: Dividir una tupla en dos partes
# ============================================================
# Dada una tupla y un índice, escribe una función que divida
# la tupla en dos partes en el índice dado y devuelva las dos
# tuplas resultantes.
# ============================================================
def separar_tuplas(tupla,indice):
    print(colored(tupla,"yellow"))
    print(colored(f"El indice dado es --> {indice}","green"))
    parte1 = tupla[:indice]
    parte2 = tupla[indice:]
    return print(parte1,parte2)

# tupla = (1, 2, 3, 4, 5, 6)
# indice = 2
# separar_tuplas(tupla,indice)

# ============================================================
# Ejercicio 8: Encontrar el elemento más común en una tupla
# ============================================================
# Dada una tupla de elementos, escribe una función que encuentre
# el elemento que más veces se repite en la tupla.
# ============================================================
def elemento_mas_comun(tupla):
    # Crear un diccionario para contar la frecuencia de cada elemento
    frecuencia = {}
    for item in tupla:
        if item in frecuencia:
            frecuencia[item] += 1
        else:
            frecuencia[item]=1
    # Encontrar el elemento con la mayor frecuencia
    elemento_comun = max(frecuencia, key=frecuencia.get)  #---------------------Saber usar esta expresion!!
    
    for item, count in frecuencia.items():
        print(colored(f"El elemento {item} aparece --> {count} veces", 'yellow'))
    
    return print(colored(f"\nEl elemento mas comun es--> {elemento_comun} \n","green"))
    
    # Encontrar el elemento con la mayor frecuencia
# tupla = ("manzana", "banana", "cereza", "pera", "banana", "manzana", "banana")
# elemento_mas_comun(tupla)

# ============================================================
# Ejercicio 9: Concatenar una lista de tuplas en una sola tupla
# ============================================================
# Dada una lista de tuplas, escribe una función que concatene
# todas las tuplas en una sola tupla.
# ============================================================
def concatenar_lista_tuplas(tupla):
    res = []
    for item in tupla:
        res += (item)
    return(print(tuple(res)))
# lista_de_tuplas = [(1, 2), (3, 4), (5, 6)]
# concatenar_lista_tuplas(lista_de_tuplas)

# ============================================================
# Ejercicio 10: Encontrar la intersección de dos tuplas
# ============================================================
# Dadas dos tuplas, escribe una función que encuentre los
# elementos comunes entre ambas tuplas y devuelva una tupla
# con esos elementos.
# ============================================================
def interseccion_2_tuplas(tupla1,tupla2):
    res = []  # Crear lista donde guardar res
    for item in tupla2:        #Bucle que recorra la tupla2
        if item in tupla1:     #Comprobar si item de la tupla2 está en la tupla 1
            res.append(item)   #Si es asi pues lo añadimos a la lista res
    print(tuple(res))          #Finalmente res se pasa como tupla

    """  ---> Version mejorada
    conjunto1 = set(tupla1)  # Convertir tupla1 en un conjunto para búsquedas rápidas
    res = [item for item in tupla2 if item in conjunto1]  # Usar comprensión de listas
    return tuple(res)  # Finalmente res se pasa como tupla

    """
tupla1 = (1, 2, 3, 4, 5)
tupla2 = (4, 5, 6, 7, 8)
interseccion_2_tuplas(tupla1,tupla2)