from scapy.all import IP, send, ICMP, sr1
from termcolor import colored

def icmp_sender(dst):
    pkt = IP(dst=dst) / ICMP()
    # Enviar un Paquete Icmp al dst y esperar respuesta
    res = sr1(pkt, timeout=2)

    # Mostrar respuesta
    if res:
        print(colored("Respuesta recibida: ","yellow"))
        # res.show()
        print(res.summary())
    else:
        print(colored("Se ha producido un error","red"))

if __name__ == "__main__":

    src = input("Dime el dominio al que se quiere hacer la peticion (p.e google.es) --> ")
    icmp_sender(src)