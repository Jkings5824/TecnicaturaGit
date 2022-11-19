#  Ejercicio Area y Longitud de un circulo

import mach
r = int(input("Ingrese el radio del circulo: "))
area = mach.pi * (r ** 2)
longitud = 2 * mach.pi * r
print(f"El Area es: {area}""\n"f"la longitud es: {longitud}")