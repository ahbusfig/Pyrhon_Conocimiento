#!/usr/bin/env 
import pickle
from notas import Nota
class GestorNotas:
    def __init__(self,archivo_nota='notas.pkl'):
        self.archivo_nota = archivo_nota

        try:
            with open(self.archivo_nota, 'rb') as f:
                self.notas = pickle.load(f)
                     
        except FileNotFoundError:
            self.notas = []

    def guardar_notas(self):
        with open(self.archivo_nota, 'wb') as f:
            pickle.dump(self.notas, f)
            
    def agregar_nota(self, contenido):
        self.notas.append(Nota(contenido))
        self.guardar_notas()

    def leer_notas(self):
        return self.notas
    
    def buscar_nota(self,textobuscado):
        return [nota for nota in self.notas if nota.coincide(textobuscado)]
    
    def eliminar_nota(self, indice):
        if indice < len(self.notas):
            self.notas.pop(indice)
            #del self.notas[indice]
            self.guardar_notas()
            return print(f"Se ha eliminado la nota correctamente!")
        else:
            return print(f"No se ha podido realizar la operacion--> ponga un indice correcto!")
