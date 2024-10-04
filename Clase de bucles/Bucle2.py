"""
Encontrar el número más grande en una lista

Dada una lista de números [3, 41, 12, 9, 74, 15],
escribe un bucle for que encuentre y muestre el número más grande.

"""
lista1 = [3,41,12,9,74,15]

#Forma rápida para obtener el máximo y min
print(f"\n Esta es la forma rapida de obtener el max max(lista1) --> {max(lista1)} " )
print(f"\n Esta es la forma rapida de obtener el min min(lista1) --> {min(lista1)} " )


# Forma manual para obtener el máximo
maximo = lista1[0]  # Inicializar con el primer elemento de la lista
for item in lista1:
    if item > maximo:
        maximo = item

print("\n Forma larga --> ", maximo)

#Forma manual para obtener el minimo de una lista 

minimo = lista1[0]
for item in lista1:
    if item < minimo:
        minimo = item

print("\n Forma larga --> ", minimo)

"""
Generar una tabla de multiplicar

Escribe un programa que genere la tabla de multiplicar del 5
usando un bucle for.
"""
#Tabla de multiplicar para el 5 --> usando un loop
n = 5 # La tabla de multiplicar para n --> n generalizar
listaMult = [0]*11
i = 0
print(listaMult)
print(f"Aqui se mostrara la lista de multiplicar para {n} --> ")
for item in listaMult:
    item = listaMult[i] + n*i
    print(f"\t {n}x{i} = ", item)
    i += 1


"""
    Imprimir números en orden inverso
    Escribe un bucle for que imprima los números del 10 al 1 en orden inverso.
"""
#Formas de crear una lista de n numeros --> range siempre el rango es hasta n-1 del que se pone
n = 12
lista1to10 = [i for i in range(1,n)]
lista1to10 = list(map(lambda x: x, range(1,n)))
print(lista1to10)
#Forma 1 -> usando reversed
listaInv = reversed(lista1to10)
i = 0
for item in listaInv:
    lista1to10[i] = item
    i +=1
print(lista1to10)
# forma2 ->  usando un bucle for
lista = [1, 2, 3, 4, 5]
lista_invertida = []
for item in lista:
    lista_invertida.insert(0, item)
print(lista_invertida)  # Output: [5, 4, 3, 2, 1]
#Forma 3 --> Usando inverse
print(lista.reverse())


"""
    Contar palabras en una cadena

Escribe un programa que cuente el número de palabras en una cadena dada usando un bucle for.
"""

cadena = "Its a game" #Creamos la cadena
contador = 0 #declarar el indice para el bucle
for caracter in cadena:
    if caracter != " ":
        contador += 1
print(f"El numero de caracteres es --> {contador}")