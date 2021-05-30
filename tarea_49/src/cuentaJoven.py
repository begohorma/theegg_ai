from cuenta import Cuenta


class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, nueva_bonificacion):
        if isinstance(nueva_bonificacion, int) and 0 <= nueva_bonificacion < 100:
            self.__bonificacion = nueva_bonificacion
        else:
            raise ValueError(" La bonificación debe ser un número entero entre 1 y 100 ")

    def es_titular_valido(self):
        # debe ser mayor de edad y menor de 25 años
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25

    def retirar(self, cantidad_retirar):
        # sobreescribir el método para comprobar que el titular es válido
        if not self.es_titular_valido():
            raise ValueError("El titular no es válido. No puede retirar dinero de la cuenta")
        else:
            return super().retirar(cantidad_retirar)

    def mostrar(self):
        return ("Cuenta Joven:\n - Titular: {0} \n - Cantidad: {1} \n - Bonificación: {2} %".
                format(self.titular.mostrar(), self.cantidad, self.bonificacion))
