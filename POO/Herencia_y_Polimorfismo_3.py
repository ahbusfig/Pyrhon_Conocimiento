class Dispositivo:
    """
    Clase base para todos los dispositivos.
    """
    def __init__(self, modelo):
        """
        Inicializa un dispositivo con un modelo específico.
        """
        self.modelo = modelo
    
    def escanear_vulnerabilidades(self):
        """
        Método que debe ser implementado por las subclases para escanear vulnerabilidades.
        """
        raise NotImplementedError("Esto se completará en las subclases!!")
    
    def __str__(self):
        """
        Devuelve una representación en cadena del dispositivo.
        """
        return f"Dispositivo {self.modelo}"
    
class Ordenador(Dispositivo):
    """
    Clase que representa un ordenador.
    """
    def __init__(self, modelo, sistema_operativo):
        """
        Inicializa un ordenador con un modelo y un sistema operativo específico.
        """
        super().__init__(modelo)
        self.sistema_operativo = sistema_operativo
    
    def escanear_vulnerabilidades(self):
        """
        Escanea vulnerabilidades específicas de un ordenador.
        """
        return f"[+] Análisis de vulnerabilidades concluido en {self.modelo} con {self.sistema_operativo}: Hay que solucionar algunos problemas"
    
class Router(Dispositivo):
    """
    Clase que representa un router.
    """
    def __init__(self, modelo, firmware_version):
        """
        Inicializa un router con un modelo y una versión de firmware específica.
        """
        super().__init__(modelo)
        self.firmware_version = firmware_version
    
    def escanear_vulnerabilidades(self):
        """
        Escanea vulnerabilidades específicas de un router.
        """
        return f"[+] Análisis de vulnerabilidades concluido en {self.modelo} con firmware {self.firmware_version}: Múltiples puertos críticos abiertos!!"
    
class Movil(Dispositivo):
    """
    Clase que representa un móvil.
    """
    def __init__(self, modelo, sistema_operativo):
        """
        Inicializa un móvil con un modelo y un sistema operativo específico.
        """
        super().__init__(modelo)
        self.sistema_operativo = sistema_operativo
    
    def escanear_vulnerabilidades(self):
        """
        Escanea vulnerabilidades específicas de un móvil.
        """
        return f"[+] Análisis de vulnerabilidades concluido en {self.modelo} con {self.sistema_operativo}: Múltiples apps con permisos excesivos!!"

# Polimorfismo
def realizar_escaneo(dispositivo):
    """
    Realiza el escaneo de vulnerabilidades en un dispositivo y muestra el resultado.
    """
    try:
        print(f"{dispositivo} --> {dispositivo.escanear_vulnerabilidades()}")
    except Exception as e:
        print(f"Error al escanear {dispositivo}: {e}")

# Crear instancias de dispositivos
pc = Ordenador("Dell XPS", "Windows 10")
router = Router("TP-Link Archer C56", "v1.0.1")
movil = Movil("iPhone 16", "iOS 14")

# Lista de dispositivos
dispositivos = [pc, router, movil]

# Bucle para realizar los escaneos
for dispositivo in dispositivos:
    realizar_escaneo(dispositivo)



"""
# Pruebas unitarias
def test_dispositivos():
    assert pc.escanear_vulnerabilidades() == "[+] Análisis de vulnerabilidades concluido en Dell XPS con Windows 10: Hay que solucionar algunos problemas"
    assert router.escanear_vulnerabilidades() == "[+] Análisis de vulnerabilidades concluido en TP-Link Archer C56 con firmware v1.0.1: Múltiples puertos críticos abiertos!!"
    assert movil.escanear_vulnerabilidades() == "[+] Análisis de vulnerabilidades concluido en iPhone 16 con iOS 14: Múltiples apps con permisos excesivos!!"
    print("Todas las pruebas pasaron!")

# Ejecutar pruebas
test_dispositivos()
"""