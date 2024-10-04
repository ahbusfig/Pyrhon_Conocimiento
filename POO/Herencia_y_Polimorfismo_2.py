class Dispositivo:
    def __init__(self,modelo):
        self.modelo = modelo
    
    def escanear_vulnerabilidades(self):
        raise NotImplementedError("Esto se completará en las subclases!!")
    
    def __str__(self):
        return f"Dispositivo {self.modelo}"
    
class Ordenador(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[+] analisis de vulnerabilidades concluido: Hay que solucionar algunos problemas"
    
class Router(Dispositivo):
     def escanear_vulnerabilidades(self):
        return f"[+] analisis de vulnerabilidades concluido: Multiples puertos criticos abierto !!"
    
class Movil(Dispositivo):
     def escanear_vulnerabilidades(self):
        return f"[+] analisis de vulnerabilidades concluido: Multiples apps con permisos excesivos !!"

#Polimorfismo
def realizar_escaneo(dispositivo):
    return print(f"{dispositivo} --> ",dispositivo.escanear_vulnerabilidades())

pc = Ordenador("Dell xps")
router = Router("Tp-link archer C56")
movil = Movil("Iphone16")

# Lista de dispositivos
dispositivos = [pc, router, movil]

# Bucle para realizar los escaneos
for dispositivo in dispositivos:
    realizar_escaneo(dispositivo)
