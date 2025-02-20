import re
from termcolor import colored

def is_valid_email():
    patron = r"^(?!.*[-_.]{2})[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

    while True:
        try:
            email = input("Introduzca su email (formato example@example.com) --> ").strip()

            if re.fullmatch(patron, email) and not re.search(r"(^[-_.]|[-_.]$)", email):
                print(colored(f"✅ El formato del email '{email}' es correcto.", 'green'))
                return email  # Devolvemos el email para que se pueda usar en otro lugar
            else:
                print(colored(f"❌ El formato del email '{email}' es incorrecto. Inténtelo de nuevo.", 'red'))

        except Exception as e:
            print(colored(f"⚠️ Ocurrió un error inesperado: {e}", 'yellow'))

# Ejemplo de uso
# is_valid_email()


# Explicacion del patron
# patron = r"^(?!.*[-_.]{2})[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

# ^(?!.*[-_.]{2}) --> Asegura que no haya dos caracteres especiales seguidos (.-_) y tampoco aparezca .* 
# [a-zA-Z0-9._%+-]+ --> Permite letras, números y ciertos caracteres especiales antes del @
# @[a-zA-Z0-9-]+ --> Asegura que haya un @ seguido de letras, números o guiones
# \.[a-zA-Z]{2,}$ --> Asegura que haya un punto seguido de al menos dos letras (dominio)

# En resumen, este patrón verifica que el email tenga un formato válido y no tenga caracteres especiales consecutivos.

def check_email(email):
    patron = r"^(?!.*[-_.]{2})[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    
    if re.fullmatch(patron, email) and not re.search(r"(^[-_.]|[-_.]$)", email):
        return True
    else:
        return False
