import dns.resolver
"""
    A: Dirección IPv4.
    AAAA: Dirección IPv6.
    MX: Servidores de correo.
    NS: Servidores de nombres.
    TXT: Registros de texto (como SPF o DKIM).
    CNAME: Nombres canónicos.
"""
#Consulta básica 
dominio = "forocoches.com"
resIpv4 = dns.resolver.resolve(dominio, "A")
resIpv6 = dns.resolver.resolve(dominio, "AAAA")
#Imprimir respuesta
for ip in resIpv4:
    print(f"Direccion IP: {ip}")

for ip in resIpv6:
    print(f"Direccion IPv6: {ip}")

#######Servidores de correo.
respuesta_mx = dns.resolver.resolve(dominio, "MX")

for registro in respuesta_mx:
    print(f"Servidor de correo: {registro.exchange}, Prioridad: {registro.preference}")
