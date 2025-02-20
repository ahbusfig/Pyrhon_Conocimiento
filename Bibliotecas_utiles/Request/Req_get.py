import requests  # Importa la biblioteca requests para hacer solicitudes HTTP

url = "https://google.es"  # URL a la que se hará la solicitud

req = requests.get(url)  # Realiza una solicitud GET a la URL especificada

print(req.status_code)  # Imprime el código de estado de la respuesta
print(req.content)  # Imprime el contenido de la respuesta
print(req.json())  # Intenta imprimir el contenido JSON de la respuesta, si existe