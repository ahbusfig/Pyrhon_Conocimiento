import os
import shutil

#Funcion para crear un directorio
def crearDirectorioAnidado(ruta,darchivo):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        os.system(f'type nul > {archivo}')
        print(f"Directorio '{ruta}' creado.")
    else:
        print(f"El directorio '{ruta}' ya existe.")

# Función para borrar un directorio y su contenido
def borrarDirectorio(ruta):

    if os.path.exists(ruta):# Verificar si el directorio existe
        
        shutil.rmtree(ruta)     #Eliminar el directorio y su contenido  --> directorio no vacio
        print(f"Directorio '{ruta}' y su contenido han sido eliminados.")

        #Si es un directorio vacio --> os.rmdir(ruta)
    else:
        print(f"El directorio '{ruta}' no existe.")

# Función para obtener el tamaño de un archivo
def obtenerTamañoArchivo(ruta):
    # Verificar si el archivo existe
    if os.path.exists(ruta):
        # Obtener el tamaño del archivo en bytes 
        tamaño = os.path.getsize(ruta)
        print(f"El tamaño del archivo '{ruta}' es {tamaño} bytes.")
    else:
        print(f"El archivo '{ruta}' no existe.")
         
"""--------------------------------#Crear una ruta combinando el directorio y el nombre del archivo---------------------"""
# Comando clave: os.path.join --> #nombreDirectorio, nombreArchivo
ruta = os.path.join("mi_directorio", "mi_archivo.txt")
print(f"\n[+] Ruta completa del archivo: {ruta}")


"""----------------------------------------# Obtener el nombre del archivo a partir de la ruta---------------------------"""
# Comando clave: os.path.basename
archivo = os.path.basename(ruta)
print(f"[+] Nombre del archivo: {archivo}")

"""----------------------------------------# Obtener el nombre del directorio a partir de la ruta-------------------------"""
# Comando clave: os.path.dirname
directorio = os.path.dirname(ruta)
print(f"[+] Nombre del directorio donde está contenido el archivo: {directorio}")


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////Usamos la funciones//////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""-------------------------------------# Ejemplo de uso de las funciones definidas-------------------------"""
#Creamos el directorio
crearDirectorioAnidado(directorio,archivo)
# Comando clave: obtenerTamañoArchivo
obtenerTamañoArchivo(archivo)
# Comando clave: borrarDirectorio
borrarDirectorio("mi_directorio")
