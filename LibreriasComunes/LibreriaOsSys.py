import os
directorio = os.getcwd() #Similar al pwd en linux
#Listar directorio actual de trabajo 
def listar_directorio(directorio):
    print(f"Directorio actual trabajo --> {directorio} ")
    files = os.listdir(directorio)
    for file in files:
        print(file)

#listar_directorio(directorio)
#Vamos a crear una nuevo directorio 
def crearDirectorioNuevo(directorio, nombre):
    if (os.path.exists(nombre) != True):## Comprobar si el directorio ya existe
        os.mkdir(nombre)
        print(f"Se ha crear un nuevo directorio --> {nombre}")
        listar_directorio(directorio)
    else:
        print("[!] Ya hay un directorio con ese nombre !")

# Crear un nuevo archivo con una extensión específica
def crearArchivo(directorio, nombre, extension):
    archivo = f"{nombre}.{extension}"  #Crear el nombre archivo 
    ruta_archivo = os.path.join(directorio, archivo) 
    if (os.path.exists(ruta_archivo) != True):  # Si el archivo no existe
        with open(ruta_archivo, 'w') as f:
            f.write(f"Este es un archivo de ejemplo con extensión .{extension}")
        print(f"Se ha creado un nuevo archivo --> {archivo}")
        listar_directorio(directorio)
    else: #Si el archivo existe
        print(f"[!] Ya hay un archivo con el nombre {archivo} !")

# Ejemplo de uso
#crearDirectorioNuevo(directorio, "Pruebas2")
#crearArchivo(directorio, "archivo_ejemplo", "txt")
#crearArchivo(directorio, "archivo_ejemplo", "md")
#crearArchivo(directorio, "archivo_ejemplo", "py")


#Verificar si existe una variable de entorno
def verifVarEntorno(nombre_VarEnt):
    if nombre_VarEnt in os.environ:
        print(f"La variable de entorno {nombre_VarEnt} --> existe")
    else:
        print(f"La variable de entorno {nombre_VarEnt} --> no existe")


# Ejemplo de uso
#verifVarEntorno("PATH")
#verifVarEntorno("HOME")
#verifVarEntorno("VARIABLE_NO_EXISTENTE")

# Listar todas las variables de entorno
def listarVariablesEntorno():
    for clave, valor in os.environ.items():
        print(f"{clave}: {valor}")

# Ejemplo de uso
#listarVariablesEntorno()


import sys

"""
print(f"\n[+] Nombre del script: {sys.argv[0]}")
print(f"\n[+] Total argumentos que se están pasando al programa:{len(sys.argv)}")
print(f"\n[+] Mostrar 1 argumento: {sys.argv[1]}")
print(f"\n[+] Mostrar 2 argumento: {sys.argv[2]}")
print(f"\n[+] Mostrar todos los argumentos: {(sys.argv)}")
"""
print(f"[+] Mostrar las rutas de Python: ")
for ruta in sys.path:
    print(ruta)

print(f"[+] Saliendo con un codigo de estado 1 --> no exitoso")
sys.exit(1) #Esto es para linux


