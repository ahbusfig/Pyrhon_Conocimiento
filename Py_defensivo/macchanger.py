#!/usr/bin/env python3
import argparse
import re
from termcolor import colored
import subprocess
import platform

def get_arguments():
    parser = argparse.ArgumentParser(description=colored("Herramienta para cambiar la mac de una interfaz de red", "yellow"))
    parser.add_argument("-i", "--interface", required=True, dest="interface", help=colored("Nombre de la interfaz de red", "green"))
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help=colored("Nueva dir. mac para la interfaz de red", "green"))
    return parser.parse_args()

def is_valid_input(interface, mac_address):
    is_valid_interface = re.match(r'^(eth|ens|enp|wlan)\d+$', interface) if platform.system() != "Windows" else True
    is_valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}:){5}[A-Fa-f0-9]{2}$', mac_address)
    return is_valid_interface, is_valid_mac_address

def change_mac_address(interface, mac_address):
    is_valid_interface, is_valid_mac_address = is_valid_input(interface, mac_address)
    if is_valid_interface and is_valid_mac_address:
        print(colored("Los datos introducidos son correctos", "green"))
        print(colored(f"[+] Cambiando la dirección MAC de {interface} a {mac_address}", "blue"))
        if platform.system() == "Linux":
            subprocess.call(["ifconfig", interface, "down"])
            subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
            subprocess.call(["ifconfig", interface, "up"])
        elif platform.system() == "Windows":
            subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=disable"])
            subprocess.call(["netsh", "interface", "set", "interface", interface, f"newmac={mac_address}"])
            subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=enable"])
        print(colored(f"[+] Dirección MAC de {interface} cambiada a {mac_address}", "green"))
    else:
        print(colored("Los datos introducidos no son correctos", "red"))

def main():
    args = get_arguments()
    change_mac_address(args.interface, args.mac_address)

if __name__ == "__main__":
    main()