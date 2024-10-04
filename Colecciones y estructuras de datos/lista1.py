puertos_tcp = [21,22,80,443,8000]
#Añadir un dato nuevo al final de la lista
puertos_tcp.append(1337)
puertos_tcp.append(23)
print(puertos_tcp)
# Para ordenar datos
puertos_tcp.sort()
for puertos in puertos_tcp:
    print(f"(De - a +) Este es el puerto {puertos}")

#Obtener longitud de una lista -> util pa bucles --> print(len(lista))

#Para vaciar una lista  --> puertos_tcp.clear()

#Quitar un elemento de la lista --> del puertos_tcp[indice] | puertos_tcp.remove("elemento_nombre") | lista.pop(indice)

#Quitar un elemento del final de la lista --> lista.pop()

#Cambiar un elemento sabiendo el indice --> lista[indice] = Lo que quieras | lista.insert(indice, "cambio")

"""lista = ["Hola", 1 ,2] 
print(lista)"""