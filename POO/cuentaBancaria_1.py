class cuentaBancaria:

    def __init__(self, nombre, iban, dinero=0):
        self.nombre = nombre
        self.iban = iban
        self.dinero = dinero

    def mostrarSaldo(self):
        return f"La cuenta: {self.iban} de {self.nombre} tiene {self.dinero}$ disponible"
    
    def ponerDinero(self, dinero):
        self.dinero += dinero
        return f"La cuenta: {self.iban} de {self.nombre} ha añadido {dinero}$ y ahora tiene {self.dinero}$ disponible"
    
    def retirarDinero(self, dinero):
        if dinero > self.dinero:
            return f"\t [!] no hay saldo suficiente, para retirar {dinero}$"
        else:
            self.dinero -= dinero
            return f"La cuenta: {self.iban} de {self.nombre} tiene {self.dinero}$ disponible"

Alain = cuentaBancaria("Alain", "12345", 1200)

print(Alain.mostrarSaldo())
print(Alain.ponerDinero(100))
print(Alain.retirarDinero(22200))