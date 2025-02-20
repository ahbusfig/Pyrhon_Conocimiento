import pandas as pd
from termcolor import colored

# Importar el archivo segun la ruta
caffe = pd.read_csv('./warmup-data/coffee.csv')
print(caffe)

'''
### Ejercicios de Visualización y Filtrado de Datos
'''

# Mostrar las 5 primeras lineas
# print(colored("Mostrar las 5 primeras lineas", "green"))
# print(colored(caffe.head(5), "cyan"))

# Mostrar las 5 ultimas lineas
# print(colored(f"Mostrar las ultimas 5 lineas --> ", "green"))
# print(colored(caffe.tail(5), "cyan"))

# Mostrar de la fila 5 al 8, las columnas [day, units sold] --> loc(usa labels!)
# print(colored("Mostrar de la fila 5 al 8, las columnas [day, units sold] --> loc(usa labels!)", "green"))
# print(colored(caffe.loc[5:8, ["Day","Units Sold"]], "cyan"))

# Mostrar de la fila 5 al 8, las columnas [day, units sold] --> iloc(usa indices!)
# print(colored("Mostrar de la fila 5 al 8, las columnas [day, units sold] --> iloc(usa indices!)", "green"))
# print(colored(caffe.iloc[5:9, [0, 2]], "cyan"))

# Mostrar las filas del DataFrame donde el tipo de café es 'Latte' y las unidades vendidas son mayores a 30
# print(colored("Mostrar las filas del DataFrame donde el tipo de café es 'Latte' y las unidades vendidas son mayores a 30", "green"))
# Latte_mayor30 = caffe[(caffe['Units Sold'] > 30) & (caffe["Coffee Type"] == 'Latte')]
# print(colored(Latte_mayor30, "cyan"))

# Filtrar las filas donde el tipo de café es 'Espresso'
# print(colored("Filtrar las filas donde el tipo de café es 'Espresso'", "green"))
# espresso_caffe = caffe[caffe['Coffee Type'] == 'Espresso']
# espresso_caffe = espresso_caffe.drop("Coffee Type", axis=1)
# print(colored(espresso_caffe, "yellow"))

# Filtrar las filas donde las unidades vendidas son mayores a 40
# print(colored("Filtrar las filas donde las unidades vendidas son mayores a 40", "green"))
# high_sales = caffe[caffe['Units Sold'] > 40]
# print(colored(high_sales, "yellow"))

# Filtrar las filas donde el día contiene 'day' (usando regex)
# print(colored("Filtrar las filas donde el día contiene 'day'", "green"))
# filtered_caffe = caffe[caffe['Day'].str.contains(r'day', regex=True)]
# print(colored(filtered_caffe, "yellow"))

'''
### Ejercicios de Transformación de Datos
'''

# Reemplazar 'Latte' con 'Cappuccino' en la columna 'Coffee Type'
print(colored("Reemplazar 'Latte' con 'Cappuccino' en la columna 'Coffee Type'", "green"))
caffe['Coffee Type'] = caffe['Coffee Type'].str.replace('Latte', 'Cappuccino')
# print(colored(caffe.head(), "yellow"))

# Agregar una nueva columna 'Revenue' que sea el resultado de multiplicar 'Units Sold' por un precio fijo (por ejemplo, 5) y ordenar descendente
print(colored("Agregar una nueva columna 'Revenue' y ordenarla", "green"))
caffe['Revenue'] = caffe['Units Sold'] * 5
caffe = caffe.sort_values(by='Revenue', ascending=False)
# print(colored(caffe, "yellow"))

'''
### Ejercicios de Agrupación y Agregación
'''

# Calcular el total de unidades vendidas para cada tipo de café
# print(colored("Calcular el total de unidades vendidas para cada tipo de café", "green"))
# total_units_sold = caffe.groupby('Coffee Type')['Units Sold'].sum()
# print(colored(total_units_sold, "yellow"))

# Reemplazar todos los días de la semana en inglés por sus equivalentes en español
# print(colored("Reemplazar todos los días de la semana en inglés por sus equivalentes en español", "green"))
# days_translation = {
#     'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miércoles',
#     'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
# }
# caffe['Day'] = caffe['Day'].replace(days_translation)
# print(colored(caffe.head(), "yellow"))

# Mostrar el promedio de unidades vendidas por tipo de café
print(colored("Mostrar el promedio de unidades vendidas por tipo de café", "green"))
average_units_sold = caffe.groupby('Coffee Type')['Units Sold'].mean()
# print(colored(average_units_sold, "yellow"))

# Calcular el total de ingresos por tipo de café
print(colored("Calcular el total de ingresos por tipo de café", "green"))
total_revenue_by_coffee = caffe.groupby('Coffee Type')['Revenue'].sum()
# print(colored(total_revenue_by_coffee, "yellow"))

# Agregar una columna 'Profit' que sea el 70% de la columna 'Revenue'
# print(colored("Agregar una columna 'Profit' que sea el 70% de la columna 'Revenue'", "green"))
# caffe['Profit'] = caffe['Revenue'] * 0.7
# print(colored(caffe, "yellow"))


'''
### Ejercicios de Ordenación de Datos
'''

# Usar el sort_values para ordenar por 'Units Sold'
# print(colored("Ordenar por 'Units Sold'", "green"))
# sorted_caffe = caffe.sort_values(by='Units Sold', ascending=False)
# print(colored(sorted_caffe, "yellow"))
#-----------------------------------------------------------------------------------
#---Ordenar el DataFrame por 'Day' y luego por 'Revenue' en orden ascendente--------
#-----------------------------------------------------------------------------------
# Definir el orden personalizado para los días de la semana
dias_orden = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
caffe['Day'] = pd.Categorical(caffe['Day'], categories=dias_orden, ordered=True)
# Ordenar el DataFrame por 'Day' y luego por 'Revenue' en orden ascendente
print(colored("Ordenar el DataFrame por 'Day' y luego por 'Revenue' en orden ascendente", "green"))
sorted_day_revenue = caffe.sort_values(by=['Day', 'Revenue'])
print(colored(sorted_day_revenue, "yellow"))