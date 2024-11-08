#!/usr/bin/env python3
import socket
from termcolor import colored
import argparse

class escaneo_puertos:
    def __init__(self, host, puerto, rango=0):
        self.host = host
        self.puerto = puerto
        self.rango = rango

    def create_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        return s

    def escaneo_simple(self):
        s = self.create_socket()
        try:
            if s.connect_ex((self.host, self.puerto)):  # Si es True --> devuelve un 0 --> como False normal
                mensaje = f"\n[+] El puerto {colored(self.puerto, 'yellow')} está cerrado!"
                print(colored(mensaje, 'red'))
            else:
                mensaje = f"\n[+] El puerto {colored(self.puerto, 'yellow')} está abierto!"
                print(colored(mensaje, 'green'))
        finally:
            s.close()

    def escaneo_intermedio(self):
        print(colored(f"\nVamos a analizar los primeros {self.rango} puertos", "light_magenta"))
        for puerto in range(1, self.rango + 1):  # Ajustar el rango para empezar en 1
            s = self.create_socket()
            try:
                if s.connect_ex((self.host, puerto)) == 0:
                    mensaje = f"\n[+] El puerto {colored(puerto, 'yellow')} está abierto!"
                    print(colored(mensaje, 'green'))
                else:
                    mensaje = f"\n[+] El puerto {colored(puerto, 'yellow')} está cerrado!"
                    print(colored(mensaje, 'red'))
            finally:
                s.close()

def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP Port Scanner")
    parser.add_argument("-t", "--target", dest="target", required=True, help="Victim target to scan (e.g., -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", type=int, required=True, help="Port to scan (e.g., -p 80)")
    parser.add_argument("-r", "--range", dest="range", type=int, default=0, help="Port range to scan (e.g., -r 200)")
    options = parser.parse_args()

    return options.target, options.port, options.range

if __name__ == "__main__":
    target, port, port_range = get_arguments()
    escanear = escaneo_puertos(target, port, port_range)
    escanear.escaneo_simple()
    if port_range > 0:
        escanear.escaneo_intermedio()