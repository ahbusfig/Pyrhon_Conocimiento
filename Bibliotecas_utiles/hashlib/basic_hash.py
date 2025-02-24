import hashlib
from termcolor import colored

# Crear un nuevo objeto hash SHA256
h = hashlib.new("sha256")

# Actualizar el objeto hash con el objeto de tipo bytes
h.update(b"Hola mundo")

# Imprimir el resumen binario del hash
print(colored("El resumen binario del hash es:", "green", attrs=["bold"]))
print(h.digest())

# Imprimir el resumen hexadecimal del hash
print(colored("El resumen hexadecimal del hash es:", "blue", attrs=["bold"]))
print(h.hexdigest())


msg = b"hola"
m = hashlib.md5()
m.update(msg)
print(m.hexdigest())