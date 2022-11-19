# Ejercicio Etapas de vida según la edad
edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10: # Sintaxis simplificada
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 19:
    mensaje = 'Tienes muchos cambios, mucho que es estudiar '
elif 20 <= edad < 29:
    mensaje = 'Amor y comienza eñ trabajo'
elif 30 <= edad < 39:
    mensaje = 'La edad no es una barrera. Es una limitación que pones en tu mente'
elif 40 <= edad < 49:
    mensaje = 'A juventud ociosa, vejez trabajosa'
elif 50 <= edad < 59:
    mensaje = 'Opino que a los cincuenta, cada uno tiene la cara que se merece'
elif 60 <= edad < 69:
    mensaje = 'Se es viejo cuando se tiene más alegría por el pasado que por el futuro'
elif 70 <= edad < 79:
    mensaje = 'La juventud no es un tiempo de la vida, es un estado del espíritu'
elif 80 <= edad < 89:
    mensaje = 'Juventud: un tesoro que se puede tener en cualquier edad, incluso en personas jóvenes'
elif 90 <= edad < 99:
    mensaje = 'La memoria y el tiempo se mueven en dos direcciones opuestas'
else:
    mensaje = 'Error, etapa de vida no reconocida'
print(f'Tu edad es: {edad}, {mensaje} ')