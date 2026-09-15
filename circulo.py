# Ejercicio 5 Walter
class circulo:
    PI: float = 3.1416

    def __init__(self, radio: float):
        self.radio = radio

    def establecer_radio(self, radio: float):
        self.radio = radio

  #Consultas
    def obtener_radio(self):
        return self.radio
    def obtener_diametro(self):
        return self.radio * 2
    def obtener_area(self):
        return self.PI * (self.radio ** 2)
    def obtener_perimetro(self):
        return 2 * self.PI * self.radio
    