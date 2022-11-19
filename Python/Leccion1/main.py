"""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los alumnos de la tecnicatura"
print(miVariable)
miVariable = "3.5"
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# las literales se escriben con x200, la variable y = x944, la variable z = x264 / referencia de memoria
print(id(y))
print(id(z))

# Tipos int, float, string, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de Cadenas (String)
miGrupofavorito = "Maroon 5"
caracteristicas = "La mejor banda de Pop"
print("Mi grupo favorito es: ", miGrupofavorito, caracteristicas)

# numero1 = "7"
# numero2 = "8"
# print(int(numero1) + int(numero2))

# Tipos boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# funcion input
# resultado = input("Didite un numero: ")  # regresa un dato tipo string
# print(resultado)

# concersion de la entrada de datos en la funcion input
numero1 = int(input("Escribe el primer numero:"))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1+numero2
print("El resultado de la suma es: ",resultado)
# Clase3 ejercicico 1 y 2
# operadores aritmeticos / inperpolacion colocar "F"
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
# print('Resultado de la suma es:', suma)
print(f"El resultado de la suma es: {suma}")
resta = operandoA - operandoB
print("Resultado de la resta es: ", resta)
print(f'El resultado de la resta es:  {resta}')

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo es: {modulo}")
exponenete = operandoA ** operandoB
print(f"El resultado del exponente es: {exponenete}")

miVariable3 = 10
print(miVariable3)
# operadores de reasignacion
miVariable3 = miVariable3 +1
print(miVariable3)
miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable -2
miVariable3 -=2
print(miVariable3)
# miVariable3 = miVariable *3
miVariable3 *=3
print(miVariable3)
# miVariable3 = miVariable /2
miVariable3 /=2
print(miVariable3)

# operadores de comparacion
d = 4
b = 6
resultado = d == b # comprobamos si son iguales
print(resultado)
# operador diferente
resultado = d != b
print(resultado)
# operador mayor que
resultado = d > b
print(resultado)
# operador menor que
resultado = d < b
print(resultado)
# operador menor o igual que
resultado = d <= b
print(resultado)
# operador menos o igual que
resultado = d >= b
print(resultado)

a = int(input("ingrese un Numero: "))
print(f"El residuo de la divicion es:, {a % 2}")
if a % 2 == 0:
    print(f"El numero ingresado es:, {a} es un numero PAR")
else:
    print(f"El numero ingresado es:, {a} es un numero  IMPAR ")

#  Determinar si es mayor de edad
a = int(input("Ingrese su edad: "))
if a >= 18:
        print(f"La edad ingresada es:, {a} años, eres MAYOR de edad")
else:
    print(f"La edad ingresada es:, {a} años, eres MENOR de edad")

#  operadores logicos and
a = False
b = False
resultado = a and b
print(resultado)

#  Operador or
resultado = a or b
print(resultado)

#  Operador not
resultado = not a
print(resultado)

#  Valor dentro de un rango
valor = int(input("Ingrese un numero entre el 0 al 5: "))
valorMinimo=0
valorMaximo=5
dentroRango = (valor >=valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} No esta dentro del rango")

#  Operador or, Operador not
vacaciones = True
diaDescanso = True
if not (vacaciones or diaDescanso):
    print('Tiene trabajo que hacer')
else:
    print('Puede asistir al juego')

#  Ejercicio: Rango entre 20 y 30 años
edad = int(input("Digite su Edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# print(treinta)
# if veinte or treinta:
#if (edad >=20 and edad < 30) or (edad >= 30 and edad < 40):
if (20<= edad < 30) or (30 <= edad < 40): # sintaxis simplificada del operador and
    print("La edad de esta dentro del rango de los (20'0) a (30'0) años")
#    if veinte:
#       print('La edad de esta dentro del rango de los (20\'0) años')
#    elif treinta:
#        print('La edad de esta dentro del rango de los (30\'0) años')
#    else:
#        print("La edad de No esta dentro del rango")
else:
    print("La edad de No esta dentro del rango de los (20'0) a (30'0) años")

# Ejercicio: El mayor de dos numeros
numero1= int(input('Digite el valor para el numero 1: '))
numero2= int(input('Digite el valor para el numero 2: '))
if numero1 > numero2:
    print(f"El numero 1 es mayor")
else:
    print(f"El numero 2 es mayor")

# Ejercicio: tienda de libros
print('Digite los siguientes datos del libro')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar si el envio es gratuito (True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'El valor es incorrecto, debe escribir True/False'
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')
"""
