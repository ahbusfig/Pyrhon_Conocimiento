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

#print(f"El resultado de {n}! es --> {calcular_factorial(n)}")
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
listado = []
for i in range(20):
    listado.append(i)

#print(listado)
#print(f"1 posicion --> {listado[1]}")
#print(f"ultima posicion --> {listado[-1]}")

def contador_elementos(lista):
    contador = 0
    i = 0
    while True:
        try:
            lista[i]
            contador += 1
            i += 1
        except IndexError:
            break
    return contador

print(contador_elementos(listado)) 
"""
14. Generar los primeros N números de la secuencia de Fibonacci
Usa un bucle for para generar los primeros N números de la secuencia de Fibonacci.
"""
n = 10

def fibonnaci_seq(n):
    total = 0
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci = [0, 1] #Definir los primeros dos 
    for i in range(2, n): #Bucle en rango de 2 a n
        siguiente = fibonacci[-1] + fibonacci[-2] #en la var siguiente se guarda la suma del ultimo y penultimo de la lista
        fibonacci.append(siguiente)#Se añade a la lista
    
    return fibonacci

#print(fibonnaci_seq(10))

"""
15. Contar apariciones de una palabra en una cadena
Dada una cadena de texto, cuenta cuántas veces aparece una palabra específica.
"""
cadena = "Esta es una cadena de texto. Esta cadena es solo un ejemplo de cadena."
palabra = "un"
def contador_palabras_en_cadena(cadena,palabra):
    contador = 0 
    cadena = cadena.split() #Separar las palabras en elementos --> para el bucle
    for elemento in cadena:
        if elemento == palabra:
            contador += 1
    if contador == 0:
        return f"La plabra no aparece "
    elif contador == 1:    
        return f"La plabra aparece {contador} vez "
    
    return f"La plabra aparece {contador} veces "
    """
        Una forma sencilla usando --> cadena.count(palabra)
    """
#print(contador_palabras_en_cadena(cadena,palabra))
"""
16. Imprimir una pirámide de números
Escribe un programa que imprima una pirámide de números. Por ejemplo, para una entrada n = 5:
"""
n = 5
def imprimir_piramide_mitad(n):
    numeros = 1
    for fila in range(1,n+1):     
        print(f"{numeros}"*fila)
        numeros += 1
    
imprimir_piramide_mitad(n)

def imprimir_piramide_completa(n):
    for fila in range(1, n + 1):
        # Imprimir espacios en blanco para centrar la pirámide
        for espacio in range(n - fila):
            print(" ", end="")
        # Imprimir los números en orden ascendente
        for numero in range(1, fila + 1):
            print(numero, end="")
        # Imprimir los números en orden descendente
        for numero in range(fila - 1, 0, -1):
            print(numero, end="")
        print()  # Nueva línea después de cada fila


imprimir_piramide_completa(n)