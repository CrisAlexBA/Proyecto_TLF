from tokens import TipoToken
from nodos import *


class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.siguiente()

    def siguiente(self):
        try:
            self.token_actual = next(self.tokens)
        except StopIteration:
            self.token_actual = None

    def nuevo_simbolo(self):
        token = self.token_actual

        if token.tipo == TipoToken.PARENTESIS_IZ:
            self.siguiente()
            resultado = self.expresion()

            if self.token_actual.tipo != TipoToken.PARENTESIS_DER:
                raise Exception('¡Falta el paréntesis derecho para la expresión!')

            self.siguiente()
            return resultado

        elif token.tipo == TipoToken.LETRA:
            self.siguiente()
            return Letra(token.valor)

    def nuevo_operador(self):
        resultado = self.nuevo_simbolo()

        while self.token_actual != None and \
                (
                        self.token_actual.tipo == TipoToken.KLEENE or
                        self.token_actual.tipo == TipoToken.MAS or
                        self.token_actual.tipo == TipoToken.INTERROGACION
                ):
            if self.token_actual.tipo == TipoToken.KLEENE:
                self.siguiente()
                resultado = Kleene(resultado)
            elif self.token_actual.tipo == TipoToken.INTERROGACION:
                self.siguiente()
                resultado = Interrogacion(resultado)
            else:
                self.siguiente()
                resultado = Mas(resultado)

        return resultado

    def expresion(self):
        resultado = self.nuevo_operador()

        while self.token_actual != None and \
                (
                        self.token_actual.tipo == TipoToken.CONCATENAR or
                        self.token_actual.tipo == TipoToken.O
                ):
            if self.token_actual.tipo == TipoToken.O:
                self.siguiente()
                resultado = Operador_O(resultado, self.nuevo_operador())

            elif self.token_actual.tipo == TipoToken.CONCATENAR:
                self.siguiente()
                resultado = Concatenar(resultado, self.nuevo_operador())

        return resultado

    def Analizar(self):
        if self.token_actual == None:
            return None

        res = self.expresion()

        return res