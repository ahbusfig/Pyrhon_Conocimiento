#Formas de poner variables en un string
a = 6 
b = 8
print(f"1F -> la suma de {a} + {b} = {a+b}")
print("2F -> La suma de {0} + {1} es {2}".format(a,b,a+b))
print("3F -> La suma de %d + %d es %d" % (a, b, a+b))

#Formas de modificar la cadena

cadena = "   Hola BUENOS dias  \n \t"
print(cadena)
print(cadena.strip()) #Strip --> quita estpacios de izq y derecha de la cadena, saltos de linea...
print(cadena.strip().upper()) # Mayuscula
print(cadena.strip().lower()) # Minuscual
print(cadena.replace("o","a")) # reemplaza

# Split
print(cadena.split()) # Divide la cadena en palabras usando espacios en blanco como delimitador
print(cadena.strip().split()) # Divide la cadena después de quitar espacios en blanco de los extremos
print(cadena.strip().split("o")) # Divide la cadena usando 'o' como delimitador
print(cadena.strip().split(" ", 1)) # Divide la cadena en dos partes usando el primer espacio como delimitador

#Comprobaciones 
cadena = "Hola mundo"
print(cadena.startswith("Hola"))
print(cadena.startswith("H"))
print(cadena.endswith("o"))
print(cadena.endswith("mundo"))

# Ejemplos con el método count
cadena = "Hola mundoo"
print("La o aparece --> ",cadena.count("o") , " Veces") # Cuenta cuántas veces aparece 'o' en la cadena
print("Hola aparece --> ",cadena.count("Hola")) # Cuenta cuántas veces aparece 'Hola' en la cadena
print("Contador de espacios en blanco --> ",cadena.count(" ")) # Cuenta cuántos espacios en blanco hay en la cadena
print("mundo aparece --> ",cadena.count("mundo")) # Cuenta cuántas veces aparece 'mundo' en la cadena
print("cuántas veces aparece 'a' en la cadena desde el índice 0 hasta el 5 --> ",cadena.count("a", 0, 5)) # Cuenta cuántas veces aparece 'a' en la cadena desde el índice 0 hasta el 5

# Ejemplos con el método join

# Unir una lista de palabras en una sola cadena con espacios
palabras = ["Hola", "mundo", "Python", "es", "genial"]
cadena_unida = " ".join(palabras)
print("Unir con espacios:", cadena_unida)

# Unir una lista de palabras en una sola cadena con comas
cadena_unida_comas = ", ".join(palabras)
print("Unir con comas:", cadena_unida_comas)

# Unir una lista de caracteres en una sola cadena
caracteres = ['H', 'o', 'l', 'a']
cadena_unida_caracteres = "".join(caracteres)
print("Unir caracteres:", cadena_unida_caracteres)

# Unir una lista de números en una sola cadena (convertir números a cadenas primero)
numeros = [1, 2, 3, 4, 5]
cadena_unida_numeros = "-".join(map(str, numeros))
print("Unir números:", cadena_unida_numeros)

# Unir una lista de palabras en una sola cadena con un salto de línea
cadena_unida_saltos = "\n".join(palabras)
print("Unir con saltos de línea:\n", cadena_unida_saltos)

#swapcase,title,capitalize
s = "hola bueNas dias"
print(s.capitalize()) #1 letra en mayuscula
print(s.title())  # 1 letra de cada palabra en mayuscula
print(s.swapcase()) # Cambias mayusc por minusc y viceversa 

# Ejemplos con métodos is...

s = "HolaMundo123"
s2 = "holamundo"
s3 = "12345"
s4 = "   "
s5 = "Hola Mundo"
s6 = "Hola_Mundo"

# Verificar si todos los caracteres son alfanuméricos (letras y números)
print(s.isalnum())  # True
print(s5.isalnum()) # False (contiene un espacio)

# Verificar si todos los caracteres son letras
print(s.isalpha())  # False (contiene números)
print(s2.isalpha()) # True

# Verificar si todos los caracteres son dígitos
print(s3.isdigit()) # True
print(s.isdigit())  # False

# Verificar si todos los caracteres son minúsculas
print(s2.islower()) # True
print(s.islower())  # False

# Verificar si todos los caracteres son mayúsculas
print(s.isupper())  # False
print(s.upper().isupper()) # True

# Verificar si la cadena es un espacio en blanco
print(s4.isspace()) # True
print(s5.isspace()) # False

# Verificar si la cadena está capitalizada (primera letra en mayúscula, el resto en minúscula)
print(s.capitalize().istitle()) # True
print(s2.istitle()) # False

# Verificar si la cadena está en formato de título (cada palabra empieza con mayúscula)
print(s5.istitle()) # True
print(s6.istitle()) # False (contiene un guion bajo)

# Verificar si la cadena es imprimible
print(s.isprintable()) # True
print("\n".isprintable()) # False (contiene un carácter de nueva línea)

# Verificar si la cadena es un identificador válido en Python
print(s.isidentifier()) # True
print(s5.isidentifier()) # False (contiene un espacio)
