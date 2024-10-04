#!/usr/bin/env python3
#Bucle anidado

lista = [[1,2,3],[1,2,3],[1,2,3]]

for element in lista:
    print(f"\n[+] Vamos a desglosar {element}")
    for el_in_list in element:
        print(el_in_list)
print("\n")

# Lista de comprension (for)

odd_lis = [1,3,5,7,9]

cuadrado = [i ** 2 for i in odd_lis]
print(cuadrado )
print("\n")


# El uso del breck en un bucle -> finalizar antes
for i in range(10):
    print(i) # --> fin en 5
    if i == 5:
        break
    #print(i) --> fin en 4 orden es importante