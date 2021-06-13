class Compressor:

    def __init__(self):
        self.window = ""  # cadena de caracteres leidos en los que se busca el contenido del buffer de búsqueda
        self.pointer = 0  # puntero que va recorriendo el texto original y va marcando el origen del buffer de búsqueda
        self.lookahead_buffer_len = 0  # tamaño incial del buffer de búsqueda
        self.window_size_max = 9999  # tamaño máximo de la ventana. Valor por defecto si no se especifica
        self.lookahead_buffer_size_max = 9999  # tamaño máximo del buffer.Valor por defecto si no se especifica


    def compress(self, original_text, buffer_size_max=9999, window_size_max=9999):

        # si no especifican el tamaño máximo del buffer y la ventana serán el tamaño del texo original

        self.window_size_max = buffer_size_max
        self.lookahead_buffer_size_max = window_size_max
        if buffer_size_max == 9999 and window_size_max == 9999:
            self.window_size_max = len(original_text)
            self.lookahead_buffer_size_max = len(original_text)

        compressed_text = list()  # lista con las tuplas que codifican los caracteres

        while self.pointer < len(original_text):
            # si el puntero está en una posición menor al tamaño máximo de la ventana
            # asignar a la ventana el contenido desde el principio de la cadena hasta el puntero
            # o comienzo del buffer
            if self.pointer - self.window_size_max < 0:
                self.window = original_text[0:self.pointer]
            else:
                # si el puntero es mayor que el tamaño máximo de la ventana hay que desplazar el comienzo de la ventana
                # para mantener el tamaño de la ventana
                self.window = original_text[self.pointer - self.window_size_max: self.pointer]
            # se mantiene el puntero en la primera posición del buffer
            # mientras se encuentre el contenido del buffer en la ventana
            # se amplia el contenido del buffer de búsqueda
            # rfind devuelve la posición de la última ocurrencia
            while self.window.rfind(original_text[self.pointer: self.pointer + self.lookahead_buffer_len + 1]) != -1 \
                    and (self.pointer + self.lookahead_buffer_len + 1 < len(original_text)):
                # ampliar tamaño del buffer (hasta el límite)
                if self.lookahead_buffer_len + 1 <= self.lookahead_buffer_size_max:
                    self.lookahead_buffer_len += 1
                else:
                    break
            # posición en la ventana donde comienza la secuencia del buffer.
            window_position = self.window.rfind(original_text[self.pointer:self.pointer + self.lookahead_buffer_len])
            # si la ventana no comienza desde el principio de la cadena original hay que tener en cuenta
            # el desplazamiento de la ventana para calcular el desplazamiento necesario
            if self.pointer - self.window_size_max > 0:
                window_position += self.pointer - self.window_size_max

            # si se ha encontrado alguna cadena en la ventana el tamaño del buffer será mayor que 0
            if self.lookahead_buffer_len > 0:
                # el código es:
                # la distancia del puntero a la posición de la cadena en la ventana
                # longitud del buffer o cadena encontrada
                # siguiente caracter de la cadena original

                code = (self.pointer - window_position, self.lookahead_buffer_len,
                        original_text[self.pointer + self.lookahead_buffer_len])
                # avanzar puntero al siguiente caracter no encontrado
                self.pointer += self.lookahead_buffer_len + 1
            else:
                # no se ha encontrado el caracter en la ventana
                # el código es:
                # distanticia 0
                # longitud de la cadena 0
                # caracter no encontrado en la ventana
                code = (0, 0, original_text[self.pointer])

                # avanzar una posición el puntero
                self.pointer += 1
            # añadir la codificación a la lista
            compressed_text.append(code)
            # incializar el tamaño del buffer a 0
            self.lookahead_buffer_len = 0

        return compressed_text

    def decompress(self, compressed_text):
        decompressed_text = ""
        # recorrer los elementos de la lista
        for tupla in compressed_text:
            # si el primer elemento de la tupla no es 0 asignar al texto descomprimido
            # el substring del texto descomprimido que comienza en el tamaño actual del texto descomprimido
            # menos el desplazamiento indicado en la primera posición de la tupla, y que finaliza tantas posiciónes
            # después como indica el segundo elemento de la tupla
            # el caracter del tercer elemento de la tupla
            if tupla[0] != 0:
                decompressed_text += decompressed_text[len(decompressed_text) - tupla[0]:
                                                         (len(decompressed_text) - tupla[0] + tupla[1])]
            # en todos los casos añadir al texto descomprimido el tercer elemento de la tupla
            decompressed_text += tupla[2]
        return decompressed_text
