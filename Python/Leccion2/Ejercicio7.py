# Ejercicio: Sistema de calificaciones
calificaciones = int(input('Digite una calificacion entre 0 y 10: '))
if 9 <= calificaciones <= 10:
    print('A')
elif 8 <= calificaciones <= 9:
    print('B')
elif 7 <= calificaciones <= 8:
    print('C')
elif 6 <= calificaciones <= 7:
    print('D')
elif 0 <= calificaciones <= 6:
    print('F')
else:
    print('Valor incorrecto...')