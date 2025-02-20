import requests

"""
response = requests.get("https://google.com")

print(f"\n [+] Status code: {response.status_code}")
print(f"\n [+] mostrando codigo fuente de la respuesta:\n")

with open("index.html","w") as f:
    f.write(response.text)
"""

#Url para esta nueva seccion 
url= "https://httpbin.org"
#Peticion get --> Para obtener los valores que queremos del  httpbin.org (servidor al que haremos la peticion)
"""
values = {"key1":"value1", "key2":"value2" ,"key3":"value3"}
response = requests.get(f"{url}/get", params=values )
print(f"\n [+] url final: {response.url}")
print(response.text)
"""
#Peticion post --> donde queremos enviar informacion 
"""payload = {"key1":"value1", "key2":"value2" ,"key3":"value3"}
response = requests.post(f"{url}/post", data=payload )
#print(f"\n [+] url final: {response.url}")
print(response.text)

print(len(payload["key1"])) #En diccionario el indice se usa la clave !


def request_exceptions(url):
    try:
        response = requests.get(url,timeout=1)
        response.raise_for_status()
    except requests.Timeout as Terror:
        print(f"\n [!] Error Timeout: {Terror}")
    except requests.HTTPError as HTTPError:
        print(f"\n [!] Error Http: {HTTPError.url}")
    except requests.RequestException as ERR:
        print(f"\n [!] error: {ERR}")

#Si respuesta formato json 
url= "https://httpbin.org/get"

response = requests.get(url)
data = response.json()

if "headers" in data and 'User-Agent' in data['headers']:
    user_agent = data['headers']['User-Agent']
    print(user_agent)
else:
    print(f"[!] No existe este campo en la respuesta")"""

#######################################################################################################
#############################----Parte 2 del video request----#########################################
#######################################################################################################
#--------------------------Basich authentication(pabeles basicos por defecto)--------------------------
#import requests
url = "https://httpbin.org/basic-auth/foo/bar"
def basic_auth(url):
    res = requests.get(url, auth=("foo","bar")) #auth --> "user","pwd"
    return res.text
#print(basic_auth(url))
#---------------------------..........--El uso de cookies-----------------------------------------------
cookies = dict(cookies_are='working')
res = requests.get('https://httpbin.org/cookies', cookies=cookies)
print(res.text)
#-------------------------------------Listar un file dentro del json -------------------------------

#--------------------Para rastrear el redireccionamiento de paginas web--------------------------------
import requests
url = "http://github.com"
def rastreo_redireccionamiento(url):
    r = requests.get(url) #Nos da codigo status 200 --> que se ha hecho bien la peticion

    for request in r.history:
        print(f"\n[+] Ha pasado por la url {request.url} y nos ha dado el codigo de estado {request.status_code}")

    print(f"\n[+] La url final es --> {r.url} y nos ha dado el codigo de estado {r.status_code}")
#rastreo_redireccionamiento(url)
#--------------------------------------Arrastre de sesiones---------------------------------------------
import requests
url = "https://httpbin.org/basic-auth/foo/bar"
def ArrastreSession(url):
    with requests.Session() as session:
        session.auth = ('foo','bar')
        res1 = session.get(url)
        print(res1.text)

        res2 = session.get(url)
        print(res2.text)
        #De esta manera se arrastra la autentificacion para las dif peticiones
        #Debido al uso de la sesion y with!