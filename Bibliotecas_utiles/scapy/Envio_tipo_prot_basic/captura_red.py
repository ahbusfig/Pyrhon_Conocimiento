from scapy.all import *

# Captura 5 paquetes TCP
pkts = sniff(count=5, filter="tcp")
pkts.summary()  # Muestra un resumen de los paquetes capturados

# Guarda los paquetes capturados en un archivo
wrpcap('captura.pcap', pkts)