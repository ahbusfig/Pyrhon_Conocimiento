import tkinter as tk
from tkinter import messagebox, filedialog

# Funciones que se activarán desde el menú o el botón
def new_file():
    messagebox.showinfo("Nuevo", "Creando un nuevo archivo...")

def open_file():
    file_path = filedialog.askopenfilename(
        title="Abrir archivo", 
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if file_path:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {file_path}")

def save_file():
    messagebox.showinfo("Guardar", "Guardando el archivo...")

def exit_app():
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Menú")
root.geometry("400x300")

# Crear la barra de menú
menu_bar = tk.Menu(root)

# Crear el menú 'Archivo'
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nuevo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=exit_app)

# Añadir el menú 'Archivo' a la barra de menú
menu_bar.add_cascade(label="Archivo", menu=file_menu)

# Crear el menú 'Ayuda'
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Ejemplo de Menú en Tkinter"))

# Añadir el menú 'Ayuda' a la barra de menú
menu_bar.add_cascade(label="Ayuda", menu=help_menu)

# Configurar la ventana para usar la barra de menú
root.config(menu=menu_bar)

# Crear un botón en el centro de la ventana para abrir archivos
open_button = tk.Button(root, text="Abrir Archivo", command=open_file)
open_button.pack(pady=100)

# Iniciar el bucle principal de la aplicación
root.mainloop()
