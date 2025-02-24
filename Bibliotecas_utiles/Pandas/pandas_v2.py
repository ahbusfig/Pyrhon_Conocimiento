import pandas as pd 
from termcolor import colored

#Importar el archivo
bio = pd.read_csv('./data/bios.csv')
'''
#Ej de Visualizar y Filtrado de Datos
'''
# Mostrar los primeros y ultimos 5 de la lista
print(colored("Mostrar los primeros 5 de la lista", "green"))
print(colored(bio.head(5), "yellow"))
print(colored("Mostrar los últimos 5 de la lista", "green"))
print(colored(bio.tail(5), "yellow"))

# Mostrar los nombres de los atletas
print(colored("Mostrar los nombres de los atletas", "green"))
print(colored(bio[['name', 'born_date', 'born_city','height_cm']].head(), "yellow"))

# Mostrar los atletas nacidos después del año 2000
print(colored("Mostrar los atletas nacidos después del año 2000", "green"))
print(colored(bio[bio['born_date'] > '2000-01-01'].tail(20), "yellow"))

# Mostrar los atletas que miden más de 180 cm
print(colored("Mostrar los atletas que miden más de 180 cm", "green"))
print(colored(bio[bio['height_cm'] > 180].head(20), "yellow"))

# Mostrar los atletas que miden entre 170 cm y 180 cm
print(colored("Mostrar los atletas que miden entre 170 cm y 180 cm", "green"))
print(colored(bio[(bio['height_cm'] >= 170) & (bio['height_cm'] <= 180)].head(20), "yellow"))

# Mostrar los atletas que pesan menos de 70 kg
print(colored("Mostrar los atletas que pesan menos de 70 kg", "green"))
print(colored(bio[bio['weight_kg'] < 70].head(20), "yellow"))

# Mostrar los atletas que nacieron en una Paris
print(colored("Mostrar los atletas que nacieron en Paris", "green"))
print(colored(bio[bio['born_city'] == 'Paris'].head(20), "yellow"))

# Mostrar los atletas nacidos antes del año 1990
print(colored("Mostrar los atletas nacidos antes del año 1990", "green"))
print(colored(bio[bio['born_date'] < '1990-01-01'].head(20), "yellow"))

# Mostrar los atletas que pesan más de 80 kg
print(colored("Mostrar los atletas que pesan más de 80 kg", "green"))
print(colored(bio[bio['weight_kg']>80],"yellow"))

# Mostrar los atletas que nacieron en una ciudad que empieza con 'L'
print(colored("Mostrar los atletas que nacieron en una ciudad que empieza con 'L'", "green"))
print(colored(bio[bio['born_city'].str.startswith('L')],"yellow"))

# Mostrar los atletas que miden más de 175 cm y pesan menos de 75 kg
print(colored("Mostrar los atletas que miden más de 175 cm y pesan menos de 75 kg", "green"))
print(colored(bio[(bio['height_cm'] > 175) & (bio['weight_kg'] < 75)], "yellow"))

# Mostrar los atletas nacidos entre 1980 y 2000
print(colored("Mostrar los atletas nacidos entre 1980 y 2000", "green"))
print(colored(bio[(bio['born_date'] > '1980-1-1') & (bio['born_date'] < '2000-1-1')], "yellow"))

# Mostrar los atletas que nacieron en una ciudad que contiene 'York'
print(colored("Mostrar los atletas que nacieron en una ciudad que contiene 'York'", "green"))
print(colored(bio[bio['born_city'].fillna('').str.contains('York', case=False)], "yellow"))

# Mostrar los atletas que nacieron en una ciudad que contiene 'San'
print(colored("Mostrar los atletas que nacieron en una ciudad que contiene 'San'", "green"))
print(colored(bio[bio['born_city'].fillna('').str.contains('San', case=False)], "yellow"))

# Mostrar los atletas que nacieron en una ciudad que termina con 's'
print(colored("Mostrar los atletas que nacieron en una ciudad que termina con 's'", "green"))
print(colored(bio[bio['born_city'].fillna('').str.endswith('s')], "yellow"))

# Mostrar los atletas cuyo nombre empieza con 'A'
print(colored("Mostrar los atletas cuyo nombre empieza con 'A'", "green"))
print(colored(bio[bio['name'].fillna('').str.startswith('A')], "yellow"))

# Mostrar los atletas cuyo nombre contiene 'John'
print(colored("Mostrar los atletas cuyo nombre contiene 'John'", "green"))
print(colored(bio[bio['name'].fillna('').str.contains('John', case=False)], "yellow"))

# Mostrar los atletas cuyo nombre termina con 'son'
print(colored("Mostrar los atletas cuyo nombre termina con 'son'", "green"))
print(colored(bio[bio['name'].fillna('').str.endswith('son')], "yellow"))

# Mostrar los atletas cuyo nombre tiene una longitud mayor a 10 caracteres
print(colored("Mostrar los atletas cuyo nombre tiene una longitud mayor a 10 caracteres", "green"))
print(colored(bio[bio['name'].fillna('').str.len() > 10], "yellow"))

# Mostrar los atletas cuyo nombre tiene una longitud menor o igual a 5 caracteres
print(colored("Mostrar los atletas cuyo nombre tiene una longitud menor o igual a 5 caracteres", "green"))
print(colored(bio[bio['name'].fillna('').str.len() <= 5], "yellow"))

# Mostrar los atletas cuyo nombre contiene la letra 'e' al menos dos veces
print(colored("Mostrar los atletas cuyo nombre contiene la letra 'e' al menos dos veces", "green"))
print(colored(bio[bio['name'].fillna('').str.count('e') >= 2], "yellow"))

# Mostrar los atletas cuyo nombre contiene una 'a' seguida de cualquier caracter y luego una 'n'
print(colored("Mostrar los atletas cuyo nombre contiene una 'a' seguida de cualquier caracter y luego una 'n'", "green"))
print(colored(bio[bio['name'].fillna('').str.contains('a.n', regex=True)], "yellow"))
