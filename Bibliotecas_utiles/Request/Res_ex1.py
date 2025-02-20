import requests  # Importa la biblioteca requests para hacer solicitudes HTTP
import json  # Importa la biblioteca json para formatear la respuesta

# Define la URL de la API de OpenWeatherMap con la ciudad y tu clave de API
lat = 40.416775
lon = -3.703790
api_key = "f9ca7dff0af4a33d2751261e511c954b"  # Reemplaza esto con tu clave de API de OpenWeatherMap
ciudad = "londres"
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
       
response = requests.get(url, timeout=3)  # Realiza una solicitud GET a la URL especificada con un tiempo de espera de 3 segundos

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    print("Solicitud exitosa!")
    # Formatea e imprime el contenido de la respuesta
    data = response.json()
    formatted_response = json.dumps(data, indent=4)
    print(formatted_response)
    
    # Guardamos la información en variables
    coord = data['coord']
    weather = data['weather'][0]
    main = data['main']
    wind = data['wind']
    clouds = data['clouds']
    sys = data['sys']
    name = data['name']    

    # Ejemplo de acceso a variables
    print(f"Ciudad: {name}")
    print(f"Coordenadas: {coord}")
    print(f"Clima: {weather['description']}")
    print(f"Temperatura: {main['temp']} K")
    print(f"Presión: {main['pressure']} hPa")
    print(f"Humedad: {main['humidity']}%")
    print(f"Velocidad del viento: {wind['speed']} m/s")
    print(f"Nubosidad: {clouds['all']}%")
    print(f"País: {'España' if sys['country'] == 'ES' else sys['country']}")

else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)  # Imprime el contenido de la respuesta en caso de error