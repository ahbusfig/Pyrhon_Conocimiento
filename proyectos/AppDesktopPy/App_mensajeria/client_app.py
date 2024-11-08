import threading
import socket as s
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def client_app():
    host = "localhost"
    port = 12345

    # Crear conexión IPv4 y TCP, además iniciar conexión con el puerto y host determinado
    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket.connect((host, port))

    # Crear nombre usuario
    username = input(f"[+] Introduce tu usuario: ")
    client_socket.sendall(username.encode())
    #-----------------------Creacion de la parte gráfica-----------------------------------------
    window = Tk()
    window.title("Chat")

    text_widget = ScrolledText(window, state="disabled")
    text_widget.pack(padx=5, pady=5, fill=BOTH, expand=1)

    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=5, fill=BOTH, expand=1)

    entry_widget = Entry(frame_widget)
    entry_widget.bind("<Return>", lambda _: send_msg(client_socket, username, text_widget, entry_widget))
    entry_widget.pack(side=LEFT, fill=BOTH, expand=1)

    button_widget = Button(frame_widget, text="Send", command=lambda: send_msg(client_socket, username, text_widget, entry_widget))
    button_widget.pack(side=RIGHT, padx=5)

    list_user_widget = Button(frame_widget, text="Lista usuarios", command=lambda: list_users(client_socket))
    list_user_widget.pack(side=RIGHT, padx=5)

    exit_widget = Button(frame_widget, text="Salir", command=lambda: exit(client_socket,window,username))
    exit_widget.pack(side=RIGHT, padx=5)
    # Crear un hilo para recibir mensajes del servidor --> cada user su propio hilo!
    thread = threading.Thread(target=receive_msg, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()
    #Crear bucle principal para la parte gráfica
    window.mainloop()
    client_socket.close()
    #------------------------------------------------------------------------------------------------

#-----------------------------Logica para que funcione la parte grafica--------------------
def send_msg(client_socket, username, text_widget, entry_widget):
    # Enviar mensaje al servidor
    msg = entry_widget.get()
    client_socket.sendall(f"{username}--> {msg}".encode())  

    # Mostrar el mensaje en el widget de texto
    entry_widget.delete(0, END)
    text_widget.configure(state="normal")
    text_widget.insert(END, f"{username}--> {msg}\n")  
    text_widget.configure(state='disabled')

def receive_msg(client_socket, text_widget):
    while True:
        try:
            # Recibir mensajes del servidor
            msg = client_socket.recv(1024).decode()
            if not msg:
                break

            # Mostrar la lista de usuarios conectados
            if msg.startswith("USERS:"):
                user_list = msg[6:].split(",")
                text_widget.configure(state="normal")
                text_widget.insert(END, f"Usuarios conectados: {', '.join(user_list)}\n")
                text_widget.configure(state='disabled')
            else:
                # Mostrar el mensaje en el widget de texto
                text_widget.configure(state="normal")
                text_widget.insert(END, f"{msg}\n")  
                text_widget.configure(state='disabled')

        except:
            break

def list_users(client_socket):
    # Enviar solicitud de lista de usuarios al servidor
    client_socket.sendall("!usuarios".encode())

def exit(client_socket,window,username):
    #Cerrar hilo
    client_socket.close()
    #Cerrar la ventana
    window.quit()
    window.destroy()
if __name__ == "__main__":
    client_app()