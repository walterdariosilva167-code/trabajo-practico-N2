from cancion import Cancion
from circulo import Circulo

# ============================================================
# PROGRAMACIÓN II
# TRABAJO PRACTICO NUMERO 2 - SECCIÓN B 
# ============================================================

# Ejercicio 1 #
print("\nEJERCICIO 1 - Se crea la clase Cancion.")

# Ejercicio 2 #
print("\nEJERCICIO 2 - Instanciar la clase Cancion 3 veces.")
cancion1 = Cancion("LA - Bassvictim", 153, "Electronica")
cancion2 = Cancion("KUCHUBURANKO - Plastic Tree", 324, "Rock")
cancion3 = Cancion("Kids from the west - Feng", 110, "HipHop")


# Ejercicio 3 #
print("\nEJERCICIO 3 - Géneros de las canciones")
print(cancion1.obtenerGenero())
print(cancion2.obtenerGenero())
print(cancion3.obtenerGenero())


# Ejercicio 4 #
print("\nEJERCICIO 4 - Modificar el género de una instancia e imprimirlo nuevamente.")
cancion1.establecerGenero("Indie-sleaze revival, electropop y cloud rap")
print(cancion1.obtenerGenero())
  

# Ejercicio 5 # 
print("\n EJERCICIO 5 - Se crea la clase Circulo")

# ejercicio 6 #
print("\n EJERCICIO 6 - Instanciar la clase circulo 3 veces")
circulo1 = Circulo(5.4)
circulo2 = Circulo(15.2)
circulo3 = Circulo(30.5)

# ejercicio 7 #
print("\n EJERCICIO 7 - imprimir el valor del diametro para cada instancia de circulo creada")

print("circulo1: ", circulo1.obtener_diametro(), "cm")
print("circulo2: ", circulo2.obtener_diametro(),"cm")
print("circulo3: ", circulo3.obtener_diametro(),"cm")

# Ejercicio 8 #
print("\nEJERCICIO 8 - Imprimir el valor de Pi para cada instancia de Circulo")

print("circulo1:", circulo1.PI)
print("circulo2:", circulo2.PI)
print("circulo3:", circulo3.PI)

# Ejercicio 9 #
print("\nEJERCICIO 9 - Crear 2 instancias con el mismo radio y compararlas")

circulo4 = Circulo(20.0)
circulo5 = Circulo(20.0)

print(circulo4 == circulo5)

# Ejercicio 10 #
print("\nEJERCICIO 10 - Comparar los perímetros de las instancias anteriores")

print(circulo4.obtener_perimetro() == circulo5.obtener_perimetro())