import tkinter as tk
from tkinter import messagebox
from procesador import validar_cadenas, explicar_regex
from automata import construir_automata, mostrar_automata_ventana

def crear_interfaz():
    ventana = tk.Tk()
    ventana.geometry("500x350")
    ventana.title("Validador de Expresiones Regulares")

    # Entrada de expresión regular
    regex_label = tk.Label(ventana, text="Ingrese expresión regular:")
    regex_label.pack()
    regex_entry = tk.Entry(ventana, width=50)
    regex_entry.pack()
    regex_entry.insert(0, "(a|b)*c")

    # Entrada de cadenas
    cadena_label = tk.Label(ventana, text="Ingrese cadenas (separadas por comas):")
    cadena_label.pack()
    cadena_entry = tk.Entry(ventana, width=50)
    cadena_entry.pack()

    # Área de resultado
    resultado_label = tk.Label(ventana, text="Resultados:")
    resultado_label.pack()
    resultado_text = tk.Text(ventana, height=10, width=50)
    resultado_text.pack()

    # Botón para validar cadenas
    validar_button = tk.Button(ventana, text="Validar Cadenas", command=lambda: validar_cadenas_interfaz(regex_entry.get(), cadena_entry.get(), resultado_text, ver_automata_button))
    validar_button.pack()

    # Botón para explicar la expresión regular
    explicar_button = tk.Button(ventana, text="Explicar Expresión", command=lambda: explicar_regex_interfaz(regex_entry.get(), resultado_text))
    explicar_button.pack()

    # Botón "Ver Autómata" oculto inicialmente
    ver_automata_button = tk.Button(ventana, text="Ver Autómata", command=lambda: ver_automata(regex_entry.get()))
    ver_automata_button.pack()
    ver_automata_button.pack_forget()  # Ocultarlo al inicio

    ventana.mainloop()

def validar_cadenas_interfaz(regex, cadenas, resultado_text, ver_automata_button):
    """Usa la función validar_cadenas del módulo procesador para validar cadenas."""
    resultado_text.delete(1.0, tk.END)
    resultado = validar_cadenas(regex, cadenas.split(','))
    resultado_text.insert(tk.END, resultado)

    # Hacer visible el botón "Ver Autómata" después de validar
    ver_automata_button.pack()  # Mostrar el botón si no estaba visible

def ver_automata(regex):
    ruta_imagen = construir_automata(regex)
    mostrar_automata_ventana(ruta_imagen)


def explicar_regex_interfaz(regex, resultado_text):
    """Usa la función explicar_regex del módulo procesador para explicar la expresión regular."""
    resultado_text.delete(1.0, tk.END)  # Limpiar el área de resultado
    explicacion = explicar_regex(regex)  # Llamada a la función de procesador
    resultado_text.insert(tk.END, explicacion)  # Mostrar la explicación

# Llamada a la función para crear la interfaz
crear_interfaz()
