# Ciclo While (Mientras o durante)
"""
contador = 0
while contador <3:
    print('Ejecutamos nuestro ciclo while', contador)
    contador += 1
else:
    print('Fin del ciclo while')

# Imprimir numeros del 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1

# Imprimir numeros del 5 al 0 con el ciclo while
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

# CIclo for (iterar (recorer cada elemento del conjunto de datos  lista de elementos, 'para', 'hasta con paso hacer')
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')

# Palabra recervada break
for  letra in 'Alemania':
    if letra == 'a':
        print(f'Letras encontradas: {letra}')
        break
else:
    print('Fin del ciclo for')
"""
# Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f'valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue  # eludir o anular todos los numero impares, en este caso
    print(f'valor: {i}')