"""
    11. Calcular el factorial de un número
Usa un bucle for para calcular el factorial de un número dado por el usuario.
p.e 5! --> 5*4*3*2*1
"""
n = 5 # Es el numero factorial de 5 
def calcular_factorial(n):
    acum = 0
    if n == 0 :
        return 1
    else:
        i = 1
        acum = 1 # Es necesario inicializarlo a 1 para la multiplicacion
        for i in range(1, n+1): #El rango --> 1 a n --> range(n) es de 0 a n-1 --> ojo !!
            acum *= i
            i += 1
        return acum    

p#rint(f"El resultado de {n}! es --> {calcular_factorial(n)}")
"""
12. Suma de valores en un diccionario
Dado un diccionario con productos y precios, calcula la suma total de los precios.
"""
productos = {"manzanas": 10 , "Platanos":11 ,"Piñas": 12, "Fresas":13}
def total_prductos(productos):
    acum = 0
    for producto, cantidad in productos.items():
        acum += cantidad
    return f"El total de todos los producctos es --> {acum} unidades"

#print(total_prductos(productos))
"""
13. Contar la cantidad de elementos en una lista
Dada una lista, usa un bucle while para contar cuántos elementos tiene la lista (sin usar len()).
"""

"""
14. Generar los primeros N números de la secuencia de Fibonacci
Usa un bucle for para generar los primeros N números de la secuencia de Fibonacci.
"""
"""
15. Contar apariciones de una palabra en una cadena
Dada una cadena de texto, cuenta cuántas veces aparece una palabra específica.
"""

"""
16. Imprimir una pirámide de números
Escribe un programa que imprima una pirámide de números. Por ejemplo, para una entrada n = 5:
"""