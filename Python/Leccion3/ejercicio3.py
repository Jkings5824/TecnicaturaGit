#  Leer 10 numeros e imprimir cuantos son positivos, negativos y neutros

print('Contador de numeros')
conteo_positivo = 0
conteo_negativo = 0
conteo_neutro = 0
for i in range(10):
    num = int(input(f'({(i+1)}) - Digite un numero: '))
    if num == 0:
        conteo_neutro += 1
    elif num > 0:
        conteo_positivo += 1
    else:
        conteo_negativo += 1
print(f"""Se han introducido:
        {conteo_neutro} numeros neutros
        {conteo_positivo} numeros positivos
        {conteo_negativo} numeros negativos
      """)

""" Ejercicio 3
Leer 10 numeros e imprimir cuantos son positivos, cuantos negativos, y cuantos neutros

positivos = 0
negativos = 0
neutros = 0
for i in range (10):
    n = int(input(f'({(i+1)}) - Digite un numero: '))
    if n == 0:
        neutros += 1
    elif n > 0:
        positivos += 1
    else:
        negativos += 1
print(f'Usted ha ingresado {positivos} numeros positivos, {negativos} negativos y {neutros} neutros.')

"""