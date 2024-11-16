class Letra:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f'{self.valor}'


class Concatenar():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'({self.a}.{self.b})'


class Operador_O():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'({self.a}|{self.b})'


class Kleene():
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'{self.a}*'


class Mas():
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'{self.a}+'


class Interrogacion():
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'{self.a}?'


class Expresion():
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def __repr__(self):
        if self.b != None:
            return f'{self.a}{self.b}'
        return f'{self.a}'