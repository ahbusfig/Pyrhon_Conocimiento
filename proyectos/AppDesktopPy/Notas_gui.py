import tkinter as tk
from tkinter import filedialog,messagebox
#Clase
class SimpleTextEditor:
    def __init__(self,root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_open_file = ""

    def new_file(self): #Muestra una hoja en blanco si antes habia contenido
        self.text_area.delete("1.0",tk.END)
        self.current_open_file = ""

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.text_area.delete("1.0", tk.END) # 1.0 --> desd la 1 linea y el 1 caracter hasta end
            with open(filename, "r") as f:
                content = f.read()  # Lee el contenido del archivo
                self.text_area.insert("1.0", content)  # Inserta el contenido en el área de texto

    def save_file(self):
        if not self.current_open_file:
            # Si no hay un archivo abierto, abrir un cuadro de diálogo para guardar el archivo
            new_file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if new_file_path:
                self.current_open_file = new_file_path  # Actualiza el archivo actualmente abierto
            else:
                return  # Si el usuario cancela, no hacer nada
        # Guardar el contenido del área de texto en el archivo actualmente abierto
        with open(self.current_open_file, "w") as f:
            f.write(self.text_area.get("1.0", tk.END))  # Escribe el contenido del área de texto en el archivo


    def quit_confirm(self):
        if messagebox.askokcancel("Salir","¿Quieres salir?"):
            self.root.destroy()
               
#Crear la app principal
root = tk.Tk()
root.title("Notas")
root.geometry("700x500")
#Declarar el obejeto
editor = SimpleTextEditor(root)
#Crear menu
menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)

menu_options.add_command(label="Nuevo", command=editor.new_file)
menu_options.add_command(label="Abrir", command=editor.open_file)
menu_options.add_command(label="Guardar", command=editor.save_file)
menu_options.add_command(label="Salir", command=editor.quit_confirm)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options)
#Bucle principal de la app
root.mainloop()
