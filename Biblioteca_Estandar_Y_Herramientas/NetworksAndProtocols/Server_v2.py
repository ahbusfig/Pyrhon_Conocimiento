import socket  # Importa el módulo socket para la comunicación de red

def iniciar_server_tcp():
    host = "localhost"  # Define la dirección del servidor
    port = 1234  # Define el puerto del servidor

    # Crea un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))  # Asocia el socket con la dirección y el puerto especificados
        print(f"\n [+] El servidor TCP escucha en {host}:{port}")
        s.listen(1)  # Escucha conexiones entrantes, con un máximo de 1 conexión en cola
        conn, addr = s.accept()  # Acepta una conexión entrante

        with conn:  # Gestiona la conexión con el cliente
            print(f"\n [+] Se ha conectado un nuevo cliente: {addr}")
            while True:  # Bucle para recibir y enviar datos
                data = conn.recv(1024)  # Recibe datos del cliente
                if not data:  # Si no hay datos, rompe el bucle
                    break
                else:
                    conn.sendall(data)  # Envía de vuelta los datos recibidos (eco)

def iniciar_server_udp():
    host = "localhost"  # Define la dirección del servidor
    port = 1234  # Define el puerto del servidor

    # Crea un socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))  # Asocia el socket con la dirección y el puerto especificados
        print(f"\n [+] El servidor UDP escucha en {host}:{port}")
        while True:  # Bucle para recibir y enviar datos
            data, addr = s.recvfrom(1024)  # Recibe datos del cliente
            print(f"\n[+] Msg enviado por el cliente --> {data.decode()}")  # Muestra el mensaje recibido
            print(f"[+] Informacion del cliente que nos ha enviado el msg --> {addr}")  # Muestra la información del cliente

# Iniciar servidor
# iniciar_server_tcp()  # Descomentar esta línea para iniciar el servidor TCP
iniciar_server_udp()