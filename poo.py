# comentario de una linea
"""
    Comentario de multiples lineas
    Esta es la segunda linea
"""
# Ejemplo de una clase vacia
class NombreClase:
    """Esta clase define un template para python
    o tambien conocido como docstring"""
    pass


class Persona:
    """Molde de una persona"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f'Yo soy { self.nombre } y tengo {self.edad}.')


john = Persona('John', 22)
maria = Persona('Maria', 21)
# intancia.variable
print(john.name)
# instancia.metodo
maria.presentarse()
