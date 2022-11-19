# calificaciones por grupo
suma = 0
menor = 10
for i in range(10):
    calificacion = float(input(f'Ingrese la calificacion del alumno N°{i+1}: '))
    suma += calificacion
    if calificacion < menor:
        menor = calificacion
        promedio = suma / 10
print(f'El promedio de la clase es de {promedio}, y la nota mas baja fue de {menor}.')