from scapy.all import IP, ICMP, send
from termcolor import colored

def send_spoofed_ip():
    # Crear y enviar un paquete IP con una capa ICMP y una dirección IP de origen falsificada
    spoofed_pkt = IP(dst="8.8.8.8") / ICMP()
    print(colored("Enviando paquete IP falsificado:", "green"))
    # spoofed_pkt.show()
    print(spoofed_pkt.summary())
    # Se envia con send --> no espera respuesta, sr--> espera respuesta
    send(spoofed_pkt)

if __name__ == "__main__":
    send_spoofed_ip()