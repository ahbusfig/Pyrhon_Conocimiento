import os
from tkinter import *
from tkinter import messagebox, filedialog

class MainWindow:
    def __init__(self, app):
        self.app = app
        self.app.title("Notas Manager")
        self.app.geometry("360x500")

        # Frame para el área de texto
        self.text_frame = Frame(self.app, bg="lightgrey")
        self.text_frame.pack(fill='both', expand=True, side='top')

        self.text_area = Text(self.text_frame, wrap='word', font=("Helvetica", 12), bg="white", fg="black")
        self.text_area.pack(fill='both', expand=True, padx=10, pady=5)

        # Frame para las opciones
        self.options_frame = Frame(self.app, bg="darkgrey")
        self.options_frame.pack(fill='x', side="bottom")

        # Frame interno para centrar los botones
        self.button_frame = Frame(self.options_frame, bg="darkgrey")
        self.button_frame.pack(expand=True)

        self.save_button = Button(self.button_frame, text="Guardar Nota", command=self.save_note, bg="blue", fg="white", font=("Helvetica", 10, "bold"))
        self.save_button.pack(side="left", padx=10, pady=10)

        self.delete_button = Button(self.button_frame, text="Eliminar Nota", command=self.delete_note, bg="red", fg="white", font=("Helvetica", 10, "bold"))
        self.delete_button.pack(side="left", padx=10, pady=10)

        self.load_button = Button(self.button_frame, text="Abrir Nota", command=self.load_note, bg="green", fg="white", font=("Helvetica", 10, "bold"))
        self.load_button.pack(side="left", padx=10, pady=10)

        # Añadir efecto de hover a los botones
        self.add_hover_effect(self.save_button)
        self.add_hover_effect(self.delete_button)
        self.add_hover_effect(self.load_button)

    def add_hover_effect(self, button):
        def on_enter(e):
            button.config(relief="raised", bd=3)
        def on_leave(e):
            button.config(relief="flat", bd=2)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def save_note(self):
        note_content = self.text_area.get("1.0", END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as note_file:
                note_file.write(note_content)
            self.text_area.delete("1.0", END)
            messagebox.showinfo(title="Alerta", message="Se ha guardado correctamente!")

    def load_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as note_file:
                self.text_area.delete("1.0", END)
                self.text_area.insert(END, note_file.read())

    def delete_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            confirm = messagebox.askyesno(title="Confirmar", message="¿Estás seguro de que deseas eliminar la nota?")
            if confirm:
                try:
                    os.remove(file_path)
                    self.text_area.delete("1.0", END)
                    messagebox.showinfo(title="Alerta", message="Se ha eliminado correctamente!")
                except Exception as e:
                    messagebox.showerror(title="Error", message=f"No se pudo eliminar el archivo: {e}")

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()
