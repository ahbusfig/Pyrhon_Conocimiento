def suma (x,y):
    return x + y

def resta(x,y):
    return x-y

def multip(x,y):
    return x*y

def div(x,y):
    if y == 0:
        raise ValueError("\n [i] No es posible dividir un num. entre 0")
    else:
        return x / y