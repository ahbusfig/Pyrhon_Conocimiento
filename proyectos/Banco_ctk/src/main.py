import customtkinter as ctk
from controller.CuentaController import añadir_dinero, retirar_dinero, consultar_saldo
from model.persona import Persona

class BancoGUI:
    def __init__(self, app):
        self.app = app
        self.app.title("Banco CTkinter")
        self.app.geometry("500x500")
        self.app.resizable(False, False)  # Evita que la ventana se pueda maximizar o cambiar de tamaño

        self.persona = Persona("Alain", "Bustamante", "26602238", 0)

        self.create_login_frame()

    def create_login_frame(self):
        self.login_frame = ctk.CTkFrame(self.app)
        self.login_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Usuario")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Contraseña", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(self.login_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.pack(pady=12, padx=10)

    def login(self):
        # Aquí puedes agregar la lógica de autenticación
        # Para este ejemplo, cualquier usuario y contraseña serán aceptados
        self.login_frame.pack_forget()
        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(self.app)
        self.main_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.main_frame, text=str(self.persona))
        self.label.pack(pady=10)

        self.add_button = ctk.CTkButton(self.main_frame, text="Añadir Dinero", command=self.add_money)
        self.add_button.pack(pady=10)

        self.withdraw_button = ctk.CTkButton(self.main_frame, text="Retirar Dinero", command=self.withdraw_money)
        self.withdraw_button.pack(pady=10)

        self.balance_button = ctk.CTkButton(self.main_frame, text="Consultar Saldo", command=self.show_balance)
        self.balance_button.pack(pady=10)

    def add_money(self):
        añadir_dinero(self.persona, 100)
        self.label.configure(text=str(self.persona))

    def withdraw_money(self):
        retirar_dinero(self.persona, 50)
        self.label.configure(text=str(self.persona))

    def show_balance(self):
        saldo = consultar_saldo(self.persona)
        ctk.CTkMessageBox.showinfo("Saldo", f"Saldo actual: {saldo}")

if __name__ == "__main__":
    app = ctk.CTk()
    banco = BancoGUI(app)
    app.mainloop()