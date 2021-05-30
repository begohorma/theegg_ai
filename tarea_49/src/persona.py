import re


class Persona:
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"

    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if not isinstance(nueva_edad, int) or nueva_edad < 0:
            raise ValueError("La edad debe ser un valor entero mayor que 0 ")
        else:
            self.__edad = nueva_edad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo_dni):
        if nuevo_dni == "":
            self.__dni = nuevo_dni
        else:
            if not re.match(r'^\d{8}[a-zA-Z]$', nuevo_dni):
                raise ValueError("La estructura del Dni no es correcta. Debe tener 8 dígitos seguidos de una letra.")
            else:
                if nuevo_dni[8].upper() == self.letras_dni[int(nuevo_dni[:8]) % 23]:
                    self.__dni = nuevo_dni
                else:
                    raise ValueError("La letra del DNI " + nuevo_dni + " no es correcta")

    def mostrar(self):
        return "Nombre: {} - Edad: {} - DNI: {}".format(self.nombre, self.edad, self.dni)

    def es_mayor_de_edad(self):
        return self.edad >= 18
