import time


def suma_lineal(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


def suma_constante(n):
    return (n / 2) * (n + 1)


def main():
    cantidad = 1000000
    for i in range(4):
        t0 = time.time()
        suma1 = suma_lineal(cantidad)
        t1 = time.time()
        suma2 = suma_constante(cantidad)
        t2 = time.time()

        print("{0}. _____  suma de {1} números _____".format(i+1, cantidad))
        print("La suma linal es: {1} y ha tardado en ejecutarse {2} segundos".format(cantidad, suma1,
                                                                                     round(t1 - t0, 4)))

        print("La suma constante es: {1} y ha tardado en ejecutarse {2} segundos".format(cantidad, suma2,
                                                                                    round(t2 - t1, 4)))
        cantidad *= 10


if __name__ == '__main__':
    main()
