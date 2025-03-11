from scapy.all import sniff
from termcolor import colored
def sniff_tcp_traffic():
    # Función para capturar paquetes TCP
    print(colored("Iniciando el sniffing de tráfico TCP...", "blue"))
    sniff(filter="tcp", prn=lambda x: x.summary(), count=10)


if __name__ == "__main__":
    sniff_tcp_traffic()
