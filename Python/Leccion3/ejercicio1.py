#  año bisiesto


print('Comprobaremos si el año es Bisiesto')
opcion = 1
while opcion == 1:
    año = int(input("Ingrese el Año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f'El año {año} es bisiesto')
    else:
        print(f'El año {año} no es bisiesto')
    opcion = int(input("Para seguir comprobando, digite la opcion 1: "))