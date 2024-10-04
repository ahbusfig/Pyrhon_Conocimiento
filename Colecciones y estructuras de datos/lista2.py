attacks = ["sqlinject", "Pishing", "Ddos", "ManInTheMiddle"]
#Podemos guardar el primer elemento en la variable primer_ataque
primer_ataque = attacks[0]
print(primer_ataque)
#Rango 1 -> mostrar el ultimo elemento
another_attacks_list = attacks[-1] 
print(another_attacks_list)

#Rango 2 -> mostrar un rango donde el ultimo elemento no lo cuenta --> caracteristica de rangos en py
another_attacks_list2 = attacks[0:2] # Este caso muestr de 0 a 1
print(another_attacks_list2)

#Rango 3 --> mostrar todos excepto el ultimo elemento
another_attacks_list3 = attacks[:-1]
print(another_attacks_list3)
