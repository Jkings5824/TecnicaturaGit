#  ejrcicios pruebas
"""
a = float(input("a ->: "))
b = float(input("b ->: "))
c = float(input("c ->: "))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"El resultado es: {resultado}")
"""


"""
a = float(input("a ->: "))
b = float(input("b ->: "))

resultado = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)
print(f'resultado: {resultado}')
"""
"""
a = input('Digite el valor de a: ')
b = input('Digite el valor de b: ')
a , b = b ,a
print(f'El valor de a es: {a}')
print(f'El valor de b es: {b}')
"""
"""
import math
radio = float(input('Digite el valor del radio: '))
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f"Radio: {area:.2f}\nlongitud: {longitud:.2f}")
"""
"""
a = float(input('Digite el precio del producto a: '))
b = float(input('Digite el precio del producto b: '))
c = float(input('Digite el precio del producto c: '))
resultado = (a + b + c)*0.15
final = (a+b+c)-resultado
print(f'El total es: {final:.2f}')
"""
"""
a = int(input('digite un num: '))
b = int(input('digite un num: '))
if a %2==0 and b %2==0:
    print('ambos son pares')
elif a %2==0 and b %2!=0:
    print(f'{a} es par')
elif a %2 != 0 and b % 2 == 0:
    print(f'{b} es par')
else:
    print('Ambos son inpares')
"""
"""
a = int(input('digite un num: '))
b = int(input('digite un num: '))
c = int(input('digite un num: '))
if a>=b  and a>=c:
    print(f'{a} es mayor')
elif b>=a  and b>=c:
    print(f'{b} es mayor')
elif c>=a  and c>=b:
    print(f'{c} es mayor')
"""
"""
caracter = input('Digite un caracter').lower()
if caracter == 'a' or caracter =='e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
    print('Es una vocal')
else:
    print('no es una vocal')
"""
"""
num1 = float(input('Digite num1: '))
num2 = float(input('Digite num2: '))
caracter = input('Digite un caracter').lower()
if caracter == 's':
    suma = num1 + num2
    print(f"suma:{num1} + {num2} = {suma}")
elif caracter == 'r':
    print(f"Resta:{num1} - {num2} =",(num1-num2))
elif caracter == 'p' or caracter == 'm':
    print(f"Resta:{num1} * {num2} =",(num1*num2))
elif caracter == 'd':
    div = num1/num2
    print(f"Resta:{num1} / {num2} ={div:.2}")

else:
    print('syntax error')
"""
"""
saldo = float(1000)
print("\t.:Menu:.")
opc = int(input("Bienvenido, que desea realizar?\n"
                "1-Ingresar Dinero\n"
                "2-Retirar Dinero\n"
                "3-Mostrar Dinero\n"
                "4-salir\n"
                ": "))
if opc == 1:
    a = float(input(f"cuanto dinero desea ingresar?: "))
    saldo += a
    print(f"El total de dinero es:$ {saldo}")
elif opc == 2:
    b = float(input(f"cuanto dinero desea retirar?:$ "))
    if b >saldo:
        print("No tiene esa cantidad de dinero disponible")
    saldo -= b
    print(f"El total de dinero es:$ {saldo}")
elif opc == 3:
    print(f"Su saldo total es: ${saldo}")
elif opc == 4:
    print("Gracias por utilizar su cajero automatico")
else:
    print("La opcion ingresada es incorrecta")
"""
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print(lista)
