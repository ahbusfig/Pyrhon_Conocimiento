import re
from termcolor import colored

def buscar_emails(texto):
    """
    Función para buscar direcciones de correo electrónico en un texto dado.
    """
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(patron, texto)

def check_email(email):
    """
    Función para validar si un correo electrónico tiene un formato correcto.
    """
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # Condiciones adicionales para evitar errores
    if (re.fullmatch(patron, email) 
            and not re.search(r"(^[-_.]|[-_.]$)", email)  # No debe empezar o terminar con - _ .
            and not re.search(r"\.\.", email)  # Evita dos puntos seguidos
            and not re.search(r"-\.", email)  # Evita combinaciones de guion y punto
            and not re.search(r"\.@", email)  # Evita un punto antes de la @
            and not re.search(r"@[-]", email)  # Evita guion justo después de @
            and not re.search(r"--@", email)  # Evita doble guion antes de @
            and not re.search(r"@\.|\.-", email)  # Evita dominio que empiece con . o termine en -
        ):
        return True
    else:
        return False



if __name__ == "__main__":
    texto = """
    Hola, puedes contactarme en example@example.com para más información.
    También puedes enviar un correo a support@domain.org o info@another-domain.net.
    Correos no válidos: -@-.com, example@-example.com, example@.example.com, example@exam..ple.com.
    Otros correos válidos: user+alias@example.com, user.name@example.co.uk, customer/department=shipping@example.com.
    
    Aquí hay algunos correos adicionales:
    - contacto@empresa.com
    - ventas@empresa.co
    - info@sub.dominio.com
    - usuario@dominio-muy-largo-con-muchos-caracteres.com
    - usuario@dominio_con_guion_bajo.com
    - usuario@dominio-con-guion-.com (inválido)
    - usuario@dominio..com (inválido)
    - usuario@dominio.c (inválido)
    - usuario@dominio.corporate (válido)
    - usuario--@dominio.travel (inválido)
    - usuario@dominio.museum (válido)
    - usuario@dominio.123 (inválido)
    """
    text2 = """ example@example.com
                support@domain.org
                info@another-domain.net
                user+alias@example.com
                user.name@example.co.uk
                customer/department=shipping@example.com
                contacto@empresa.com
                ventas@empresa.co
                info@sub.dominio.com
                usuario@dominio-muy-largo-con-muchos-caracteres.com
                usuario@dominio_con_guion_bajo.com
                usuario@dominio-con-guion-.com
                usuario@dominio..com
                usuario@dominio.c
                usuario@dominio.corporate
                usuario--@dominio.travel
                usuario@dominio.museum
                usuario@dominio.123
                -user@domain.com
                user@-domain.com
                user@domain..com
                user@domain.
                user.@domain.com
                user@.domain.com
    """
    
    emails = buscar_emails(text2)
    print(colored(f"Buscando posibles emails ...", "yellow"))
    print(colored(f"Se ha encontrado un total de {len(emails)} emails", "yellow"))
    for email in emails:
        if check_email(email):
            print(colored(f"El email {email} es válido", "green"))
        else:
            pass