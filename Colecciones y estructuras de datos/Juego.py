juegos = ["Mario bros", "Zelda", "Dark souls","Ciberpunk 2077"]
tope = 500
#generos
generos = {
    "Mario bros": "aventura",
    "Zelda": "Aventura",
    "Dark souls": "Rol",
    "Ciberpunk 2077": "Rol"
}
#Ventas y stock
ventas_y_stock = {
    "Mario bros": (400,200),
    "Zelda": (600,20),
    "Dark souls": (60,120),
    "Ciberpunk 2077": (900,3)
}
#Clientes
clientes = {
     "Mario bros": ("Marco","Alain","Raul","Hackavis","Lobotec"),
    "Zelda": ("Hackavis","Laura","Sofia","Alex","Raul"),
    "Dark souls": ("Hackavis","Laura","Alain","Carlos","Pedro"),
    "Ciberpunk 2077": ("Pepe","Lucia","Martin","Agustin","Berly")
}

mi_juego = "Mario bros"
def sumario(mi_juego):
    #Resumen
    print(f"\n [i] Resumen del juego {mi_juego}")
    print(f"\t [+] Genero del juego --> {generos[mi_juego]}")
    print(f"\t [+] Total de ventas del juego --> {ventas_y_stock[mi_juego][0]}")
    print(f"\t [+] Total de stock del juego --> {ventas_y_stock[mi_juego][1]}")
    print(f"\t [+] Clientes que han adquirido el juego --> {' , '.join(clientes[mi_juego])}")

#Probar funcion para un juego
#sumario(mi_juego)

#Probar funcion para todos los juegos
print("Vamos a mostrar los juegos que han tenido >= 500 ventas")
for juego in juegos:
    if ventas_y_stock[juego][0] >= tope: 
        sumario(juego)

#Para obtener el numero total de ventas para los juegos que tienen >= 500 ventas

ventas_totales = lambda: sum(ventas for juego ,(ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] >= tope) 
print(f"\n El num. total de ventas de todos los juegos han sido --> {ventas_totales()}")

#Para obtener el numero total de ventas para todos los juegos
"""  
ventas_totales = lambda: sum(ventas for ventas, _ in ventas_y_stock.values())
print(f"\n El num. total de ventas de todos los juegos han sido --> {ventas_totales()}")
"""