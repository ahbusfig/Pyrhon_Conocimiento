import socket
            
# Crear un socket de servidor utilizando IPv4 (AF_INET) y TCP (SOCK_STREAM)
"""         # AF_INIT --> Constante que indica uso del protocolo de direcciones IPv4.
            # SOCK_STREAM --> Constante que indica uso del protocolo de transporte TCP.
"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto del servidor
server_address = ("localhost", 1234)

# Enlazar el socket del servidor a la dirección y puerto especificados
server_socket.bind(server_address)

# Escuchar conexiones entrantes (el servidor puede aceptar conexiones)
server_socket.listen(1) #Solo 1 conexion a la vez!b

# Bucle infinito para aceptar y manejar conexiones de clientes
while True:
    # Aceptar una nueva conexión de un cliente
    client_socket, client_address = server_socket.accept()

    # Recibir datos del cliente (hasta 1024 bytes)
    data = client_socket.recv(1024)

    # Imprimir el mensaje recibido del cliente
    print(f"\n[+] Mensaje recibido del cliente: {data}")

    # Imprimir la información del cliente que se ha comunicado con el servidor
    print(f"[+] Información del cliente que se ha comunicado con nosotros: {client_address}")

    # Enviar una respuesta al cliente
    client_socket.sendall("Un saludo crack".encode()) #Esto se le envia al cliente despues de este hacer la conexion e envie algo
                                                      #Esta codificado por q necesita estar en formato b
    # Cerrar la conexión con el cliente
    client_socket.close()




