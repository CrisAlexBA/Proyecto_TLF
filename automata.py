from pythomata import SimpleDFA
from utils import WriteToFile

FILA_ESTADOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class AFD:
    def __init__(self, arbol, simbolos, regex):

        # Útil para el árbol sintáctico
        self.nodos = list()

        # Propiedades del autómata
        self.simbolos = simbolos
        self.estados = list()
        self.func_transicion = dict()
        self.estados_aceptados = set()
        self.estado_inicial = 'A'

        # Propiedades de la clase
        self.arbol = arbol
        self.regex = regex
        self.estado_aumentado = None
        self.iter = 1

        self.ESTADOS = iter(FILA_ESTADOS)
        try:
            self.simbolos.remove('e')
        except:
            pass

        # Inicializar construcción del AFD
        self.procesar_arbol(self.arbol)
        self.calcular_followpos()

    def calcular_followpos(self):
        for nodo in self.nodos:
            if nodo.valor == '*':
                for i in nodo.lastpos:
                    nodo_hijo = next(filter(lambda x: x._id == i, self.nodos))
                    nodo_hijo.followpos += nodo.firstpos
            elif nodo.valor == '.':
                for i in nodo.c1.lastpos:
                    nodo_hijo = next(filter(lambda x: x._id == i, self.nodos))
                    nodo_hijo.followpos += nodo.c2.firstpos

        # Iniciar generación de estados
        estado_inicial = self.nodos[-1].firstpos

        # Filtrar nodos que tienen un símbolo
        self.nodos = list(filter(lambda x: x._id, self.nodos))
        self.estado_aumentado = self.nodos[-1]._id

        # Recursión
        self.calcular_nuevos_estados(estado_inicial, next(self.ESTADOS))

    def calcular_nuevos_estados(self, estado, estado_actual):

        if not self.estados:
            self.estados.append(set(estado))
            if self.estado_aumentado in estado:
                self.estados_aceptados.update(estado_actual)

        # Iterar por cada símbolo
        for symbol in self.simbolos:

            # Obtener todos los nodos con el mismo símbolo en followpos
            simbolos_iguales = list(
                filter(lambda x: x.valor == symbol and x._id in estado, self.nodos))

            # Crear un nuevo estado con los nodos
            nuevo_estado = set()
            for nodo in simbolos_iguales:
                nuevo_estado.update(nodo.followpos)

            # Si el nuevo estado no está en la lista de estados
            if nuevo_estado not in self.estados and nuevo_estado:

                # Obtener la letra para este nuevo estado
                self.estados.append(nuevo_estado)
                siguiente = next(self.ESTADOS)

                # Añadir estado a la función de transición
                try:
                    self.func_transicion[siguiente]
                except:
                    self.func_transicion[siguiente] = dict()

                try:
                    estados_existentes = self.func_transicion[estado_actual]
                except:
                    self.func_transicion[estado_actual] = dict()
                    estados_existentes = self.func_transicion[estado_actual]

                # Añadir la referencia
                estados_existentes[symbol] = siguiente
                self.func_transicion[estado_actual] = estados_existentes

                # ¿Es un estado de aceptación?
                if self.estado_aumentado in nuevo_estado:
                    self.estados_aceptados.update(siguiente)

                # Repetir con este nuevo estado
                self.calcular_nuevos_estados(nuevo_estado, siguiente)

            elif nuevo_estado:
                # Si el estado ya existe... ¿cuál es?
                for i in range(0, len(self.estados)):

                    if self.estados[i] == nuevo_estado:
                        ref_estado = FILA_ESTADOS[i]
                        break

                # Añadir la transición del símbolo
                try:
                    estados_existentes = self.func_transicion[estado_actual]
                except:
                    self.func_transicion[estado_actual] = {}
                    estados_existentes = self.func_transicion[estado_actual]

                estados_existentes[symbol] = ref_estado
                self.func_transicion[estado_actual] = estados_existentes

    def procesar_arbol(self, nodo):
        nom_metodo = nodo.__class__.__name__ + 'Nodo'
        metodo = getattr(self, nom_metodo)
        return metodo(nodo)

    def LetraNodo(self, node):
        nuevo_nodo = Nodo(self.iter, [self.iter], [
            self.iter], value=node.valor, nullable=False)
        self.nodos.append(nuevo_nodo)
        return nuevo_nodo

    def Operador_ONodo(self, nodo):
        nodo_a = self.procesar_arbol(nodo.a)
        self.iter += 1
        nodo_b = self.procesar_arbol(nodo.b)

        is_nullable = nodo_a.nullable or nodo_b.nullable
        firstpos = nodo_a.firstpos + nodo_b.firstpos
        lastpos = nodo_a.lastpos + nodo_b.lastpos

        self.nodos.append(Nodo(None, firstpos, lastpos,
                               is_nullable, '|', nodo_a, nodo_b))
        return Nodo(None, firstpos, lastpos, is_nullable, '|', nodo_a, nodo_b)

    def ConcatenarNodo(self, nodo):
        nodo_a = self.procesar_arbol(nodo.a)
        self.iter += 1
        nodo_b = self.procesar_arbol(nodo.b)

        is_nullable = nodo_a.nullable and nodo_b.nullable
        if nodo_a.nullable:
            firstpos = nodo_a.firstpos + nodo_b.firstpos
        else:
            firstpos = nodo_a.firstpos

        if nodo_b.nullable:
            lastpos = nodo_b.lastpos + nodo_a.lastpos
        else:
            lastpos = nodo_b.lastpos

        self.nodos.append(
            Nodo(None, firstpos, lastpos, is_nullable, '.', nodo_a, nodo_b))

        return Nodo(None, firstpos, lastpos, is_nullable, '.', nodo_a, nodo_b)

    def KleeneNodo(self, nodo):
        nodo_a = self.procesar_arbol(nodo.a)
        firstpos = nodo_a.firstpos
        lastpos = nodo_a.lastpos
        self.nodos.append(Nodo(None, firstpos, lastpos, True, '*', nodo_a))
        return Nodo(None, firstpos, lastpos, True, '*', nodo_a)

    def PlusNode(self, nodo):
        nodo_a = self.procesar_arbol(nodo.a)

        self.iter += 1

        nodo_b = self.KleeneNodo(nodo)

        is_nullable = nodo_a.nullable and nodo_b.nullable
        if nodo_a.nullable:
            firstpos = nodo_a.firstpos + nodo_b.firstpos
        else:
            firstpos = nodo_a.firstpos

        if nodo_b.nullable:
            lastpos = nodo_b.lastpos + nodo_a.lastpos
        else:
            lastpos = nodo_b.lastpos

        self.nodos.append(
            Nodo(None, firstpos, lastpos, is_nullable, '.', nodo_a, nodo_b))

        return Nodo(None, firstpos, lastpos, is_nullable, '.', nodo_a, nodo_b)

    def QuestionNode(self, nodo):
        # Node_a is epsilon
        nodo_a = Nodo(None, list(), list(), True)
        self.iter += 1
        nodo_b = self.procesar_arbol(nodo.a)

        is_nullable = nodo_a.nullable or nodo_b.nullable
        firstpos = nodo_a.firstpos + nodo_b.firstpos
        lastpos = nodo_a.lastpos + nodo_b.lastpos

        self.nodos.append(Nodo(None, firstpos, lastpos,
                               is_nullable, '|', nodo_a, nodo_b))
        return Nodo(None, firstpos, lastpos, is_nullable, '|', nodo_a, nodo_b)

    def evaluar_RegEx(self):
        estado_actual = 'A'
        for simbolo in self.regex:

            if not simbolo in self.simbolos:
                return 'No'

            try:
                estado_actual = self.func_transicion[estado_actual][simbolo]
            except:
                if estado_actual in self.estados_aceptados and simbolo in self.func_transicion['A']:
                    estado_actual = self.func_transicion['A'][simbolo]
                else:
                    return 'No'

        return 'Si' if estado_actual in self.estados_aceptados else 'No'

    def graficar_AFD(self):
        estados = set(self.func_transicion.keys())
        alfabeto = set(self.simbolos)

        afd = SimpleDFA(estados, alfabeto, self.estado_inicial,
                        self.estados_aceptados, self.func_transicion)

        grafo = afd.trim().to_graphviz()
        grafo.attr(rankdir='LR')

        source = grafo.source
        WriteToFile('./output/AFD.png', source)
        grafo.render('./output/AFD', format='png', cleanup=True)


class Nodo:
    def __init__(self, _id, firstpos=None, lastpos=None, nullable=False, value=None, c1=None, c2=None):
        self._id = _id
        self.firstpos = firstpos
        self.lastpos = lastpos
        self.followpos = list()
        self.nullable = nullable
        self.valor = value
        self.c1 = c1
        self.c2 = c2

    def __repr__(self):
        return f'''
    id: {self._id}
    value: {self.valor}
    firstpos: {self.firstpos}
    lastpos: {self.lastpos}
    followpos: {self.followpos}
    nullabe: {self.nullable}
    '''