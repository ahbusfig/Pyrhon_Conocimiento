# Ejemplos de diferentes tipos de bucles en Python

# Bucle for con range -> se repite 5 veces 
print("Bucle --> range")
for i in range(5):
    print(f"Iteración {i}")
print("\n")
# Bucle for sobre una lista
print("Bucle --> array")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
print("\n")

# Bucle for sobre un diccionario
print("Bucle --> diccionario")
edades = {"Juan": 25, "Ana": 30, "Luis": 35}
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")
print("\n")

# Bucle while
print("Bucle --> while")
contador = 0
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1
print("\n")

# Bucle while con break
print("Bucle --> while con break")
contador = 0
while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador >= 5:
        break
print("\n")

# Bucle for con else
print("Bucle --> for-else")
for i in range(5):
    print(f"Iteración {i}")
else:
    print("Bucle for terminado")
print("\n")

# Bucle while con else
print("Bucle --> while-else")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("Bucle while terminado")