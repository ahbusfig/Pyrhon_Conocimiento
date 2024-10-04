class libro:
    iva = 0.21  # Atributo de clase

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __eq__(self, other):
        if isinstance(other, libro):
            return self.titulo == other.titulo and self.autor == other.autor and self.paginas == other.paginas
        return False

    def __str__(self) -> str:
        return f"libro(titulo={self.titulo}, autor={self.autor}, paginas={self.paginas})"
    
    @staticmethod
    def es_libro_grande(paginas):
        return paginas > 300
    
    @staticmethod
    def precio_con_iva(precio):
        precio += precio * libro.iva 
        return f"El precio con iva es --> {precio} euros"
    
    @classmethod
    def desde_cadena(cls, cadena):
        titulo, autor, paginas = cadena.split(',')
        return cls(titulo, autor, int(paginas))

# Ejemplos de uso
libro1 = libro("El Quijote", "Miguel de Cervantes", 500)
libro2 = libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
libro3 = libro("El Principito", "Antoine de Saint-Exupéry", 96)

print(libro1)  # libro(titulo=El Quijote, autor=Miguel de Cervantes, paginas=500)
print(libro1 == libro2)  # False
print(libro1 == libro("El Quijote", "Miguel de Cervantes", 500))  # True
print(libro.es_libro_grande(libro1.paginas))  # True
print(libro.es_libro_grande(libro3.paginas))  # False 
print(libro.precio_con_iva(21))  # El precio con iva es --> 25.41 euros

# Usando el método de clase
cadena_libro = "Don Quijote,Miguel de Cervantes,500"
libro4 = libro.desde_cadena(cadena_libro)
print(libro4)  # libro(titulo=Don Quijote, autor=Miguel de Cervantes, paginas=500) 