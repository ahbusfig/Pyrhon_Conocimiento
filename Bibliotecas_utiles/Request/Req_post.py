import requests  # Importa la biblioteca requests para hacer solicitudes HTTP
import json  # Importa la biblioteca json para formatear la respuesta

url = "https://httpbin.org/post"  # URL a la que se hará la solicitud

data = {'key': 'value'}  # Datos que se enviarán en la solicitud POST

response = requests.post(url, data=data)  # Realiza una solicitud POST a la URL especificada con los datos

print(response.status_code)  # Imprime el código de estado de la respuesta

# Formatea e imprime el contenido de la respuesta
formatted_response = json.dumps(response.json(), indent=4)
print(formatted_response)