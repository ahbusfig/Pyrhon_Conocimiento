import tkinter as tk

root = tk.Tk()  # Crea la ventana principal de la aplicación
root.title("tercera Gui")  # Establece el título de la ventana

# Declaramos las labels (etiquetas)
label1 = tk.Label(root, text="Esto es la label 1", bg="red")  # Crea una etiqueta con texto y fondo rojo
label2 = tk.Label(root, text="Esto es la label 2", bg="blue")  # Crea una etiqueta con texto y fondo azul
label3 = tk.Label(root, text="Esto es la label 3", bg="green")  # Crea una etiqueta con texto y fondo verde

# Instanciamos las labels en la GUI usando grid
label1.grid(row=0, column=0, sticky="ew")  # Añade la etiqueta 1 a la ventana en la fila 0, columna 0, expandida horizontalmente
label2.grid(row=0, column=1, sticky="ns")  # Añade la etiqueta 2 a la ventana en la fila 0, columna 1, expandida verticalmente
label3.grid(row=1, column=0, columnspan=2, sticky="ew")  # Añade la etiqueta 3 a la ventana en la fila 1, columna 0, expandida horizontalmente a través de dos columnas

# Configura las columnas para que se expandan
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Iniciar el bucle de la aplicación
root.mainloop()  # Inicia el bucle principal de la aplicación   