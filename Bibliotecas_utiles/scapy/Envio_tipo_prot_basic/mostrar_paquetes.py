from scapy.all import IP, send

pkt = IP(dst="8.8.8.8")  # Crear un paquete IP con destino a 8.8.8.8
send(pkt)  
pkt.show()  # Muestra la estructura del paquete
