  ##########################################################################################
 ##################----Como trabajar con ficheros----######################################
##########################################################################################

""" Write --> sobreescribe
f = open("Ejemplo2.txt","w") #W --> sobreescribe lo que habia antes
f.write("Hola a todos \n")
f.close()
"""

""" Append --> añade
f = open("Ejemplo2.txt","a") #a --> añade a lo ya está puesto y no sobreescribe
f.write("Hola a todos \n")
f.close()
"""
"""  # Leer
print("Forma sin caracteres especiales")
with open("Ejemplo2.txt","r") as f:
    for line in f.readlines(): #Carga las lineas en memoria antes  f.readline --> lee 1 linea solo!
        print(line.strip()) #Strip evita el salto de linea

print("Forma con caracteres especiales")
with open("Ejemplo2.txt","rb") as f:
    for line in f: #No carga las lineas en memoria antes 
        print(line.decode().strip())
"""
#Escribir de un objeto iterable 
mi_lista = ["1 linea\n", "2 linea\n","3 linea \n" ]
with open("Ejemplo2.txt","w") as f:
    #for line in mi_lista:
    #   f.write(line)
    f.writelines(mi_lista)


def copiar_contenido_fichero(rutaCopia,rutaPegado):
    with open(rutaCopia,"rb") as f_in, open(rutaPegado,"wb") as f_out:
        file_content = f_in.read()
        f_out.write(file_content)
        #Ruta copia --> /alain/Desktop/archivo.png o txt
        #Ruta Pegado --> poner el nombre del archivo yaban --> copiado.txt o png o ...

 #Manejar excepciones
try:
    with open("Ejemplo2.txt","r") as f:
        print(f.read())
except FileNotFoundError: #Se pone el error esperado en las except
    print(f"[i] Error! No se ha encontrado el archivo!")