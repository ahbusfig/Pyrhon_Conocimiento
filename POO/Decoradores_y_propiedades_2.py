def mi_funcion(funcion):
    def funcion_decorada(*args, **kwargs):
        print("Esto es una función dada por el decorador")
        return funcion(*args, **kwargs)
    return funcion_decorada

class Persona:
    def __init__(self,dni,nombre,edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"El dni {self.dni} --> es {self.nombre} y tiene {self.edad} años."
    
    def __eq__(self, otro):
        return self.dni == otro.dni and self.nombre == otro.nombre and self.edad == otro.edad
    
    @staticmethod
    def es_mayor_edad(edad):
        if edad >= 18:
            return f"\n El usuario es mayor de edad"
        else:
            return f"\n No es mayor de edad"
        
    def mostrar_edad(self):
        res = Persona.es_mayor_edad(self.edad)
        return f" {res}, El usuario tiene {self.edad} años."
    
    @mi_funcion
    def funcion(self):
        return f"Esto es la funcion dentro de la clase"
    
    
"""    
persona1 = Persona("26602238r", "Alain", 13)
persona2 = Persona("26602238r", "Alain", 13)

print(persona1.mostrar_edad())
print(persona1.funcion())
"""

#####################################################################################
##############################Clase Pizza############################################
#####################################################################################

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} terminó de ejecutarse")
        return result
    return wrapper

class Pizza:
    def __init__(self, nombre, precio, *ingredientes):
        self._nombre = nombre
        self._precio = precio
        self._ingredientes = list(ingredientes)

    @property #Decorador para obtener el getter 
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    @property
    def ingredientes(self):
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self, valor):
        if not isinstance(valor, list):
            raise ValueError("Los ingredientes deben ser una lista.")
        self._ingredientes = valor

    @log_decorator
    def agregar_ingrediente(self, ingrediente):
        self._ingredientes.append(ingrediente)
        print(f"Ingrediente {ingrediente} agregado.")

    def __str__(self) -> str:
        return f"La pizza se llama {self._nombre} y cuesta {self._precio} euros y sus ingredientes son --> {', '.join(self._ingredientes)}"
"""
# Crear una instancia de Pizza
pizza1 = Pizza("Hawaina", 12, "Piña", "Bacon", "Verduras")

# Usar los getters y setters
print(pizza1.nombre)  # Hawaina
print(pizza1.precio)  # 12
print(pizza1.ingredientes , "\n")  # ['Piña', 'Bacon', 'Verduras']

# Cambiar los valores usando los setters
pizza1.nombre = "Pepperoni"
pizza1.precio = 15
pizza1.ingredientes = ["Pepperoni", "Queso"]

# Verificar los cambios
print(pizza1.nombre)  # Pepperoni
print(pizza1.precio)  # 15
print(pizza1.ingredientes)  # ['Pepperoni', 'Queso']

# Usar el método decorado
pizza1.agregar_ingrediente("Champiñones")

# Imprimir la representación de la pizza
print(pizza1)  # La pizza se llama Pepperoni y cuesta 15 euros y sus ingredientes son --> Pepperoni, Queso, Champiñones
"""
