import requests  # Importa la biblioteca requests para hacer solicitudes HTTP
import json  # Importa la biblioteca json para formatear la respuesta

url = "https://httpbin.org/get"  # URL a la que se hará la solicitud

response = requests.get(url, timeout=3)  # Realiza una solicitud GET a la URL especificada con un tiempo de espera de 3 segundos

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    print("Solicitud exitosa!")
    # Formatea e imprime el contenido de la respuesta
    formatted_response = json.dumps(response.json(), indent=4)
    print(formatted_response)
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)  # Imprime el contenido de la respuesta en caso de error