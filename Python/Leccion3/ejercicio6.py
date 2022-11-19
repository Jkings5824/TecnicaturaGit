# Salario 5 empleados
"""
empleado = 0
suma = 0
for i in range(5):
    empleado = (input('Salario del Empleado: '))
    horas = int(input("Digite las horas trabajadas: "))
    tarifa = float(input("Digite el precio por hora trabajada: "))
    salario = horas * tarifa
    print(salario)
    suma += salario
    i = (i + 1)

print(f'Suma de los salarios de todos los empleados: {suma}')
"""
i = 1
horas = 0
suma = 0
while i <= 5:
    print(f'Salario del Empleado {i}')
    horas = int(input("Digite las horas trabajadas: "))
    print(horas)
    tarifa = float(input("Digite el precio por hora trabajada:$ "))
    print(tarifa)
    salario = horas * tarifa
    print(f"El salario es:$ {salario}")
    suma += salario
    i += 1
print(f'Suma de los salarios de todos los empleados: {suma}')