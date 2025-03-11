from scapy.all import IP,TCP,send
import random

def generate_tcp_spoof_packet():
    # Generar un puerto de origen aleatorio
    puerto_aleatorio = random.randint(1024, 65535)

    # Crear un paquete TCP con IP falsa y puerto aleatorio
    paquete = IP(src="10.0.0.200", dst="192.168.1.1") / TCP(sport=puerto_aleatorio, dport=80, flags="S")

    # Enviar el paquete
    send(paquete)

if __name__ == "__main__":
    generate_tcp_spoof_packet()
