from termcolor import colored
"""
    Convierte una lista en una tupla ordenada ascendentemente.

    Parámetros:
    lista (list): Lista de números enteros.

    Retorno:
    tuple: Tupla con los números ordenados de menor a mayor.
"""

lista = [4, 2, 9, 1]

def convert_to_tuple_and_sort(lista):
    return tuple(sorted(lista))

def convert_to_tuple_and_sort_conBucle(lista):
    n = len(lista)      # Guardamos la longitud de la lista
    res = lista         # Creamos una referencia a la lista original para ordenarla

    # Bucle externo para controlar el número de pasadas
    for i in range(n):  # i va de 0 hasta n-1 (longitud de la lista - 1)
        
        # Bucle interno para la comparación de pares adyacentes
        for j in range(0, n - i - 1):  # j va de 0 a n-i-2 (compara hasta donde la lista ya está ordenada)
            
            # Comparamos elementos adyacentes
            if res[j] > res[j + 1]:    # Si el elemento actual es mayor que el siguiente:
                
                # Intercambiamos los elementos
                aux = res[j]           # Guardamos el valor de res[j] en una variable auxiliar
                res[j] = res[j + 1]    # res[j] toma el valor de res[j+1]
                res[j + 1] = aux       # res[j+1] toma el valor original de res[j] desde aux

    return tuple(res)  # Convertimos la lista ordenada de vuelta a tupla

#Ejecutamos las funciones
print(colored(f"Metodo usado para ordenar--> sorted","green"))
print(convert_to_tuple_and_sort(lista))  # Salida esperada: (1, 2, 4, 9)

print(colored(f"Metodo usado para ordenar--> burbuja","green"))
print(convert_to_tuple_and_sort_conBucle(lista))
