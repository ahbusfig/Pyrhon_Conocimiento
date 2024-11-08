#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()# Crea la ventana principal de la aplicación.
root.title("Canvas() Widget")# Establece el título de la ventana como "Canvas() Widget".

# Crear un widget de lienzo (canvas) dentro de la ventana principal.
canvas = tk.Canvas(root, width=400, height=400, bg="white")# El lienzo tiene un ancho y alto de 400 píxeles y un fondo blanco.

canvas.pack(pady=15)# Empaqueta el widget de lienzo dentro de la ventana con un margen vertical (pady) de 15 píxeles.

# Dibuja un óvalo en el lienzo con las coordenadas especificadas.
oval = canvas.create_oval(50, 50, 150, 150, fill="red")# Las coordenadas (50, 50) son las del borde superior izquierdo, y (150, 150) las del borde inferior derecho.

# Dibuja un rectángulo en el lienzo con las coordenadas especificadas.
rect = canvas.create_rectangle(170, 50, 350, 100, fill="green")# Las coordenadas (170, 50) son las del borde superior izquierdo, y (350, 100) las del borde inferior derecho.

# Dibuja una línea en el lienzo desde el punto (50, 250) hasta (200, 320).
line = canvas.create_line(50, 250, 200, 320, width=5, fill="blue")# La línea tiene un ancho de 5 píxeles y es de color azul.

# Inicia el bucle principal de la appw
root.mainloop()
