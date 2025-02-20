import customtkinter as ctk

class MainWindow:

    def __init__(self, app):
        self.app = app
        self.app.title("Calculadora")
        self.app.geometry("360x500")
        self.app.resizable(False, False)  # Evita que la ventana se pueda maximizar o cambiar de tamaño

        # Configurar el grid del contenedor principal
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_rowconfigure(1, weight=2)
        self.app.grid_columnconfigure(0, weight=1)

        # Parte del resultado
        ## Frame 
        self.res_frame = ctk.CTkFrame(self.app)
        self.res_frame.grid(row=0, column=0, sticky="nsew")
        ### Entry que guarda el resultado
        self.res = ctk.CTkEntry(self.res_frame, justify='right', font=("Arial", 48))
        self.res.pack(fill="both", expand=True)

        # Parte de las teclas
        self.teclado_frame = ctk.CTkFrame(self.app)
        self.teclado_frame.grid(row=1, column=0, sticky="nsew")

        # Configurar el grid del teclado
        for i in range(5):
            self.teclado_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.teclado_frame.grid_columnconfigure(j, weight=1)

        # Crear botones
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            btn = ctk.CTkButton(self.teclado_frame, text=button, command=lambda b=button: self.on_button_click(b), border_width=3)
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.res.get())
                self.res.delete(0, 'end')
                self.res.insert(0, str(result))
            except Exception as e:
                self.res.delete(0, 'end')
                self.res.insert(0, "Error")
        else:
            current_buttom = self.res.get()
            new_text = current_buttom + char
            self.res.delete(0, 'end')
            self.res.insert(0, new_text)

if __name__ == "__main__":
    app = ctk.CTk()
    window = MainWindow(app)
    app.mainloop()