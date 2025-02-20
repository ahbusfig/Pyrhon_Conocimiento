import customtkinter as ctk
import requests
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

class WeatherGui:

    def __init__(self, app):
        self.app = app
        self.app.title('Aplicación del Clima')
        self.app.geometry('500x500')
        self.app.resizable(False, False)

        # Frame principal
        self.main_frame = ctk.CTkFrame(self.app, width=500, height=500)
        self.main_frame.pack(fill="both", padx=50, pady=75)

        # Widget de pantalla de inicio
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self.main_frame, text="Ingrese el nombre de la ciudad:", font=("Arial", 18))
        self.label.pack(pady=20)

        self.entrada = ctk.CTkEntry(self.main_frame, font=("Arial", 18), width=300)
        self.entrada.pack(pady=10)

        self.search_button = ctk.CTkButton(self.main_frame, text="Buscar", command=self.buscar, font=("Arial", 18), width=200)
        self.search_button.pack(pady=10)

        self.result_frame = ctk.CTkFrame(self.main_frame, width=400, height=200, corner_radius=10, bg_color="blue")
        self.result_frame.pack(pady=20)

        self.result_label = ctk.CTkLabel(self.result_frame, text="Aquí se mostrarán los resultados...", font=("Arial", 18))
        self.result_label.pack(pady=10, padx=10)

    def buscar(self):
        ciudad = self.entrada.get()
        api_key = os.getenv('API_KEY')  # La clave la obtiene del archivo .env
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

        try:
            res = requests.get(url, timeout=3)
            res.raise_for_status()
            data = res.json()
            self.mostrar_resultados(data)
        except requests.exceptions.RequestException:
            self.result_label.configure(text="No se encontraron resultados")

    def mostrar_resultados(self, data):
        if data:
            ciudad = data.get('name')
            temp = data['main']['temp']
            descripcion = data['weather'][0]['description']
            humedad = data['main']['humidity']
            viento = data['wind']['speed']
            self.result_label.configure(text=f"Ciudad: {ciudad}\nTemperatura: {temp}°C\nDescripción: {descripcion}\nHumedad: {humedad}%\nViento: {viento} m/s")
        else:
            self.result_label.configure(text="No se encontraron resultados")

if __name__ == "__main__":
    app = ctk.CTk()
    WeatherApp = WeatherGui(app)
    app.mainloop()