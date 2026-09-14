# Ejercicio 5 Walter
class circulo:
    Pi:float = 3.1416

    def __init__(self, radio: float):
        self.radio = radio
    def establecer_radio(self, radio: float):
        self.radio = radio

  #consultas
    def obtener_radio(self):
        return self.radio
    def obtener_diametro(self):
        return self.radio * 2
    def obtener_area(self):
        return self.Pi * (self.radio ** 2)
    def obtener_perimetro(self):
        return self.Pi * self.radio
    