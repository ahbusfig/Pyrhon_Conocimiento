import re
def validar_ip(ip):
    """
    Función para validar si una dirección IP (IPv4) tiene un formato correcto.
    """
    patron = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    p  = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    return re.fullmatch(p, ip) is not None

if __name__ == "__main__":
    ip = "192.168.1.2"  # Dirección IP
    if validar_ip(ip):
        print(f"La dirección IP {ip} es válida.")
    else:
        print(f"La dirección IP {ip} no es válida.")



"""
📍 1. ^ y $ → Inicio y fin de la cadena
^ indica que la coincidencia debe empezar desde el inicio de la cadena.
$ indica que la coincidencia debe terminar al final de la cadena.
Esto evita que la regex coincida con una subcadena dentro de otra más larga.

📍 2. ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3} → Primeros 3 octetos de la IP
La expresión ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3} representa los tres primeros octetos de la dirección IP, cada uno seguido por un punto (.).

(25[0-5]) → Coincide con números del 250 al 255.
| → Es un "o lógico" (OR), separa opciones posibles.
(2[0-4][0-9]) → Coincide con números del 200 al 249.

([01]?[0-9][0-9]?) → Coincide con números del 0 al 199:
    [01]? → Permite 0 o 1 opcionalmente. --> 0,1," "
    [0-9] → Obliga a tener al menos un dígito (0-9).
    [0-9]? → Permite un segundo dígito opcional (para formar 99 o 199).
    Este patrón captura números de 0 a 199, pero no 200-255 (eso se maneja con otro patrón).

📍 3. (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) → Último octeto de la IP
Es el mismo patrón que los octetos anteriores, pero sin el punto final (.) porque la dirección termina aquí.

📍 4. {3} → Se repite exactamente 3 veces
((...)\.){3} indica que la parte que define un octeto seguida de un . debe repetirse tres veces (para los tres primeros octetos de la IP).
"""