class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludo(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"
    
marcelo = Persona("Marcelo", 23)

print(marcelo.saludo())

class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def saludo(self):
        print(f"Hola soy {self.nombre} y soy un {self.tipo} ")

perro = Animal("Lucas","Perro")
gato = Animal("Puc","Gato")

perro.saludo()
gato.saludo()

print(perro) #Sin el __str__ creado --> nos dice que es un objeto yaban