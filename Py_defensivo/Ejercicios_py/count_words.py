"""
    Instrucciones:
    Crea una función count_words que reciba una lista de palabras y 
    devuelva un diccionario donde las claves son las palabras y los valores 
    son el número de veces que cada palabra aparece en la lista.

Ejemplo de entrada:
    palabras = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]
Salida esperada:
    {'manzana': 3, 'banana': 2, 'naranja': 1}
"""
palabras = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]

def count_words(lista_palabras):
    # Creamos un diccionario vacío para contar las palabras
    contador_palabras = {}
    
    # Iteramos sobre cada palabra en la lista
    for palabra in lista_palabras:
        # Si la palabra ya está en el diccionario, incrementamos su contador
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        # Si la palabra no está, la agregamos al diccionario con valor 1
        else:
            contador_palabras[palabra] = 1

    return contador_palabras

print(count_words(palabras))
