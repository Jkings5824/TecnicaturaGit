# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por ultimo mostrar la lista.

# Creamos una lista

var = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4']
print(var)
# conjunto = set(var) # pasamos la lista var a un conjunto tipo set
# var = list(conjunto) # Convertimos el conjunto a una lista
var = list(set(var)) # La conversion hecha en una sola linea de codigo (eficiente)
print(var)

# Para mantener el orden de la lista
# data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4']
# result = []
# for item in data:
#     if item not in result:
#         result.append(item)
#
# print(result)