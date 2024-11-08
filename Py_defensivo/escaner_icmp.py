import argparse
from termcolor import colored
import subprocess
import sys
import signal
from concurrent.futures import ThreadPoolExecutor
import platform

# Señal para salir del programa
def def_handler(sig, frame):
    print(colored("\n[!] Saliendo del programa\n", "red"))
    sys.exit(1)
# Asigna el handler de salida a la señal SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, def_handler)

# Función donde se declaran los argumentos pedidos por el script
def get_arguments():
    parser = argparse.ArgumentParser(description=colored("Herramienta para descubrir hosts activos en una red", "yellow"))
    parser.add_argument("-t", "--target", required=True, dest="target", help=colored("Dir. objetivo del script", "cyan"))

    # Devuelve el valor del argumento --target
    args = parser.parse_args()
    return args.target

# Aquí vamos a pasar la IP o rango de IPs a un formato correcto
def parse_target(target_str):
    # Ejemplo de input: 192.168.1.1-100
    target_str_splitted = target_str.split('.')  # Divide la dirección IP en octetos
    first_three_octets = '.'.join(target_str_splitted[:3])  # Obtiene los primeros tres octetos (ej: 192.168.1)

    # Comprueba si es una IP completa o un rango
    if len(target_str_splitted) == 4:
        if "-" in target_str_splitted[3]:  # Si el último octeto tiene un rango (ej: 1-100)
            start, end = target_str_splitted[3].split('-')  # Separa el inicio y el final del rango
            # Retorna una lista de IPs en el rango especificado
            return [f"{first_three_octets}.{i}" for i in range(int(start), int(end) + 1)]
        else:
            # Retorna una lista con una sola IP
            return [target_str]
    else:
        print(colored("[!] Formato de IP o rango de IP no válido", "red"))
        sys.exit(1)

# Función para descubrir hosts activos
def host_discovery(target):
    try:
        # Detecta el sistema operativo y usa el comando adecuado para ping
        if platform.system() == "Windows":
            ping = subprocess.run(["ping", "-n", "1", target], timeout=1, stdout=subprocess.DEVNULL)
        else:
            ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)
        
        # Si el código de retorno es 0, significa que el host respondió
        if ping.returncode == 0:
            print(colored(f"\t[i] La IP {target} está activa", "green"))
    except subprocess.TimeoutExpired:
        # Si el ping excede el tiempo límite, se ignora
        pass

# Función principal
def main():
    # Obtiene el argumento de entrada y parsea el rango de IPs
    target_str = get_arguments()
    targets = parse_target(target_str)

    # Si el rango es válido, procede a buscar hosts activos
    if targets:
        print(colored("\n[+] Hosts activos en la red:\n", "green"))

        max_threads = 100  # Número máximo de hilos para realizar el ping concurrentemente
        # Crea un pool de hilos para realizar pings concurrentemente
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            # Asigna la función host_discovery a cada IP en la lista de targets
            executor.map(host_discovery, targets)

# Llama a la función main si el script se ejecuta directamente
if __name__ == "__main__":
    main()