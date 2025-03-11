# Ejercicio 1: Encontrar la sublista con la suma máxima
# Escribe una función que encuentre la sublista continua con la suma máxima en una lista de números.
def encontrar_sublista_maxima(lista):  #Algoritmo de kadene
    max_actual = max_global = lista[0]
    inicio = fin = temp_inicio = 0

    for i in range(1, len(lista)):
        if lista[i] > max_actual + lista[i]:
            max_actual = lista[i]
            temp_inicio = i
        else:
            max_actual += lista[i]

        if max_actual > max_global:
            max_global = max_actual
            inicio = temp_inicio
            fin = i

    return lista[inicio:fin+1]

# # Ejemplo de uso
# lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# sublista_maxima = encontrar_sublista_maxima(lista)
# print(sublista_maxima)  # Output: [4, -1, 2, 1]

# Ejercicio 2: Permutaciones de una lista
# Escribe una función que genere todas las permutaciones posibles de una lista.
from itertools import permutations
def permutacion(lista):
    return print(list(permutations(lista)))

lista = [1, 2, 3]
permutacion(lista)
# Ejercicio 3: Combinaciones de una lista
# Escribe una función que genere todas las combinaciones posibles de una lista para un tamaño dado.
def combinaciones_lista(lista, tam):
    if tam == 0:
        return [[]]
    if tam > len(lista):
        return []
    
    combinaciones = []
    for i in range(len(lista)):
        elemento_actual = lista[i]
        lista_restante = lista[i+1:]
        for c in combinaciones_lista(lista_restante, tam-1):
            combinaciones.append([elemento_actual] + c)
    
    return combinaciones

# # Ejemplo de uso
# lista = [1, 2, 3]
# tamaño = 2
# combinaciones = combinaciones_lista(lista, tamaño)
# print(combinaciones)

# Ejercicio 4: Producto cartesiano de listas
# Escribe una función que tome dos listas y devuelva el producto cartesiano de ambas listas.
def producto_cartesiano(lista1, lista2):
    res = []
    if len(lista1) == 0 or len(lista2) == 0:
        return print("La lista 1 o 2 necesita almenos un elemento")
    
    for element in lista1:
        for element2 in lista2:
            res.append((element,element2))
    print(res)
# lista1 = [1,2,3]
# lista2 = ['a', 'b', 'c']
# producto_cartesiano(lista1, lista2)

# Ejercicio 5: Eliminar elementos duplicados manteniendo el orden
# Escribe una función que elimine los elementos duplicados de una lista manteniendo el orden original.
def eliminar_duplicados(lista):
    res = []
    for elemento in lista:
        if elemento not in res:
            res.append(elemento)
    print(res)

lista = [1, 2, 2, 3, 4, 4, 5]
eliminar_duplicados(lista)
# Ejercicio 6: Encontrar la intersección de múltiples listas
# Escribe una función que tome múltiples listas y devuelva una nueva lista con los elementos comunes a todas las listas.

# Ejercicio 7: Dividir una lista en partes iguales
# Escribe una función que divida una lista en n partes iguales. Si la lista no se puede dividir exactamente, las partes restantes deben ser lo más iguales posible.

# Ejercicio 8: Encontrar la mediana de una lista
# Escribe una función que encuentre la mediana de una lista de números.

# Ejercicio 9: Ordenar una lista de listas por un índice específico
# Escribe una función que tome una lista de listas y la ordene por un índice específico de las sublistas.

# Ejercicio 10: Encontrar la diferencia simétrica de dos listas
# Escribe una función que encuentre la diferencia simétrica de dos listas (elementos que están en una lista o en la otra, pero no en ambas).