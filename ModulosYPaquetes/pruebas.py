#import OperacionesMatematicas

from  OperacionesMatematicas import suma,resta

print(suma(1,3)) #Si hemos hecho el from --> se ponde directo el metodo importado!

#print(OperacionesMatematicas.suma(5,3))  --> si hemos hecho import de todo



####Vamos a importar la libreria math
#1 forma --> importar todo y ponerle un alias
import math as m
print(m.sqrt(25))
#2 forma --> importar un metodo y ponerle un alias de math
from math import sqrt as raiz
print(raiz(25))

