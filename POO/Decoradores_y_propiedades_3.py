def contador_llamadas(funcion):
    contador_llamadas.llamadas = 0  # Inicializa el contador de llamadas

    def envolver(*args, **kwargs):
        contador_llamadas.llamadas += 1
        print(f"Iniciando función {funcion.__name__}")
        resultado = funcion(*args, **kwargs)  # Ejecuta la función original
        print(resultado)  # Imprime el resultado antes del mensaje de finalización
        print(f"Finalizando función {funcion.__name__}")
        print(f"Función {funcion.__name__} llamada {contador_llamadas.llamadas} veces")

    return envolver


class ejemplo: 
    def __init__(self, a ,b , c,*listaNum):
        self._a = a
        self._b = b
        self._c = c
        self._listaNum = list(listaNum)

        #Vamos a crear los getter y setters
    @property
    def a(self):
        return self._a 
    @a.setter
    def a(self, valor):
        if valor < 0 or not valor:
            raise ValueError("El valor debe ser >0 o no estar vacio")
        self._a = valor
        return f"Se ha cambiado el valor --> a = {valor} "
    @property
    def b(self):
        return self._b
    @b.setter
    def b(self, valor):
        if valor < 0 or not valor:
            raise ValueError("El valor debe ser > 0 o no estar vacio")
        self._b = valor 
        return f"Se ha cambiado el valor --> b = {valor} "
    @property
    def c(self):
        return self._c
    @c.setter
    def c(self, valor):
        if valor < 0 or not valor:
            raise ValueError("El valor debe ser > 0 o no estar vacio")
        self._c = valor 
        return f"Se ha cambiado el valor --> c = {valor} "
    @property
    def listaNum(self):
        return self._listaNum

    @listaNum.setter
    def listaNum(self, valor):
        if not isinstance(valor, list):
            raise ValueError("listaNum debe ser una lista")
        self._listaNum = valor

#   Vamos a definir como se imprime el objeto
    def __str__(self) -> str:
        return f"Los valores de a es {self._a}, b es {self._b} , c es {self._c} y la lista es --> {self._listaNum}"
    #Metodo estatico para sumar a,b,c
    @staticmethod
    def suma(a,b,c):
        return a + b + c
    @contador_llamadas
    def sumar(self):
        sumaT = self.suma(self.a, self.b, self.c)
        return f"La suma de a+b+c --> {sumaT}" 
    
ej1 = ejemplo(1,2,3,2,4) # Los 3 primeros valors -> a b c , el resto es para la lista
print(ej1)
print(f"El valor de a --> ",ej1.a) #Getter de a 
ej1.a = 10 #setter de a 

#print(f"El valor de c --> ",ej1.c) #Getter de c
#ej1.c = 10 #setter de c 

#print(ej1.listaNum) #Para acceder a atributos de la clase no poner parentesis
print(ej1)

ej1.sumar()