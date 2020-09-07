class Maximizer:

    def __init__(self, cows_total_num, lorry_total_weight, cows_weights, cows_production_day):
        self._cows_total_num = cows_total_num
        self._lorry_total_weight = lorry_total_weight
        self._cows_weights = cows_weights
        self._cows_production_day = cows_production_day
        self._solutions_table = self.make_all_solutions_table

    def get_maximun_production(self):
        # la producción máxima se corresponde con la última columna y la última fila de la tabla
        solution = self._solutions_table[-1][-1]
        return solution

    @property
    def make_all_solutions_table(self):
        # solución utilizando programación dinámica
        # crear tabla con tantas columnas como kg acepta el camión +1 para incluir el 0
        # y filas como vacas hay disponibles

        table = [[0 for x in range(self._lorry_total_weight + 1)] for y in range(self._cows_total_num)]

        # se va resolviendo el problema para cada vaca y cada peso disponible.
        # primer bucle cada vaca (fila)
        # el segundo bucle por los pesos disponibles (columna)
        for index in range(self._cows_total_num):
            for weight in range(self._lorry_total_weight + 1):
                # Si la vaca pesa más que la capacidad de la columna ( no se puede subir la vaca) la solución es la
                # solución de la fila anterior ( la producción conseguida con las vacas que se habian podido subir
                # con el peso disponible)
                if self._cows_weights[index] > weight:
                    table[index][weight] = table[index - 1][weight]
                    continue
                # si el peso de la vaca es menor que la capacidad de la columna (se puede subir la vaca) hay que
                # comparar la mejor solución obtenida hasta ahora para la capacidad disponible, el valor de la fila
                # superior con la nueva mejor opción que es la producción de la vaca más la mejor solución anterior
                # para el espacio que queda disponible después de subir a la vaca actual. Se asigna como solución el
                # mayor de estos dos posibles valores.
                previous_value = table[index - 1][weight]

                new_best_option = self._cows_production_day[index] + table[index - 1][
                    weight - self._cows_weights[index]]

                table[index][weight] = max(previous_value, new_best_option)

        return table
