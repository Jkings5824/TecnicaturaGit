# listas
"""
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) # solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # indice a mostrar 0, 1, 2,
# desde el indice hasta el final
print(nombres[1: ])
# modificar el valor dentro de una lista
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')
# preguntamos cuantos elementos tiene una lista
print(len(nombres)) # le pasamos como parametro la lista

# agregamos un elemento
nombres.append('Marcelo')
print(nombres)
# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Devora')
print(nombres)
# Remover un elemento de la lista especificado
nombres.remove('Alberto')
print(nombres)
# eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)
# eliminar indice especifico
del nombres[2] # del significa delete (eliminar)
print(nombres)
# eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)
# Eliminar lista
#del nombres
#print(nombres)

# Definimos una tupla (Las tuplas son inmutables, no se pueden modificar como las listas),
# excepto si convertimos la tupla a lista agregamos lo que queremos y luego la volvemos tupla nuevamente
# no es una practica recomendada
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))
# Acceder a un elemento, para esto utilizamos corchetes no parentecis
print(cocina[0])
# mostrar de manera inversa
print(cocina[-1])
# Acceder a un rango
print(cocina[0:2])
# Ejemplo
verduras = ('papa',)# Una tupla necesita aunque sea un elemento LA COMA
# de lo contrario seria una cadena (si no le ponemos una coma)

# recoremos los elementos de la lista
for cocinar in cocina:# print esta usando \n para saltos de lines por default
    print(cocinar, end=' ')# Usamos , end=' ' para eliminar los salos de linea, concatenar en una sola linea
# del cocina, para poder eliminar la tupla

cocinaLista = list(cocina)
cocinaLista[0] ='Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# Tipo set, cambia de lugar los elementos de la lista
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas)) # Usamos la funcion len = length significa largo cantidad

# Revisar si un elemento existe dentro de set
print('Marte' in planetas) # nos devuelve un booleano, para la busqueda tiene que tener los mismos elementos,
# puede preguntar si esta o no esta (in, no in)

# agregar un elemento, no se pueden agregar elementos duplicados o repetidos (sive para nombre, dni, etc)
planetas.add('Tierra') # add es una funcion
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') # Esta funcion a un mal ingreso u inexistencia de los elementos da error
print(planetas)
planetas.discard('Tierra') # Esta funcion a un mal ingreso u inexistencia de los elementos da NO GENERA ERROR
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
print(planetas)# al eliminar nos muestra un error
"""

# 'Maradona' :10 (todo esto es un diccionario)
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Environmet',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}
# verificamos la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE']) # Ser detallista con los datos a ingresar, deben ser precisos

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario['IDE'])

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)# Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# Existencia de algun valor
print('IDE' in diccionario) # devuelve un booleano

# Agregamos un elemento

