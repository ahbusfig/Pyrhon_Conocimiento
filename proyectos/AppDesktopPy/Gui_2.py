import tkinter as tk

root = tk.Tk()  # Crea la ventana principal de la aplicación
root.title("Segunda Gui")  # Establece el título de la ventana

# Declaramos las labels (etiquetas)
label1 = tk.Label(root, text="Esto es la label 1", bg="red")  # Crea una etiqueta con texto y fondo rojo
label2 = tk.Label(root, text="Esto es la label 2", bg="blue")  # Crea una etiqueta con texto y fondo azul
label3 = tk.Label(root, text="Esto es la label 3", bg="green")  # Crea una etiqueta con texto y fondo verde

# Instanciamos las labels en la GUI
label1.pack(side="left", fill=tk.X)  # Añade la etiqueta 1 a la ventana, alineada a la izquierda y expandida horizontalmente
label2.pack(side="right", fill=tk.Y)  # Añade la etiqueta 2 a la ventana, alineada a la derecha y expandida verticalmente
label3.pack(side="bottom", fill=tk.X)  # Añade la etiqueta 3 a la ventana, alineada en la parte inferior y expandida horizontalmente

# Iniciar el bucle de la aplicación
root.mainloop()  # Inicia el bucle principal de la aplicación