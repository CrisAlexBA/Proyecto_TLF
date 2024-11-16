from tokens import Token, TipoToken

LETRAS = 'abcdefghijklmnopqrstuvwxyz01234567890.'


class Lector:

    def __init__(self, string: str):
        self.string = iter(string.replace(' ', ''))
        self.input = set()
        self.parentesisDer_pendiente = False
        self.siguiente()

    def siguiente(self):
        try:
            self.caracter_actual = next(self.string)
        except StopIteration:
            self.caracter_actual = None

    def crear_tokens(self):
        while self.caracter_actual != None:

            if self.caracter_actual in LETRAS:
                self.input.add(self.caracter_actual)
                yield Token(TipoToken.LETRA, self.caracter_actual)

                self.siguiente()

                # Finalmente, verifica si es necesario agregar un token de concatenación
                if self.caracter_actual != None and \
                        (self.caracter_actual in LETRAS or self.caracter_actual == '('):
                    yield Token(TipoToken.CONCATENAR, '.')

            elif self.caracter_actual == '|':
                yield Token(TipoToken.O, '|')

                self.siguiente()

                if self.caracter_actual != None and self.caracter_actual not in '()':
                    yield Token(TipoToken.PARENTESIS_IZ)

                    while self.caracter_actual != None and self.caracter_actual not in ')*+?':
                        if self.caracter_actual in LETRAS:
                            self.input.add(self.caracter_actual)
                            yield Token(TipoToken.LETRA, self.caracter_actual)

                            self.siguiente()
                            if self.caracter_actual != None and \
                                    (self.caracter_actual in LETRAS or self.caracter_actual == '('):
                                yield Token(TipoToken.CONCATENAR, '.')

                    if self.caracter_actual != None and self.caracter_actual in '*+?':
                        self.parentesisDer_pendiente = True
                    elif self.caracter_actual != None and self.caracter_actual == ')':
                        yield Token(TipoToken.PARENTESIS_DER, ')')
                    else:
                        yield Token(TipoToken.PARENTESIS_DER, ')')

            elif self.caracter_actual == '(':
                self.siguiente()
                yield Token(TipoToken.PARENTESIS_IZ)

            elif self.caracter_actual in (')*+?'):

                if self.caracter_actual == ')':
                    self.siguiente()
                    yield Token(TipoToken.PARENTESIS_DER)

                elif self.caracter_actual == '*':
                    self.siguiente()
                    yield Token(TipoToken.KLEENE)

                elif self.caracter_actual == '+':
                    self.siguiente()
                    yield Token(TipoToken.MAS)

                elif self.caracter_actual == '?':
                    self.siguiente()
                    yield Token(TipoToken.INTERROGACION)

                if self.parentesisDer_pendiente:
                    yield Token(TipoToken.PARENTESIS_DER)
                    self.parentesisDer_pendiente = False

                # Finalmente, verifica si es necesario agregar un token de concatenación
                if self.caracter_actual != None and \
                        (self.caracter_actual in LETRAS or self.caracter_actual == '('):
                    yield Token(TipoToken.CONCATENAR, '.')

            else:
                raise Exception(f'Invalid entry: {self.caracter_actual}')

        yield Token(TipoToken.CONCATENAR, '.')
        yield Token(TipoToken.LETRA, '#')

    def obtener_simbolos(self):
        return self.input