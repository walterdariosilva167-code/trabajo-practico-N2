# Ejercicio 5 Walter
class Circulo:
    PI: float = 3.1416

    def __init__(self, radio: float):
        self.radio = radio

    def establecerRadio(self, radio: float):
        self.radio = radio

    def obtenerRadio(self) -> float:
        return self.radio

    def obtenerDiametro(self) -> float:
        return self.radio * 2

    def obtenerArea(self) -> float:
        return self.PI * (self.radio ** 2)

    def obtenerPerimetro(self) -> float:
        return 2 * self.PI * self.radio

    