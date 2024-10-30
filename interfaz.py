import tkinter as tk
from tkinter import messagebox
from procesador import validar_cadenas, explicar_regex  # Importamos funciones necesarias

def crear_interfaz():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Validador de Expresiones Regulares")

    # Entrada de expresión regular
    regex_label = tk.Label(ventana, text="Ingrese expresión regular:")
    regex_label.pack()
    regex_entry = tk.Entry(ventana, width=50)
    regex_entry.pack()
    regex_entry.insert(0, "(a|b)*c")  # Inserta la expresión regular por defecto

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

    # Botón para validar cadenas usando validar_cadenas de procesador
    validar_button = tk.Button(ventana, text="Validar Cadenas", command=lambda: validar_cadenas_interfaz(regex_entry.get(), cadena_entry.get(), resultado_text))
    validar_button.pack()

    # Botón para explicar la expresión regular usando explicar_regex de procesador
    explicar_button = tk.Button(ventana, text="Explicar Expresión", command=lambda: explicar_regex_interfaz(regex_entry.get(), resultado_text))
    explicar_button.pack()

    # Ejecutar el bucle principal
    ventana.mainloop()

def validar_cadenas_interfaz(regex, cadenas, resultado_text):
    """Usa la función validar_cadenas del módulo procesador para validar cadenas."""
    resultado_text.delete(1.0, tk.END)  # Limpiar el área de resultado
    resultado = validar_cadenas(regex, cadenas.split(','))  # Llamada a la función de procesador
    resultado_text.insert(tk.END, resultado)  # Mostrar el resultado

def explicar_regex_interfaz(regex, resultado_text):
    """Usa la función explicar_regex del módulo procesador para explicar la expresión regular."""
    resultado_text.delete(1.0, tk.END)  # Limpiar el área de resultado
    explicacion = explicar_regex(regex)  # Llamada a la función de procesador
    resultado_text.insert(tk.END, explicacion)  # Mostrar la explicación

# Llamada a la función para crear la interfaz
crear_interfaz()
