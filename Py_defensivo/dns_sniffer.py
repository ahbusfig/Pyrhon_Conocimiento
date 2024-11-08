#!/usr/bin/env python3

# Importamos el módulo scapy para trabajar con paquetes de red
import scapy.all as scapy

# Función para procesar cada paquete DNS capturado
def process_dns_packet(packet):
    # Verificamos si el paquete tiene una capa DNS
    if packet.haslayer(scapy.DNSQR):
        # Extraemos el nombre de dominio de la consulta DNS y lo decodificamos
        domain = packet[scapy.DNSQR].qname.decode()
        
        # Lista de palabras clave a excluir de la captura
        exclude_keywords = ["google", "cloud", "bing", "static", "sensic"]
        
        # Verificamos si el dominio no ha sido visto antes y si no contiene ninguna de las palabras clave de exclusión
        if domain not in domains_seen and not any(keyword in domain for keyword in exclude_keywords):
            # Añadimos el dominio al conjunto de dominios vistos
            domains_seen.add(domain)
            # Imprimimos el dominio que coincide con nuestros filtros
            print(f"[+] Dominio: {domain}")

# Función para capturar los paquetes DNS en una interfaz específica
def sniff(interface):
    # Capturamos solo los paquetes UDP en el puerto 53 (DNS) y llamamos a la función 'process_dns_packet' para procesarlos
    scapy.sniff(iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0)

# Función principal
def main():
    # Llamamos a la función 'sniff' con la interfaz de red específica
    sniff("ens33")

# Punto de entrada del script
if __name__ == '__main__':
    # Declaramos 'domains_seen' como global para almacenar dominios únicos
    global domains_seen
    # Inicializamos un conjunto vacío para almacenar dominios que ya han sido vistos
    domains_seen = set()
    # Ejecutamos la función principal
    main()
