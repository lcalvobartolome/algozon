"""
import time
progreso = 7
total = 10

# Construcción dinámica de la cadena
barra = "#" * progreso + "-" * (total - progreso)
print("[" + barra + "]")

for progreso in range(total + 1):
    barra = "#" * progreso + "-" * (total - progreso)
    porcen = (progreso / total) * 100
    print(f"\r[{barra}] | {porcen}%", end="")
    time.sleep(0.5)
"""

"""
M, P, B = 8, 2, 6 
t = "MENÚ PRINCIPAL"
s = "Selecciona una opción"
s *=5
# Margen, Padding, Borde
ancho = max(len(t), len(s)) + M
linea = "*" * ancho
print(linea)
print("*" + " " * P + t.center(ancho - B) + " " * P + "*")
print("*" + " " * P + s.center(ancho - B) + " " * P + "*")
print(linea)
"""

"""
opciones = "1. Jugar, 2. Salir"
print(opciones.split())
"""

"""
import datetime
# Fecha y hora actual
ahora = datetime.datetime.now()
# Crear una fecha concreta (Año, Mes, Día, [Hora, Min...])
hace_un_anio = datetime.datetime(2025, 2, 3, 12, 0)

# Acceso a componentes individuales
print(f"Año: {ahora.year}, Mes: {ahora.month}, Día: {ahora.day}")
# Comparación lógica (funciona como números)
if hace_un_anio < ahora:
    print("El pasado quedó atrás")
"""

"""
l = [0, 1, 2, 3, 4, 5]
print(l)
print()
l[::2] = [10, 20, 30]
print(l)

l = [0, 1, 2, 3, 4, 5]

print(l)
print(l[2:4])

l[2:4] = [100, 200, 300, 400]
print(l)
"""

"""
t = (1, 2, 3)
try:
    t[0] = 99
except Exception as e:
    print(e)

l = list(t)
l[0] = 99
print(l)

t = tuple(l)
print(t)
print(type(t))
"""

"""
def funcion(x,y):
    x +=5
    y.append(99)
    
a = 7
b = [17,23]

funcion(a,b)

print(a)
print(b)
"""

class Coche:
    def __init__(self, nombre, marca, gasolina):
        self.nombre = nombre # Atributos de instancia
        self.marca = marca
        self.gasolina = gasolina
    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("Tanque vacío")
        
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
        print(f"Quedan {self.gasolina} litros")
        
    def __str__(self):
        return f"Coche {self.nombre} de marca {self.marca} con {self.gasolina} litros de gasolina."
    

if __name__ == "__main__":
    
    mycoche = Coche("micra", "nissan", 50)
    mycoche.arrancar()
    mycoche.conducir()
    print(mycoche.nombre)
    print(mycoche)