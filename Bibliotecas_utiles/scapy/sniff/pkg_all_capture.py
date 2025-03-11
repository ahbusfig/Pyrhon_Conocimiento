from scapy.all import * 
from termcolor import colored 

paquetes = sniff(count=5)# Captura 5 paquetes de red
contador = 1 

for pkt in paquetes:
    # Imprime el número del paquete en color amarillo
    print(colored(f"\nPaquete numero --> {contador}\n", "yellow"))
    # pkt.show()  # Muestra los detalles del paquete
    # print(pkt) # similar a summary pero no es tan conciso
    print(pkt.summary())
    contador += 1 # Incrementa el contador

