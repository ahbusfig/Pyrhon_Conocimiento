#!/usr/bin/env python
#Importaciones
from termcolor import colored
#Clase
class dict_ej_avanzado:
    def __init__(self, diccionario1, diccionario2=0):
        self.diccionario1 = diccionario1
        self.diccionario2 = diccionario2
    """
    Inverting Dictionary with Duplicate Values
        Task: Write a function that takes a dictionary and inverts its keys and values. If there are duplicate values in the original dictionary, store the corresponding original keys in a list.
        Example:
        original = {"a": 1, "b": 2, "c": 1}
        # Output: {1: ["a", "c"], 2: ["b"]}
    """
    def invert_dict_with_duplicates_values(self):
        # Invertir y juntar duplicados
        print(self.diccionario1)  #original = {"a": 1, "b": 2, "c": 1}
        res = {}
        for key, value in self.diccionario1.items():
            if value in res:
                res[value].append(key)
            else:
                res[value] = [key] # Invierte el diccionario
        print(res)
    """
    Merging Dictionaries with Summed Values
        Task: Write a function that takes two dictionaries with numerical values and returns a new dictionary. If a key exists in both dictionaries, the values should be summed; otherwise, include the key with its original value.
        Example:
        dict1 = {"a": 10, "b": 20, "c": 30}
        dict2 = {"b": 15, "c": 5, "d": 25}
        # Output: {"a": 10, "b": 35, "c": 35, "d": 25}
    """
    def Dictionaries_with_Summed_Values(self):
        res = {}
        for key, value in self.diccionario1.items():
            if key in self.diccionario2:
                res[key] = value + self.diccionario2[key]
            else:
                res[key] = value

        for key, value in self.diccionario2.items():
            if key not in res:
                res[key] = value
        print(res)

#Ejecucion de las funciones y clase
diccionario1 = {"a": 1, "b": 2, "c": 23 , "D": 23, "L":2}
diccionario2 = {"a": 4, "b": 3, "c": 27 , "D": 23, "R":4}

ej_advanced = dict_ej_avanzado(diccionario1, diccionario2)

#Ej1 --> Inverting Dictionary with Duplicate Values
#ej_advanced.invert_dict_with_duplicates_values()
ej_advanced.Dictionaries_with_Summed_Values()