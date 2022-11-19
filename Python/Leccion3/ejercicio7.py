#  numeros pares e impares

#  n_elementos = 0
i = 0
num = 0
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0
promedio_impares = float()

n_elementos = int(input('Digite la cantidad de elementos a ingresar: '))
i += 1
suma_pares += 0
conteo_pares += 0
suma_impares += 0
conteo_impares += 0
while i <= n_elementos:
    num = int(input('Digite un número: '))
    if num / 2 == 0:
        suma_pares += 1
        conteo_pares += 1
        i += 1
    else:
        suma_impares += 1
        conteo_impares += 1
        i += 1

