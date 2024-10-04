# Como usar el enumerate en el contexto del hacking ético

"""El enumerate en Python se usa para iterar sobre una secuencia 
(como una lista o una tupla) y obtener tanto el índice como el valor 
del elemento en cada iteración. Aquí tienes un ejemplo de cómo usarlo:"""

# Lista de servicios en un servidor
servicios = ['SSH', 'FTP', 'HTTP', 'HTTPS', 'SMTP']

# Usando enumerate para obtener el índice y el nombre del servicio
for indice, servicio in enumerate(servicios):
    print(f"Escaneando el servicio {indice + 1}: {servicio}")