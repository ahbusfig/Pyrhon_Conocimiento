class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True
    
    def __str__(self):
        return f"El vehiculo {self.modelo} tiene la matricula {self.modelo}, disponibilidad --> {self.disponible}"

    def alquilar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False
        
    def devolver(self):
        if self.disponible == False: #Significa --> esta siendo alquilado
            self.disponible = True
            return True
        else:
            return False
class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehiculo agregado correctamente.")

    def mostrar_flota(self):
        for vehiculo in self.vehiculos:
            #if vehiculo.disponible:
                print(vehiculo) 

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                if vehiculo.alquilar() == True:
                    return f"El vehiculo {vehiculo.modelo} con matricula {vehiculo.matricula} ha sido alquilado correctamente!"
                else:
                    return f"El vehiculo {vehiculo.modelo} con matricula {vehiculo.matricula} no está disponible actualmente!"
            else:
                return f"No se ha encontrado la matriculas --> {vehiculo.matricula}"
        
    def devolver_vehiculo(self,matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula: #Comprobar si existe la matricula
                if vehiculo.devolver() == True:
                    return f"El vehiculo {vehiculo.modelo} con matricula {vehiculo.matricula} ha sido devuelto correctamente!"
                else:
                    return f"El vehiculo {vehiculo.modelo} con matricula {vehiculo.matricula} no habia sido alquilado a nadie, no puedes devolverlo!"
            else:
                return f"No se ha encontrado la matriculas --> {vehiculo.matricula}"
        


if __name__ == "__main__":
    flota = Flota("Flota de vehículos")

    # Ejemplos de vehículos
    vehiculo1 = Vehiculo("ABC123", "Toyota Corolla")
    vehiculo2 = Vehiculo("DEF456", "Honda Civic")
    vehiculo3 = Vehiculo("GHI789", "Ford Focus")

    # Agregar vehículos a la flota
    flota.agregar_vehiculo(vehiculo1)
    flota.agregar_vehiculo(vehiculo2)
    flota.agregar_vehiculo(vehiculo3)

    # Imprimir la lista de vehículos en la flota
    flota.mostrar_flota()

    #Vamos a aquilar vehiculo 
    print(flota.alquilar_vehiculo("ABC123"))
    print(flota.alquilar_vehiculo("ABC123"))

    #Mostrar vehiculos 
    flota.mostrar_flota()
 
    #Devolver vehiculo 
    #Si vehiculo esta alquilado se puede devolver, sino muestra mensaje de que el vehiculo no está alquilado
    print(flota.devolver_vehiculo("ABC123")) #Se devuelve --> ok
    print(flota.devolver_vehiculo("ABC123"))   # No se devuelve --> el coche ya se habia devuelto en el anterior y por tanto no estaba alquilado
    print(flota.devolver_vehiculo("ABC144423")) #Error no existe esta matricula

