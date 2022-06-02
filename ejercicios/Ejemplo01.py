# Leonardo Chuquimarca y José Guerrero
# Ejemplo de implementación de clases, objetos y constructores con valores determinados

class Provincia():             # -> Clase creada
    def __init__(self, nomProvincia, nomCapital):  # -> Constructor creado
        self.provincia = nomProvincia
        self.capital = nomCapital

provincia1 = Provincia("Guayas", "Guayaquil")  # -> Primer objeto creado
provincia2 = Provincia("Pichincha", "Quito")  # -> Segundo objeto creado

mensaje = "La capital de la provincia %s es %s" % (provincia1.provincia, provincia1.capital)
mensaje2 = "La capital de la provincia %s es %s" % (provincia2.provincia, provincia2.capital)

print(mensaje)
print(mensaje2)