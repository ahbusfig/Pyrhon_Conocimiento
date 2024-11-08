from termcolor import colored
"""
Conjuntos: Intersección y Unión de Elementos Únicos
    Instrucciones:

Crea una función unique_elements que tome dos listas y realice lo siguiente:
    1.Convierte las listas en conjuntos para obtener los elementos únicos.
    2.Devuelve dos resultados: el conjunto de elementos que están en ambas listas (intersección) y el conjunto de todos los elementos (unión).

Ejemplo de entrada:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

Salida esperada:
({4, 5}, {1, 2, 3, 4, 5, 6, 7, 8})
"""
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

def unique_elements(lista1,lista2):
    Union= set(lista1).union(set(lista2))
    Interseccion= set(lista1).intersection(set(lista2))
    res = [Interseccion,Union]
    return res

def unique_elements_v2(lista1, lista2):
    # Convertimos las listas a conjuntos y calculamos la intersección y unión
    union = set(lista1) | set(lista2)
    interseccion = set(lista1) & set(lista2)
    
    # Devolvemos el resultado en una tupla
    return interseccion, union

print(colored(f"Solucion --> v1","grey"))
print(colored(unique_elements(lista1,lista2),"green"))
print(colored(f"Solucion --> v2 -->logica + simplificada","grey"))
print(colored(unique_elements_v2(lista1,lista2),"light_cyan"))
