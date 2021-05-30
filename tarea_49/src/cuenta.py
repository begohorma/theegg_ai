class Cuenta:

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    @property
    def cantidad(self):
        return self.__cantidad

    def mostrar(self):
        return ("Datos de la cuenta:\n - Titular: {0} \n - Cantidad: {1}".
                format(self.titular.mostrar(), self.cantidad))

    def ingresar(self, cantidad_ingresar):
        if cantidad_ingresar > 0 and (isinstance(cantidad_ingresar, float) or isinstance(cantidad_ingresar, int)):
            self.__cantidad += cantidad_ingresar
            return "Se ha ingresado {0} en la cuenta de {1}. El nuevo saldo es: {2}".format(cantidad_ingresar, self.titular.nombre, self.cantidad)
        else:
            return "La cantidad a ingresar es < 0. El saldo de la cuenta de {0} no se modifica".format(self.titular.nombre)
            # no lanzar excepción si la cantidad es negativa ya que el enunciado dice que no se hace nada.
            # raise ValueError("La cantidad a ingresar debe ser superior a 0.")

    def retirar(self, cantidad_retirar):
        # Como se permite que la cuenta quede en números rojos no se comprueba
        # que la cantidad a retirar sea menor al saldo actual de la cuenta
        if cantidad_retirar > 0:
            self.__cantidad -= cantidad_retirar
            if self.cantidad < 0:
                return ("Se ha retirado {0} de la cuenta de {1}. La cantidad actual de la cuenta es: {2}. ¡¡La cuenta está en Números Rojos!!".
                        format(cantidad_retirar, self.titular.nombre, self.cantidad))
            else:
                return ("Se ha retirado {0} de la cuenta de {1}. La cantidad actual de la cuenta es: {2}".format(
                    cantidad_retirar, self.titular.nombre, self.cantidad))
