def decorador_Persona(funcion):
    def envoltura(*args, **kwargs):
        print(f"Inicio de la función {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(resultado)
        print(f"Final de la función {funcion.__name__}")
        return resultado
    return envoltura

class Persona:
    listaPersonas = []
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        #Para guardar una lista que va guardando el objeto
        Persona.listaPersonas.append(self)
    @property #Decorador getter --> nombre
    def nombre(self):
        return self._nombre

    @nombre.setter #Decorador setter --> nombre
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @property #Decorador getter --> edad
    def edad(self):
        return self._edad

    @edad.setter #Decorador setter --> edad
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = valor
    def __str__(self):
        return f"Me llamo {self._nombre} y tengo {self._edad} años"
    
    @decorador_Persona
    @staticmethod
    def obtener_lista_personas():
        return Persona.listaPersonas
    
    def __repr__(self):
       return f"Persona(nombre={self._nombre}, edad={self._edad})"

# Crear una instancia de Persona
persona = Persona("Juan", 30)

# Usar el getter para obtener el nombre y la edad
print(persona.nombre)  # Juan
print(persona.edad)    # 30

# Usar el setter para cambiar el nombre y la edad
persona.nombre = "Ana"
persona.edad = 25

# Verificar los cambios
print(persona.nombre)  # Ana
print(persona.edad)    # 25

# Intentar asignar un nombre vacío (esto lanzará una excepción)
try:
    persona.nombre = ""
except ValueError as e:
    print(e)  # El nombre no puede estar vacío.

# Intentar asignar una edad negativa (esto lanzará una excepción)
try:
    persona.edad = -5
except ValueError as e:
    print(e)  # La edad no puede ser negativa.

# Imprimir la representación de la persona
print(persona)  # Persona(nombre=Ana, edad=25)

#Añadir una 2 persona
persona2 = Persona("Marta",21)
#Imprimir lista de dnis
lista_personas = Persona.obtener_lista_personas()
"""i = 0
for persona in lista_personas:
    print(f"La persona {i+1} --> ", persona)
    i += 1"""