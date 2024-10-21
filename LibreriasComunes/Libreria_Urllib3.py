#Tiene similitudes con request pero más facil de usar !
#print(dir(response))  --> lista los metodos diponibles para http.request('GET', url)
import urllib3
#----------------------Petición get simple---------------------
print(f"\n[+] Peticion get\n")
http = urllib3.PoolManager() #Controlador de conexiones!!
url = "https://httpbin.org/get"
response = http.request('GET', url)
print(response.status) # 200 --> Ok
print(response.data.decode('utf-8')) #Hay que decodificar la info --> está en binario

#----------------------Peticion post simple---------------------
import json
print(f"\n[+] Peticion POST\n")

http = urllib3.PoolManager()
url = "https://httpbin.org/post"
data = {"key1": "value1", "key2": "value2"}
encoded_data = json.dumps(data).encode('utf-8')

response = http.request(
    'POST',
    url,
    body=encoded_data,
    headers={'Content-Type': 'application/json'}
)

print("Status code --> ",response.status , "--> okey" if response.status==200 else "--> Error" )
print(response.data.decode('utf-8'))

#-----------------------------Basic Autentication-------------------
from urllib3.util import make_headers

http = urllib3.PoolManager()
url = "https://httpbin.org/basic-auth/foo/bar"
headers = make_headers(basic_auth='foo:bar')

response = http.request('GET', url, headers=headers)

print(response.status)
print(response.data.decode('utf-8'))
#-----------------------------Manejar cookies-------------------
import urllib3

http = urllib3.PoolManager()
url = "https://httpbin.org/cookies"
cookies = {'cookies_are': 'working'}

response = http.request('GET', url, headers={'Cookie': 'cookies_are=working'})

print(response.status)
print(response.data.decode('utf-8'))

#-----------------------------Manejar Redireccionamiento-------------------

import urllib3

http = urllib3.PoolManager()
url = "http://github.com"

response = http.request('GET', url, redirect=True)

print(response.status)
print(response.geturl())
print(response.data.decode('utf-8'))


#------------------------Manejar session para authentication------------------
class SessionWithAuth:
    def __init__(self, username, password):
        self.http = urllib3.PoolManager()
        self.headers = urllib3.util.make_headers(basic_auth=f'{username}:{password}')

    def get(self, url):
        return self.http.request('GET', url, headers=self.headers)

url = "https://httpbin.org/basic-auth/foo/bar"
session = SessionWithAuth('foo', 'bar')

response1 = session.get(url)
print(response1.status)
print(response1.data.decode('utf-8'))

response2 = session.get(url)
print(response2.status)
print(response2.data.decode('utf-8'))