class Libro:
    def __init__(self, id_libro, autor, nombre_libro):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self):
        return f"Libro {self.id_libro}, autor {self.autor}, nombre {self.nombre_libro}"

    def __repr__(self):
        return self.__str__()

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro
            return "[i] Se ha añadido correctamente !"
        else:
            return "[e] Ya existe este libro !"

    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
            return f"[i] El libro con id {id_libro} ha sido prestado."
        else:
            return f"[e] No es posible prestar el libro con id {id_libro}"

    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]

class BibliotecaInfantil(Biblioteca):
    def __init__(self):
        super().__init__()
        self.libros_infantiles = {}  # Diccionario

    def agregar_libro(self, libro, es_infantil):
        super().agregar_libro(libro)
        self.libros_infantiles[libro.id_libro] = es_infantil

    def prestar_libro(self, id_libro):
        return super().prestar_libro(id_libro)

    @property
    def mostrar_libros_infantiles(self):
        return [libro for libro in self.libros.values() if self.libros_infantiles.get(libro.id_libro, False) and not libro.esta_prestado]

if __name__ == "__main__":
    biblioteca = BibliotecaInfantil()

    libro1 = Libro(1, "Alain Bustamante", "How to be successful")
    libro2 = Libro(2, "Robert Kiyosaki", "Padre rico padre pobre")
    libro3 = Libro(3, "Robert Kiyosaki", "Hagase rico y no sea tonto")
    libro4 = Libro(4, "Rubio", "Aprende a escribir")

    biblioteca.agregar_libro(libro1, False)
    biblioteca.agregar_libro(libro2, False)
    biblioteca.agregar_libro(libro3, False)
    biblioteca.agregar_libro(libro4, True)

    # Prestar un libro
    print(biblioteca.prestar_libro(1))
    print(biblioteca.prestar_libro(2))

    # Mostrar libros disponibles
    print("Libros disponibles:")
    for libro in biblioteca.mostrar_libros:
        print(libro)

    # Mostrar libros infantiles disponibles
    print("Libros infantiles disponibles:")
    for libro in biblioteca.mostrar_libros_infantiles:
        print(libro)