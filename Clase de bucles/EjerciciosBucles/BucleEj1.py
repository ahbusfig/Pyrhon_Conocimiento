"""Ejercicio 1: Imprimir números del 1 al 10
Escribe un bucle for que imprima los números del 1 al 10."""

print("Ejercicio 1: Imprimir números del 1 al 10")
i = 0
while i< 11:
    print(i)
    i+=1
print("\n")

"""Ejercicio 2: Sumar números del 1 al 100
Escribe un bucle while que sume los números del 1 al 100 y muestre el resultado."""

accum = 0
i = 0
for i in range(101):
    accum += i
    i +=1 
print("Forma 1 --> El resultado es %d" %accum)

i= 0
accum = 0
while i < 101:
    accum += i
    i += 1
print("Forma 2 --> El resultado es %d" %accum)
