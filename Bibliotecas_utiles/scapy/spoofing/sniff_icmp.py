from scapy.all import sniff
from termcolor import colored
import re

patron = r""
def sniff_icmp():
    # Captura un paquete ICMP
    sniff_pkts_icmp = sniff(filter="icmp", count=2)
    contador = 1
    for pkt in sniff_pkts_icmp:
        print(colored(f"Paquete ICMP {contador}", "yellow"))
        print(pkt.summary())
        contador += 1

if __name__ == "__main__":
    sniff_icmp()