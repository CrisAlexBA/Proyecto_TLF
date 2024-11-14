from graphviz import Digraph
import tkinter as tk
from tkinter import Toplevel

def construir_automata(regex):
    # Crear un objeto Digraph para representar el autómata
    dot = Digraph(comment='Autómata Generado')
    dot.attr(rankdir='LR')  # Orientación de izquierda a derecha

    # Manejar algunos casos comunes
    if regex == r"\d{3}-\d{2}-\d{4}":
        # Automata para un patrón de número de seguridad social (NNN-NN-NNNN)
        dot.node('q0', 'q0', shape='circle')
        dot.node('q1', 'q1', shape='circle')
        dot.node('q2', 'q2', shape='circle')
        dot.node('q3', 'q3', shape='circle')
        dot.node('q4', 'q4', shape='doublecircle')

        dot.edge('q0', 'q1', label=r'\d{3}')
        dot.edge('q1', 'q2', label='-')
        dot.edge('q2', 'q3', label=r'\d{2}')
        dot.edge('q3', 'q4', label='-')
        dot.edge('q4', 'q4', label=r'\d{4}')

    elif regex == r"^[a-zA-Z]+$":
        # Automata para un patrón que acepta solo letras (una o más)
        dot.node('q0', 'q0', shape='circle')
        dot.node('q1', 'q1', shape='doublecircle')

        dot.edge('q0', 'q1', label='a-z, A-Z')
        dot.edge('q1', 'q1', label='a-z, A-Z')

    elif regex == "(a|b)*c":
        # Automata para el patrón (a|b)*c
        dot.node('q0', 'q0', shape='circle')
        dot.node('q1', 'q1', shape='circle')
        dot.node('q2', 'q2', shape='doublecircle')

        dot.edge('q0', 'q1', label='a, b')
        dot.edge('q1', 'q1', label='a, b')
        dot.edge('q1', 'q2', label='c')

    else:
        # Caso por defecto: mensaje de error
        dot.node('error', 'Patrón no soportado', shape='plaintext')

    # Guardar el gráfico en un archivo temporal
    dot.render('/tmp/automata', format='png', cleanup=False)
    return '/tmp/automata.png'

def mostrar_automata_ventana(ruta_imagen):
    ventana_automata = Toplevel()  # Crear una ventana secundaria
    ventana_automata.title("Autómata de la Expresión Regular")
    ventana_automata.geometry("500x400")

    # Mostrar la imagen del autómata en la ventana
    imagen = tk.PhotoImage(file=ruta_imagen)
    label_imagen = tk.Label(ventana_automata, image=imagen)
    label_imagen.image = imagen  # Para que la referencia no se elimine
    label_imagen.pack()
