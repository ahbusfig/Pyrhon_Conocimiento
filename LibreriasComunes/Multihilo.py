import threading
import time

def tarea(num_tarea):
    print(f"\n[+] Tarea {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Tarea {num_tarea} finalizando")
#Ejecutar tareas sin hilos --> Se hace secuencialmente
#tarea(1)
#tarea(2)


#Ejecutar tareas con hilos --> Se hacen las tareas en paralelo
"""Tarea_hilo1 = threading.Thread(target=tarea,args=(1,)) #"," pq es una tupla el argumento!
Tarea_hilo2 =threading.Thread(target=tarea,args=(2,))

Tarea_hilo1.start()
Tarea_hilo2.start()

print(f"Finalizando tareas con hilos")
"""

#####-----------------------------Multiprocessing-----------------------------
import multiprocessing
import time

# Ejecutar tareas con procesos
if __name__ == "__main__":
    Tarea_proceso1 = multiprocessing.Process(target=tarea, args=(1,))
    Tarea_proceso2 = multiprocessing.Process(target=tarea, args=(2,))

    Tarea_proceso1.start()
    Tarea_proceso2.start()

    Tarea_proceso1.join()
    Tarea_proceso2.join()

    print("Finalizando tareas")