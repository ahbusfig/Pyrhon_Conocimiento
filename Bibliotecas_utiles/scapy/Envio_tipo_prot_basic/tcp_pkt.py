from scapy.all import IP, TCP, sr1,send

def send_tcp_simple(dst):
    pkt = IP(dst=dst) / TCP(dport=80, flags="S")
    respuesta = sr1(pkt, timeout=2)
    
    if respuesta:
        print(respuesta.show())
    else:
        print("No hubo respuesta.")

def send_tcp_syn(dst, dport):
    # Crear un paquete IP con un segmento TCP SYN
    pkt = IP(dst=dst) / TCP(dport=dport, flags='S')
    print(pkt.summary())  # Imprimir un resumen del paquete creado
    
    # Enviar el paquete y esperar una respuesta
    respuesta = sr1(pkt, timeout=2)
    
    # Analizar la respuesta
    if respuesta:
        # Verificar si la respuesta tiene una capa TCP y si las banderas son 'SA' (SYN-ACK)
        if respuesta.haslayer(TCP) and respuesta[TCP].flags == "SA":
            print(f"El puerto {dport} está ABIERTO.")
        # Verificar si la respuesta tiene una capa TCP y si las banderas son 'RA' (RST-ACK)
        elif respuesta.haslayer(TCP) and respuesta[TCP].flags == "RA":
            print(f"El puerto {dport} está CERRADO.")
        else:
            print("Respuesta desconocida.")
    else:
        # Si no hubo respuesta, puede que el puerto esté filtrado
        print("No hubo respuesta, puede estar filtrado.")

if __name__ == "__main__":
    dst = "google.com"  # Dirección IP de destino
    dport = 80  # Puerto de destino (por ejemplo, HTTP)
    send_tcp_syn(dst, dport)