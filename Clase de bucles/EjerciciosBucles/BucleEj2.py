"""
    1. Suma de números pares e impares en un rango p.e 20
"""
#Los numeros pares se obtiene al dividir el numero/2 y obtener un resto = 0
def num_par(num):
    return num%2 == 0   #print(num_par(9)) Devuelve False pq no es par , 10 seria True

#Para obtener el impar simplemente el resto ha de ser != de 0
def num_impar(num):
    return num%2 != 0

n = 20 #Definimos el rango de 0 a 20
listaPares = []
for i in range(n+1):
    if num_par(i):
        listaPares.append(i)

listaImpares = []
for i in range(n+1):
    if num_impar(i):
        listaImpares.append(i)

print(f"\nLista de numeros Pares --> {', '.join(map(str, listaPares))}")
print(f"Lista de numeros Impares --> { listaImpares } \n")


"""
    2. Imprimir los elementos de una lista
    Dada una lista, imprime cada uno de los elementos usando un bucle for.
"""
mi_lista = ["manzana", "banana", [1,2,3, [1,2]],  {
    "Nmap": "Herramienta de escaneo de red"}, 3]

i = 0
for elemento in mi_lista:
    print(f"Elemento {i+1} --> {elemento}")
    i+= 1

"""
    3. Contar vocales en una cadena
    Escribe un programa que reciba una cadena y cuente cuántas vocales hay usando un bucle for y condicionales.
"""
def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    contador = 0
    for elemento in cadena: #Cada letra en la cadena 
        for vocal in vocales: #Cada vocal en vocales
            if vocal == elemento: #comparar en cada iteracion si el elemento es alguna vocal
                contador += 1 #Si lo es suma 1 al contador
    return f"Se han contado {contador} vocales en la cadena"

cadena = "Hola Esta es Una cadena " #10 vocales
#print(contar_vocales(cadena))


"""
    4. Imprimir elementos de una tupla
    Usa un bucle while para recorrer una tupla y imprimir cada uno de sus elementos.
"""
tupla = (1,2,3,4,5)
i = 0
lista = []
while i < len(tupla):
    lista.append(tupla[i])
    i += 1

print( ', '.join(map(str,lista)))



"""
    5. Filtrar elementos de una lista
    Dada una lista de números, imprime solo aquellos que sean < que 10 usando un bucle while
    y una condición if.
"""
import random
#Inicializar lista
lista = []
#Hacemos una lista de 20 elementos aleatorios de 1 a 20
for i in range(20):
    lista.append(random.randint(1,20))

def menor_10(lista):
    print(lista , len(lista))
    lista_menor_10 = []
    i = 0
    while i < len(lista):
        if lista[i] <= 10:
            lista_menor_10.append(lista[i])
        i+=1
    return lista_menor_10

#print(menor_10(lista))

"""
    6. Buscar un valor en un diccionario
    Dado un diccionario con nombres y edades, encuentra e imprime el nombre de la persona cuya edad es mayor a 30.
"""
diccionario = {"Alain":23, "Marta":40, "Laia":30, "Raul":34, "Pepe":52}
def mayor_30(diccionario):
    for nombre,edad in diccionario.items():
        if edad >= 30:
            print(f"{nombre} tiene {edad} años")

#print(mayor_30(diccionario))
"""
    7. Tabla de multiplicar
    Usa un bucle while para generar la tabla de multiplicar de un número dado por el usuario.
"""
num = 5
def tabla_multiplicar(num):
    i = 0
    print(f"Tabla de multiplicar del--> {num}")
    while i <= 10:
        print(f"\t {num}x{i}= {num*i}")
        i += 1
#tabla_multiplicar(num)
"""
    8. Invertir una lista
    Escribe un programa que use un bucle para invertir una lista sin utilizar métodos predefinidos como .reverse().
"""
lista = []
for i in range(15):
    lista.append(i)

def revertir_lista(lista):
    print(lista)
    i = len(lista) - 1
    lista_inv = []
    while i <= len(lista) and i >= 0:
        lista_inv.append(lista[i])
        i -= 1
    return lista_inv

#print(revertir_lista(lista))

"""
9. Eliminar duplicados en una lista
Dada una lista con elementos repetidos, utiliza un conjunto (set) para eliminar los duplicados 
y luego convierte el conjunto en una lista.
"""
#Manera más sencilla
lista_dup = [1,2,2,4,5,5,5,6,7,7,8]
#print(lista_dup)
#lista_sindup = list(set(lista_dup))
#print(lista_sindup)

#Manera con bucles
def elimina_dup(lista):
    lista_sin_dup = []
    contador = 0
    # Iterar sobre la lista original
    for numero in lista:
        # Si el número no está en la lista de únicos, lo añadimos
        if numero not in lista_sin_dup:
            lista_sin_dup.append(numero)
        contador += 1  # Incrementar el contador en cada iteración
    print(f"Total de iteraciones: {contador}")
    return lista_sin_dup

print(elimina_dup(lista_dup))

"""
10. Imprimir los números del 1 al 100 que sean divisibles por 3 o 5
Usa un bucle for y un condicional para imprimir todos los números entre 1 y 100 que sean divisibles por 3 o por 5.
"""
def imprimir_divisibles():
    lista = []
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0: #Condicion de que sea divisibles por 3 o por 5
            lista.append(i)
    return lista

# Llamada a la función
print(imprimir_divisibles())