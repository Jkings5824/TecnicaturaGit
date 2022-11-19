# Ejercicio 2: operaciones de conjuntos con listas
# escriba un programa que tenga 2 listas y que a continuacion
# cree las listas (en las que no deben haber repetidos)
# 1 listas de palabras que aparecen en las listas
# 2 listas de palabras que aparecen en la primera lista, pero no en la segunda
# 3 listas de palabras que aparecen en la segunda lista, pero no en la primera
# 4 listas de palabras que aparecen en ambas listas

lista1 = ['arbol', 'luna', 'perro', 'gato', 'sol', 'luna', 'perro']
lista2 = ['mar', 'pes', 'vaso', 'barco', 'nube', 'pes', 'vaso']
lista1 = list(set(lista1))
lista2 = list(set(lista2))
# print(lista1)
# print(lista2)
lista3 = lista1 + lista2
print(lista3[ :5])
print(lista3[5: ])
print(lista3)

lista1.extend(lista2)
print(lista1)
