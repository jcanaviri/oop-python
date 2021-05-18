class Vehiculo:
    def __init__(self, matricula, modelo, potencia):
        self.matricula = matricula
        self.modelo = modelo
        self.potencia = potencia

    def get_matricula(self):
        return self.matricula

class Taxi(Vehiculo):
    """Esta clase hereda o es hija de la clase Vehiculo"""
    def __init__(self, matricula, modelo, potencia, num_licencia):
        super().__init__(matricula, modelo, potencia)
        self.num_licencia = num_licencia


mi_taxi = Taxi('132F', 2020, 60, '123')
print(mi_taxi.num_licencia)
