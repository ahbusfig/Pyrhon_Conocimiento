#!/usr/bin/env python
#Importaciones
from termcolor import colored
#Clase
class dict_ej_intermedios:
    def __init__(self, diccionario1, diccionario2):
        self.diccionario1 = diccionario1
        self.diccionario2 = diccionario2

    def ej1_contar_elementos_dict(self):
        print(colored(self.diccionario1, "green"))
        contador_claves = 0
        lista_claves = []
        lista_valores = []
        elementos_por_clave = {}
        
        for clave, valor in self.diccionario1.items():
            if clave:
                contador_claves += 1
                lista_claves.append(clave)
                lista_valores.append(str(valor))
                
                # Contar elementos por cada clave
                if isinstance(valor, (list, tuple, set, dict)):
                    elementos_por_clave[clave] = len(valor)
                else:
                    if valor == "":
                        elementos_por_clave[clave]= 0
                    else:    
                        elementos_por_clave[clave]= 1

        
        print(f"\nLas claves son {' , '.join(lista_claves)}.")
        print(f"Los valores son {' , '.join(lista_valores)}.")
        print(f"El diccionario tiene {contador_claves} claves")
        print(f"Elementos por cada clave: {elementos_por_clave} ")

    def ej2_fusionar_2_dict(self):
        print(colored(f"Vamos a unir dos diccionarios diferentes --> ", "green"))
        print(colored(self.diccionario1, "green"))
        print(colored(self.diccionario2, "green"))
        #Crear otro dict para guardar dict1 y se modifique el nuevo sin modificar el original
        diccionario3 = self.diccionario1
        diccionario3.update(self.diccionario2) #Update modifica el dict3 en este caso!
        return print(f"{diccionario3}\n")
    
    @staticmethod
    def ej3_dict_cuadrado(n):
        # n --> numero de claves del diccionario
        dic_cuadrado = {}
        for clave in range(1, n+1):
            cuadrado = clave*clave
            dic_cuadrado.update({clave: cuadrado})
        return print(dic_cuadrado)

        #Forma simplidicada
        #cuadrados = {n: n**2 for n in range(1, 6)}
        #return print(cuadrados)

# Ejemplo de uso
diccionario1 = {
    'a': [1, 2, 3],
    'b': (4, 5),
    'c': {6, 7, 8, 9},
    'd': 'hola'
}
diccionario2 = {"nombre":"Joan", "edad":30, "ciudad":"Valencia"}
dict_ej = dict_ej_intermedios(diccionario1,diccionario2)
dict_ej.ej1_contar_elementos_dict()
dict_ej.ej2_fusionar_2_dict()
dict_ej.ej3_dict_cuadrado(5)
