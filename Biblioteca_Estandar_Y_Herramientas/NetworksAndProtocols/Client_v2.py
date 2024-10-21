import socket  # Importa el módulo socket para la comunicación de red

def iniciar_cliente():
    host = "localhost"  # Define la dirección del servidor
    port = 1234  # Define el puerto del servidor

    # Crea un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))  # Conecta el socket al servidor especificado
        s.sendall(b"Hola, servidor!")  # Envía un mensaje al servidor
        data = s.recv(1024)  # Recibe datos del servidor

    print(f"\n[+] Mensaje recibido del servidor: {data.decode()}")  # Imprime el mensaje recibido del servidor

def iniciar_udp_cliente():
    host = "localhost"  # Define la dirección del servidor
    port = 1234  # Define el puerto del servidor

    # Crea un socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # message = "Hola este es un msg".encode("utf-8")  # Evitar error con tildes así
        s.sendto(b"Hola, vamos a enviar un msg ", (host, port))  # Envía un mensaje al servidor

# Iniciar cliente
# iniciar_cliente()  # Descomentar esta línea para iniciar el cliente TCP
iniciar_udp_cliente()  # Inicia el cliente UDP