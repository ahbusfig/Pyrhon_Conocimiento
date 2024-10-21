import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost",1234)
client_socket.connect(server_address)

try:
    msg = b"Este es un msg de prueba que envio al servidor"
    client_socket.sendall(msg)
    data = client_socket.recv(1024)

    print(f"[+]El servidor nos ha respondido con este mensaje: {data.decode()}")
finally:
    client_socket.close()