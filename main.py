from cancion import Cancion
from circulo import circulo

# ============================================================
# PROGRAMACIÓN II
# TRABAJO PRACTICO NUMERO 2 - SECCIÓN B 
# ============================================================

# Ejercicio 2 Leonardo
print("\nEJERCICIO 2 - Instanciar la clase Cancion 3 veces.")
cancion1 = Cancion("LA - Bassvictim", 153, "Electronica")
cancion2 = Cancion("KUCHUBURANKO - Plastic Tree", 324, "Rock")
cancion3 = Cancion("Kids from the west - Feng", 110, "HipHop")


# Ejercicio 3 Leonardo
print("\nEJERCICIO 3 - Géneros de las canciones")
print(cancion1.obtenerGenero())
print(cancion2.obtenerGenero())
print(cancion3.obtenerGenero())


# Ejercicio 4 Leonardo
print("\nEJERCICIO 4 - Modificar el género de una instancia e imprimirlo nuevamente.")
cancion1.establecerGenero("Indie-sleaze revival, electropop y cloud rap")
print(cancion1.obtenerGenero())
  

# ejercicio 5
print("\n EJERCICIO 5 -cuadrado lados en centimetros")

# ejercicio 6 #
print("\n EJERCICIO 6 - instanciar la clase circulo 3 veces")
circulo1 = circulo(5.4)
circulo2 = circulo(15.2)
circulo3 = circulo(30.5)

# ejercicio 7 #
print("\n EJERCICIO 7 - imprimir el valor del diametro para cada instancia de circulo creada")

print("circulo1: ", circulo1.obtener_diametro(), "cm")
print("circulo2: ", circulo2.obtener_diametro(),"cm")
print("circulo3: ", circulo3.obtener_diametro(),"cm")

# Ejercicio 8 Jere


# Ejercicio 9 Jere


# Ejercicio 10 Jere
