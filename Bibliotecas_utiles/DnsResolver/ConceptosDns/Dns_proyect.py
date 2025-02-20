import dns.resolver
import dns.reversename

def consultar_registro(dominio, tipo):
    """Consulta registros DNS de un tipo específico."""
    try:
        respuesta = dns.resolver.resolve(dominio, tipo)
        return [registro.to_text() for registro in respuesta]
    except dns.resolver.NoAnswer:
        return [f"No se encontraron registros {tipo}."]
    except dns.resolver.NXDOMAIN:
        return ["El dominio no existe."]
    except dns.resolver.Timeout:
        return ["La consulta DNS expiró."]
    except Exception as e:
        return [f"Error inesperado: {e}"]

def resolver_inverso(ip):
    """Realiza una resolución inversa para una dirección IP."""
    try:
        nombre_inverso = dns.reversename.from_address(ip)
        respuesta = dns.resolver.resolve(nombre_inverso, "PTR")
        return [registro.to_text() for registro in respuesta]
    except dns.resolver.NoAnswer:
        return [f"No se encontraron registros PTR para {ip}."]
    except Exception as e:
        return [f"Error inesperado en resolución inversa: {e}"]

def auditoria_dns(dominio):
    """Realiza una auditoría completa de DNS para un dominio."""
    registros_a_consultar = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
    informe = {"Dominio": dominio, "Registros": {}}

    print(f"Auditoría DNS para el dominio: {dominio}")
    for tipo in registros_a_consultar:
        print(f"\nConsultando registros {tipo}...")
        registros = consultar_registro(dominio, tipo)
        informe["Registros"][tipo] = registros
        for registro in registros:
            print(f" - {registro}")

    # Realizar resolución inversa para todas las IP obtenidas en registros A
    if "A" in informe["Registros"]:
        ips = [registro for registro in informe["Registros"]["A"] if registro not in ["No se encontraron registros A.", "El dominio no existe."]]
        print("\nResolviendo nombres inversos para las IP obtenidas...")
        informe["Resolución inversa"] = {}
        for ip in ips:
            inverso = resolver_inverso(ip)
            informe["Resolución inversa"][ip] = inverso
            for host in inverso:
                print(f" - {ip} -> {host}")

    return informe

# Dominio a auditar
dominio = "google.com"
informe = auditoria_dns(dominio)

# Opcional: Guardar el informe en un archivo
with open("informe_dns.txt", "w") as f:
    f.write("Auditoría DNS\n")
    f.write(f"Dominio: {informe['Dominio']}\n\n")
    for tipo, registros in informe["Registros"].items():
        f.write(f"Registros {tipo}:\n")
        for registro in registros:
            f.write(f" - {registro}\n")
        f.write("\n")
    if "Resolución inversa" in informe:
        f.write("Resolución inversa:\n")
        for ip, hosts in informe["Resolución inversa"].items():
            f.write(f"IP {ip}:\n")
            for host in hosts:
                f.write(f" - {host}\n")
