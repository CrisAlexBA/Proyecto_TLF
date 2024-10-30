from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

def convertir_afn_a_afd():
    """Define y convierte un autómata finito no determinista (AFN) a un autómata finito determinista (AFD)"""
    # Definir un autómata finito no determinista (AFN) basado en una expresión regular de ejemplo
    nfa = NFA(
        states={'q0', 'q1', 'q2'},
        input_symbols={'a', 'b', 'c'},
        transitions={
            'q0': {'a': {'q0'}, 'b': {'q0'}, 'c': {'q1'}},
            'q1': {'c': {'q2'}}
        },
        initial_state='q0',
        final_states={'q2'}
    )

    # Convertir el AFN a un autómata finito determinista (AFD)
    dfa = DFA.from_nfa(nfa)
    return dfa

def validar_cadena(dfa, cadena):
    """Valida si la cadena es aceptada por el AFD"""
    return dfa.accepts_input(cadena)
