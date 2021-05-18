# Decoradores
# Definicion: foo(foo2) -> foo3
def decorador(foo):
    def foo2():
        print('Pasara antes')
        foo()
        print('Pasara despues')
    return foo2

# Los decoradores usan una sintaxis muy particular
# ya que usan el caracter de @ para definirse
@decorador
def saludo():
    print('Hola')

saludo()

class Point:
    """Usaremos la clase Point para definir
    dos metodos estaticos @staticmethod y @classmethod"""
    def __init__(self, x):
        self.x = x

    @staticmethod
    def message():
        print('Este es un metodo estatico')

    @classmethod
    def get_instance(cls, x):
        return cls(x)

p1 = Point(2)
Point.message()

p2 = Point.get_instance(12)
print(p2.x)
