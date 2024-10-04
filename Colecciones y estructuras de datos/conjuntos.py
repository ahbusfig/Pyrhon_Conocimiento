"""
  conjuntos propiedades:
        Elementos Únicos: No hay elementos repetidos y no suele estar ordenados

        Mutable: Se pueden modificar igual que las lista, pero sin repetir un el. existente

        Operaciones de Conjuntos: Los conjuntos soportan operaciones matemáticas como 
                                  unión, intersección, diferencia y diferencia simétrica.

        Tipos de Datos: Los elementos de un conjunto deben ser inmutables (por ejemplo, números, cadenas, tuplas). 
                        No se pueden usar listas o diccionarios como elementos de un conjunto.
"""
mi_conjunto = {1,2,3}
print("\n Vamos a usar metodos utiles para modificar conjuntos --> add, update, remove, discar")
mi_conjunto.add(4) #Añade un nuevo el. al conjunto
mi_conjunto.update({5,6,7,8})#Añade varios el. ...
print(mi_conjunto)
mi_conjunto.remove(3)#Remueve un elemento -> q exista ojoo
mi_conjunto.discard(11)#Elimina el el. si existe sino no hace nadas
print(mi_conjunto)

print("\n Vamos a hacer operaciones de conjuntos")
primer_con = {1,2,3,4}
segundo_con = {2,9,1,8,15}

conj_final = primer_con.union(segundo_con) #Une los conjuntos sin repeticion
print(conj_final)


print("\n La operacion issubset -> para saber si un conjunto contiene un subconjunto de otro ")
primer_con = {1,2,3,4}
segundo_con = {2,9,1,3,4,15} #issubset se usa para cualquier tipo de elemento !
print(primer_con.issubset(segundo_con)) #Será true debido a que dentro 2 conj está el subconj 1



print("\n Es util para transformar una lista con elementos repes en otra sin ese problema")
lista1 = [1,2,2,3,3,7,5,6,9,0,2,3,5,7,4,9]
print("lista original --> %s" %lista1)
norepeat = list(set(lista1))#set() --> lo transforma en conj y list() --> lo vuelve a pasar a lista
print(norepeat)



mi_conjunto = set(range(20))
print( 1,2,3,4 in mi_conjunto)

# Ejemplo de intersección
print("\n La operacion intersection -> para obtener los elementos comunes entre dos conjuntos")
primer_con = {1, 2, 3, 4}
segundo_con = {2, 9, 1, 3, 4, 15}
interseccion = primer_con.intersection(segundo_con)
print("Intersección:", interseccion) # Salida: {1, 2, 3, 4}

# Ejemplo de diferencia
print("\n La operacion difference -> para obtener los elementos que están en el primer conjunto pero no en el segundo")
diferencia = primer_con.difference(segundo_con)
print("Diferencia:", diferencia) # Salida: set() ya que todos los elementos de primer_con están en segundo_con

# Ejemplo de diferencia con elementos no comunes
primer_con = {1, 2, 3, 4, 5}
segundo_con = {2, 9, 1, 3, 4, 15}
diferencia = primer_con.difference(segundo_con)
print("Diferencia con elementos no comunes:", diferencia) # Salida: {5}