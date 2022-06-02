# Leonardo Chuquimarca y José Guerrero
# Ejemplo de implementación de clases, objetos y constructores con valores ingresados por teclado

class Propietario():               # -> Clase creada
    def __init__(self, nomPersona, CL):    # -> Constructor creado
        self.nombrePersona = nomPersona
        self.numeroCedula = CL

persona = str(input("Ingrese los nombres y apellidos completos de la persona"))
cedula = str(input("Ingrese la cédula de la persona"))
persona2 = str(input("Ingrese los nombres y apellidos nombre de la segunda persona"))
cedula2 = str(input("Ingrese la cédula de la segunda persona"))

datosPersona = Propietario(persona, cedula)  # -> Primer objeto creado
datosPersona2 = Propietario(persona2, cedula2)  # -> Segundo objeto creado

mensaje = "El persona perteneciente a la cédula %s es %s" \
          % (datosPersona.numeroCedula, datosPersona.nombrePersona)
mensaje2 = "El persona perteneciente a la cédula %s es %s" \
          % (datosPersona2.numeroCedula, datosPersona2.nombrePersona)

print(mensaje)
print(mensaje2)