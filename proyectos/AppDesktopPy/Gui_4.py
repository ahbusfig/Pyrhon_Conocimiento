import tkinter as tk

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Ejemplo de Posiciones Relativas y Absolutas")

# Establecer el tamaño de la ventana
root.geometry("400x300")

# Crear una etiqueta con texto
label_absolute = tk.Label(root, text="Posición Absoluta", bg="red")
# Posicionar la etiqueta usando coordenadas absolutas
label_absolute.place(x=50, y=50)

# Crear otra etiqueta con texto
label_relative = tk.Label(root, text="Posición Relativa", bg="blue")
# Posicionar la segunda etiqueta usando coordenadas relativas
label_relative.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Iniciar el bucle principal de la aplicación
root.mainloop()