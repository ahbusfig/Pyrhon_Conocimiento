import dns.resolver

#Limitar tiempo de vida o time out
resolver = dns.resolver.Resolver()
resolver.timeout = 2  # Tiempo máximo de espera por consulta (segundos)
resolver.lifetime = 5  # Tiempo total permitido para resolver la consulta

dominio = "noexiste.com"

try:
    respuesta = dns.resolver.resolve(dominio, "A")
    for ip in respuesta:
        print(f"Dirección IP: {ip}")
except dns.resolver.NXDOMAIN:
    print("El dominio no existe.")
except dns.resolver.NoAnswer:
    print("No hay respuesta para el tipo de consulta.")
except dns.resolver.Timeout:
    print("La consulta DNS ha expirado.")
except Exception as e:
    print(f"Error inesperado: {e}")
