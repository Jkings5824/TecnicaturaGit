# calcular el factorial

num = int(input("Digite el numero a calcular: "))
factorial = 1
if num >= 0:
    for i in range(1, num+1):
        factorial = factorial*i
print(f"El facrotial de {num} es: {factorial}")