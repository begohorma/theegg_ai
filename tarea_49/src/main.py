from persona import Persona
from cuenta import Cuenta
from cuentaJoven import CuentaJoven


def main():
    try:
        print("\nCreando personas:")
        print("---------------------")
        laura = Persona('Laura', 23, '25678445A')
        print(laura.mostrar())
        jon = Persona('Jon', 15, '30123456B')
        print(jon.mostrar())
        print("¿Es laura mayor de edad ?: {0}".format(laura.es_mayor_de_edad()))
        print("¿Es jon mayor de edad ?: {0}".format(jon.es_mayor_de_edad()))

        print("\nCreando cuentas:")
        print("---------------------")
        cuenta_jon = Cuenta(jon, 60)
        print(cuenta_jon.mostrar())
        cuenta_laura = Cuenta(laura, 286)
        print(cuenta_laura.mostrar())
        maria = Persona("Maria", 25, "25885613X")
        cuenta_maria = Cuenta(maria)
        print(cuenta_maria.mostrar())

        print("\nIngresar y retirar de las cuentas:")
        print("---------------------------------------")
        print(cuenta_maria.ingresar(23.5))
        print(cuenta_maria.ingresar(200))
        print(cuenta_maria.retirar(50))
        print(cuenta_jon.retirar(25))
        print(cuenta_jon.retirar(85))
        print(cuenta_jon.ingresar(-67))

        print("\nCreando cuentas Jovenes:")
        print("---------------------")
        cuenta_joven_laura = CuentaJoven(laura, 300, 5)
        print(cuenta_joven_laura.mostrar())
        print(cuenta_joven_laura.ingresar(500))
        print(cuenta_joven_laura.retirar(200))
        cuenta_joven_jon = CuentaJoven(jon)
        print(cuenta_joven_jon.mostrar())
        print(cuenta_joven_jon.ingresar(100))
        print(cuenta_joven_jon.retirar(50))



    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
