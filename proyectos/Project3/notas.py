#!/usr/bin/env 
class Nota:
    def __init__(self,contenido):
        self.contenido = contenido

    def __str__(self):
        return f"{self.contenido}"
    
    def __rptr__(self):
        return f"{self.contenido}"

    def coincide(self, texto_buscado):
        return texto_buscado in self.contenido