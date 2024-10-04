#Vamos a crear  una calculadora con metodos estaticos
class calculadora:
    @staticmethod
    def suma(num1,num2):
        return num1+num2
    @staticmethod
    def resta(num1,num2):
        return num1-num2
    @staticmethod
    def multiplicacion(num1,num2):
        return num1*num2
    @staticmethod
    def dividir(num1,num2):
        try:
            return num1/num2
        except (TypeError,SyntaxError,ZeroDivisionError):
            return "\n [i] Los valores deben ser numéricos o != de 0\n"

#print(calculadora.suma(1,4))
#print(calculadora.resta(1,3))
#print(calculadora.multiplicacion(4,3))
#print(calculadora.dividir(1,0))

class automovil:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @classmethod
    def deportivos(cls, marca):
        return cls(marca, "Deportivo")
    
    @classmethod
    def sean(cls, marca):
        return cls(marca, "Sean")
    
    def __str__(self):
        return f"El coche es un {self.marca} y es un modelo --> {self.modelo}"
    
#deportivo = print(automovil.deportivos("Ferrari"))
#sean = print(automovil.sean("Toyota"))


class estudiante:
    estudiantes = []

    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        estudiante.estudiantes.append(self)

    @staticmethod
    def es_mayor_edad(edad):
        if edad >= 18:
            return edad >= 18

    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor_edad(edad):
            return cls(nombre,edad)
        else:
            return f"Error: El estudiante {nombre} es menor de edad"
    
    @staticmethod
    def mostrar_estudiantes():
        print("\n [i] Lista de estudiantes: ")
        for i, alumno in enumerate(estudiante.estudiantes):
            print(f"\t [i] Estudiante {i+1}: {alumno}")
        
    def __str__(self):
       return f"El estudiante se llama {self.nombre} y tiene {self.edad} años"
    
print(estudiante("Prueba",31))
print(estudiante.crear_estudiante("Alain",24))
print(estudiante.crear_estudiante("Marta",14))
print(estudiante.crear_estudiante("Leo",54))
print(estudiante.crear_estudiante("Juan",28))
print(estudiante.crear_estudiante("Laia",22))

print(estudiante.mostrar_estudiantes())
