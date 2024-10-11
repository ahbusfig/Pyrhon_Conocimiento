#!/usr/bin/env 
import os
import pickle
from gestor_notas import GestorNotas
def main():
    gestor = GestorNotas()

    while True:
        print(f"\n---------------\nMenu\n---------------\n")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Buscar una nota")
        print("4. Eliminar una nota")
        print("5. Salir")

        opcion = input("\n[+] Escoge una opcion: ")

        if opcion == "1":
            contenido = input("\n[+] Contenido de la nota: ")
            gestor.agregar_nota(contenido)

        elif opcion == "2":
            notas = gestor.leer_notas()
            print("\n Mostrando todas las notas contenidas \n")
            for i,nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == "3":
            texto_buscado = input("\nIntroduzca la palabras clave para hacer la busqueda --> ")
            nota = gestor.buscar_nota(texto_buscado)

            for i,NOTA in enumerate(nota):
                print(f"{i}: {NOTA}")

        elif opcion =="4":
            notas = gestor.leer_notas()
            print("\n Mostrando todas las notas: \n")
            for i,nota in enumerate(notas):
                print(f"{i}: {nota}")
            ##Parte para eliminar una nola
            try:
                indice=int(input(f"\nDime el indice de la nota para eliminarla --> "))
            except ValueError:
                    return print("Ha de ser un numero el indice")
            gestor.eliminar_nota(indice)

        elif opcion == "5":
            break
        else:
            print("\n[+] La opcion escogida es incorrecta\n ")

        input(f"\n[+] Presiona <Enter> para continuar...")
        os.system('cls' if os.name=='nt' else 'clear')

        
if __name__ == "__main__":
    main()