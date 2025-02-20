from termcolor import colored

# ============================================================
# Ejercicio 1: Ordenar una tupla de tuplas por múltiples criterios
# ============================================================
# Dada una tupla de tuplas, escribe una función que ordene
# las tuplas internas primero por el segundo elemento y luego
# por el primer elemento en caso de empate.
# ============================================================
def ordenar_tuplas_multiples_criterios(tupla):
    res = []
    # Ordenamos la tupla de tuplas utilizando sorted() y una función lambda
    # La función lambda ordena primero por el segundo elemento y luego por el primer elemento en caso de empate
    res = sorted(tupla, key=lambda tuple_element: (tuple_element[1], tuple_element[0]))    
    print(colored(f"La tupla ordenada es: {res}", 'green'))
    return res 
# tupla_de_tuplas = ((1, 3), (3, 2), (2, 2), (1, 2), (3, 1))
# ordenar_tuplas_multiples_criterios(tupla_de_tuplas)

# ============================================================
# Ejercicio 2: Encontrar la tupla con la suma más alta
# ============================================================
# Dada una tupla de tuplas de números, escribe una función que
# encuentre la tupla cuya suma de elementos sea la más alta.
# ============================================================
def tupla_mas_alta(tupla):
    lista_puntos = []
    puntos = 0
    for item in tupla:
        puntos = sum(item)  # Calcular la suma de la tupla actual
        lista_puntos.append((puntos, item))  # Añadir la suma y la tupla a la lista
    
    # Encontrar la tupla con la suma más alta
    max_tupla = max(lista_puntos, key=lambda x: x[0])[1]
    
    print(colored(f"La tupla con la suma más alta es: {max_tupla}", 'green'))
    print(lista_puntos)
    return max_tupla

# tupla_de_tuplas = ((1, 2, 3), (4, 5), (0, 0, 0, 10), (6, 7, 8))
# tupla_mas_alta(tupla_de_tuplas)

# ============================================================
# Ejercicio 3: Convertir una tupla de tuplas en un diccionario
# ============================================================
# Dada una tupla de tuplas, donde cada tupla contiene dos elementos,
# escribe una función que convierta esta tupla de tuplas en un
# diccionario.
# ============================================================
def tupla_to_diccionario(tupla):
    res = {} #Crear el diccionario
    for item in tupla: #Bucle para ir en cada item de la tupla
        res[item[0]] = item[1]  #Pasar al diccionario de forma correcta
    print(colored(f"\nEl diccionario resultante es: {res}\n", 'green'))
    return res

# tupla_de_tuplas = (("a", 1), ("b", 2), ("c", 3))
# tupla_to_diccionario(tupla_de_tuplas)#{"a": 1, "b": 2, "c": 3}

# ============================================================
# Ejercicio 4: Encontrar la tupla más larga
# ============================================================
# Dada una tupla de tuplas, escribe una función que encuentre
# la tupla con la mayor cantidad de elementos.
# ============================================================
def get_largest_subtuple(tupla):
    contador = []
    for item in tupla:
        contador.append(len(item))
    
    # Encontrar el índice del valor máximo en contador
    max_index = contador.index(max(contador))
    
    # Obtener la tupla más larga usando el índice encontrado
    largest_tuple = tupla[max_index]
    
    print(colored(f"La tupla más larga es: {largest_tuple}", 'green'))
    return largest_tuple

# Ejemplo de uso
# tupla_de_tuplas = ((1, 2), (3, 4, 5), (6,), (7, 8, 9, 10))
# resultado = get_largest_subtuple(tupla_de_tuplas)
# ============================================================
# Ejercicio 5: Filtrar tuplas por longitud
# ============================================================
# Dada una tupla de tuplas, escribe una función que filtre y
# devuelva solo las tuplas que tienen una longitud mayor a un
# valor dado.
# ============================================================
def filtrar_por_longitud(tupla):
    #Preguntar por la longitud
    while True:
        longitud_minima = int(input(colored(f"\n[+]Dime la longitud minima deseada --> ","yellow")))
        break
    
    #Filtrar la tupla
    res = []
    for item in tupla:
        if len(item) >= longitud_minima:
            res.append(item)
    print(tuple(res))
    return tuple(res)

# tupla_de_tuplas = ((1, 2), (3, 4, 5), (6,), (7, 8, 9, 10))
# filtrar_por_longitud(tupla_de_tuplas)

# ============================================================
# Ejercicio 6: Intercalar dos tuplas
# ============================================================
# Dadas dos tuplas, escribe una función que intercale sus elementos
# y devuelva una nueva tupla con los elementos intercalados.
# ============================================================
def intercalar_2_tuplas(tupla1, tupla2):
    res = []
    # Iterar sobre los elementos de ambas tuplas simultáneamente
    for elem1, elem2 in zip(tupla1, tupla2):
        res.append(elem1)
        res.append(elem2)
    
    # Si una tupla es más larga, añadir los elementos restantes
    if len(tupla1) > len(tupla2):
        res.extend(tupla1[len(tupla2):])
    elif len(tupla2) > len(tupla1):
        res.extend(tupla2[len(tupla1):])
    
    return tuple(res)
# # Ejemplo de uso
# tupla1 = (1, 3, 5, 7)
# tupla2 = (2, 4, 6, 8)
# resultado = intercalar_2_tuplas(tupla1, tupla2)
# print(resultado)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# # Ejemplo con tuplas de diferente longitud
# tupla1 = (1, 3)
# tupla2 = (2, 4, 6, 8)
# resultado = intercalar_2_tuplas(tupla1, tupla2)
# print(resultado)  # Output: (1, 2, 3, 4, 6, 8)

# ============================================================
# Ejercicio 7: Encontrar la diferencia simétrica de dos tuplas
# ============================================================
# Dadas dos tuplas, escribe una función que encuentre la diferencia
# simétrica entre ambas tuplas y devuelva una tupla con los elementos
# que están en una tupla o en la otra, pero no en ambas.
# ============================================================
def encontrar_dif(tupla1, tupla2):
    """------------------------  Forma mediante bucles------------------------------------
    res = []
    for item in tupla1:
        if item not in tupla2:
            res.append(item)
    for item in tupla2:
        if item not in tupla1:
            res.append(item)
    return print(colored(f"La diferencia simetrica es --> {tuple(res)}","green"))
    """
    """------------------------Forma mediante conjuntos----------------------------------"""
    # Convertir las tuplas en conjuntos
    set1 = set(tupla1)
    set2 = set(tupla2)
    # Encontrar la diferencia
    dif = set1.symmetric_difference(set2)
    #Retornar resultado
    return print(colored(f"La diferencia simetrica es --> {tuple(dif)}","green"))
# tupla1 = (1, 2, 3, 4)
# tupla2 = (3, 4, 5, 6)
# encontrar_dif(tupla1,tupla2)
# ============================================================
# Ejercicio 8: Agrupar elementos de una tupla por su tipo
# ============================================================
# Dada una tupla de elementos de diferentes tipos, escribe una función
# que agrupe los elementos por su tipo y devuelva un diccionario donde
# las claves sean los tipos y los valores sean listas de elementos de
# ese tipo.
# ============================================================
def agrupar_elementos_por_tipo(tupla):
    #Crear lista de tipos
    res = {}
    #Recorrer la tupla y logica para la funcion
    for item in tupla:
        tipo = type(item).__name__ #Obtener el tipo sin <class "tipo"> solo tipo!
        if tipo not in res:
            res[tipo] = []    
        res[tipo].append(item)
    return print(res)
# tupla = (1, "a", 2.5, "b", 3, 4.0, "c")
# agrupar_elementos_por_tipo(tupla)
# ============================================================
# Ejercicio 9: Crear una tupla de tuplas con índices
# ============================================================
# Dada una tupla de elementos, escribe una función que cree una nueva
# tupla de tuplas, donde cada tupla interna contenga el índice y el
# elemento correspondiente de la tupla original.
# ============================================================
def tupla_con_indice(tupla):
    res = []
    for i, item in enumerate(tupla):
        res.append((i, item))
    return print(colored(tuple(res),"green"))
# tupla = ("a", "b", "c", "d")
# tupla_con_indice(tupla)


# Ejercicio 10: Encontrar subsecuencias comunes en dos tuplas
# ============================================================
# Dadas dos tuplas, escribe una función que encuentre todas las
# subsecuencias comunes entre ambas tuplas y devuelva una lista
# de estas subsecuencias.
# ============================================================

def subsecuencias_comun_en2_tuplas(tupla1, tupla2):
    subsecuencias = []
    len1, len2 = len(tupla1), len(tupla2)
    
    # Buscar subsecuencias comunes
    for i in range(len1):
        for j in range(len2):
            k = 0
            while (i + k < len1) and (j + k < len2) and (tupla1[i + k] == tupla2[j + k]):
                k += 1
                if k > 1:  # Considerar solo subsecuencias de longitud mayor a 1
                    subsecuencias.append(tupla1[i:i + k])
    
    return subsecuencias

# Ejemplo de uso
tupla1 = (1, 2, 3, 4, 5, 6)
tupla2 = (3, 4, 5, 7, 8, 9, 10, 5, 6)
resultado = subsecuencias_comun_en2_tuplas(tupla1, tupla2)
print(resultado)  # Output: [(3, 4, 5), (5, 6)]