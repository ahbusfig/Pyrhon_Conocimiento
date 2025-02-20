import re 
from termcolor import colored

#buscar la palabra clave
# substituirla 

def substituir_palabra_clave(palabra, reemplazo,texto):
    patron = rf"\b{palabra}\b"
    return re.sub(patron, reemplazo,texto)

def substituir(palabra, reemplazo, texto):
    res = []
    texto = texto.split()
    for pal in texto:
        if pal == palabra:
            res.append(reemplazo)
        else:
            res.append(pal)

    return ' '.join(res)

if __name__ == "__main__":
    texto = """
    Python es un lenguaje de programación muy popular. 
    Muchas personas aprenden Python como su primer lenguaje de programación.
    Python es conocido por su simplicidad y legibilidad.
    """
    palabra_clave = "Python"
    reemplazo = "JavaScript"
    
    texto_modificado = substituir_palabra_clave(palabra_clave, reemplazo, texto)
    print(colored(texto_modificado, 'green'))

    print(substituir(palabra_clave, reemplazo, texto))