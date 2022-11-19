class Persona: #Creamos una clase

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Javi', 'Reyes', 28)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona ('Osvaldo', 'Giordanini', 45)
print('El objeto')
