from scapy.all import *
from termcolor import colored

pkts = sniff(filter="icmp", count=5) #sin count captura indefinidamente !!
contador = 1
for pkt in pkts:
    print(colored(f"\nPaquete numero --> {contador}\n", "yellow"))
    # pkt.show()        # Da info completa
    print(pkt.summary()) #Resument compacto
    contador += 1