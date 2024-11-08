import socket as s  # Importa el módulo socket y lo renombra como 's'
import threading  # Importa el módulo threading para manejar hilos

def client_thread(client_socket, clients, usernames):
    # Recibir el nombre de usuario del cliente
    username = client_socket.recv(1024).decode()
    # Almacenar el nombre de usuario en el diccionario 'usernames'
    usernames[client_socket] = username

    print(f"Se ha conectado {username} al chat")

    # Notificar a los demás clientes que un nuevo usuario se ha unido al chat
    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] El user {username} ha entrado al chat\n\n".encode())
    
    while True:
        try:
            # Recibir mensajes del cliente
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            
            # Si el mensaje es "!usuarios", enviar la lista de usuarios al cliente solicitante
            if msg == "!usuarios":
                user_list = ",".join(usernames.values())
                client_socket.sendall(f"USERS:{user_list}".encode())
            else:
                # Retransmitir el mensaje a todos los demás clientes
                for client in clients:
                    if client is not client_socket:
                        client.sendall(f"{msg}".encode())

        except:
            break

    # Cerrar la conexión del cliente y eliminarlo de las listas --> Se ejecuta cuando se sale del chat!
    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]
    for client in clients:
        client.sendall(f"\n[+] El user {username} ha dejado el chat\n\n".encode())

def server_program():# Función principal del servidor
    # Declarar el nombre del host y el puerto usado
    host = "localhost"
    port = 12345

    # Crear un socket de servidor IPv4 y TCP
    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    # Permitir reutilizar la dirección del socket
    server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    # Enlazar el socket al host y puerto especificados
    server_socket.bind((host, port))
    # Poner el servidor en modo de escucha
    server_socket.listen()

    print(f"\n[+] El server está en escucha de conexiones in...")

    clients = []  # Lista para almacenar los sockets de los clientes
    usernames = {}  # Diccionario para almacenar los nombres de usuario de los clientes

    while True:
        # Aceptar una nueva conexión de cliente
        client_socket, address = server_socket.accept()
        # Añadir el socket del cliente a la lista de clientes
        clients.append(client_socket)

        print(f"\n[+] Se ha conectado un nuevo cliente: {address}")

        # Crear un nuevo hilo para manejar la comunicación con el cliente
        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True  # Facilita fin conexion
        thread.start()  # Iniciar el hilo

    server_socket.close()

if __name__ == "__main__":
    # Ejecutar la función principal del servidor si el script se ejecuta directamente
    server_program()