from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

def convertir_afn_a_afd(expresion_regular):
    # Definir un autómata finito no determinista (AFN) basado en la expresión regular
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
    # Verifica si la cadena es aceptada por el AFD
    return dfa.accepts_input(cadena)
