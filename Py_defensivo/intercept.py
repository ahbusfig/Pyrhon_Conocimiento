#!/usr/bin/env python3
import scapy.all as scapy

# Función para procesar los paquetes capturados
def process_packet(packet):
    # Verifica si el paquete tiene una respuesta DNS (DNSRR)
    if packet.haslayer(scapy.DNSRR):
        # Obtiene el nombre de la consulta DNS (DNSQR)
        qname = packet[scapy.DNSQR].qname

        # Verifica si el nombre de la consulta contiene "hack4u.io"
        if b"hack4u.io" in qname:
            print(f"\n------------------")
            # Muestra los detalles del paquete
            print(packet.show())

# Captura paquetes en la interfaz "ens33" que sean UDP y en el puerto 53 (DNS)
scapy.sniff(iface="ens33", filter="udp and port 53", prn=process_packet, store=0)