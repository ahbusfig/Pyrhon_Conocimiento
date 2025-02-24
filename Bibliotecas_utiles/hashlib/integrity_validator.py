import hashlib
from termcolor import colored

# Primero obtener el hash de la pwd que se quiere validar 
pwd_1 = hashlib.sha1()
pwd_1.update(b"alain")
hash1 = pwd_1.hexdigest()

def pwd_validator(pwd):
    pwd_comp = hashlib.sha1()
    pwd_comp.update(pwd.encode())  # Pasar el texto plano a bytes!!
    hash_comp = pwd_comp.hexdigest()
    
    if hash_comp == hash1:
        print(colored("Password valida", "green"))
        return "valido"
    else:
        print(colored("Password invalido", "red"))
        return "invalido"

if __name__ == "__main__":
    contador = 0
    while True:
        pwd = input(colored("Introduce el pwd porfavor --> ","yellow"))
        valid = pwd_validator(pwd)
        if valid == "valido":
            break

        if contador == 2:
            print(colored("Numero de intentos  max. excedido --> cuenta bloqueada", "red"))
            break
        contador += 1


