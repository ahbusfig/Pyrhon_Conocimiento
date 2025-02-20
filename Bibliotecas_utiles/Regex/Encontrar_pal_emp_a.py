import re
from termcolor import colored

def encontrar_aAá_texto(texto):
    """
    Función para encontrar todas las palabras que empiezan con la letra 'a' en un texto dado.
    """
    patron = r'\b[aAá]\w*'
    return re.findall(patron, texto, re.IGNORECASE)

def encontrar_(texto):
    res = []
    for palabra in texto.split():
        palabra = palabra.strip(",.")
        if palabra.startswith(("a", "á", "A", "'a'")):
            res.append(palabra)
    return res

            


if __name__ == "__main__":
    texto = """
    Aquí hay un ejemplo de texto. Algunas palabras empiezan con la letra 'a', como: árbol, amigo, avión, amor, arte.
    Otras palabras no empiezan con 'a', como: casa, perro, sol, luna.
    """
    palabras = encontrar_aAá_texto(texto)
    for palabra in palabras:
        print(colored(palabra, 'green'))

    #Forma 2 

    palabras = encontrar_(texto)
    for palabra in palabras:
        print(colored(palabra, 'yellow'))