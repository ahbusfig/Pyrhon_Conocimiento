class Persona:
    def __init__(self, nombre, apellido, dni, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.saldo = saldo

    def __str__(self):
        return f"Persona({self.nombre}, {self.apellido}, {self.dni}, Saldo: {self.saldo})"

    def añadir_dinero(self, cantidad):
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        return f"Saldo disponible --> {self.saldo} euros" 