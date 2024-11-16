import tkinter as tk
from tkinter import messagebox
from procesador import validar_cadenas, explicar_regex
from generadorAutomata import construir_automata, mostrar_ventana_automata

def crear_interfaz():
    ventana = tk.Tk()
    ventana.geometry("600x400")
    ventana.title("Validador y Visualizador de Autómatas")

    # Entrada de expresión regular
    tk.Label(ventana, text="Ingrese expresión regular:").pack()
    regex_entry = tk.Entry(ventana, width=50)
    regex_entry.pack()
    regex_entry.insert(0, "(a|b)*c")

    # Entrada de cadenas
    tk.Label(ventana, text="Ingrese cadenas (separadas por comas):").pack()
    cadena_entry = tk.Entry(ventana, width=50)
    cadena_entry.pack()

    # Área de resultado
    tk.Label(ventana, text="Resultados:").pack()
    resultado_text = tk.Text(ventana, height=10, width=70)
    resultado_text.pack()

    # Botón para validar cadenas
    tk.Button(
        ventana,
        text="Validar Cadenas",
        command=lambda: validar_cadenas_interfaz(
            regex_entry.get(), cadena_entry.get(), resultado_text
        ),
    ).pack()

    # Botón para explicar expresión regular
    tk.Button(
        ventana,
        text="Explicar Expresión",
        command=lambda: explicar_regex_interfaz(regex_entry.get(), resultado_text),
    ).pack()

    # Botón para mostrar autómata
    tk.Button(
        ventana,
        text="Ver Autómata",
        command=lambda: ver_automata(regex_entry.get()),
    ).pack()

    ventana.mainloop()

def validar_cadenas_interfaz(regex, cadenas, resultado_text):
    resultado_text.delete(1.0, tk.END)
    cadenas = cadenas.split(",")
    resultado = validar_cadenas(regex, cadenas)
    resultado_text.insert(tk.END, resultado)

def explicar_regex_interfaz(regex, resultado_text):
    resultado_text.delete(1.0, tk.END)
    explicacion = explicar_regex(regex)
    resultado_text.insert(tk.END, explicacion)


def ver_automata(regex):
    # Construir el AFD desde la expresión regular

    ruta_imagen = construir_automata(regex)
    if ruta_imagen:
        # Mostrar la imagen del DFA generado
        mostrar_ventana_automata(ruta_imagen)


crear_interfaz()