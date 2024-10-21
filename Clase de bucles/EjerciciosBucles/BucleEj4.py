""" 
1. **Filtrar y ordenar una lista de tuplas**
   - Dada una lista de tuplas, donde cada tupla contiene un nombre y una edad, 
    filtra las tuplas para incluir solo aquellas personas mayores de 30 años y luego
    ordena la lista por edad en orden descendente.
"""
personas = [("Juan", 25), ("Ana", 32), ("Luis", 45), ("Marta", 29), ("Pedro", 35)]
print(type(personas))
def filtroMayor30(personas):
   resultado = []
   for item in personas:
      if item[1] > 29:
         resultado.append(item)
   return resultado
#print(filtroMayor30(personas))

def ordenarMayor30(personas):
   #return sorted(personas, key=lambda x: x[1], reverse=True)
   n = len(personas)
   for i in range(n):
      for j in range(0, n-i-1):
            if personas[j][1] < personas[j+1][1]:
               # Intercambiar si el elemento encontrado es menor que el siguiente elemento
               personas[j], personas[j+1] = personas[j+1], personas[j]
   return personas

#print(ordenarMayor30(filtroMayor30(personas)))


"""
2. **Contar palabras únicas en un texto**
   - Dado un texto, cuenta cuántas palabras únicas hay en el texto. Ignora las diferencias entre mayúsculas
    y minúsculas y elimina la puntuación.
"""
import string
texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."
def ContarPalabrasUnicas(texto):
   res = texto.translate(str.maketrans("", "", string.punctuation))
   res = res.lower().split()
   #Usamos conjuntos para obtener las palabras/elementos unicas   
   #return set(res)

   #Mediante bucles --> tamb es posible
   palabras_unicas = []
   for palabra in res: #Itera por cada palabra del texto
      if palabra not in palabras_unicas:
         palabras_unicas.append(palabra)
   return palabras_unicas


#print(ContarPalabrasUnicas(texto))
#print(f"El texto tienen {len(ContarPalabrasUnicas(texto))} palabras unicas")

""" 
3. **Intersección de conjuntos**
   - Dado un diccionario donde las claves son nombres de estudiantes y los valores son conjuntos de cursos 
   en los que están inscritos, encuentra los cursos comunes a todos los estudiantes.
"""
estudiantes_cursos = {
    "Juan": {"Matemáticas", "Física", "Química"},
    "Ana": {"Matemáticas", "Biología", "Química"},
    "Luis": {"Matemáticas", "Física", "Química", "Biología"},
    "Marta": {"Matemáticas", "Química"}
}

def cursos_comunes_con_bucle(estudiantes_cursos):
    # Obtener la lista de conjuntos de cursos
    lista_cursos = list(estudiantes_cursos.values()) #Devuelve lista con todos las asignaturas de todos los estudiantes
   
    cursos_comunes = lista_cursos[0]
    
    # Iterar sobre los conjuntos de cursos restantes y actualizar la intersección
    for cursos in lista_cursos[1:]:
        cursos_comunes = cursos_comunes.intersection(cursos)
    
    return cursos_comunes

#print(cursos_comunes_con_bucle(estudiantes_cursos))
"""
4. **Agrupar elementos por clave**
   - Dada una lista de tuplas, donde cada tupla contiene una clave y un valor, agrupa los valores por clave en un diccionario.
"""
lista_tuplas = [
    ("a", 1),
    ("b", 2),
    ("a", 3),
    ("b", 4),
    ("c", 5),
    ("a", 6),
    ("c", 7)
]

def agrupar_por_clave(lista_tuplas):
    # Diccionario para agrupar los valores por clave
    diccionario_agrupado = {}
    
    # Iterar sobre la lista de tuplas
    for clave, valor in lista_tuplas:
        # Si la clave no está en el diccionario, agregarla con una lista vacía
        if clave not in diccionario_agrupado:
            diccionario_agrupado[clave] = []
        # Agregar el valor a la lista correspondiente a la clave
        diccionario_agrupado[clave].append(valor)
    
    return diccionario_agrupado

print(agrupar_por_clave(lista_tuplas))
"""
5. **Encontrar la moda en una lista**
   - Dada una lista de números, encuentra el número que más veces se repite (la moda). 
   Si hay más de una moda, devuelve todas.
"""

"""
6. **Transformar un diccionario**
   - Dado un diccionario donde las claves son nombres de productos y los valores son listas de precios históricos,
    transforma el diccionario para que las claves sean los nombres de los productos y los valores sean el precio 
    promedio de cada producto.
"""

"""
7. **Generar una matriz de adyacencia**
   - Dada una lista de aristas de un grafo no dirigido, donde cada arista es una tupla de dos nodos,
   genera una matriz de adyacencia que represente el grafo.
"""

"""
8. **Contar elementos únicos en listas anidadas**
   - Dada una lista de listas, cuenta cuántos elementos únicos hay en total en todas las listas anidadas.
"""

"""
9. **Encontrar la subsecuencia creciente más larga**
   - Dada una lista de números, encuentra la subsecuencia creciente más larga. Una subsecuencia es 
   una secuencia que se puede derivar de otra secuencia eliminando algunos elementos sin cambiar el 
   orden de los elementos restantes.
"""

"""
10. **Combinar diccionarios**
    - Dado un diccionario donde las claves son nombres de productos y los valores son listas de precios 
    en diferentes tiendas, combina los diccionarios de dos tiendas diferentes para obtener un solo diccionario 
    con los precios más bajos para cada producto.

"""