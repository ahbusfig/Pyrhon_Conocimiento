import dns.resolver
import dns.reversename

# IP para realizar la resolución inversa
ip = "8.8.8.8"

def dns_reverse(ip):
    # Convertir la IP a su formato de nombre inverso
    nombre_inverso = dns.reversename.from_address(ip)
    print(nombre_inverso)
    # Realizar la consulta DNS para el registro PTR
    try:
        nombre_resuelto = dns.resolver.resolve(nombre_inverso, "PTR")
        resultado = [str(host) for host in nombre_resuelto]
    except dns.resolver.NXDOMAIN:
        resultado = ["No existe un registro PTR para esta IP."]
    except dns.resolver.NoAnswer:
        resultado = ["No se obtuvo respuesta para el registro PTR."]
    except dns.resolver.Timeout:
        resultado = ["La consulta DNS expiró."]
    except Exception as e:
        resultado = [f"Error inesperado: {e}"]
        
    print(resultado)


dns_reverse(ip)