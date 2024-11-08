import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        
        # Crear un widget de entrada con un borde de 10 píxeles y fondo azul marino claro
        self.display = tk.Entry(root, width=15, font=("Arial", 23), bd=10, insertwidth=1, bg="#ADD8E6", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)  # Posicionar el widget en la cuadrícula
        
        # Crear botones
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            "7","8","9","/","4","5","6","+",
            "1","2","3","-","C","0",".","*",
            "="
        ]
        
        row = 1
        col = 0

        for boton in buttons:
            self.button_build(boton, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_build(self, button, row, col):
        if button == "C":  # Si el botón es C
            b = tk.Button(self.root, text=button, width=8, command=self.button_clear)  # Crear el botón 
        elif button == "=":
            b = tk.Button(self.root, text=button, width=8, command=self.button_calculate)  # Crear el botón 
        else:  # Si es otro botón
            b = tk.Button(self.root, text=button, width=8, command=lambda b=button: self.click(b))  # Usar lambda para diferir la evaluación
        b.grid(row=row, column=col)  # Posicionar el botón según su fila y columna en el grid

    #-----------------------Funciones lógicas de la calculadora------------------------------
    def button_clear(self):
        self.display.delete("0", tk.END)  # Borra desde el primer carácter hasta el fin

    def button_calculate(self):
        try:
            result = str(eval(self.display.get()))  # Evaluar la expresión
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def click(self, button):
        self.display.insert(tk.END, button)  # Inserta el texto al final del contenido actual

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Calculadora")

# Crear una instancia de la clase Calculadora
my_gui = Calculadora(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()