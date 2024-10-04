#Herencia
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def hablar(self):
        pass

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} es un gato y por tanto --> Miau"
    
class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} es un perro y por tanto --> Guau"
    
perro = Perro("Lucas")
gato = Gato("Lau")

print(perro.hablar())
print(gato.hablar())

#Polimorfismo 

def animal_habla(Animal):
    return f"{Animal.nombre} está intentando hablar"

print(animal_habla(perro))