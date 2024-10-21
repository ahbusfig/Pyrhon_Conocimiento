#!/usr/bin/env python3
import requests
import threading
import time

def realizar_peticion(url):
    response = requests.get(url)
    print(f"\n[+] Url {response.url}: {len(response.content)} bytes")

dominios = [
    "https://google.es",
    "https://wikipedia.org",
    "https://yahoo.com"
]

def peticion_hilos(dominios):
    start_time = time.time()
    hilos = []
    for url in dominios:
        hilo = threading.Thread(target=realizar_peticion, args=(url,))
        hilo.start()
        # Vamos a almacenar el resultado en la lista hilos
        hilos.append(hilo)

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    end_time = time.time()

    print(f"\n[+] Tiempo total {round(end_time - start_time, 2)} segundos")
peticion_hilos(dominios)
##############################################################################################################################
#############################-------------------Multiprocessing-----------####################################################
##############################################################################################################################
#!/usr/bin/env python3
import requests
import multiprocessing
import time

def realizar_peticion(url):
    response = requests.get(url)
    print(f"\n[+] Url {response.url}: {len(response.content)} bytes")

dominios = [
    "https://google.es",
    "https://wikipedia.org",
    "https://yahoo.com"
]

def realizar_multiprocessing(dominios):
    start_time = time.time()
    procesos = []
    for url in dominios:
        proceso = multiprocessing.Process(target=realizar_peticion, args=(url,))
        proceso.start()
        # Vamos a almacenar el resultado en la lista procesos
        procesos.append(proceso)

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    end_time = time.time()

    print(f"\n[+] Tiempo total {round(end_time - start_time, 2)} segundos")

#if __name__ == "__main__":
    #realizar_multiprocessing(dominios)