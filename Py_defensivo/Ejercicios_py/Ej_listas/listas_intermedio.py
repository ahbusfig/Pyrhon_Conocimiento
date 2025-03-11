#!/usr/bin/env python
from termcolor import colored
# Ejercicio 1: Eliminar duplicados
# Escribe una función que elimine los elementos duplicados de una lista y devuelva una nueva lista con los elementos únicos.
def eliminar_duplicados(lista):
    # res = []
    # for item in lista:
    #     if item not in res:
    #         res.append(item)
    # return print(res)
    return print(list(set(lista)))  #Forma usando conjuntos
# lista1 = [1,2,3,4,3,3,4,1]
# eliminar_duplicados(lista1)

# Ejercicio 2: Encontrar el segundo mayor
# Escribe una función que encuentre el segundo mayor número en una lista de números.
def segundo_mayor(lista):
    """lista_2 = set(lista)
    mayor = max(lista_2)
    lista_2.remove(mayor)
    segundo_mayor = max(lista_2)
    return print(f"El 2 maximo es --> {segundo_mayor}")
    """
    if len(lista) < 2:
        return print(colored(f"No hay segundo mayor si la lista tiene menos de dos elementos","red"))  
    
    lista_unica = list(set(lista))  # Eliminar duplicados
    if len(lista_unica) < 2:
        return print(colored(f"No hay segundo mayor si la lista tiene menos de dos elementos","red"))  
    lista_unica.sort(reverse=True)  # Ordenar la lista en orden descendente
    return lista_unica[1]  # El segundo mayor es el segundo elemento
# lista1 = [1,2,3,4,3,3,4,1,6,7]
# segundo_mayor(lista1)

# Ejercicio 3: Rotar una lista
# Escribe una función que rote una lista hacia la derecha por un número dado de pasos.
def rotar_lista(lista,pasos):
    """ ----------------Pensando logicamente--------------------------
    res = []
    i = 0
    step_count = 0
    while True:
        if i < len(lista)-1:
            if i + pasos > len(lista)-1:
                i = 0
                pasos = 0
            res.append(lista[i+pasos])
            i +=1
            #Contar la iteraciones del bucle
            step_count +=1
            if step_count > len(lista)-1:
                break 
    print(res)"""
    """--------------Solucion eficiente-----------------------------"""
    if not lista:
        return lista  # Si la lista está vacía, retornar la lista vacía
    pasos = pasos % len(lista)  # Asegurarse de que los pasos no excedan la longitud de la lista
    return print(lista[-pasos:] + lista[:-pasos])
lista1 = [1, 2, 3, 4, 5]
pasos = 2
rotar_lista(lista1,pasos)

# Ejercicio 4: Intercalar listas
# Escribe una función que tome dos listas y devuelva una nueva lista que intercale los elementos de ambas listas.
def intercalar_listas(lista1,lista2):
    res = []
    len1, len2 = len(lista1), len(lista2)
    min_len = min(len1, len2)
    
    # Intercalar elementos de ambas listas hasta la longitud mínima o si son cuadradas
    for i in range(min_len):
        res.append(lista1[i])
        res.append(lista2[i])
    
    # Añadir los elementos restantes de la lista más larga
    if len1 > len2:
        res.extend(lista1[min_len:])
    else:
        res.extend(lista2[min_len:])
    
    return res
lista1 = [1, 3, 5]
lista2 = [2, 4, 6,7,8,9]
print(intercalar_listas(lista1,lista2))

# Ejercicio 5: Encontrar elementos comunes
# Escribe una función que tome dos listas y devuelva una nueva lista con los elementos comunes a ambas listas.
def elementos_comunes_listas(lista1,lista2):
    #Pasar a conjunts
    set1 = set(lista1)
    set2 = set(lista2)
    #Buscar los comunes
    comunes = set1.intersection(set2)
    #Imprimir res
    return print(list(comunes))
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [4, 5, 6, 7, 8]
# elementos_comunes_listas(lista1,lista2)

# Ejercicio 6: Dividir lista en sublistas
# Escribe una función que divida una lista en sublistas de tamaño n.
def separar_listas(lista,indice):
    print(colored(lista,"yellow"))
    print(colored(f"El indice dado es --> {indice}","green"))
    parte1 = lista[:indice]
    parte2 = lista[indice:]
    return print(parte1,parte2)

# lista1 = [1, 2, 3, 4, 5]
# separar_listas(lista1,2)

# Ejercicio 7: Suma acumulativa
# Escribe una función que tome una lista de números y devuelva una nueva lista donde cada elemento es la suma acumulativa de los elementos anteriores.
def suma_acum(lista):
    res = []
    acum= 0
    for item in lista:
        acum += item
        res.append(acum)
    print(colored(res,"green"))
# lista = [1, 2, 3, 4, 5]
# suma_acum(lista)

# Ejercicio 8: Eliminar elementos en índices impares
# Escribe una función que elimine los elementos en los índices impares de una lista.
def eliminar_indice_impar(lista):
    """------------------------Forma 1 --> lógica-------------------------------
    res = []
    for item in lista:
        if lista.index(item)%2 == 0:
            res.append(item)
    print(colored(res,"green"))"""
    """-------------------------Forma 2 --> Enumerate---------------------------- """
    res = [item for index, item in enumerate(lista) if index % 2 == 0]
    return print(colored(res,"green"))           
# lista = [1, 2, 3, 4, 5, 6]
# eliminar_indice_impar(lista)

# Ejercicio 9: Encontrar la sublista más larga de elementos consecutivos
# Escribe una función que encuentre la sublista más larga de elementos consecutivos en una lista de números.
def sublista_mas_grande(lista):
    if not lista: # Si la lista esta vacia
        return []

    longest = []  #Lista donde se guardará la sublista mas grande
    current = [lista[0]] #Valor actual

    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1] + 1:
            current.append(lista[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [lista[i]]

    if len(current) > len(longest):
        longest = current

    return print(longest)
lista = [1, 2, 3, 5, 2 , 3, 6, 7, 8, 9]
sublista_mas_grande(lista)

# Ejercicio 10: Ordenar lista de listas por longitud
# Escribe una función que tome una lista de listas y la ordene por la longitud de las sublistas.
def ordenar_por_long_sublistas(lista):
    res = lista
    #Comprobar que todos sean sublistas
    for item in lista:
        if type(item).__name__ != "list":
            return print(colored(f"[!] All items must be lists","red"))
    # Ordenar las sublistas por longitud
    res.sort(key=len)
    return print(colored(res,"green"))  

# lista_de_listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
# ordenar_por_long_sublistas(lista_de_listas)

def invertir_palabras(texto):
    palabra = ""
    palabras = []
    
    for char in texto:
        if char == " ":
            palabras.append(palabra)
            palabra = ""
        else:
            palabra += char
    palabras.append(palabra)  # Última palabra
    
    resultado = ""
    for palabra in reversed(palabras):
        resultado += palabra + " "
    
    return resultado.strip()

# print(invertir_palabras("Hola mundo desde Python"))


#Ej 12 Implementa una función que encuentre el primer número repetido en una lista.

lista = [1,2,3,4,4,3,2]

def encontrar_primer_num_rep_v1(lista):
    res = 0
    num_anterior = 0

    for num in lista:

        if num < num_anterior:
            num_anterior = num
        elif num > num_anterior:
            num_anterior = num
        elif num_anterior == num:
            res = num
            return print(res)

def encontrar_primer_rep_v2(lista):
    vistos = set() #Def un conjunto vacio
    for num in lista:
        if num in vistos: # Si el numero está dentro del conjunto es el repetido
            return print(num)
        vistos.add(num) # Añadir num al conjunto de vistos
    return None  # Si no hay números repetidos


# encontrar_primer_num_rep_v1(lista)
encontrar_primer_rep_v2(lista)