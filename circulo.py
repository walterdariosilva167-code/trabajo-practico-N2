# Ejercicio 5 Walter
class circulo:
    Pi:float = 3.1416

    def __init__(self, radio: float):
        self.radio = radio
    def establecer_radio(self, radio: float):
        self.radio = float

  #consultas
    def obtener_radio(self, radio: float): 
        self.radio = radio
    def obtener_diametro(self, radio: float):
         self.radio * 2
    def obtener_area(self, radio: float):
         self.Pi * (self.radio ** 2)
    def obtener_perimetro(self, radio: float):
        self.Pi * self.radio
    