class cuentaBancaria:

    def __init__(self, num_cuenta, titular, saldoInicial):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.__saldo = saldoInicial #Atributo privado

    def añadirSaldo(self, cantidad):

        if cantidad > 0:
            self.__saldo += cantidad
            return f"\n [i] Se ha añadido {cantidad} euros a la cuenta. \n"
        
    def retirarSaldo(self,  cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"\n [i] Se ha retirado {cantidad} euros a la cuenta \n"
        else:
            return f"\n [e] No se ha podido retirar {cantidad}, de forma correcta.\n"
        
    def mostrarSaldo(self):
        return f"El saldo del usuario {self.titular} es de {self.__saldo} euros"
cuenta1 = cuentaBancaria("12345", "Alain", 100)
cuenta2 = cuentaBancaria("54321", "Laura", 200)

print(cuenta1.añadirSaldo(1000))
print(cuenta2.añadirSaldo(1000))

print(cuenta1.retirarSaldo(260))
print(cuenta1.retirarSaldo(260000))

print(cuenta1.mostrarSaldo())
print(cuenta2.mostrarSaldo())


# Acceso a atributos públicos
print(f"Número de cuenta : {cuenta1.num_cuenta}")
print(f"Titular de la cuenta : {cuenta2.titular}")

# Intento de acceso directo a un atributo privado (esto fallará)
"""try:
    print(f"Saldo de la cuenta de Alain: {cuenta1.__saldo}")
except AttributeError as e:
    print(f"Error: {e}")

# Acceso a un atributo privado a través de un método público
print(cuenta1.mostrar_saldo())
print(cuenta2.mostrar_saldo())
"""
# Modificación de un atributo público
cuenta1.num_cuenta = "67890"
print(f"Número de cuenta modificado de Alain: {cuenta1.num_cuenta}")

# Intento de modificación directa de un atributo privado (esto fallará)

"""try:
    cuenta1.__saldo = 500
except AttributeError as e:
    print(f"Error: {e}")
"""


class Pizza:
    def __init__(self,size,*ingredientes):
        self.size = size
        self.ingredientes = ingredientes

    def descripcion(self):

        print(f"Esta pizza tiene {self.size} cm y los ingredientes son : {", ".join(self.ingredientes)}")

pizza1 = Pizza(12, "Chorizo", "Jamon", "Bacon")

pizza1.descripcion()

