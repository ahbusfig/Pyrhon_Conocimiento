import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Ejemplos de Widgets")

# Ejemplos de cada widget
label = tk.Label(root, text="Este es un Label")
label.pack()

button = tk.Button(root, text="Haz clic", command=lambda: messagebox.showinfo("Info", "¡Botón presionado!"))
button.pack()

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root, height=2, width=30)
text.pack()

checkbutton = tk.Checkbutton(root, text="Opción 1")
checkbutton.pack()

radio1 = tk.Radiobutton(root, text="Opción A", value=1)
radio2 = tk.Radiobutton(root, text="Opción B", value=2)
radio1.pack()
radio2.pack()

scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack()

spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

listbox = tk.Listbox(root)
listbox.insert(1, "Elemento 1")
listbox.insert(2, "Elemento 2")
listbox.pack()

canvas = tk.Canvas(root, width=100, height=100, bg="white")
canvas.create_line(0, 0, 100, 100)
canvas.pack()

root.mainloop()
