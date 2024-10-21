import tkinter as tk  # Importa el módulo tkinter para crear interfaces gráficas

def accion_boton():
    # Función que se ejecuta cuando se presiona el botón
    print(f"\n[+] Se ha presionado el boton \n")

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Mi primera GUI!")  # Establece el título de la ventana

# Crea un botón con el texto "Presioname" que llama a la función accion_boton cuando se presiona
button = tk.Button(root, text="Presioname", command=accion_boton)
button.pack()  # Añade el botón a la ventana

root.mainloop()  # Inicia el bucle principal de la aplicación