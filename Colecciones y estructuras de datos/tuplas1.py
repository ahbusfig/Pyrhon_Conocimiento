example = (1,2,3,4,5)
print(example[1])

#No podemos hacer cambios en la tupla como en la lista
#example[0] = 1 --> da error  --> no usa mismo comandos que listas, menos comandos!

#Tupla con varios tipos de elementos
example2 = (1,"test",[1,2,3], True, {"Manzana":1, "Pera":2},6)
#Tupla contenida dentro de otra tupla
example3 = (1,"test",(1,2,3), True, {"Manzana":1, "Pera":2},6)

#Podemos asignar el contenido de la tupla a variables de esta forma
tupla = (1,2,3,4)
a,b,c,d = tupla
print(a, b , c)

#Para añadir o quitar elementos de una tupla de forma directa como las listas
#Como las tuplas son inmutables -> podemos crear nuevas tuplas a partir de antiguas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2 #(1, 2, 3, 4, 5, 6)
print(tupla3)
tupla4 = tupla1*3 + tupla2 #Simplemente multiplica la longitud de la tupla resultante
print(tupla4) #(1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6)


#!/usr/bin/env python3
#Creamos una tupla nueva 
mi_tupla = (1,2,3,4,5,6,7,8)
#Crear otra tupla a partir de la original, que cumpla ciertas condiciones
numeros_pares = tuple(i for i in mi_tupla if i % 2 == 0) #Queremos listar de la tupla orig, los num. pares
print(numeros_pares)


"""ahbusfig: Diferencia entre tupla y lista

GitHub Copilot: Las principales diferencias entre una tupla y una lista en Python son:

1. **Mutabilidad**:
   - **Tupla**: Inmutable. Una vez creada, no se pueden cambiar sus elementos.
   - **Lista**: Mutable. Se pueden modificar, añadir o eliminar elementos después de su creación.

2. **Sintaxis**:
   - **Tupla**: Se define usando paréntesis `()`.
   - **Lista**: Se define usando corchetes `[]`.

3. **Uso**:
   - **Tupla**: Se usa cuando se necesita una colección de elementos que no deben cambiar a lo largo del tiempo.
   - **Lista**: Se usa cuando se necesita una colección de elementos que puede cambiar.

4. **Rendimiento**:
   - **Tupla**: Generalmente más rápida que una lista debido a su inmutabilidad.
   - **Lista**: Puede ser más lenta debido a la sobrecarga de la mutabilidad.

5. **Métodos**:
   - **Tupla**: Tiene menos métodos disponibles debido a su inmutabilidad.
   - **Lista**: Tiene más métodos disponibles para modificar su contenido.

Ejemplo de tupla:
```python
mi_tupla = (1, 2, 3)
```

Ejemplo de lista:
```python
mi_lista = [1, 2, 3]
```

"""