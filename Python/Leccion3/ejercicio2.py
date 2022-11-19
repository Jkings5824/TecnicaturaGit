#  Calcular la suma de "N" primeros numeros
print("Digite la cantidad de numero a sumarse")
n = int(input(": "))
suma = int(input(": "))
i = int(input(': '))
resultado = n + suma + i
print(f'La suma es:{n}+{suma}+{i} =',resultado)


suma = 0
N = int(input('Digite la cantidad de numeros a sumarse: '))
for i in range(1, N+1):
    suma += i
print(f'La suma es: {suma}')
