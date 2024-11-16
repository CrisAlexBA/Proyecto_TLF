from enum import Enum


class TipoToken(Enum):
    LETRA = 0
    CONCATENAR = 1
    O = 2
    KLEENE = 3
    MAS = 4
    INTERROGACION = 5
    PARENTESIS_IZ = 6
    PARENTESIS_DER = 7


class Token:
    def __init__(self, tipo: TipoToken, valor=None):
        self.tipo = tipo
        self.valor = valor
        self.precedencia = tipo.value

    def __repr__(self):
        return f'{self.tipo.name}: {self.valor}'