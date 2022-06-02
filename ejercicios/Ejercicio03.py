# Leonardo Chuquimarca y José Guerrero
# Ejemplo de implementación de clases, objetos y constructores con ingreso de valores por teclado de un jugador de fútbol

class Futbolista():
    def __init__(self, nomFutbolista, añosFutbolista, equiFutbolista ):
        self.nombreFutbolista = nomFutbolista
        self.edadFutbolista = añosFutbolista
        self.equipoFutbolista = equiFutbolista

nombre = str(input("Ingrese el nombre del jugador"))
edad = int(input("Ingrese la edad del jugador"))
equipo = str(input("Ingrese el equipo donde se encuentra el jugador"))

futbolista = Futbolista(nombre, edad, equipo)
mensaje = "Datos del jugador\nNombre del jugador: %s\nEdad del jugador: %d\nEquipo: %s\n" \
             % (futbolista.nombreFutbolista, futbolista.edadFutbolista, futbolista.equipoFutbolista)
print(mensaje)