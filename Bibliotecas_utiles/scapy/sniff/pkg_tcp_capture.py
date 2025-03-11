from scapy.all import *
from termcolor import colored

pkts = sniff(filter="tcp and (port 80 or port 443)", count=5)
contador = 1 

for pkt in pkts:
    # Imprime el número del paquete en color amarillo
    print(colored(f"\nPaquete TCP numero --> {contador}\n", "yellow"))
    pkt.show()  # Muestra los detalles del paquete
    contador += 1 # Incrementa el contador

