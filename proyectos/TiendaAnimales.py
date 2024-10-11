class Animal:
    def __init__(self, nombre,especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False
    
    def alimentar(self):
        self.alimentado = True

    def vender(self): #Para que animal se venda sin haberlo alimentado
        self.alimentado = False

    def __str__(self):
        return f"El {self.especie.lower()} se llama {self.nombre} - { 'Alimentado' if self.alimentado else 'hambriento' }"
class TiendaAnimales:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = [] #Creamos la lista vacia

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()

    def vender_animal(self,nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                animal.vender()
                self.animales.remove(animal)
                return f"\n[+] {nombre} ha sido vendido correctamente !"
            else:
                return f"\n[+] El nombre {nombre} no pertenece a ningun animal"

if __name__ == "__main__":
    tienda = TiendaAnimales("MiTiendaDeAnimales")
    gato = Animal("Max", "Gato")
    perro = Animal("Lucas", "Perro")

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)
    print("Mostrando los animales sin alimentar")
    tienda.mostrar_animales()
    print("Mostrando los animales una vez han sido alimentados")
    tienda.alimentar_animales()
    tienda.mostrar_animales()

    print("Vamos a vender animales")

    print(tienda.vender_animal("Max2"))
    print(tienda.vender_animal("Max"))
    tienda.mostrar_animales()
