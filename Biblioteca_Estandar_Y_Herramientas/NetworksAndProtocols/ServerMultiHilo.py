import threading  # Importa el módulo threading para permitir la ejecución de hilos

# Clase que hereda de threading.Thread para manejar la conexión de cada cliente en un hilo separado
class ClientThread(threading.Thread):
    def __init__(self, client_sock, client_addr):
        super().__init__()  # Inicializa la clase base threading.Thread
        self.client_sock = client_sock  # Guarda el socket del cliente
        self.client_addr = client_addr  # Guarda la dirección del cliente
        
        # Mensaje que indica la conexión de un nuevo cliente
        print(f"\n[+] Nuevo cliente conectado: {client_addr}")

    # Método que se ejecuta cuando el hilo comienza a correr
    def run(self):
        message = ''  # Inicializa la variable para almacenar los mensajes recibidos

        # Bucle infinito para recibir mensajes del cliente hasta que el mensaje sea 'bye'
        while True:
            data = self.client_sock.recv(1024)  # Recibe un máximo de 1024 bytes desde el socket del cliente
            message = data.decode()  # Decodifica los datos recibidos a texto

            # Si el cliente envía 'bye', se rompe el bucle y se cierra la conexión
            if message == 'bye':
                break

            # Muestra el mensaje enviado por el cliente
            print(f"\n[+] Mensaje enviado por el cliente: {message}")
            self.client_sock.send(data)  # Envía de vuelta el mensaje al cliente (eco)

        # Mensaje que indica que el cliente se ha desconectado
        print(f"\n[+] Cliente {self.client_addr} desconectado")
        #Cerrar conexion
        self.client_sock.close()

# Datos de configuración del servidor
HOST = 'localhost'  # Dirección del servidor (localhost para pruebas locales)
PORT = 1234  # Puerto en el que el servidor estará escuchando

# Crea un socket de servidor usando TCP/IP (AF_INET y SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Configura el socket para reutilizar direcciones rápidamente tras cerrarse (evitar TIME_WAIT)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Asocia el socket con la dirección y el puerto definidos
    server_socket.bind((HOST, PORT))

    # Mensaje que indica que el servidor está esperando conexiones entrantes
    print(f"\n[+] En espera de conexiones entrantes...")

    # Bucle infinito para aceptar nuevas conexiones de clientes
    while True:
        server_socket.listen()  # Pone el socket en modo de escucha para recibir conexiones
        client_sock, client_addr = server_socket.accept()  # Acepta una conexión entrante
        
        # Crea un nuevo hilo para manejar la conexión con el cliente
        new_thread = ClientThread(client_sock, client_addr)
        new_thread.start()  # Inicia el hilo (ejecuta el método run)
