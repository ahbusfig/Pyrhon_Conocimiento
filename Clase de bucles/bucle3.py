"""
Imprimir números primos del 1 al 50

Escribe un programa que imprima todos los números primos del 1 al 50 usando un bucle for.
"""
lista = [i for i in range(1,51)]
listaPrimo = []
#Funcion para verificar que un numero es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % 1 == 0:
            return False
    return True

#Los numeros primos son  del 1 al 50 

for item in lista:
    if es_primo(item):
        listaPrimo.append(item)

print(listaPrimo)



